#! /usr/bin/env bash

# Create secrets
kubectl create secret generic mysql-credentials --from-env-file mysql.env
kubectl create secret generic ghost-credentials --from-env-file ghost.env

kubectl apply -f mysql.yaml -f ghost.yaml