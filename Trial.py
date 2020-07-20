import math
import os
import sys

import matplotlib
import requests

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)