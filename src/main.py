import argparse
import sys
import requests
import random
import json
import os

SERVICE_NAME = 'HelloWordrApp'
#DEFAULT_HOST = "http://controlpanel.nonrtric.svc.cluster.local:8080"
DEFAULT_HOST = "http://policymanagementservice.nonrtric.svc.cluster.local:9080"
BASE_PATH = "/a1-policy/v2"

base_url = DEFAULT_HOST + BASE_PATH
type_to_use = "2"
# policy_body_path = 'pihw_template.json'
policy_body_path = 'nonrtric-rapp-helloword/src/pihw_template.json'


# This function `get_rics_from_agent()` sends a GET request to the API endpoint `/rics`
# using the `requests` module. If the response is successful (status code 200),
# it returns the JSON data from the response. If the response is not successful,
# it prints an error message and returns an empty dictionary.
def get_rics_from_agent():
    resp = requests.get(base_url + '/rics')
    if not resp.ok:
        verboseprint(f'Unable to get Rics {resp.status_code}')
        return {}
    return resp.json()


def put_policy(ric_name):
    policy_number  = random.randint(10 ** (15 - 1), (10 ** 15) - 1)
    policy_id = f'policy_{policy_number}'
    complete_url = base_url + '/policies'
    headers = {'content-type': 'application/json'}
    policy_obj = json.loads(policy_data.replace('XXX', str(policy_number)))
    body = {
        "ric_id": ric_name,
        "policy_id": policy_id,
        "service_id": SERVICE_NAME,
        "policy_data": policy_obj,
        "policytype_id": type_to_use
    }
    print(f'PUT {complete_url} with body {body}')
    resp = requests.put(complete_url, json=body, headers=headers, verify=False)
    if not resp.ok:
        verboseprint(f'Unable to create policy {resp}')
        print(f'Unable to create policy {resp.text}')
        return False
    else:
        return True

def get_policy_instances():
    complete_url = f'{base_url}/policy-instances'
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f'Unable to get policy {resp}')
        print(f'Unable to get policy {resp.text}')
        return False
    else:
        verboseprint(f'Policy {resp.text}')
        print(f'Policy {resp.text}')
        return True

def get_policy_types():
    complete_url = f'{base_url}/policy-types'
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f'Unable to get policy {resp}')
        print(f'Unable to get policy {resp.text}')
        return False
    else:
        verboseprint(f'Policy {resp.text}')
        print(f'Policy {resp.text}')
        return True
        
    
def get_policy(policy_id):
    complete_url = f'{base_url}/policies/{policy_id}'
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f'Unable to get policy {resp}')
        print(f'Unable to get policy {resp.text}')
        return False
    else:
        verboseprint(f'Policy {resp.text}')
        print(f'Policy {resp.text}')
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument(
        '--pmsHost', help='The host of the A1 PMS, e.g. http://localhost:8081')
    parser.add_argument(
        '--policyTypeId', help='The ID of the policy type to use')
    parser.add_argument(
        '--policyBodyPath', help='The path to the JSON body of the policy to create')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Turn on verbose printing')
    parser.add_argument('--version', action='version', version='%(prog)s 1.1')
    args = vars(parser.parse_args())

    if args['verbose']:
        def verboseprint(*args, **kwargs):
            print(*args, **kwargs)
    else:
        verboseprint = lambda *a, **k: None  # do-nothing function

    if args["pmsHost"]:
        base_url = args["pmsHost"] + BASE_PATH
    else:
        base_url = DEFAULT_HOST + BASE_PATH

    if args["policyTypeId"]:
        type_to_use = args["policyTypeId"]

    if args["policyBodyPath"]:
        policy_body_path = args["policyBodyPath"]
        if not os.path.exists(policy_body_path):
            print(f'Policy body {policy_body_path} does not exist.')
            sys.exit(1)

    verboseprint(f'Using policy type {type_to_use}')
    print(f'Using policy type {type_to_use}')
    verboseprint(f'Using policy file {policy_body_path}')
    print(f'Using policy file {policy_body_path}')

    with open(policy_body_path) as json_file:
        policy_data = json_file.read()
        verboseprint(f'Policy body: {policy_data}')

    with open(policy_body_path) as json_file:
        policy_data = json_file.read()
        verboseprint(f'Policy body: {policy_data}')

    try:
        rics_from_agent = get_rics_from_agent()
        verboseprint(f'Got RICs from agent: {rics_from_agent}')
        #print(f'Got RICs from agent: {rics_from_agent}')
    except ConnectionError:
        print(f'A1PMS is not answering on {base_url}, cannot start!')

    put_policy('ric4')
    #get_policy('3f15db1d-fd5f-49bf-99ad-7ba2c076d252')
    #get_policy_instances()
    #get_policy_types()