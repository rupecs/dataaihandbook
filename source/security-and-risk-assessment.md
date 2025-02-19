# Security and Risk Assessment Overview

In a financial institution like a bank, deploying a machine learning (ML) application into production requires a rigorous security assessment to ensure the system complies with regulatory requirements and maintains the integrity, confidentiality, and availability of sensitive financial data. Below is a comprehensive explanation of what such a security assessment entails:

---

### 1. **Regulatory Compliance and Governance**

- **Identification of Applicable Regulations:**  
  Financial institutions must adhere to strict regulations (e.g., GDPR, PCI DSS, SOX, FFIEC guidelines) that govern data privacy, security, and operational risk. The assessment starts by identifying and mapping relevant legal and regulatory requirements to the ML application.

- **Data Protection and Privacy:**  
  The security assessment ensures that all data handling practices (data collection, storage, processing, and transmission) comply with privacy regulations. This includes data anonymization, encryption (both at rest and in transit), and secure data retention policies.

- **Audit and Reporting Requirements:**  
  The system must support detailed logging and auditing to enable regulatory reporting and forensic analysis. Audit trails should cover data access, model training, and prediction processes.

---

### 2. **Threat Modeling and Risk Assessment**

- **Asset Identification:**  
  Identify all critical assets such as datasets, model weights, training pipelines, and inference endpoints. Understand the value of these assets from both business and security perspectives.

- **Threat Identification:**  
  Enumerate potential threats including:
  - **External threats:** Hackers, adversaries attempting model inversion or data exfiltration.
  - **Internal threats:** Insider misuse or accidental breaches due to misconfigurations.
  - **Adversarial attacks:** Specific to ML such as adversarial examples that could manipulate model predictions.

- **Vulnerability Analysis:**  
  Evaluate the system for vulnerabilities, including insecure API endpoints, unpatched software, and insufficient isolation of components (e.g., segregated development, staging, and production environments).

- **Risk Evaluation:**  
  Quantify risks based on the likelihood and potential impact of each identified threat. Develop risk mitigation strategies that align with the institution’s risk appetite.

---

### 3. **Secure Development Lifecycle (SDL) for ML**

- **Security by Design:**  
  Incorporate security controls from the early stages of model development. This involves secure coding practices, proper access controls, and the use of secure libraries and frameworks.

- **Data Pipeline Security:**  
  Ensure the data ingestion, pre-processing, and model training pipelines have built-in security controls. This includes:
  - **Data validation:** Check for data integrity and potential injection of malicious data.
  - **Encryption:** Secure data during transit and storage.

- **Model Security:**  
  - **Adversarial Robustness:** Implement defenses against adversarial attacks. This might involve adversarial training or monitoring for unusual patterns during inference.
  - **Version Control and Model Provenance:** Maintain a secure audit trail for model versions, ensuring that any changes are tracked and can be audited.

---

### 4. **Infrastructure and Network Security**

- **Segmentation and Isolation:**  
  Deploy the ML application in a segmented network architecture to minimize lateral movement in case of a breach. Use network segmentation to isolate critical components.

- **Access Control:**  
  - **Authentication and Authorization:** Implement strong multi-factor authentication (MFA) and role-based access control (RBAC) to restrict access to the ML system and its data.
  - **Least Privilege:** Ensure that each component, user, and service operates with the minimum level of privileges necessary.

- **Secure API Endpoints:**  
  Use secure communication protocols (e.g., HTTPS/TLS) for all API interactions. Regularly test endpoints for vulnerabilities such as injection flaws or broken authentication.

---

### 5. **Monitoring, Incident Response, and Continuous Assessment**

- **Security Monitoring:**  
  Deploy continuous monitoring tools to track anomalous behavior in real-time. This includes:
  - **Log Aggregation and Analysis:** Collect logs from various components (data pipelines, model training servers, inference endpoints) for real-time analysis.
  - **Intrusion Detection Systems (IDS):** Use IDS/IPS to detect and respond to potential threats.

- **Incident Response Plan:**  
  Develop and regularly update an incident response plan specific to the ML application. This plan should outline the steps to be taken in the event of a breach, including communication, containment, and remediation procedures.

- **Regular Penetration Testing and Audits:**  
  Conduct periodic penetration tests, vulnerability scans, and third-party audits to ensure the system remains secure over time. This includes testing both the ML components and the underlying infrastructure.

---

### 6. **Documentation and Training**

