ospf cost
=========

ospf cost

Function
--------



The **ospf cost** command sets a cost for an OSPF interface.

The **undo ospf cost** command restores the default cost.



By default, the cost of an OSPF interface is calculated using the following formula: Interface cost = Bandwidth reference value/Interface bandwidth, in which the bandwidth reference value can be changed using the bandwidth-reference command.


Format
------

**ospf cost** *value*

**undo ospf cost**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the cost of an OSPF interface. | The value is an integer ranging from 1 to 65535. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF can automatically calculate the link cost of an interface based on the interface bandwidth or set the link cost using the **ospf cost** command. When there are multiple routes with the same discovery protocol, cost, and destination address, these routes meet the conditions for load balancing. You can determine whether to perform load balancing by changing the interface cost according to the actual networking.If the cost of an OSPF interface is not set using the **ospf cost** command, OSPF automatically calculates the cost of the interface based on the interface bandwidth. The calculation formula is as follows: Cost of an interface = Bandwidth reference value/Interface bandwidth. The integer of the calculation result is used as the cost of the interface. If the calculation result is smaller than 1, the cost of the interface is 1. You can change the interface cost by changing the bandwidth reference value.By default, the bandwidth reference value of OSPF is 100 Mbit/s. For example, according to the formula 100000000/Bandwidth, the default cost of an Ethernet (100 Mbit/s) interface is 1. The cost of a trunk interface is the sum of all member interfaces, and the member interfaces are variable. Therefore, a trunk interface does not have a default cost.

**Precautions**

The **ospf cost** command cannot run on null interfaces.


Example
-------

# Set the cost of an interface that runs OSPF to 65.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf cost 65

```