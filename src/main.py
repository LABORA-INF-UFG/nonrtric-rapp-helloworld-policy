import argparse
import sys
import requests
import random
import json
import os
import pprint
import time
import yaml

VERSION: str = "0.0.1"
SERVICE_NAME: str = "HelloWordrApp"
SERVICE_DESCRIPTION: str = "Hello Word rApp for testing Non-RT RIC guide development of future rApps and demo purposes"
SERVICE_DISPLAY_NAME: str = "Hello Word rApp"
DEFAULT_HOST_PMS: str = "http://nonrtricgateway.nonrtric.svc.cluster.local:9090"
BASE_PATH_PMS: str = "/a1-policy/v2"
DEFAULT_HOST_rAPP_CATALOGUE: str = (
    "http://rappcatalogueservice.nonrtric.svc.cluster.local:9085"
)
BASE_PATH_rAPP_CATALOGUE: str = "/services"
DEFAULT_POLICY_BODY_PATH: str = "nonrtric-rapp-helloword/src/pihw_template.json"
DEFAULT_POLICY_TYPE_ID: str = "2"
DEFAULT_POLICY_ID: str = "1"
DEFAULT_RIC_ID: str = "ric4"


base_url_rApp_catalogue = DEFAULT_HOST_rAPP_CATALOGUE + BASE_PATH_rAPP_CATALOGUE
base_url_pms = DEFAULT_HOST_PMS + BASE_PATH_PMS
type_to_use = DEFAULT_POLICY_TYPE_ID
ric_to_use = DEFAULT_RIC_ID
body_type_to_use = DEFAULT_POLICY_TYPE_ID
body_path_to_use = DEFAULT_POLICY_BODY_PATH
policy_id_to_use = DEFAULT_POLICY_ID

def register_service_rApp_catalalogue():
    """
    Sends a PUT request to a specified URL with a JSON payload containing the version, display name,
    and description of a service. If the response is not successful, it prints an error message and returns False.
    Otherwise, it returns True.

    Returns:
        bool: True if the request was successful, False otherwise.
    """
    complete_url = base_url_rApp_catalogue + "/" + SERVICE_NAME
    headers = {"content-type": "application/json"}
    body = {
        "version": VERSION,
        "display_name": SERVICE_DISPLAY_NAME,
        "description": SERVICE_DESCRIPTION,
    }
    verboseprint(f"PUT {complete_url} with body {body}")
    resp = requests.put(complete_url, json=body, headers=headers, verify=False)
    if not resp.ok:
        verboseprint(f"Unable to register rApp {resp}")
        print(f"Unable to register rApp {resp.text}")
        return False
    else:
        return True

def get_rics_from_agent():
    """
    Sends a GET request to the API endpoint `/rics` using the `requests` module.
    If the response is successful (status code 200), it returns the JSON data from the response.
    If the response is not successful, it returns an empty dictionary.

    Returns:
        dict: A dictionary containing the JSON data from the response if the request was successful,
              an empty dictionary otherwise.
    """
    resp = requests.get(base_url_pms + "/rics")
    if not resp.ok:
        verboseprint(f"Unable to get Rics {resp.status_code}")
        return {}
    return resp.json()

def put_policy(ric_name, policy_id):
    """
    Sends a PUT request to the API endpoint `/policies` using the `requests` module.
    It creates a random threshold value and replaces the 'XXX' string in the `policy_data` with the threshold value.
    It then creates a dictionary `body` containing the `ric_name`, `policy_id`, `SERVICE_NAME`, `policy_data`,
    and `type_to_use`. It sends the PUT request with the `body` and `headers` as parameters.
    If the response is successful (status code 200), it prints a message indicating that the policy has been updated
    and returns True. If the response is not successful, it prints an error message and returns False.

    Args:
        ric_name (str): The name of the RIC.
        policy_id (str): The ID of the policy.

    Returns:
        bool: True if the request was successful, False otherwise.
    """
    threshold = random.randint(10 ** (15 - 1), (10**15) - 1)
    complete_url = base_url_pms + "/policies"
    headers = {"content-type": "application/json"}
    policy_obj = json.loads(policy_data.replace("XXX", str(threshold)))
    body = {
        "ric_id": ric_name,
        "policy_id": policy_id,
        "service_id": SERVICE_NAME,
        "policy_data": policy_obj,
        "policytype_id": type_to_use,
    }
    verboseprint(f"PUT {complete_url} with body {body}")
    resp = requests.put(complete_url, json=body, headers=headers, verify=False)
    if not resp.ok:
        verboseprint(f"Unable to create policy {resp}")
        print(f"Unable to create policy {resp.text}")
        return False
    else:
        print(f"Updating policy: {policy_id} threshold now: {threshold}")
        return True

