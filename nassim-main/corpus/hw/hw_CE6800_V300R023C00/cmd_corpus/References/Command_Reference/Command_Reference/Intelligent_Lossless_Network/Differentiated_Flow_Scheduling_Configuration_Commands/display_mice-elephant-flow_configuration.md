display mice-elephant-flow configuration
========================================

display mice-elephant-flow configuration

Function
--------



The **display mice-elephant-flow configuration** command displays the configuration of differentiated flow scheduling.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mice-elephant-flow configuration** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **interface** *interface-type* *interface-number* | Displays the configuration of differentiated flow scheduling on a specified interface.   * interface-type specifies the type of an interface. * interface-number specifies the number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check the configuration of differentiated flow scheduling.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of differentiated flow scheduling. (CE6820H, CE6820S, CE6820H-K, CE6863H, CE6863H-K, CE6881H, and CE6881H-K)
```
<HUAWEI> display mice-elephant-flow configuration
Assigned Queues: 1
Adjust to Queue: 2
Scheduling Mode: hybrid
------------------------------------
Interface      Distinguishing Status
------------------------------------
100GE1/0/1     enable
100GE1/0/2     enable
100GE1/0/3     enable
------------------------------------

```

# Display the configuration of differentiated flow scheduling. (CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE8851-32CQ8DQ-P, CE8851K, CE8850-SAN, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> display mice-elephant-flow configuration
Aging Time(ms): 10
Assigned Queues: 1
Mice-flow Packet Number: 200
------------------------------------
Interface      Distinguishing Status
------------------------------------
100GE1/0/1     enable
100GE1/0/2     enable
100GE1/0/3     enable
------------------------------------

```

**Table 1** Description of the **display mice-elephant-flow configuration** command output
| Item | Description |
| --- | --- |
| Assigned Queues | Queue for which differentiated flow scheduling is enabled. |
| Adjust to Queue | Mice-flow queue. The mice flows in the elephant-flow queue where differentiated flow scheduling is enabled are moved to the mice-flow queue. |
| Scheduling Mode | Scheduling mode.  hybrid: indicates the hybrid scheduling mode.  -: The scheduling mode is not configured. |
| Interface | Interface. |
| Distinguishing Status | Enablement status of the interface. |
| Aging Time(ms) | Aging time of flow entries. |
| Mice-flow Packet Number | Number of packets in a mice flow. You can run the mice-flow packet-number <number> command to set the number of packets in a mice flow. The first several (specified by <number>) packets in a flow are identified as a mice flow. |