- **Comprehensive Documentation:**  
  Maintain detailed documentation covering:
  - The system architecture and data flow.
  - Security controls in place.
  - Compliance mapping to regulatory requirements.
  - Incident response procedures.

- **Employee Training:**  
  Ensure that all stakeholders, from data scientists to IT staff, are trained on the secure handling of data, recognizing security threats, and following best practices for ML security.

---

### Conclusion

A thorough security assessment for a productionized ML application in a bank is not a one-time activity but an ongoing process. It involves understanding regulatory requirements, identifying and mitigating risks, embedding security into every stage of development, securing the infrastructure, continuous monitoring, and having a robust incident response plan. By taking these comprehensive measures, a financial institution can safeguard its ML applications against threats while complying with regulatory mandates and ensuring the integrity and trustworthiness of its systems.


# Data Classifiction Standars

Yes, there is a commonly used approach known as a **data classification matrix** that helps organizations, especially in highly regulated environments like banks, to categorize data based on sensitivity, value, and the impact that its compromise could have. This classification is fundamental to ensuring that the appropriate security controls are applied to different types of data.

Below is an example of a data classification matrix:

| **Classification Level**  | **Description**                                                                                                            | **Examples**                                       | **Handling Requirements**                                                                                   |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Public**                | Data intended for public disclosure; its release poses no risk to the organization or its customers.                      | Press releases, marketing materials, published reports | Minimal security; can be freely shared; minimal access controls.                                             |
| **Internal / Unclassified**  | Data meant for internal use only; while not highly sensitive, its unauthorized disclosure could still have a minor impact.  | Internal policies, non-sensitive operational documents, basic employee directories | Limited access; internal distribution only; moderate controls and monitoring.                              |
| **Confidential**          | Sensitive data that, if compromised, could result in financial or reputational damage; requires significant protection.    | Customer data, account numbers, internal financial reports, non-public business plans | Strong access controls; encryption at rest and in transit; rigorous monitoring and logging; restricted sharing. |
| **Restricted / Highly Confidential** | Data whose unauthorized disclosure, modification, or loss could cause severe harm, such as significant financial loss or regulatory penalties. | Personally Identifiable Information (PII), proprietary algorithms, trade secrets, sensitive regulatory data | Highest level of security; strict access controls, multi-factor authentication; comprehensive audit trails; stringent encryption and data handling procedures. |

### Key Considerations in Data Classification:

1. **Regulatory Requirements:**  
   Ensure that the classification aligns with legal and regulatory mandates (e.g., GDPR, PCI DSS) regarding the handling and protection of data, especially for customer information and sensitive financial data.

2. **Risk Impact:**  
   Evaluate the potential impact (financial, reputational, operational) if the data were compromised. This risk assessment informs the level of protection needed.

3. **Data Lifecycle:**  
   Consider how data is collected, stored, processed, and transmitted. Each stage should reflect the appropriate classification level and corresponding security measures.

4. **Access Control:**  
   Define who within the organization can access data at each classification level. For example, only specific roles might have access to Restricted or Highly Confidential data.

5. **Encryption and Storage:**  
   Apply suitable encryption protocols for both data at rest and in transit, especially for confidential and restricted data.

6. **Audit and Monitoring:**  
   Implement logging and monitoring to track access and modifications. This is particularly critical for highly sensitive data to ensure compliance and for rapid incident response.

By applying a data classification matrix, banks and financial institutions can clearly define policies, implement appropriate security measures, and ensure that data is handled in a manner that minimizes risk while complying with industry and regulatory standards.

# Application Classification Standars

Banks typically use a risk matrix to classify applications based on the potential impact of a security breach or failure and the likelihood of such an event occurring. This systematic approach enables the institution to prioritize remediation efforts and implement security controls that are commensurate with the risk level. Below is an explanation of how applications are classified in a bank using a risk matrix:

---

### 1. **Risk Matrix Dimensions**

A typical risk matrix has two key dimensions:

- **Likelihood (Probability):**  
  This axis assesses how likely it is that a threat will exploit a vulnerability in the application. It often includes categories such as Low, Medium, and High.

- **Impact (Consequence):**  
  This axis evaluates the potential severity of the consequences if an incident occurs. Impact might be measured in terms of financial loss, reputational damage, regulatory implications, and operational disruption. Again, common categories are Low, Medium, and High.

---

### 2. **Risk Matrix Example**

Here’s an example of a simple risk matrix:

