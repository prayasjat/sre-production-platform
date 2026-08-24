                     USER
                       │
                       │ HTTP request
                       ▼
                Kubernetes Service
                       │
              ┌────────┴────────┐
              ▼                 ▼
        ┌───────────┐      ┌───────────┐
        │ API Pod 1 │      │ API Pod 2 │
        │ FastAPI   │      │ FastAPI   │
        └─────┬─────┘      └─────┬─────┘
              │                  │
              │  /health         │
              │  /ready          │
              │  /metrics       │
              │                  │
              └────────┬─────────┘
                       │
                       ▼
                  Prometheus
                       │
                       │ metrics
                       ▼
                    Grafana
                       │
                       ▼
                  SRE Dashboard


          Kubernetes continuously monitors:
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
        Liveness   Readiness   Resources
            │          │          │
            └──────────┼──────────┘
                       ▼
                  Self Healing


        SRE OPERATIONS
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
      SLO   Runbook  Incident
       │      │       │
       └──────┼───────┘
              ▼
        Reliability
