display vbst port-vlan statistics
=================================

display vbst port-vlan statistics

Function
--------



The **display vbst port-vlan statistics** command displays statistics of PV nums.




Format
------

**display vbst port-vlan statistics**


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

The PV number is the total number of VLANs in which VBST has been enabled and into which all VBST-enabled interfaces are added. For example, if VBST is enabled on 10 interfaces and each interface is added into 100 VLANs in which VBST is enabled, the number of PVs occupied by all interfaces on the switch is 1000. If the number of occupied PVs exceeds the specifications, the CPU usage may be high. As a result, the switch cannot process tasks in a timely manner, protocol calculation is affected, and the switch cannot be managed by the NMS.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on the PV number after VBST is enabled on a switch.
```
<HUAWEI> display vbst port-vlan statistics
PV statistics:                                                                                                                      
----------------------------------------------------------                                                                    
Current PV Num         : 4000                                                                                                     
Support PV Num         : 24000                                                                                                    
----------------------------------------------------------

```

**Table 1** Description of the **display vbst port-vlan statistics** command output
| Item | Description |
| --- | --- |
| Current PV Num | Number of PVs occupied by all interfaces. |
| Support PV Num | Maximum number of PVs that can be occupied by all interfaces. |