def get_policy_instances():
    """
    Sends a GET request to the API endpoint `/policy-instances` using the `requests` module.
    If the response is successful (status code 200), it returns the JSON data from the response.
    If the response is not successful, it prints an error message and returns False.

    Returns:
        dict: A dictionary containing the JSON data from the response if the request was successful,
              False otherwise.
    """
    complete_url = f"{base_url_pms}/policy-instances"
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f"Unable to get policy {resp}")
        return False
    else:
        verboseprint(f"Policy {resp.text}")
        return resp.json()

def get_policy_types():
    """
    Sends a GET request to the API endpoint `/policy-types` using the `requests` module.
    If the response is successful (status code 200), it returns the JSON data from the response.
    If the response is not successful, it prints an error message and returns False.

    Returns:
        dict: A dictionary containing the JSON data from the response if the request was successful,
              False otherwise.
    """
    complete_url = f"{base_url_pms}/policy-types"
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f"Unable to get policy types {resp}")
        return False
    else:
        verboseprint(f"Policy types {resp.text}")
        return resp.json()
def put_policy(ric_name, policy_id):
    threshold = random.randint(10 ** (15 - 1), (10**15) - 1)
    complete_url = base_url_pms + "/policies"
    headers = {"content-type": "application/json"}
    policy_obj = json.loads(policy_data.replace("XXX", str(threshold)))
    body = {
        "ric_id": ric_name,
        "policy_id": policy_id,
        "service_id": SERVICE_NAME,
        "policy_data": policy_obj,
        "policytype_id": type_to_use,
    }
    verboseprint(f"PUT {complete_url} with body {body}")
    resp = requests.put(complete_url, json=body, headers=headers, verify=False)
    if not resp.ok:
        verboseprint(f"Unable to create policy {resp}")
        print(f"Unable to create policy {resp.text}")
        return False
    else:
        print(f"Updating policy: {policy_id} threshold now: {threshold}")
        return True

def get_policy_instances():
    """
    Sends a GET request to the API endpoint `/policy-instances` using the `requests` module.
    If the response is successful (status code 200), it returns the JSON data from the response.
    If the response is not successful, it prints an error message and returns False.

    Returns:
        dict: A dictionary containing the JSON data from the response if the request was successful,
              False otherwise.
    """
    complete_url = f"{base_url_pms}/policy-instances"
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f"Unable to get policy {resp}")
        return False
    else:
        verboseprint(f"Policy {resp.text}")
        return resp.json()

def get_policy_types():
    """
    Sends a GET request to the API endpoint `/policy-types` using the `requests` module.
    If the response is successful (status code 200), it returns the JSON data from the response.
    If the response is not successful, it prints an error message and returns False.

    Returns:
        dict: A dictionary containing the JSON data from the response if the request was successful,
              False otherwise.
    """
    complete_url = f"{base_url_pms}/policy-types"
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f"Unable to get policy {resp}")
        return False
    else:
        verboseprint(f"Policy {resp.text}")
        return resp.json()

def get_policy(policy_id):
    """
    Sends a GET request to the API endpoint `/policies/{policy_id}` using the `requests` module.
    If the response is successful (status code 200), it prints the JSON data from the response
    and returns True. If the response is not successful, it prints an error message and returns False.

    Args:
        policy_id (str): The ID of the policy to retrieve.

    Returns:
        bool: True if the request was successful, False otherwise.
    """
    complete_url = f"{base_url_pms}/policies/{policy_id}"
    resp = requests.get(complete_url)
    if not resp.ok:
        verboseprint(f"Unable to get policy {resp}")
        print(f"Unable to get policy {resp.text}")
        return False
    else:
        verboseprint(f"Policy {resp.text}")
        print(f"Policy {resp.text}")
        return True


