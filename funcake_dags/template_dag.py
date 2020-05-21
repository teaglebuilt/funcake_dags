from funcake_dags.template import create_dag
from airflow import DAG # Required or airflow-webserver skips file.

"""
This file will automatically create a dag for every dag_id added to the config dictionary below.

The config dictionary maps dag_ids to dag configurations.  If no configuration
is mapped for a particular dag_id, then the template will also assume that an associated
airflow variables is present in airflow. For example for the id 'westchester'
the following associated airflow variables will be assumed to exist:

WESTCHESTER_HARVEST_CONFIG

Example of Harvest Config value (in JSON format)
{
    "endpoint": "http://digital.klnpa.org/oai/oai.php",
    "md_prefix": "oai_qdc",
    "all_sets": False, <--- OPTIONAL
    "excluded_sets": [], <--- OPTIONAL
    "included_sets": ["aebye","ajt","amc", ...], <--- OPTIONAL
    "schematron_filter": "validations/dcingest_reqd_fields.sch",
    "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
    "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
    "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
    "xsl_branch": "master",
    "xsl_filename": "transforms/qdcCDMingest.xsl",
    "xsl_repository": "tulibraries/aggregator_mdx"
}

Optionally per dag id we can set a target alias environment that is set to a default value of (dev) if not defined:

For example for the "westchester" dag id we can define "WESTCHESTER_TARGET_ALIAS_ENV"
"""

# Note that ids will automatically be prefixed with 'funcake_' as a namespace.
# The dag_id for "westchester" will automatically be "funcake_westchester".

