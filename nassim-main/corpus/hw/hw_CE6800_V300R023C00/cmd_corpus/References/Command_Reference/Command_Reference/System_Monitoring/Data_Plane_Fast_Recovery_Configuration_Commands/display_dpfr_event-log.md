display dpfr event-log
======================

display dpfr event-log

Function
--------



The **display dpfr event-log** command displays DPFR logs.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dpfr event-log** [ **recover** | **resource-fail** | **port-status** ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **recover** | Fault link convergence log. | - |
| **resource-fail** | Resource insufficiency log. | - |
| **port-status** | Port status log. | - |
| **slot** *slot-id* | Slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view DPFR logs on the device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DPFR logs.
```
<HUAWEI> display dpfr event-log slot 1
Recover     : Data plane fast failover event.    
ResourceFail: Resource failures causes DPFR function to fail. 
PortStatus  : Port down event.
--------------------------------------------------------------------------------
EventType      Log
--------------------------------------------------------------------------------
recover        DIP:1.1.1.1,srcPort:10GE1/0/1,dstPort:10GE1/0/2
               recover: 2000/12/12 12:00:00 
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display dpfr event-log** command output
| Item | Description |
| --- | --- |
| Recover | Fast convergence of faulty links. |
| PortStatus | Port status log. |
| EventType | Event type. |
| Log | Logs. |
| ResourceFail | Resource insufficiency log. |