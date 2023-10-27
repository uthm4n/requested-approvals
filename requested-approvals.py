import requests
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import warnings 

warnings.filterwarnings("ignore")

url = "https://{MORPHEUS-APPLIANCE-URL}/api/approvals?max=100&offset=0&sort=name&direction=asc"

headers = {
    "accept": "application/json",
    "authorization": "Bearer {MORPHEUS-API-KEY}"
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

requestedApprovalsQuery = parse("$.approvals[?(@.status[*] = '1 requested')]")       # only retrieve subtenant roles
requestedApprovals = [match.value for match in requestedApprovalsQuery.find(data)]

print(f"\r\nNumber of items awaiting approval: {len(requestedApprovals)}\n" + "------------------------------------\n")
print(json.dumps(requestedApprovals, indent=2))
