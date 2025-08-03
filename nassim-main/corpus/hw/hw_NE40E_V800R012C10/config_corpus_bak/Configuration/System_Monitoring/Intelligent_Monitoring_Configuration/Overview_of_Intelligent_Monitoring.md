Overview of Intelligent Monitoring
==================================

Intelligent monitoring analyzes and detects interface traffic data on devices to help quickly locate faults and exceptions. This aids resource allocation and troubleshooting.

#### Basic Functions

Intelligent monitoring consists of intelligent exception identification, intelligent log exception detection, and intelligent resource trend prediction. It reports exception detection results to help users adjust services in advance or quickly locate faults. This aids in ensuring service quality. [Table 1](#EN-US_CONCEPT_0000001463275597__table568532443712) describes the basic functions of intelligent monitoring.

**Table 1** Basic functions of intelligent monitoring
| Basic Function | Overview |
| --- | --- |
| Intelligent exception identification | This function consists of KPI exception identification and silent traffic fault identification. They are implemented based on interface data monitoring.   * KPI exception identification: This function is performed based on KPI data. Each KPI instance acts like a small state machine and determines whether data is abnormal. It then reports abnormal results to help users quickly locate faults. * Silent traffic fault identification: This function monitors device traffic KPIs, analyzes whether traffic increases or decreases sharply, and reports the analysis result to the controller for troubleshooting. It is based on KPI exception identification. |
| Intelligent log exception detection | This function acts like network O&M experts. It involves automatically identifying fault logs from numerous logs. |
| Intelligent resource trend prediction | This function can predict network resource trends by reporting detection results, helping users adjust services in advance or quickly locate faults. It is implemented through the state machine. |



#### Benefits

Intelligent monitoring brings the following benefits to O&M personnel:

* Quickly detect service faults and use existing fault locating methods to identify and rectify them, reducing their impact.
* Monitor device running status and preemptively allocate resources and adjust services, reducing the possibility of service loss.