|                   | **Low Impact**               | **Medium Impact**                     | **High Impact**                      |
|-------------------|------------------------------|---------------------------------------|--------------------------------------|
| **Low Likelihood**  | Low Risk (Tolerable)         | Medium Risk (Mitigate)                | High Risk (Mitigate and Monitor)     |
| **Medium Likelihood** | Medium Risk (Mitigate)       | High Risk (Mitigate and Monitor)      | Very High Risk (Immediate Action)    |
| **High Likelihood**   | High Risk (Mitigate and Monitor) | Very High Risk (Immediate Action)     | Critical Risk (Immediate Action)     |

---

### 3. **Classification Process**

The process of classifying applications using the risk matrix typically involves the following steps:

1. **Asset Identification:**  
   Identify all applications and understand their purpose, data processed, and business impact. This includes customer-facing apps, internal systems, and third-party integrations.

2. **Threat and Vulnerability Analysis:**  
   Analyze potential threats (e.g., cyberattacks, insider threats) and vulnerabilities (e.g., outdated libraries, weak authentication). Determine how likely these threats are to materialize against the application's vulnerabilities.

3. **Assessing Impact:**  
   Evaluate the impact if an application were compromised. Factors include:
   - **Financial Impact:** Direct costs, fines, or loss of revenue.
   - **Reputational Impact:** Loss of customer trust or market share.
   - **Operational Impact:** Disruption to services or critical business processes.
   - **Regulatory Impact:** Breach of compliance requirements leading to legal consequences.

4. **Determining Likelihood:**  
   Consider historical data, threat intelligence, and the current security posture to estimate how likely a threat is to occur. Factors might include exposure to the internet, known vulnerabilities, and security controls already in place.

5. **Assigning a Risk Rating:**  
   Based on the above assessments, assign each application a risk rating (e.g., Low, Medium, High, Very High, or Critical). This rating is derived from the intersection of the likelihood and impact scores on the risk matrix.

---

### 4. **Application Examples**

- **Critical Banking Applications:**  
  Applications that handle core banking operations, customer transactions, or sensitive personal data typically fall into the **High or Critical** risk categories. They require robust security measures, frequent monitoring, and immediate remediation actions in the event of a threat.

- **Internal Support Applications:**  
  Applications used for non-critical functions (such as internal scheduling or HR systems) might be classified as **Medium or Low risk**, assuming they do not handle sensitive financial data or personally identifiable information (PII). However, they still need to adhere to baseline security standards.

- **Third-Party Integrations:**  
  These may also vary in risk depending on the data shared and the security posture of the third party. The bank may consider these applications as **Medium or High risk** if there is potential for data leakage or compliance issues.

---

### 5. **Remediation and Controls Based on Risk Levels**

- **Low Risk:**  
  Standard monitoring and periodic reviews are sufficient. Minimal security controls might be acceptable given the low likelihood and impact.

- **Medium Risk:**  
  Requires more active monitoring, regular vulnerability assessments, and enhanced security controls such as stronger access management and encryption.

- **High / Very High / Critical Risk:**  
  Demands immediate remediation, advanced threat detection measures, stringent access controls, and regular penetration testing. Incident response plans should be in place, and senior management might need to be informed about any risks identified.

---

### 6. **Ongoing Risk Management**

The risk classification isn’t static—banks continuously reassess the risk levels as threat landscapes evolve, business priorities change, or new vulnerabilities are discovered. This proactive approach ensures that all applications remain secure and compliant with regulatory requirements.

---

In summary, by classifying applications through a risk matrix, banks can systematically evaluate and prioritize risks, ensuring that the most critical systems receive the highest level of protection and immediate attention if any vulnerabilities or threats are detected.

# Sample Risk Assessment 

Below is the updated risk assessment document that now includes an **Application Classification Estimate** section. This section evaluates the overall application risk based on the architecture, data sensitivity, and security controls implemented throughout the project lifecycle.

---

# Comprehensive Risk Assessment Document

**Project Title:**  
Predictive Model for Retail Banking Customer Defaults

**Project Scenario:**  
A predictive model is being developed to identify retail banking customers likely to default in the next 3–6 months. This involves collecting sensitive customer data, processing it through various GCP services, training the model, and deploying it in production—all in strict compliance with APRA’s regulatory standards.

---

## 1. Project Overview and Data Classification

### 1.1 Scenario  
- **Objective:**  
  Identify customers likely to default by leveraging historical and real-time data.  
