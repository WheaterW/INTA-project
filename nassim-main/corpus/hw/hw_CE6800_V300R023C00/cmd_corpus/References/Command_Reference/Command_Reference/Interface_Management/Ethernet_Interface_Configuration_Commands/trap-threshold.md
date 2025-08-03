trap-threshold
==============

trap-threshold

Function
--------



The **trap-threshold input-rate** command sets the alarm threshold for inbound bandwidth usage on an interface.

The **undo trap-threshold input-rate** command restores the default alarm threshold for inbound bandwidth usage on an interface.

The **trap-threshold output-rate** command sets the alarm threshold for outbound bandwidth usage on an interface.

The **undo trap-threshold output-rate** command restores the default alarm threshold for outbound bandwidth usage on an interface.



By default, the alarm threshold for inbound or outbound bandwidth usage is 90%.


Format
------

**trap-threshold input-rate** *bandwidth-in-use* [ **resume-rate** *resume-threshold* ]

**trap-threshold output-rate** *bandwidth-in-use* [ **resume-rate** *resume-threshold* ]

**undo trap-threshold input-rate**

**undo trap-threshold output-rate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **resume-rate** *resume-threshold* | Specifies a clear alarm threshold for outbound bandwidth usage. | The value is an integer ranging from 1 to 100.   * If the resume-rate <outResumeValue> command is not run, the default value of this parameter is 90. * The value of resume-rate <outResumeValue> must be less than or equal to that of resume-rate <outResumeValue>. * If resume-rate <outResumeValue> is not configured, the system automatically sets the clear alarm threshold for bandwidth usage to be the same as the alarm threshold for bandwidth usage. |
| **output-rate** *bandwidth-in-use* | Specifies the outbound bandwidth threshold for generating an alarm. | The value is an integer, ranging from 1 to 100. |
| **input-rate** *bandwidth-in-use* | Specifies the inbound bandwidth threshold for generating an alarm. | The value is an integer, ranging from 1 to 100. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Monitoring bandwidth usage helps you keep track of the load on a device. If the bandwidth usage exceeds a specified threshold, bandwidth resources are insufficient, and the device capacity needs to be expanded. For example, if the bandwidth usage exceeds 95%, an alarm is generated, indicating that bandwidth resources are almost exhausted. As a result, some services may be interrupted before device capacity is expanded. In this case, run the **trap-threshold** command to configure an alarm threshold and a clear alarm threshold for inbound or outbound bandwidth usage. This ensures that device capacity is expanded in advance to prevent service interruption caused by bandwidth exhaustion.The outbound bandwidth usage on an interface is calculated using the following formula: Outbound bandwidth usage (Ratio of the traffic sent by the interface to the total bandwidth of the interface) = (Outbound traffic rate on an interface/Bandwidth of the physical interface) \* 100The inbound bandwidth usage on an interface is calculated using the following formula: Inbound bandwidth usage (Ratio of the traffic received by the interface to the total bandwidth of the interface) = (Inbound traffic rate on an interface/Bandwidth of the physical interface) \* 100Specify parameters in the **trap-threshold** command as required,triggering a log alarm when the threshold is reached.Run the trap-threshold input-rate bandwidth-in-use resume-rate resume-threshold command to set an alarm threshold and a clear alarm threshold for inbound bandwidth usage.

* If the inbound bandwidth usage exceeds the threshold specified by bandwidth-in-use, an hwIfMonitorInputRateRising alarm is generated, indicating that the inbound bandwidth usage exceeds the configured threshold.
* If the inbound bandwidth usage falls below the threshold specified by resume-threshold, an hwIfMonitorInputRateResume alarm is generated, indicating that the inbound bandwidth usage falls below the threshold.Run the trap-threshold output-rate bandwidth-in-use resume-rate resume-threshold command to set an alarm threshold and a clear alarm threshold for outbound bandwidth usage.
* If the outbound bandwidth usage exceeds the threshold specified by bandwidth-in-use, an hwIfMonitorOutputRateRising alarm is generated, indicating that the outbound bandwidth usage exceeds the configured threshold.
* If the outbound bandwidth usage falls below the threshold specified by resume-threshold, an hwIfMonitorOutputRateResume alarm is generated, indicating that the outbound bandwidth usage falls below the threshold.

**Precautions**



To prevent alarms from being frequently generated or cleared, set a large difference between the bandwidth-in-use and resume-threshold values.




Example
-------

# Set an alarm threshold for outbound bandwidth usage to 80% on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] trap-threshold output-rate 80

```

# Restore the default alarm threshold for inbound bandwidth usage on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1
[*HUAWEI-100GE1/0/1.1] undo trap-threshold input-rate

```