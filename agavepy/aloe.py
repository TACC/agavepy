"""Aloe compatibility
"""

__all__ = ['LAST_PRE_ALOE_VERSION', 'EXCEPTION_MODELS']

LAST_PRE_ALOE_VERSION = '2.2.22-r7deb380'

# response models which are dependent on the version of the API response -
EXCEPTION_MODELS = {
    "Job": {
        "version_cutoff": LAST_PRE_ALOE_VERSION,
        "model": "AloeJob"
    },
    "JobSummary": {
        "version_cutoff": LAST_PRE_ALOE_VERSION,
        "model": "AloeJobSummary"
    },
}
