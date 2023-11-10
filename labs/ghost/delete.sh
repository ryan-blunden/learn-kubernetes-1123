#! /usr/bin/env bash

kubectl delete secret mysql-credentials
kubectl delete secret ghost-credentials
kubectl delete -f mysql.yaml -f ghost.yaml