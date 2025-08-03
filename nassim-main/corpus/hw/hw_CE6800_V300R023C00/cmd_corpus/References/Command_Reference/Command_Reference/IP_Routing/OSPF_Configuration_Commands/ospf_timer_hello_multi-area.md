ospf timer hello multi-area
===========================

ospf timer hello multi-area

Function
--------



The **ospf timer hello multi-area** command configures the interval at which a multi-area adjacency interface sends Hello packets.

The **undo ospf timer hello multi-area** command restores the default interval at which a multi-area adjacency interface sends Hello packets.



By default, a P2P multi-area adjacency interface sends Hello packets at an interval of 10s.


Format
------

**ospf timer hello** *interval* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf timer hello multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which Hello packets are sent by the interface. | The value is an integer ranging from 1 to 65535, in seconds. Setting a value that is larger than 20 for the interval is recommended. If the interval is less than 20s, adjacencies may be interrupted. |
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

OSPF interfaces use Hello packets to establish and maintain adjacencies. A Hello packet includes information about the designated router (DR), backup designated router (BDR), timers, and known neighbors.To set the interval at which Hello packets are sent, run the ospf timer hello multi-area command. The hello interval value will be added to Hello packets. A smaller hello interval value indicates a larger route cost and a higher speed in detecting topology changes. Ensure that parameters on the interface and those on its neighbor are the same.

**Prerequisites**

The **ospf enable multi-area** command has been run.

**Precautions**

The ospf timer hello multi-area command does not apply to null interfaces.


Example
-------

# Configure the interval at which multi-area adjacency interface sends Hello packets to 20s.
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
[*HUAWEI-100GE1/0/1] ospf timer hello 20 multi-area 1

```