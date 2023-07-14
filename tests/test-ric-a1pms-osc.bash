#!/bin/bash

curl -v -X PUT http://controlpanel.nonrtric.svc.cluster.local:8080/a1-policy/v2/policies \
-H "Content-Type: application/json" \
-d '{
  "ric_id": "ric3",
  "policy_id": "78c9675d-162b-42ae-9d3b-e4304aa35ec1",
  "transient": false,
  "service_id": "curl",
  "policy_data": {
  },
  "status_notification_uri": "",
  "policytype_id": ""
}'
