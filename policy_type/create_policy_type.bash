#!/bin/bash

curl -v -X PUT http://service-ricplt-a1mediator-http.ricplt.svc.cluster.local:10000/A1-P/v2/policytypes/2 \
-H "Content-Type: application/json" \
-d '{
    "name": "hwpolicy",
    "description": "Hellow World policy type",
    "policy_type_id": 2,
    "create_schema": {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "title": "HW Policy",
      "description": "Hello World Policy Type",
      "type": "object",
      "properties": {
        "threshold": {
          "type": "integer",
          "default": 0
        }
      },
      "additionalProperties": false
    }
  }'