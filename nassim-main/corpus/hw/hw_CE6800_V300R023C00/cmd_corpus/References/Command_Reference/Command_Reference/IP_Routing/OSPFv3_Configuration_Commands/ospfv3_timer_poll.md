ospfv3 timer poll
=================

ospfv3 timer poll

Function
--------



The **ospfv3 timer poll** command sets the poll interval at which Hello packets are sent on an NBMA network.

The **undo ospfv3 timer poll** command restores the default value.



The default interval is 120 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 timer poll** *interval* [ **instance** *instance-id* ]

**undo ospfv3 timer poll** [ *interval* ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a poll interval. | The value is an integer ranging from 1 to 65535. |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an NBMA network, after a neighbor becomes invalid, the device sends Hello packets at the polling interval set by the ospfv3 timer poll command. The polling interval must be at least four times the interval for sending Hello packets.

**Precautions**

OSPFv3 does not support null interface configurations.


Example
-------

# Set the poll interval at which Hello packets are sent on an interface to 130 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 timer poll 130

```