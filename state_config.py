"""
State configuration for this NevadaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "NV"
STATE_NAME = "Nevada"
APP_NAME = "NevadaDischargeWatch"
APP_TAGLINE = "Nevada Discharge Monitoring"
DOMAIN = "nevadadischargewatch.org"
DATA_FILE = "nv_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@nevadadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "PST"
EPA_REGION = 9
