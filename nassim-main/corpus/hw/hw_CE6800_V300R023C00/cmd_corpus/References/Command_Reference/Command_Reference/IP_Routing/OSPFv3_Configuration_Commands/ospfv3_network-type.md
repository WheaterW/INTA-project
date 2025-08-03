ospfv3 network-type
===================

ospfv3 network-type

Function
--------



The **ospfv3 network-type** command sets the network type for an OSPFv3 interface.

The **undo ospfv3 network-type** command restores the default network type.



By default, the network type of an interface is determined by the physical interface. For details, see "IP Routing" > "OSPFv3 Configuration" > "Configuring OSPFv3 Attributes on Different Types of Networks" > "Configuring the Network Type for an OSPFv3 Interface" in the Configuration Guide.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 network-type** { **broadcast** | **nbma** | **p2mp** [ **non-broadcast** ] | **p2p** } [ **instance** *instance-id* ]

**undo ospfv3 network-type** [ **broadcast** | **nbma** | **p2mp** [ **non-broadcast** ] | **p2p** ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Sets the network type to broadcast. | - |
| **nbma** | Sets the network type to NBMA. | - |
| **p2mp** | Sets the network type to point-to-multipoint. | - |
| **non-broadcast** | Sets the network type to point-to-multipoint non-broadcast. | - |
| **p2p** | Sets the network type to point-to-point. | - |
| **instance** *instance-id* | Specifies an interface instance ID. | The value is an integer ranging from 0 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When link layer protocols remain unchanged, you can change network types and configure OSPF features to flexibly build networks.The network type can be changed from NBMA to broadcast only when a direct virtual circuit is available between any two devices (the network must be fully meshed). If the condition is not met, change the network type to point-to-multipoint. In this manner, two indirectly connected devices can communicate with the help of one or two directly connected and reachable devices. After the network type of the interface is changed to point-to-multipoint, no neighbors need to be configured.If there are only two devices that run OSPF in the same network segment, the network type of an interface can be changed to P2P.

**Prerequisites**

OSPFv3 has been enabled in the interface view using the **ospfv3 area** command.

**Precautions**

OSPFv3 does not support null interfaces.The network types of the OSPFv3 interfaces on both ends of a link must be the same. Otherwise, the neighbor relationship cannot be established.


Example
-------

# Set network type of 100GE 1/0/1 to NBMA.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 network-type nbma

```