config = {
        "penn_digitalimages": {
            "endpoint": "http://dla.library.upenn.edu/dla/archives/oai-pmh.xml",
            "md_prefix": "oai_dc",
            "all_sets": True,
            "excluded_sets": [],
            "included_sets": [],
            "schematron_filter": "validations/qdcingest_reqd_fields.sch",
            "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
            "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
            "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
            "xsl_branch": "master",
            "xsl_filename": "transforms/penn_digitalimages.xsl",
            "xsl_repository": "tulibraries/aggregator_mdx",
            },
        "penn_holy": {
            "endpoint": "http://dla.library.upenn.edu/dla/holyland/oai-pmh.xml",
            "md_prefix": "oai_dc",
            "all_sets": True,
            "excluded_sets": [],
            "included_sets": [],
            "schematron_filter": "validations/qdcingest_reqd_fields.sch",
            "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
            "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
            "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
            "xsl_branch": "master",
            "xsl_filename": "transforms/penn_holy.xsl",
            "xsl_repository": "tulibraries/aggregator_mdx",
            },
        "penn_inhand": {
            "endpoint": "http://dla.library.upenn.edu/dla/medren/oai-pmh.xml",
            "md_prefix": "oai_dc",
            "all_sets": True,
            "excluded_sets": [],
            "included_sets": [],
            "schematron_filter": "validations/qdcingest_reqd_fields.sch",
            "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
            "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
            "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
            "xsl_branch": "master",
            "xsl_filename": "transforms/penn_inhand.xsl",
            "xsl_repository": "tulibraries/aggregator_mdx",
            },
        "penn_print": {
            "endpoint": "http://dla.library.upenn.edu/dla/print/oai-pmh.xml",
            "md_prefix": "oai_dc",
            "all_sets": True,
            "excluded_sets": [],
            "included_sets": [],
            "schematron_filter": "validations/qdcingest_reqd_fields.sch",
            "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
            "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
            "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
            "xsl_branch": "master",
            "xsl_filename": "transforms/penn_print.xsl",
            "xsl_repository": "tulibraries/aggregator_mdx",
            },
        "penn_wheeler": {
                "endpoint": "http://dla.library.upenn.edu/dla/wheeler/oai-pmh.xml",
                "md_prefix": "oai_dc",
                "all_sets": True,
                "excluded_sets": [],
                "included_sets": [],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/penn_wheeler.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "penn_women": {
                "endpoint": "http://digital.library.upenn.edu/webbin/OAI-celebration",
                "md_prefix": "oai_dc",
                "all_sets": True,
                "excluded_sets": [],
                "included_sets": [],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/penn_women.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "lasalle_cdm": {
                "endpoint": "http://cdm15860.contentdm.oclc.org/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "p15860coll1",
                    "p15860coll5",
                    "p15860coll7"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/qdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "penn_walters_csv": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/generic_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "lehigh_csv": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/lehigh_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "free_library": {
                "schematron_filter": "validations/padigital_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/free_library_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "philamuseumofart": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/generic_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "statelibrary_csv": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/generic_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "catholicresearchctr": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/generic_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "uscranton_csv": {
                "schematron_filter": "validations/csv_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/uscranton_csv.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "historic_pitt": {
                "endpoint": "http://historicpittsburgh.org/oai2",
                "md_prefix": "oai_dc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "pitt_collection.32",
                    "pitt_collection.241",
                    "pitt_collection.324",
                    "pitt_collection.317",
                    "pitt_collection.72",
                    "pitt_collection.320",
                    "pitt_collection.321",
                    "pitt_collection.322",
                    "pitt_collection.328",
                    "pitt_collection.205",
                    "pitt_collection.249",
                    "pitt_collection.258",
                    "pitt_collection.250",
                    "pitt_collection.173",
                    "pitt_collection.212",
                    "pitt_collection.97"
                    ],
                "schematron_filter": "validations/dcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/historicpitt.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "shi": {
                "endpoint": "https://digital.sciencehistory.org/oai",
                "md_prefix": "oai_dc",
                "all_sets": True,
                "excluded_sets": [],
                "included_sets": [],
                "schematron_filter": "validations/dcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/SHIingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "pennstate": {
                "endpoint": "http://digital.libraries.psu.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "aebye",
                    "ajt",
                    "amc",
                    "benson",
                    "brentwilson",
                    "ejb",
                    "Forbes",
                    "jdp",
                    "maps1",
                    "mdfls",
                    "mwh",
                    "pab",
                    "pnd",
                    "psuphoto",
                    "whf",
                    "wpamaps",
                    "ww1stereo"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/pennstateingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "uscranton": {
                "endpoint": "http://digitalservices.scranton.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "aquinas",
                    "basketball",
                    "commencement",
                    "costello",
                    "ics",
                    "medieval",
                    "p15111coll2",
                    "p15111coll4",
                    "p16214coll1",
                    "p9000coll4",
                    "p9000coll6",
                    "p9000coll7",
                    "passionists",
                    "prpubs",
                    "publications",
                    "scholarship",
                    "SCRYB03",
                    "zanerbloser"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/qdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "westchester": {
                "endpoint": "http://digital.klnpa.org/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "p17189coll1",
                    "p17189coll4",
                    "chester",
                    "diaries",
                    "philips",
                    "qwcaralia",
                    "qwcarch",
                    "qwccivilwar",
                    "qwcphoto",
                    "qwcpost",
                    "redware",
                    "sharples",
                    "wcnp01",
                    "wcudoll",
                    "wcutreasure",
                    "wpa"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/KLNqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "slipperyrock": {
                "endpoint": "http://digital.klnpa.org/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "audio",
                    "photograph",
                    "postcard",
                    "yearbooks"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/KLNqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "millersville": {
                "endpoint": "http://digital.klnpa.org/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "mvsphoto",
                    "wingpost"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/KLNqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "bloomsburg": {
                "endpoint": "http://digital.klnpa.org/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "blmmap",
                    "blmphoto",
                    "blmpost",
                    "CHSminutes"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/KLNqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "lehigh": {
                "endpoint": "http://cdm.lib.lehigh.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "letters",
                    "postal"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/qdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "brynmawr": {
                "endpoint": "http://triptych.brynmawr.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "almaclarke",
                    "BMC_AdvertisingCards",
                    "BMC_collnew",
                    "BMC_photoarc",
                    "BMC_postcard",
                    "BMC_scrpbks",
                    "BMC_yrbks",
                    "castle",
                    "Mellink"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/TriCoqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "swathaverford": {
                "endpoint": "http://triptych.brynmawr.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "SC_Truman",
                    "SC_Broad"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/TriCoqdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "widener": {
                "endpoint": "http://digitalwolfgram.widener.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "p16069coll20",
                    "p16069coll34",
                    "p16069coll5",
                    "p16069coll19",
                    "p16069coll24",
                    "p16069coll27",
                    "p16069coll22",
                    "p16069coll32",
                    "p16069coll12",
                    "p16069coll23",
                    "p16069coll17",
                    "p16069coll31"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/qdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "temple": {
                "endpoint": "http://digital.library.temple.edu/oai/oai.php",
                "md_prefix": "oai_qdc",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "p15037coll1",
                    "p15037coll10",
                    "p15037coll14",
                    "p15037coll15",
                    "p15037coll17",
                    "p15037coll18",
                    "p15037coll19",
                    "p15037coll2",
                    "p15037coll3",
                    "p15037coll4",
                    "p15037coll5",
                    "p15037coll7",
                    "p16002coll1",
                    "p16002coll14",
                    "p16002coll16",
                    "p16002coll17",
                    "p16002coll19",
                    "p16002coll2",
                    "p16002coll24",
                    "p16002coll26",
                    "p16002coll28",
                    "p16002coll3",
                    "p16002coll31",
                    "p16002coll4",
                    "p16002coll5",
                    "p16002coll6",
                    "p16002coll7",
                    "p16002coll9",
                    "p245801coll0",
                    "p245801coll12",
                    "p245801coll13"
                    ],
                "schematron_filter": "validations/qdcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/qdcCDMingest.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "villanova": {
                "endpoint": "http://digital.library.villanova.edu/OAI/Server",
                "all_sets": False,
                "excluded_sets": [],
                "included_sets": [
                    "dpla"
                    ],
                "md_prefix": "oai_dc",
                "schematron_filter": "validations/dcingest_reqd_fields.sch",
                "schematron_report": "validations/padigital_missing_thumbnailURL.sch",
                "schematron_xsl_filter": "validations/padigital_reqd_fields.sch",
                "schematron_xsl_report": "validations/padigital_missing_thumbnailURL.sch",
                "xsl_branch": "master",
                "xsl_filename": "transforms/villanova.xsl",
                "xsl_repository": "tulibraries/aggregator_mdx",
                },
        "dplah": None,
        }

for dag_id, dag_config in config.items():
    dag = create_dag(dag_id, config)
    globals()[dag.dag_id] = dag
