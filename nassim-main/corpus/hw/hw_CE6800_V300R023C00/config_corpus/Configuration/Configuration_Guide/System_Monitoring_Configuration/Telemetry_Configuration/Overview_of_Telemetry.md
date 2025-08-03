Overview of Telemetry
=====================

Overview of Telemetry

#### Definition

Telemetry is a technology that remotely collects data from physical or virtual devices at a high speed. These devices periodically send interface traffic statistics, CPU usage, and memory usage to collectors in push mode. Compared with the traditional pull mode (question-answer interaction), the push mode provides faster and real-time data collection.


#### Purpose

As the software-defined networking (SDN) scale increases, more and more services need to be carried, and users have placed higher requirements on intelligent SDN O&M. Specifically, monitoring data requires a sampling interval with higher precision, so that microburst traffic can be efficiently detected and adjusted. The monitoring process should have little impact on device functions and performance in order to improve device and network utilization.

Conventional network monitoring methods, such as Simple Network Management Protocol (SNMP) Get and command line interface (CLI), offer low management efficiency and are unable to meet user requirements due to the following disadvantages:

* Pull mode is used to obtain monitoring data from devices. This mode cannot be used to monitor a large number of network nodes, which limits the network growth.
* Generally, a sampling interval is accurate to minute. To improve accuracy, data must be queried more frequently, which increases network node CPU usage, and affects normal device functions.
* Data obtained from monitored network nodes is inaccurate due to network transmission delays.

Therefore, telemetry technology has been developed to implement large-scale and high-performance monitoring on network devices. Through this technology, the intelligent O&M system can manage more devices, monitoring data can be obtained in real time with higher precision, and the monitoring process has little impact on device functions and performance. Telemetry also provides the most important big data basis for fast fault locating and network quality optimization. It converts network quality analysis into big data analytics, effectively supporting intelligent O&M. [Table 1](#EN-US_CONCEPT_0000001563754521__en-us_concept_0275777949_tab_1) compares telemetry and conventional network monitoring modes.

**Table 1** Comparison between telemetry and conventional network monitoring modes
| Item | Telemetry | SNMP Get | SNMP Trap | CLI | Syslog |
| --- | --- | --- | --- | --- | --- |
| Working mode | Push | Pull | Push | Pull | Push |
| Precision | Subseconds | Minutes | Seconds | Minutes | Seconds |
| Structured | Structured using the YANG model | Structured using MIBs | Structured using MIBs | Non-structured | Non-structured |


![](public_sys-resources/note_3.0-en-us.png) 

As described in [Table 1](#EN-US_CONCEPT_0000001563754521__en-us_concept_0275777949_tab_1), although SNMP trap and syslog use the push mode, only traps or events are pushed. Monitoring data such as interface traffic statistics cannot be collected or sent.



#### Benefits

Using telemetry technology, a collector can collect a large amount of device data and send the data to an analyzer for comprehensive analysis. The analyzer sends the results to a controller, which then adjusts device configurations accordingly, enabling you to determine whether the adjusted device status meets expectations in real time.

As shown in [Figure 1](#EN-US_CONCEPT_0000001563754521__en-us_concept_0275777949_fig143311526135620), DeviceA and DeviceB support telemetry. Assume that traffic of DeviceA and DeviceB is transmitted to DeviceC along the paths in green. When the optimal path changes, telemetry-enabled devices can collect data indicators and push them to the collector. The analyzer reads the data indicators stored in the collector, analyzes them and makes appropriate decisions, and sends the results to the controller. The controller then sends the configurations to be adjusted to DeviceA and DeviceB, and the traffic of these devices is then transmitted to DeviceD through the paths in blue. The traffic optimization result can be quickly reported to the operations support system (OSS) and is used to determine whether traffic optimization meets the expectations.

**Figure 1** Diagram of telemetry traffic optimization  
![](figure/en-us_image_0000001563754573.png)

Compared with traditional network monitoring modes, telemetry greatly reduces both the adjustment and feedback delays. It frees you from being affected by traffic path changes and facilitates management and maintenance.