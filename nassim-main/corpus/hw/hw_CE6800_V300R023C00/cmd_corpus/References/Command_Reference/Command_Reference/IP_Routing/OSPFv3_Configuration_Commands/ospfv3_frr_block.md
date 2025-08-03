ospfv3 frr block
================

ospfv3 frr block

Function
--------



The **ospfv3 frr block** command blocks FRR on an OSPFv3 interface.

The **undo ospfv3 frr block** command restores the default configuration.



By default, FRR is not blocked on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 frr block** [ **instance** *instance-id* ]

**undo ospfv3 frr block** [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the instance ID of an interface. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent the link that travels through the devices running important services from becoming a backup link, run the ospfv3 frr block command on the devices. In this manner, services on the devices are not affected when FRR calculation is performed.

**Precautions**

Before configuring OSPFv3 IP FRR, you need to run the ospfv3 frr block command to block FRR on a specified interface. In this manner, the link where the interface resides is not calculated as a backup link during FRR calculation.


Example
-------

# Block OSPFv3 IP FRR on the interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 frr block

```