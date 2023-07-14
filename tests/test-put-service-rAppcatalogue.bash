#!/bin/bash

curl -v -X PUT http://rappcatalogueservice.nonrtric.svc.cluster.local:9085/services/HelloWordrApp \
    -H "Content-Type: application/json" \
    -d '{
    "version": "0.1",
    "display_name": "Hello Word rApp",
    "description": "rApp for testing"
    }'