# This script is the main entry point for the nonrtric-rapp-helloworld application.
# It defines a number of command line arguments that can be used to configure the
# application, and then uses these arguments to set up the necessary connections
# to the A1 Policy Manager and the rApp Catalogue. Once the connections are set up,
# the script registers the service with the rApp Catalogue, retrieves the available
# policy types from the A1 Policy Manager, and then enters a loop where it periodically
# sends a PUT request to the A1 Policy Manager to update the policy with the specified
# ID. The script can be terminated by pressing Ctrl-C, at which point it prints out
# the current policy instances and exits.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PROG")
    parser.add_argument(
        "--rAppHost", help="The host of the A1 PMS, e.g. http://localhost:9085"
    )
    parser.add_argument("--ricId", help="The ID of the policy type to use")
    parser.add_argument(
        "--pmsHost", help="The host of the A1 PMS, e.g. http://localhost:8081"
    )
    parser.add_argument("--policyId", help="The ID of the policy to use")
    parser.add_argument("--policyTypeId", help="The ID of the policy type to use")
    parser.add_argument(
        "--policyBodyPath", help="The path to the JSON body of the policy to create"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Turn on verbose printing"
    )
    parser.add_argument("--version", action="version", version="%(prog)s 1.1")
    args = vars(parser.parse_args())

    if args["verbose"]:

        def verboseprint(*args, **kwargs):
            print(*args, **kwargs)

    else:
        verboseprint = lambda *a, **k: None  # do-nothing function

    if args["rAppHost"]:
        base_url_rApp_catalogue = args["pmsHost"] + BASE_PATH_rAPP_CATALOGUE
    else:
        base_url_rApp_catalogue = DEFAULT_HOST_rAPP_CATALOGUE + BASE_PATH_rAPP_CATALOGUE

    if args["pmsHost"]:
        base_url_pms = args["pmsHost"] + BASE_PATH_PMS
    else:
        base_url_pms = DEFAULT_HOST_PMS + BASE_PATH_PMS

    if args["ricId"]:
        ric_to_use = args["ricId"]
    else:
        ric_to_use = DEFAULT_RIC_ID

    if args["policyId"]:
        policy_id_to_use = args["policyId"]
    else:
        policy_id_to_use = DEFAULT_POLICY_ID

    if args["policyTypeId"]:
        type_to_use = args["policyTypeId"]
    else:
        type_to_use = DEFAULT_POLICY_TYPE_ID

    if args["policyBodyPath"]:
        body_type_to_use = args["policyTypeId"]
    else:
        body_type_to_use = DEFAULT_POLICY_BODY_PATH

    try:
        rics_from_agent = get_rics_from_agent()
        verboseprint(f"Got RICs from agent: {rics_from_agent}")
    except ConnectionError:
        print(f"A1 Policy Manager is not answering on {base_url_pms}, cannot start!")

    if not os.path.exists("config/config.yaml"):
        print(
            f"Config file config.yaml does not exist, using default configuration or parameters."
        )
    else:
        print(f"Using configurations from config.yaml.")

        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)

        base_url_rApp_catalogue = config["base_url_rApp_catalogue"]
        base_url_pms = config["base_url_pms"]
        type_to_use = config["type_to_use"]
        ric_to_use = config["ric_to_use"]
        body_type_to_use = config["body_type_to_use"]
        body_path_to_use = config["body_path_to_use"]
        policy_id_to_use = config["policy_id_to_use"]

    print(f"base_url_rApp_catalogue: {base_url_rApp_catalogue}")
    print(f"base_url_pms: {base_url_pms}")
    print(f"type_to_use: {type_to_use}")
    print(f"ric_to_use: {ric_to_use}")
    print(f"body_type_to_use: {body_type_to_use}")
    print(f"body_path_to_use: {body_path_to_use}")
    print(f"policy_id_to_use: {policy_id_to_use}")

    with open(body_path_to_use) as json_file:
        policy_data = json_file.read()
        verboseprint(f"Policy body: {policy_data}")

    print(f"Registring in rApp catalog  {SERVICE_NAME}")
    register_service_rApp_catalalogue()
    pprint.pprint(get_policy_types())
    try:
        while True:
            time.sleep(5)
            put_policy(ric_to_use, policy_id_to_use)
    except KeyboardInterrupt:
        pprint.pprint(get_policy_instances())
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
