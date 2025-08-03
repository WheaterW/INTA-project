ospf network-type
=================

ospf network-type

Function
--------



The **ospf network-type** command sets the network type for an OSPF interface.

The **undo ospf network-type** command restores the default network type.



By default, the network type of an interface is determined by the physical interface. For details, see "IP Routing" > "OSPF Configuration" > "Configuring OSPF on the NBMA or P2MP Network" > "Configuring Network Types for OSPF Interfaces" in the Configuration Guide.


Format
------

**ospf network-type** { **broadcast** | **p2p** | **p2mp** | **nbma** }

**undo ospf network-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Indicates that the network type of the interface is changed to broadcast. | - |
| **p2p** | Indicates that the network type of the interface is changed to point-to-point. | - |
| **p2mp** | Indicates that the network type of the interface is changed to point-to-multipoint. | - |
| **nbma** | Indicates that the network type of the interface is changed to NBMA. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When link layer protocols remain unchanged, you can change network types and configure OSPF features to flexibly build networks.

* On the broadcast network, if there is a device that does not support multicast addresses, you can change the network type of the interface to NBMA.
* If the network type of the interface is NBMA which is then changed to broadcast, no neighbors need to be configured.The network type can be changed from NBMA to broadcast only when a direct virtual circuit is available between any two devices (the network must be fully meshed). If the condition is not met, change the network type to point-to-multipoint. In this manner, two indirectly connected devices can communicate with the help of one or two directly connected and reachable devices. After the network type of the interface is changed to point-to-multipoint, no neighbors need to be configured.If there are only two devices that run OSPF in the same network segment, the network type of an interface can be changed to P2P.

**Precautions**

* OSPF does not support the configuration on null interfaces.
* When the network type of an interface is NBMA or the network type of an interface is changed to NBMA manually by using this command, you must run the **peer** command to configure the neighbor.
* If the network type of an OSPF interface is NBMA, OSPF does not advertise information about the interface to RSVP-TE. As a result, the TE tunnel that passes through the interface cannot go Up.
* Generally, the network types of OSPF interfaces on both ends of a link must be the same. Otherwise, the two interfaces cannot establish a neighbor relationship.
* The network type of a star topology cannot be set to the P2P type. Otherwise, a deadlock may occur after the Layer 2 link is interrupted and then recovers.


Example
-------

# Set network type of an interface to NBMA.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf network-type nbma

```