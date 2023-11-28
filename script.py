import requests
import json
import os

# cancel the previous run
print('canceling previous run')

try:
    url = f"https://api.github.com/repos/kevinphillips11/trigger-series/actions/runs/{os.environ['PREVIOUS_RUN_ID']}/cancel"

    payload = json.dumps({
    "ref": "main",
    "inputs": {
        "manual_trigger": "true"
    }
    })
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
except:
    pass

# middle part - print hello

print('hello!')

# trigger the next run
print('triggering next run')

url = "https://api.github.com/repos/kevinphillips11/trigger-series/actions/workflows/run.yml/dispatches"

payload = json.dumps({
"ref": "main",
"inputs": {
    "previous_run_id": os.environ['CURRENT_RUN_ID']
}
})
headers = {
'Accept': 'application/vnd.github+json',
'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
'X-GitHub-Api-Version': '2022-11-28',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# wait to be canceled by the next run
print('waiting to be canceled by next run')
while True:
    pass
