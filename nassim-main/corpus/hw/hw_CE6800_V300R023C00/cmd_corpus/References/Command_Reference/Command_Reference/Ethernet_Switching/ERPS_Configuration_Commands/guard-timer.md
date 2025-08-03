guard-timer
===========

guard-timer

Function
--------



The **guard-timer** command sets the Guard timer of an ERPS ring.

The **undo guard-timer** command restores the default value of the Guard timer.



By default, the Guard timer is 200 centiseconds for the ERPS ring.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**guard-timer** *time-value*

**undo guard-timer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the value of the Guard timer for the ERPS ring. | The value is an integer ranging from 1 to 200, in centiseconds. |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After a faulty link or node recovers, the nodes on the two ends of the link or the faulty node sends ring auto protection switching (R-APS) protocol data units (PDUs) to inform the other nodes of the link or node recovery and starts a Guard timer. Before the timer expires, each involved node does not receive any R-APS PDU to avoid receiving out-of-date R-APS PDUs indicating that the link or node fails. If the involved node receives an RAPS packet indicating that another port fails, the local port enters the Forwarding state.


Example
-------

# Set the Guard timer to 100 centiseconds for ERPS ring 10.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 10
[*HUAWEI-erps-ring10] guard-timer 100

```