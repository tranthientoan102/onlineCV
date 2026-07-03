# DataOps Engineer - Transport for NSW (Job #107915)
**Salary:** $137,551 - $154,055 | **Location:** Macquarie Park NSW | **Closes:** 11:59 PM Wednesday, 8 July 2026

---

## Q1: Describe your key skills and experience, and how they make you a strong fit for this role?

With 12+ years across full-stack development, data engineering, and system integration — including a Master of Data Science from the University of Adelaide — I bring a combination of strong technical depth and real-world delivery experience directly aligned with this DataOps Engineer role.

Data pipeline design and automation is central to my recent work. At eHealth NSW and NSWHP, I designed and deployed Snowflake-based data pipelines using UDFs, stored procedures, tasks, and dynamic tables to automate large-scale clinical data migration into Epic — transforming raw source data into precisely structured HL7 and flat-file formats for ingestion. These pipelines reduced manual intervention significantly, replacing error-prone manual steps with scheduled, monitored automation.

SQL and Python are my primary tools — both used fluently during my day-to-day work. I use Python for ETL scripting, data profiling, and orchestration logic, and SQL (particularly Snowflake SQL) for transformation, validation, and performance-optimised data shaping. I'm comfortable working across the full pipeline lifecycle, from raw extraction to validated, business-ready output.

DevOps and CI/CD have been part of my workflow throughout my career. At NSWHP, I managed Azure Kubernetes clusters, deployments, VMs, SQL servers, and Service Bus resources — owning the operational reliability of live services across NSW Health networks. I've worked hands-on with Docker, Kubernetes, Bash scripting, and CI/CD pipelines to automate deployments, reduce configuration drift, and maintain platform stability.

Beyond the tools, I bring experience working within the NSW Health ecosystem — navigating complex multi-environment setups (DEV, TEST, PROD), understanding clinical data sensitivity, and collaborating across technical and non-technical stakeholders. I'm confident I can adapt quickly with the scope at Transport for NSW and earger to contribute my best.

I'm driven by building things that are reliable, maintainable, and genuinely useful — which aligns directly with TfNSW's goal of keeping data workflows efficient, monitored, and continuously improving.

---

## Q2: Can you describe your experience designing and supporting integrations or APIs in a cloud environment, and how you ensure reliability and secure data exchange?

My most relevant experience here is from eHealth NSW, where I led the design and development of a cloud-native proof-of-concept to replace the existing Mirth Connect + sTunnel integration stack with a single, unified Java service exposing secure REST APIs. The existing architecture was multi-component, operationally heavy, and difficult to version-control. My solution consolidated it into one deployable service with a smaller memory footprint, faster processing, TLS-secured endpoints, and a CI/CD-compatible deployment model — improving both the security posture and the maintainability of the integration layer.

Prior to that, I operated the Mirth Connect and sTunnel configuration across four critical SDPR environments (PJX, REL, SUP, PRD), responsible for transforming and securely routing HL7 messages between healthcare systems. Reliability here was non-negotiable — clinical workflows depended on accurate, timely data flow. I maintained connection stability across NSW Health networks, quickly diagnosing and resolving integration failures to minimise operational impact.

At NSWHP, I managed Azure Service Bus integrations alongside Kubernetes-hosted services, ensuring durable, ordered message delivery between distributed components. I used environment-specific configuration management and structured deployment pipelines to reduce the risk of cross-environment contamination.

Earlier in my career at ZaloPay (a high-volume fintech platform), I built and maintained payment channel integrations with banks via Spring Boot REST APIs — with reliability benchmarked using Gatling load tests I developed myself. I also used Grafana to monitor channel health in real time, enabling proactive incident response.

Across all these contexts, my approach to reliability and security comes down to three things: **defence in depth** (TLS, authentication, environment isolation), **observability** (logging, monitoring, alerting at integration boundaries), and **automation** (CI/CD so that deployments are consistent and human error is minimised). In government and health contexts especially, I treat data exchange security as a first-class design concern, not an afterthought.
