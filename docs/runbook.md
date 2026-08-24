# Simple SRE API Runbook

## Service

simple-sre-api

## Health Check

GET /health

## Readiness Check

GET /ready

## Metrics

GET /metrics

## Kubernetes Namespace

default

## Check Pods

kubectl get pods

## Check Deployment

kubectl get deployment simple-sre-api

## Check Service

kubectl get svc simple-sre-api

## Check Logs

kubectl logs deployment/simple-sre-api

## Restart Application

kubectl rollout restart deployment simple-sre-api

## Scale Application

kubectl scale deployment simple-sre-api --replicas=3

## Check Events

kubectl get events --sort-by=.lastTimestamp

## Incident Procedure

1. Check pod status.
2. Check application logs.
3. Check readiness/liveness.
4. Check service.
5. Check recent deployments.
6. Check resource usage.
7. Identify root cause.
8. Restore service.
9. Document incident.
