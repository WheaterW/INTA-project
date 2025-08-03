Overview of EVA
===============

Overview of EVA

#### Definition

Event Versus Action (EVA) is a function that uses Python or JSON scripts to analyze and judge data collected by devices and perform troubleshooting based on the analysis and judgment result. You can define the data to be subscribed to, analysis and judgment rules, and troubleshooting strategies in the scripts. For example, you can define in Python or JSON scripts that logs are recorded when the CPU usage and memory usage exceed 90%.

You can use scripts to subscribe to the following data: data subscribed through telemetry, log data, internal data (known as KPI data throughout this document), and alarm data. EVA can also store KPI data generated within a period of time, which can be queried using related commands.


#### Purpose

A network management system (NMS) can subscribe to XPaths in YANG through channels such as telemetry, NETCONF, and RESTCONF to obtain data from its managed YANG-capable devices. By analyzing the data in real time, the NMS can determine whether such a device is faulty and, if it is, quickly send a troubleshooting strategy to the device.

For the devices that are not managed by any NMS, network O&M personnel still use traditional fault locating methods to determine device status. After EVA is enabled on devices, network O&M personnel can use the open programmability capability provided by the devices to locate and troubleshoot faults quickly.

Currently, network O&M personnel use preventive maintenance inspection (PMI) tools to log in to devices one by one and frequently deliver commands to collect data. As a result, the data collection takes a long time, the efficiency is low, a large amount of data is collected, and the formats are inconsistent, leading to a long PMI time and low PMI efficiency. The EVA function supported by the device allows you to write the PMI logic into a script. After the script is loaded and registered, the PMI is automatically performed and the PMI data is automatically saved in a unified format. In this way, the centralized PMI based on the PMI tool is changed to the distributed PMI based on devices, reducing the PMI time and improving the PMI efficiency.