- **Components:**  
  - Data ingestion using Cloud Storage and Cloud Pub/Sub.  
  - Data processing and feature engineering using Cloud Dataflow and BigQuery.  
  - Model development using Vertex AI.  
  - Model productionization using containerization and deployment on Google Kubernetes Engine (GKE).

### 1.2 Data Classification & Handling

1. **Customer Data**  
   - **Classification:** Highly Sensitive (Confidential)  
   - **Handling:**  
     - Encrypt data at rest using Customer-Managed Encryption Keys (CMEK) via Cloud KMS.  
     - Encrypt data in transit using HTTPS/TLS.  
     - Apply strict IAM policies and maintain comprehensive logging and audit trails.

2. **Intermediate Data & Features**  
   - **Classification:** Sensitive  
   - **Handling:**  
     - Use data masking and tokenization.  
     - Ensure secure storage (encryption in transit and at rest).

3. **Machine Learning Model**  
   - **Classification:** Critical  
   - **Handling:**  
     - Subject the model to rigorous validation, version control, and continuous monitoring.  
     - Ensure model artifacts and training logs are secured with encryption and strict access controls.

---

## 2. Application Classification Estimate

### 2.1 Overview  
Given the nature of the application—which handles highly sensitive customer data, processes it through multiple GCP services, and drives high-stakes decision-making—the overall application risk classification is determined by evaluating both the likelihood of potential threats and the impact of a breach or failure.

### 2.2 Risk Matrix for Application Classification

|                       | **Low Impact**                           | **Medium Impact**                              | **High Impact**                              |
|-----------------------|------------------------------------------|------------------------------------------------|----------------------------------------------|
| **Low Likelihood**    | Low Risk (Acceptable)                    | Medium Risk (Mitigate)                         | High Risk (Mitigate & Monitor)               |
| **Medium Likelihood** | Medium Risk (Mitigate)                   | High Risk (Mitigate & Monitor)                 | Very High Risk (Immediate Action Required)   |
| **High Likelihood**   | High Risk (Mitigate & Monitor)           | Very High Risk (Immediate Action Required)     | Critical Risk (Immediate Action Required)    |

### 2.3 Application Risk Estimate  
Based on the following considerations:

- **Data Sensitivity:**  
  The application processes highly sensitive customer data (Highly Sensitive/Confidential), which increases the impact of any data breach.

- **Data Flow Complexity:**  
  Multiple GCP services (Cloud Storage, Pub/Sub, Dataflow, BigQuery, Vertex AI, GKE) introduce additional complexity, thereby increasing the likelihood of misconfiguration or vulnerability if not properly managed.

- **Regulatory Requirements:**  
  Adherence to APRA’s Prudential Standard CPS 234 mandates rigorous security controls, which mitigates some risks but also indicates the critical nature of the application.

- **Security Controls:**  
  Comprehensive encryption (both at rest and in transit), strict IAM/RBAC, secure network configurations, continuous monitoring, and audit logging are in place to reduce overall risk.

**Estimated Classification:**  
Given the above, the overall application classification is determined as **High Risk**.  
- **Likelihood:** Medium – Given robust security controls, the probability of a breach is mitigated but not zero.  
- **Impact:** High – Due to the sensitivity of customer data and the potential for significant financial, operational, and reputational damage if compromised.

This **High Risk** classification necessitates continuous monitoring, periodic re-assessments, and a proactive incident response plan to maintain an acceptable security posture.

---

## 3. Data Ingestion, Processing, and Storage with Security Controls

### 3.1 Step 1: Data Ingestion

#### Cloud Storage
- **Usage:**  
  - Raw customer data files (CSV, JSON, etc.) are uploaded to regionally hosted Cloud Storage buckets.
- **Encryption at Rest:**  
  - Data is encrypted using CMEK via Cloud KMS.
- **Encryption in Transit:**  
  - Data transfers use HTTPS/TLS.
- **Global vs. Local Hosting:**  
  - **Local:** Data stored in a specific region (e.g., Australia Southeast) minimizes latency and meets local residency requirements.  
  - **Global:** Multi-region buckets provide redundancy/disaster recovery with consistent encryption.
- **Access Controls:**  
  - Fine-grained IAM policies restrict bucket access to authorized roles.

#### Cloud Pub/Sub
- **Usage:**  
  - Facilitates real-time ingestion of streaming customer transaction data.
- **Encryption:**  
  - Data in transit is encrypted using TLS.
