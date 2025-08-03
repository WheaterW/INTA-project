traffic-analysis tcp timeout inactive
=====================================

traffic-analysis tcp timeout inactive

Function
--------



The **traffic-analysis tcp timeout inactive** command configures the inactive aging period of a TCP flow in intelligent traffic analysis.

The **undo traffic-analysis tcp timeout inactive** command restores the default configuration.



By default, the inactive aging period of a TCP flow in intelligent traffic analysis is 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-analysis tcp timeout inactive** *inactive-interval*

**undo traffic-analysis tcp timeout inactive** [ *inactive-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *inactive-interval* | Specifies the inactive aging period of a TCP flow in intelligent traffic analysis. | The value is an integer that ranges from 5 to 500. in second. The default value is 30. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the memory capacity of the TAP is limited. Earlier flows in the memory need to be exported to release memory space for new flows. The process of exporting old flows is called aging. Because the storage space of the TAP is also limited, all analyzed flows must be aged out and exported to the TDA for further processing.When the inactive time (from the last packet receiving time to the current time) of a TCP flow in intelligent traffic analysis exceeds the configured inactive aging period, the flow is exported to the specified destination.

**Precautions**

If multiple aging modes are configured on the switch, a flow is aged out when it meets any aging condition.


Example
-------

# Set the inactive aging period of an intelligent traffic analysis flow to 120 seconds for TCP packets.
```
<HUAWEI> system-view
[~HUAWEI] traffic-analysis tcp timeout inactive 120

```