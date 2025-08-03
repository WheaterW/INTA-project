ospf p2mp-mask-ignore
=====================

ospf p2mp-mask-ignore

Function
--------



The **ospf p2mp-mask-ignore** command prevents a device from checking the network mask on a Point-to-Multipoint (P2MP) network.

The **undo ospf p2mp-mask-ignore** command configures the device to check the network mask on a P2MP network.



By default, no device on a P2MP network checks the network mask.


Format
------

**ospf p2mp-mask-ignore**

**undo ospf p2mp-mask-ignore**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF checks the network masks carried in Hello packets. If the network mask carried in a received Hello packet is not the same as the network mask of the local device, the Hello packet is discarded.On a P2MP network, when the mask lengths of devices are different, you can use the ospf p2mp-mask-ignore command to prevent the device from checking the network mask in Hello packets. In this manner, the OSPF neighbor relationship can be established.

**Prerequisites**

A non-fully connected Non-Broadcast Multi-Access (NBMA) network has been changed to common P2MP network using the **ospf network-type p2mp** command.


Example
-------

# Prevent the device from checking the network mask on a P2MP network.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf network-type p2mp
[*HUAWEI-100GE1/0/1] ospf p2mp-mask-ignore

```