- **Security:**  
  - IAM policies control access to Pub/Sub topics and subscriptions.

---

### 3.2 Step 2: Data Processing and Feature Engineering

#### Cloud Dataflow
- **Usage:**  
  - Executes ETL operations by reading data from Cloud Storage and Pub/Sub, cleansing and transforming data, and performing feature engineering.
- **Encryption at Rest:**  
  - Intermediate datasets are encrypted using CMEK.
- **Encryption in Transit:**  
  - Dataflow pipelines securely transfer data within the VPC using TLS.
- **Additional Controls:**  
  - **DLP API Integration:** Scans and classifies sensitive data elements to enforce masking or tokenization.  
  - **Network Security:** Dataflow jobs run within secure VPCs with strict egress controls.

#### BigQuery
- **Usage:**  
  - Stores processed data for analytics and model training.
- **Encryption at Rest:**  
  - Data is encrypted by default (option to use CMEK for enhanced control).
- **Encryption in Transit:**  
  - Queries and data transfers are secured with TLS.
- **Access Controls:**  
  - Column-level security, dataset permissions, and audit logging are employed.

---

### 3.3 Step 3: Data Quality and Governance

#### Data Catalog & Metadata Management
- **Usage:**  
  - Maintains metadata and data lineage for governance and compliance.
- **Security:**  
  - Access is controlled via IAM, with all modifications logged for audit purposes.

---

## 4. Model Development and Productionization

### 4.1 Step 4: Model Development with Vertex AI

#### Vertex AI Notebooks and Training
- **Usage:**  
  - Data scientists use Vertex AI Notebooks to explore data from BigQuery, develop, and prototype the model.
- **Training Jobs:**  
  - Managed training jobs run in containerized environments.
- **Encryption & Security:**  
  - Data pulled from BigQuery is encrypted in transit (TLS).  
  - Detailed logging and version control ensure model traceability.

---

### 4.2 Step 5: Model Validation and Testing

#### Validation Pipelines
- **Usage:**  
  - Automated pipelines validate model performance (accuracy, precision, recall) and check for bias.
- **Governance:**  
  - Validation results, logs, and metrics are stored securely with restricted access and audit trails.

---

### 4.3 Step 6: Containerization and Production Deployment with GKE

#### Containerization
- **Usage:**  
  - Package the trained model into Docker containers for consistent deployment.
- **Security:**  
  - Containers are scanned for vulnerabilities and adhere to secure software supply chain best practices.

#### Google Kubernetes Engine (GKE)
- **Usage:**  
  - Deploy the containerized model for production serving.
- **Networking & Security:**  
  - **Cluster Security:** Deployed in private VPCs with pod security and network policies.  
  - **Encryption at Rest:** Kubernetes secrets and persistent volumes are encrypted.  
  - **Encryption in Transit:** Communication is secured using mTLS and HTTPS.  
  - **Ingress & Egress:** HTTPS load balancers provide secure global access; internal communications use private IPs.
- **Access Controls:**  
  - RBAC policies and IAM roles enforce the principle of least privilege.
- **Monitoring:**  
  - Cloud Monitoring & Logging track performance and logs, with automated alerts for anomalies.

---

## 5. Identified Risks, Controls, and Mitigation Strategies

