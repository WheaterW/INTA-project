display stp vlan bridge
=======================

display stp vlan bridge

Function
--------



The **display stp vlan bridge** command displays details about the spanning tree of a bridge.




Format
------

**display stp vlan** [ *vlan-id* ] **bridge** { **local** | **root** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays details about the spanning tree of a bridge in a specified VLAN.  If vlan vlan-id is not specified, details about the spanning trees of bridges in all VLANs are displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **local** | Displays details about the spanning tree of the local bridge. | - |
| **root** | Displays details about the spanning tree of the root bridge. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When a device provides many interfaces, running the **display stp** command displays a large amount of information, and it is difficult to find information about the spanning trees of the root and local bridges.Using the display stp bridge command, you can easily view details about the spanning trees of the root and local bridges.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details about the spanning tree of the root bridge running VBST in VLAN 10.
```
<HUAWEI> display stp vlan 10 bridge root
------------------------------------------------------------------------------                                                      
                                     Hello  Max Forward                                                                             
VLANID RootID               RootCost  Time  Age   Delay RootPort                                                                    
------------------------------------------------------------------------------                                                      
    10 4106.0025-9e95-7c21         0     2   20      15                                                                             
------------------------------------------------------------------------------

```

# Display details about the spanning tree of the local bridge running VBST in VLAN 10.
```
<HUAWEI> display stp vlan 10 bridge local
------------------------------------------------------------------              
VLANID BridgeID             HelloTime MaxAge ForwardDelay Protocol              
------------------------------------------------------------------              
    10 32778.0aff-ff5c-6c01         2     20           15     VBST              
------------------------------------------------------------------

```

**Table 1** Description of the **display stp vlan bridge** command output
| Item | Description |
| --- | --- |
| VLANID | VLAN ID. |
| RootID | VBST root bridge ID. |
| RootCost | VBST root path cost. |
| RootPort | Root interface. |
| BridgeID | VBST local bridge ID. |
| HelloTime | Interval at which Bridge Protocol Data Units (BPDUs) are sent from the root switch. |
| MaxAge | Maximum TTL of a BPDU. |
| ForwardDelay | Delay in interface status transition. |
| Protocol | Protocol type. |