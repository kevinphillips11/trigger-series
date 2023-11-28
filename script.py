import requests
import json
import os

# cancel the previous run

url = f"https://api.github.com/repos/kevinphillips11/REPO/actions/runs/{os.environ['PREVIOUS_RUN_ID']}/cancel"

payload = {}
headers = {
  'Accept': 'application/vnd.github+json',
  'Authorization': 'Bearer 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',
  'X-GitHub-Api-Version': '2022-11-28'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# middle part - print hello

print('hello!')

# trigger the next run

url = "https://api.github.com/repos/kevinphillips11/trigger-series/actions/workflows/run.yml/dispatches"

payload = json.dumps({
"ref": "main",
"inputs": {
    "manual_trigger": "true",
    "previous_run_id": os.environ['CURRENT_RUN_ID']
}
})
headers = {
'Accept': 'application/vnd.github+json',
'Authorization': 'Bearer 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',
'X-GitHub-Api-Version': '2022-11-28',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# wait to be canceled by the next run

while True:
    pass
