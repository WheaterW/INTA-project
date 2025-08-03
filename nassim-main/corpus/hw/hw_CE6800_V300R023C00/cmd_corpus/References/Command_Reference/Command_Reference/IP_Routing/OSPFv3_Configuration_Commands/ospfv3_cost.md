ospfv3 cost
===========

ospfv3 cost

Function
--------



The **ospfv3 cost** command sets a cost for an OSPFv3 interface.

The **undo ospfv3 cost** command restores the default cost.



By default, the cost of an OSPFv3 interface is calculated based on the interface bandwidth.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 cost** *value* [ **instance** *instanceId* ]

**undo ospfv3 cost** [ *value* ] [ **instance** *instanceId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the cost for running OSPFv3. | The value is an integer ranging from 1 to 65535. |
| **instance** *instanceId* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPFv3 can automatically calculate the link cost for an interface based on the interface bandwidth. You can also set the link cost for the interface using the **ospfv3 cost** commands.

**Prerequisites**

OSPFv3 has been enabled in the interface view using the **ospfv3 area** command.

**Configuration Impact**

The **ospfv3 cost** command cannot be run on null interfaces.

**Precautions**

If no cost is set for an OSPFv3 interface using the **ospfv3 cost** command, OSPFv3 automatically calculates its cost based on the interface bandwidth. The calculation formula is as follows: Cost of the interface = Bandwidth reference value/Interface bandwidth. The integer of the calculated result is the cost of the interface. If the calculated result is smaller than 1, the cost is 1. Changing the bandwidth reference value can change the cost of an interface.


Example
-------

# Set the cost for instance 1 to run OSPFv3 to 33.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 cost 33 instance 1

```