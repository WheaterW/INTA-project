ospf timer dead multi-area
==========================

ospf timer dead multi-area

Function
--------



The **ospf timer dead multi-area** command configures a dead interval of OSPF neighbor relationships for a multi-area adjacency interface.

The **undo ospf timer dead multi-area** command restores the default dead interval.



By default, the dead interval of OSPF neighbor relationships on a P2P multi-area adjacency interface is 40s.


Format
------

**ospf timer dead** *interval* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf timer dead multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the dead timer of OSPF neighbor relationships. | The value is an integer ranging from 1 to 235926000, in seconds. Setting a value that is larger than 20 for the interval is recommended. If the interval is less than 20s, adjacencies may be interrupted. |
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

If an interface does not receive Hello packets from an OSPF neighbor within the dead interval, the interface considers the neighbor Down. The dead interval must be greater than the interval at which Hello packets are sent, and devices on the same network segment must have the same dead interval.By default, the dead interval of OSPF neighbor relationships is four times the interval at which Hello packets are sent.

**Prerequisites**

Run the **ospf enable multi-area** command first.

**Precautions**

The ospf timer dead multi-area command does not apply to null interfaces.


Example
-------

# Set the dead interval of OSPF neighbor relationships to 60s for multi-area adjacency interface.
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
[*HUAWEI-100GE1/0/1] ospf timer dead 60 multi-area 1

```