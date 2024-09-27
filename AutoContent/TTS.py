import requests
import json
import time

text = """The technological singularity or simply the singularity is a hypothetical point in time at which technological growth becomes uncontrollable and irreversible, 
resulting in unforeseeable changes to human civilization. According to the most popular version of the singularity hypothesis, called intelligence explosion, 
an upgradable intelligent agent will eventually enter a "runaway reaction" of self-improvement cycles, each new and more intelligent 
generation appearing more and more rapidly, causing an "explosion" in intelligence and resulting in a powerful superintelligence that qualitatively 
far surpasses all human intelligence.
"""

url = "https://large-text-to-speech.p.rapidapi.com/tts"
payload = {"text": text}

headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "large-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': "26c20d8ec1msh4bdba7f61d0eb8dp1a0afajsn289c255960e8"
    }

# POST request
response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
print(response.text)

# get id and eta of the job from the response
id = json.loads(response.text)['id']
eta = json.loads(response.text)['eta']

print(f'Waiting {eta} seconds for the job to finish...')
time.sleep(eta)

# GET the result from the API
response = requests.request("GET", url, headers=headers, params={'id': id})
# if url not returned yet, wait and try again
while "url" not in json.loads(response.text):
    response = requests.get(url, headers=headers, params={'id': id})
    time.sleep(5)
# if no error, get url and download the audio file
if not "error" in json.loads(response.text):
    result_url = json.loads(response.text)['url']
    # download the waw file from results_url
    response = requests.get(result_url)
    # save the waw file to disk
    with open('output.wav', 'wb') as f:
        f.write(response.content)
    print("File output.wav saved!")
else:
    print(json.loads(response.text)['error'])