display vbst local
==================

display vbst local

Function
--------



The **display vbst local** command displays information in the VBST internal data area.




Format
------

**display vbst local instance** [ **vlan** *vlan-id* ]

**display vbst local port port-id** *port-id*

**display vbst local port-instance port-id** *port-id*

**display vbst local portlist**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays information about instances in the internal data area of a VBST-enabled VLAN.  If vlan vlan-id is not specified, information about instances in the internal data area of all VBST-enabled VLANs is displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **port** | Displays interface information in the VBST internal data area. | - |
| **port-id** *port-id* | Displays information about instances in the internal data area of a VBST-enabled interface.  If port-id port-id is not specified, information about instances in the internal data area of all VBST-enabled interfaces is displayed. | The value is an integer that ranges from 1 to 2304. |
| **port-instance** | Displays the mapping between VLANs and instances on the interface in the VBST internal data area. | - |
| **portlist** | Displays spanning tree information about the interface list. | - |
| **instance** | Displays information about instances in the VBST internal data area. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display vbst local** command to check instance information in the VBST internal data area, which helps you locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about instances in the internal data area of all VBST-enabled VLANs.
```
<HUAWEI> display vbst local instance
---------------------------------------------------------------- 
VlanID InstID InstIndex StaticFlag VlanCreateFlag SpecialVlanNum 
----------------------------------------------------------------  
    11      2         2          0              1              0 
----------------------------------------------------------------

```

# Display information about the internal data area on port 7 enabled with VBST.
```
<HUAWEI> display vbst local port port-id 7
---------------------------------------------------------------------------
IsUpdated LinkStatus Duplex     Speed(M) PhyType Pvid LinkType  MaxSpeed(M)
---------------------------------------------------------------------------
        0          0      1        25000       0    1        1            0
---------------------------------------------------------------------------

```

# Display the mapping between VLANs and instances of the internal data area on port 7 enabled with VBST.
```
<HUAWEI> display vbst local port-instance port-id 7
--------------------
PortID VlanID InstID
--------------------
     7      1      1
--------------------

```

# Display the mapping between VBST interfaces and physical interfaces.
```
<HUAWEI> display vbst local portlist
--------------------
Ifindex PortID            
-------------
     5      4
     6      5
     7      6
     8      7
     9      8
    10      9
    11     10
-------------

```

**Table 1** Description of the **display vbst local** command output
| Item | Description |
| --- | --- |
| VlanID | VLAN ID. |
| InstID | Instance ID.   * 4094:Reserved instance ID. |
| InstIndex | Instance index. |
| StaticFlag | Whether the instance is created statically.   * 0:Non-static configuration. * 1:Static configuration. |
| VlanCreateFlag | Whether the VLAN is created.   * 0:Not created. * 1:Manual configuration. |
| SpecialVlanNum | Number of special VLANs. |
| IsUpdated | Delivery status.   * 0:Delivery status. * 1:Non-delivery status. |
| LinkStatus | Link status of the interface.   * 0:Link down. * 1:Link up. |
| Duplex | Duplex mode of the interface.   * 1:Full-duplex mode. * 2:Half-duplex mode. |
| Speed(M) | Interface rate. |
| PhyType | Interface type.   * 0: Layer 2 interface. * 1: Layer 3 interface. |
| Pvid | Default VLAN ID of an interface. |
| LinkType | Connection type of the interface.   * 0:Invalid type. * 1:Access. * 2:Trunk. * 3:Hybrid. * 4:QinQ. |
| MaxSpeed(M) | Maximum interface rate in Eth-Trunk members. |
| PortID | Interface ID. |
| Ifindex | Index of the physical interface. |