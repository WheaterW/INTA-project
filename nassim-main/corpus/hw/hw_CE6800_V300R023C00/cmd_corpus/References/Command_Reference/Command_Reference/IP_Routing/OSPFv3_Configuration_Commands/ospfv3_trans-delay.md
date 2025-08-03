ospfv3 trans-delay
==================

ospfv3 trans-delay

Function
--------



The **ospfv3 trans-delay** command sets the delay for transmitting LSA on an interface.

The **undo ospfv3 trans-delay** command restores the default value.



By default, the delay is 1 second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 trans-delay** *interval* [ **instance** *instance-id* ]

**undo ospfv3 trans-delay** [ *interval* ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the delay for transmitting LSAs on an interface. | The value is an integer ranging from 1 to 800 seconds. |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The LSA ages (increased by 1 per second) in the LSDB of the local device, but does not age during transmission. To ensure the correctness of routing information, you need to add a certain delay to the aging time of LSAs before sending them.


Example
-------

# Set the delay for transmitting LSAs on an interface in instance 1 to 3 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 trans-delay 3 instance 1

```