| **Risk ID** | **Risk Description** | **Affected Component** | **Likelihood** | **Impact** | **Controls/Mitigation** |
|-------------|----------------------|------------------------|----------------|------------|-------------------------|
| **R1**      | Unauthorized access to raw customer data | Cloud Storage | Medium | High (Highly Sensitive data compromise) | - Enforce fine-grained IAM policies.<br> - Encrypt data at rest (CMEK) and in transit (HTTPS/TLS).<br> - Regular audits and logging. |
| **R2**      | Data tampering during transit | Cloud Storage & Pub/Sub | Low | High | - Use HTTPS/TLS for all transfers.<br> - Implement integrity checks (hashing). |
| **R3**      | Unauthorized access/manipulation of streaming data | Cloud Pub/Sub | Medium | Medium | - Strict IAM policies for Pub/Sub topics/subscriptions.<br> - TLS encryption.<br> - Monitor logs for anomalies. |
| **R4**      | Leakage of sensitive data during ETL | Cloud Dataflow | Medium | High | - Execute Dataflow jobs in secure VPCs with strict egress controls.<br> - Encrypt intermediate data using CMEK.<br> - Use DLP API for masking/tokenization. |
| **R5**      | Inadequate data governance and lineage tracking | Data Catalog | Low | Medium | - Enforce IAM controls on Data Catalog.<br> - Log all metadata modifications.<br> - Regular reviews of data lineage. |
| **R6**      | Exposure of sensitive data during model training | Vertex AI | Low | High | - Secure data transfers (TLS) from BigQuery to Vertex AI.<br> - Enforce RBAC and IAM.<br> - Monitor training environments and restrict data exports. |
| **R7**      | Model poisoning or adversarial attacks | Vertex AI & Training Pipelines | Medium | Critical | - Implement robust model validation and performance testing.<br> - Monitor training data quality and detect anomalies.<br> - Regular updates and patching. |
| **R8**      | Vulnerabilities in container images | Docker Containers | Medium | High | - Perform vulnerability scans on Docker images before deployment.<br> - Follow secure containerization practices. |
| **R9**      | Insecure communication within/outside GKE clusters | GKE Deployment | Medium | High | - Enforce mTLS and HTTPS.<br> - Deploy GKE in private VPCs with pod/network policies.<br> - Regularly update and patch clusters. |
| **R10**     | Delayed detection of security incidents | Monitoring & Logging (Cloud Monitoring, Audit Logs) | High | High | - Deploy continuous monitoring with Cloud Monitoring and Logging.<br> - Set up automated alerts for anomalies.<br> - Regular testing of the incident response plan. |

---

## 6. Industry Best Practices & Regulatory Alignment

- **Encryption & Key Management:**  
  - Use CMEK via Cloud KMS for Cloud Storage, BigQuery, and Kubernetes persistent volumes.  
  - Ensure all data transfers use TLS/HTTPS; enforce mTLS within GKE.

- **Access Management:**  
  - Apply strict IAM and RBAC policies across all GCP services, adhering to the principle of least privilege.

- **Data Minimization & Governance:**  
  - Only process and store data essential for the predictive model.  
  - Use Data Catalog for complete metadata management.

- **Audit & Monitoring:**  
  - Leverage Cloud Audit Logs, Cloud Monitoring, and Cloud Logging to track data access and movement in compliance with APRA’s CPS 234.

- **Regulatory Compliance:**  
  - Ensure that all operations comply with APRA’s Prudential Standard CPS 234 and relevant local data residency/privacy requirements.  
  - Regular reviews and updated incident response plans are mandatory.

---

## 7. Conclusion and Recommendations

### 7.1 Summary  
This risk assessment incorporates the concrete architectural and operational details of the project—from data ingestion to processing, model development, and production deployment—while ensuring strict adherence to APRA’s data classification and security standards. The overall application is classified as **High Risk** based on the sensitivity of customer data and the potential impact of any breach.

### 7.2 Recommendations & Action Items  
- **Enforce and Audit Access Controls:**  
  Regularly review IAM and RBAC policies on Cloud Storage, Pub/Sub, BigQuery, Vertex AI, and GKE.
- **Regular Vulnerability & Penetration Testing:**  
  Schedule periodic scans and tests across all components.
- **Enhance Incident Response:**  
  Update and test incident response plans regularly for rapid detection and mitigation.
- **Continuous Monitoring:**  
  Ensure that Cloud Monitoring, Logging, and Audit Logs are active 24/7 and integrated with alerting systems.
- **Ongoing Compliance Reviews:**  
  Periodically verify that security measures meet APRA’s standards and address any new regulatory requirements.

---

## 8. Appendices

### Appendix A: Detailed Risk Matrix  
*(Refer to Section 2.2 and Section 5 for details.)*

### Appendix B: Control Checklist  
- **Data Ingestion:** CMEK, HTTPS/TLS, IAM policies  
- **Data Processing:** Secure VPCs, DLP API, encryption for Dataflow and BigQuery  
- **Model Development:** TLS for Vertex AI, detailed logging, version control  
- **Production Deployment:** Secure Docker practices, GKE with mTLS/HTTPS, private VPC, RBAC/IAM  
- **Monitoring:** Cloud Monitoring, Logging, Audit Logs, automated alerts  

### Appendix C: Regulatory and Best Practice References  
- APRA Prudential Standard CPS 234  
- GCP Security Best Practices  
- Industry standards for encryption, access management, and data governance

---

This document, including the **Application Classification Estimate**, should be reviewed periodically and updated to reflect any changes in technology, threat landscape, or regulatory requirements, ensuring continuous alignment with APRA’s security standards and best practices.
