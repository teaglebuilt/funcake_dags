""" DAG to harvest data from Free Library of Philadelphia csv files"""
import os
from airflow import DAG
from airflow.hooks.base_hook import BaseHook
from airflow.models import Variable
from tulflow import harvest, tasks, validate
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

"""
INIT SYSTEMWIDE VARIABLES
check for existence of systemwide variables shared across tasks that can be
initialized here if not found (i.e. if this is a new installation) & defaults exist
"""

AIRFLOW_APP_HOME = Variable.get("AIRFLOW_HOME")
AIRFLOW_USER_HOME = Variable.get("AIRFLOW_USER_HOME")
SCRIPTS_PATH = AIRFLOW_APP_HOME + "/dags/funcake_dags/scripts"
CSV_SCHEMATRON_FILTER = "validations/dcingest_reqd_fields.sch"
CSV_SCHEMATRON_REPORT = "validations/dcingest_reqd_fields.sch"

# Data Bucket Variables
AIRFLOW_S3 = BaseHook.get_connection("AIRFLOW_S3")
AIRFLOW_DATA_BUCKET = Variable.get("AIRFLOW_DATA_BUCKET")

# Define the DAG
DEFAULT_ARGS = {
    "owner": "dpla",
    "depends_on_past": False,
    "start_date": datetime(2019, 8, 27),
    "on_failure_callback": tasks.execute_slackpostonfail,
    "retries": 0,
    "retry_delay": timedelta(minutes=10),
}

DAG = DAG(
    dag_id="funcake_free_library_of_philadelphia",
    default_args=DEFAULT_ARGS,
    catchup=False,
    max_active_runs=1,
    schedule_interval=None
)

"""
CREATE TASKS
Tasks with all logic contained in a single operator can be declared here.
Tasks with custom logic are relegated to individual Python files.
"""

SET_COLLECTION_NAME = PythonOperator(
    task_id='set_collection_name',
    python_callable=datetime.now().strftime,
    op_args=["%Y-%m-%d_%H-%M-%S"],
    dag=DAG
)

TIMESTAMP = "{{ ti.xcom_pull(task_ids='set_collection_name') }}"

CSV_TRANSFORM = BashOperator(
    task_id="csv_transform",
    bash_command="csv_transform_to_s3.sh ",
    env={**os.environ, **{
        "PATH": os.environ.get("PATH", "") + ":" + SCRIPTS_PATH,
        "DAGID": "funcake_free_library_of_philadelphia",
        "HOME": AIRFLOW_USER_HOME,
        "AIRFLOW_APP_HOME": AIRFLOW_APP_HOME,
        "BUCKET": AIRFLOW_DATA_BUCKET,
        "FOLDER": DAG.dag_id + "/" + TIMESTAMP + "/new-updated",
        "AWS_ACCESS_KEY_ID": AIRFLOW_S3.login,
        "AWS_SECRET_ACCESS_KEY": AIRFLOW_S3.password,
        "TIMESTAMP": "{{ ti.xcom_pull(task_ids='set_collection_name') }}"

        }},
    dag=DAG,
)

HARVEST_SCHEMATRON_REPORT = PythonOperator(
    task_id="harvest_schematron_report",
    provide_context=True,
    python_callable=validate.report_s3_schematron,
    op_kwargs={
        "access_id": AIRFLOW_S3.login,
        "access_secret": AIRFLOW_S3.password,
        "bucket": AIRFLOW_DATA_BUCKET,
        "destination_prefix": DAG.dag_id + "/{{ ti.xcom_pull(task_ids='set_collection_name') }}/new-updated",
        "schematron_filename": CSV_SCHEMATRON_REPORT,
        "source_prefix": DAG.dag_id + "/{{ ti.xcom_pull(task_ids='set_collection_name') }}/new-updated/"
    },
    dag=DAG
)

HARVEST_FILTER = PythonOperator(
    task_id="harvest_filter",
    provide_context=True,
    python_callable=validate.filter_s3_schematron,
    op_kwargs={
        "access_id": AIRFLOW_S3.login,
        "access_secret": AIRFLOW_S3.password,
        "bucket": AIRFLOW_DATA_BUCKET,
        "destination_prefix": DAG.dag_id + "/{{ ti.xcom_pull(task_ids='set_collection_name') }}/new-updated-filtered/",
        "schematron_filename": CSV_SCHEMATRON_FILTER,
        "source_prefix": DAG.dag_id + "/{{ ti.xcom_pull(task_ids='set_collection_name') }}/new-updated/",
        "report_prefix": DAG.dag_id + "/{{ ti.xcom_pull(task_ids='set_collection_name') }}/harvest_filter",
        "timestamp": "{{ ti.xcom_pull(task_ids='set_collection_name') }}"
    },
    dag=DAG
)

# SET UP TASK DEPENDENCIES
CSV_TRANSFORM.set_upstream(SET_COLLECTION_NAME)
HARVEST_SCHEMATRON_REPORT.set_upstream(CSV_TRANSFORM)
HARVEST_FILTER.set_upstream(CSV_TRANSFORM)