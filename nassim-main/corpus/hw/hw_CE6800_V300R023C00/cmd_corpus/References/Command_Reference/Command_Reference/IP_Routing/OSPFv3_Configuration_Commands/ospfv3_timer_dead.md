ospfv3 timer dead
=================

ospfv3 timer dead

Function
--------



The **ospfv3 timer dead** command sets the dead interval for the OSPFv3 neighbor in the instance to which an interface belongs.

The **undo ospfv3 timer dead** command restores the default value.



By default, the dead interval of OSPFv3 neighbors is 40 seconds on a P2P or broadcast interface, and is 120 seconds on an NBMA or P2MP interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 timer dead** *interval* [ **instance** *instance-id* ]

**undo ospfv3 timer dead** [ *interval* ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a dead interval. | The value is an integer ranging from 1 to 65535. |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer that ranges from 0 to 255. The default value is <b>0</b>. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no Hello packet is received from a neighbor within a dead interval, the neighbor is considered invalid. The dead interval of devices in the same network segment must be consistent.

**Precautions**

* OSPFv3 does not support null interfaces. If the dead interval is less than 10s, the neighbor relationship may be interrupted. Therefore, if dead interval is set to a value less than 10s, the actual dead interval of an OSPFv3 neighbor is greater than or equal to 10s. If the **ospfv3 timer hello** command is run and the conservative parameter is specified to enable the conservative mode of the neighbor dead timer, and the configured neighbor dead interval is less than 10 seconds, the system determines whether the neighbor is invalid based on the configured value.
* The neighbor dead interval cannot be configured on P2MP or NBMA interfaces.

Example
-------

# Set the dead interval for the neighbor in instance 1 to 80 seconds on the interface.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 timer dead 80 instance 1

```