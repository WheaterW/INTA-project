ospf cost multi-area
====================

ospf cost multi-area

Function
--------



The **ospf cost multi-area** command configures a cost for an OSPF multi-area adjacency interface.

The **undo ospf cost multi-area** command restores the default cost.



By default, the cost is calculated using the Interface cost = Bandwidth reference value/Interface bandwidth formula, in which the bandwidth reference value can be changed using the bandwidth-reference command.


Format
------

**ospf cost** *cost* **multi-area** { *area-id* | *area-id-ipv4* }

**undo ospf cost multi-area** { *area-id* | *area-id-ipv4* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cost* | Specifies a cost. | The value is an integer ranging from 1 to 65535. |
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

OSPF can automatically calculate the link cost of an interface based on the interface bandwidth or have the link cost set using the **ospf cost** command. When there are multiple routes with the same discovery protocol, cost, and destination address, these routes meet the conditions for load balancing. You can determine whether to perform load balancing by changing the interface cost according to the actual networking.If the cost of a multi-area adjacency interface is not set using the **ospf cost multi-area** command, OSPF automatically calculates the cost of the interface based on the interface bandwidth. The calculation formula is as follows: Cost of an interface = Bandwidth reference value/Interface bandwidth. The integer of the calculation result is used as the cost of the interface. If the calculation result is smaller than 1, the cost of the interface is 1. You can change the cost of an interface by changing the bandwidth reference value.By default, the bandwidth reference value of OSPF is 100 Mbit/s, and the cost of an Ethernet (100 Mbit/s) interface is 1.The bandwidth of a trunk interface is the sum of all member interfaces, and the member interfaces are variable. Therefore, the trunk interface does not have a default interface cost.

**Prerequisites**

Run the **ospf enable multi-area** command first.

**Precautions**

OSPF does not support the **ospf cost multi-area** command on null interfaces.


Example
-------

# Set the cost to 65 for multi-area adjacency interface.
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
[*HUAWEI-100GE1/0/1] ospf cost 65 multi-area 1

```