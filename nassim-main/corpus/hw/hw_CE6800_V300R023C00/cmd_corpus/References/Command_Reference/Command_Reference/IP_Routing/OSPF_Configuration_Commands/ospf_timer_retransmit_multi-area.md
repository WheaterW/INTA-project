ospf timer retransmit multi-area
================================

ospf timer retransmit multi-area

Function
--------



The **ospf timer retransmit multi-area** command configures an LSA retransmission interval on a multi-area adjacency interface.

The **undo ospf timer retransmit multi-area** command restores the default LSA retransmission interval.



By default, the LSA retransmission interval on multi-area adjacency interfaces is 5s.


Format
------

**ospf timer retransmit** *interval* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf timer retransmit multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an LSA retransmission interval. | The value is an integer ranging from 1 to 3600, in seconds. |
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

To set up an OSPF neighbor relationship with a neighbor, a device sends an LSA and waits for an LSAck packet from the neighbor. If the device does not receive an LSAck packet within the specified interval, it retransmits the LSA.The LSA retransmission interval must not be too small; otherwise, unnecessary retransmission occurs.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Precautions**

The ospf timer retransmit multi-area command does not apply to null interfaces.


Example
-------

# Set the LSA retransmission interval to 8s on multi-area adjacency interface.
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
[*HUAWEI-100GE1/0/1] ospf timer retransmit 8 multi-area 1

```