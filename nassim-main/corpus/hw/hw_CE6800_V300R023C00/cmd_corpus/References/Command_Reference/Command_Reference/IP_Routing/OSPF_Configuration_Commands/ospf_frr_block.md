ospf frr block
==============

ospf frr block

Function
--------



The **ospf frr block** command blocks FRR on a specified OSPF interface.

The **undo ospf frr block** command restores the default configuration.



By default, FRR is not blocked on an interface.


Format
------

**ospf frr block**

**undo ospf frr block**


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

To prevent the link that travels through the devices running important services from becoming a backup link, run the ospf frr block command on the devices. In this manner, services on the devices are not affected when FRR calculation is performed.

**Precautions**

Before configuring OSPF IP FRR, run the ospf frr block command to block FRR on a specified interface. In this manner, the link where the interface resides is not calculated as a backup link during FRR calculation.


Example
-------

# Block OSPF IP FRR on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf frr block

```