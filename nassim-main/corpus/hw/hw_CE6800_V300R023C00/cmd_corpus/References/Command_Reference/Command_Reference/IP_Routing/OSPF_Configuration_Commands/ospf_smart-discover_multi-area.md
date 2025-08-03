ospf smart-discover multi-area
==============================

ospf smart-discover multi-area

Function
--------



The **ospf smart-discover multi-area** command enables smart-discover on a multi-area adjacency interface.

The **undo ospf smart-discover multi-area** command disables smart-discover on a multi-area adjacency interface.



By default, smart-discover is disabled on multi-area adjacency interfaces.


Format
------

**ospf smart-discover multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf smart-discover multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *area-id* | Specifies the ID of an OSPF area. The value is an integer. | The value is a decimal integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies the ID of an OSPF area, in the format of an IP address. | The value is in the format X.X.X.X, where each X represents a value from 0 to 255 |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, routers periodically send Hello packets through OSPF interfaces to establish and maintain OSPF neighbor relationships and elect a DR or BDR on a multi-access network (broadcast or NBMA network). However, Hello packets are not sent to neighbors until the Hello timer expires, which slows down the establishment of neighbor relationships and DR or BDR election.To address this problem, run the ospf smart-discover multi-area command to enable smart-discover on a multi-area adjacency interface so that Hello packets are sent to neighbors immediately, regardless of the Hello timer.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Implementation Procedure**

If smart-discover is enabled on a broadcast or NBMA interface, it works as follows:

* If the neighbor status reaches 2-way for the first time or returns to Init from 2-way or a higher state, the smart-discover-capable interface sends Hello packets to its neighbor immediately when detecting that the neighbor's status changes.
* If the interface status of the DR or BDR on the multi-access network changes, the smart-discover-capable interface sends Hello packets within its network segment and participates in DR or BDR election.The fast neighbor relationship establishment process on a P2P or P2MP network is similar to that on a broadcast or NBMA network.

**Configuration Impact**

The interval at which Hello packets are sent is determined by the interval at which Hello packets are sent.

**Precautions**

The default interval for sending Hello packets varies according to the network type.


Example
-------

# Enable smart-discover on a multi-area adjacency interface.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] area 0
[*HUAWEI-ospf-1-area-0.0.0.0] quit
[*HUAWEI-ospf-1] area 1
[*HUAWEI-ospf-1-area-0.0.0.1] quit
[*HUAWEI-ospf-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf enable 1 area 0
[*HUAWEI-100GE1/0/1] ospf enable multi-area 1
[*HUAWEI-100GE1/0/1] ospf smart-discover multi-area 1

```