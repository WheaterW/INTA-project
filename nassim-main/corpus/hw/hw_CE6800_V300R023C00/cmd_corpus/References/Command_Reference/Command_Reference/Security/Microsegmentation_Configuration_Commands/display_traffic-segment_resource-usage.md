display traffic-segment resource-usage
======================================

display traffic-segment resource-usage

Function
--------



The **display traffic-segment resource-usage** command displays information about chip resources used by an EPG.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display traffic-segment resource-usage**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check chip resource information used by an EPG, run the **display traffic-segment resource-usage** command. This command can only display chip resource information in the inbound direction.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about chip resources used by EPGs.
```
<HUAWEI> display traffic-segment resource-usage
Slot: 1    Chip: 0
------------------------------------------------------------------
Resource              Total        Used         Limit        Free 
------------------------------------------------------------------
TCAM Block               90          66            12          12 
------------------------------------------------------------------
------------------------------------------------------------------
Entry                 Current-Used    Max-Remaining               
------------------------------------------------------------------
EPG Member                       0             7168               
EPG                              0             8192               
GBP                              0            10237               
------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-segment resource-usage** command output
| Item | Description |
| --- | --- |
| Resource | Resource name. |
| Total | Total number of available microsegmentation resources. |
| Used | Number of resources occupied by non-default services. |
| Limit | Number of resources occupied by the default service. |
| Free | Number of remaining resources. |
| TCAM Block | Block resources of the TCAM chip. |
| Entry | Entry name. |
| Current-Used | Number of entries that have been successfully delivered. |
| Max-Remaining | Maximum number of remaining entries. |
| EPG Member | Number of microsegmentation member resources. |
| EPG | Number of microsegmentation group resources. |
| GBP | Microsegmentation traffic control policy. |
| Slot | Slot ID. |
| Chip | Chip ID. |