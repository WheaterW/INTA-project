Configuring RMON
================

Configuring RMON helps to monitor network status and traffic.

#### Applicable Environment

RMON allows the NMS to remotely manage and monitor devices. It provides traffic statistics and alarm functions.

* Statistics function
  
  Traffic statistics function enables a managed device to periodically or continuously collect traffic statistics on its connected network segment. The statistics include the total number of received packets and the number of received long packets.
* Alarm function
  
  This function allows a managed device to generate a log and send a trap message to the NMS after the managed device finds that a bound variable of a MIB object exceeds the alarm threshold (for example, an interface rate or the percentage of broadcast packets reaches a specific value).

RMON can be used to monitor or collect statistics about traffic on a network segment.

There are no restrictions on the start time of RMON. It can be started to monitor a specific interface, or can be started when the traffic of the sub-network to which an interface connects is suspected of being abnormal. RMON provides two functions:

* Traffic statistics function: is deployed on interfaces that have abnormal traffic.
* Alarm function: is used to measure one or more indexes. After upper and lower thresholds are set for an index, an alarm is generated if the index exceeds the upper threshold or falls below the lower threshold.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

RMON provides traffic statistics and information about abnormalities, but cannot prevent them. Other management methods are required to eliminate the abnormalities.



#### Pre-configuration Tasks

Before configuring RMON, complete the following task:

* Configuring basic SNMP functions

#### Data Preparation

| No. | Data |
| --- | --- |
| 1 | Name of the interface on which the traffic statistics function needs to be enabled and traffic statistics parameters |
| 2 | Alarm thresholds |



[Configuring the RMON Statistics Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rmon_cfg_0006.html)

Configuring the RMON statistics function helps to collect and record statistics of an interface.

[Configuring the RMON Alarm Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rmon_cfg_0007.html)

After the RMON alarm function is configured on a device, the device will generate a log or an alarm if the sampling value exceeds the alarm threshold.

[Verifying the RMON Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rmon_cfg_0008.html)

After configuring RMON, you can view the traffic statistics collected by RMON.