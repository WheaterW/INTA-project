display mice-elephant-flow statistics
=====================================

display mice-elephant-flow statistics

Function
--------



The **display mice-elephant-flow statistics** command displays statistics about mice flows on an interface where differentiated flow scheduling is enabled.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mice-elephant-flow statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about mice flows on a specified interface where differentiated flow scheduling is enabled.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| **interface** *interface-name* | Displays statistics about mice flows on a specified interface where differentiated flow scheduling is enabled.  interface-name specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view statistics about mice flows on an interface where differentiated flow scheduling is enabled, including the number of forwarded packets, packet forwarding rate, number of discarded packets, and packet discarding rate.

**Precautions**

When both iNOF zone isolation and differentiated flow scheduling are configured, statistics about forwarded packets displayed in the **display mice-elephant-flow statistics** command output include the number of packets in mice flows that are discarded due to iNOF zone isolation.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about mice flows on a specified interface where differentiated flow scheduling is enabled. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> display mice-elephant-flow statistics interface 100GE1/0/1
Mice-flow Statistics:
-------------------------------------------------------------------------------------------------
Interface     Passed Packets  Passed Rate(pps)  Drop Packets  Drop Rate(pps)  Drop Time
-------------------------------------------------------------------------------------------------
100GE1/0/1                80                15             0               0  -
-------------------------------------------------------------------------------------------------

```

# Display statistics about mice flows on a specified interface where differentiated flow scheduling is enabled. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> display mice-elephant-flow statistics interface 100GE1/0/1
Mice-flow Statistics:
------------------------------------------------------------------------------------------------------------
Interface         Queue  Passed Packets  Passed Rate(pps)  Drop Packets  Drop Rate(pps)  Drop Time
------------------------------------------------------------------------------------------------------------
100GE1/0/1            0              80                15             0               0  -
------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display mice-elephant-flow statistics** command output
| Item | Description |
| --- | --- |
| Mice-flow Statistics | Mice flow statistics. |
| Interface | Interface. |
| Passed Packets | Number of forwarded packets in mice flows. |
| Passed Rate(pps) | Rate at which packets in mice flows are forwarded. |
| Drop Packets | Number of discarded packets in mice flows. |
| Drop Rate(pps) | Rate at which packets in mice flows are discarded. |
| Drop Time | Time when packets are discarded. |
| Queue | Queue for which differentiated flow scheduling is enabled. |