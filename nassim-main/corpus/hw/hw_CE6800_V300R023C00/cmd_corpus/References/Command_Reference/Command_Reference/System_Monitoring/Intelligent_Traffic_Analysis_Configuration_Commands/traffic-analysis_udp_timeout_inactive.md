traffic-analysis udp timeout inactive
=====================================

traffic-analysis udp timeout inactive

Function
--------



The **traffic-analysis udp timeout inactive** command configures the inactive aging period of UDP flows.

The **undo traffic-analysis udp timeout inactive** command restores the default configuration.



By default, the inactive aging period of UDP flows is 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis udp timeout inactive** *inactive-interval*

**undo traffic-analysis udp timeout inactive** [ *inactive-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *inactive-interval* | Specifies the inactive aging period of a UDP flow in intelligent traffic analysis. | The value is an integer that ranges from 5 to 500. in seconds. The default value is 30. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After intelligent traffic analysis for UDP flows is enabled, the TAP exports the flow table that contains flow analysis results to the specified TDA for further processing and graphical display of the flow information.When a UDP flow is continuously received, analysis results of the UDP flow are periodically sent to the TDA based on the block granularity. However, when the inactive time (the time from when the last UDP packet is received to the current time) of the UDP flow exceeds the configured inactive aging period, the switch considers that the UDP flow is inactive (the flow is interrupted). In this case, the switch forcibly sends the current flow table to the TDA and deletes it from the switch. This process is called inactive aging.

**Precautions**

If multiple aging modes are configured on the switch, a flow is aged out when it meets any aging condition.


Example
-------

# Set the inactive aging period of UDP flows to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis udp timeout inactive 120

```