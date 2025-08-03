ospfv3 timer retransmit
=======================

ospfv3 timer retransmit

Function
--------



The **ospfv3 timer retransmit** command sets the interval at which LSAs are retransmitted on an interface.

The **undo ospfv3 timer retransmit** command restores the default value.



By default, the interval at which LSAs are retransmitted on an interface is 5 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 timer retransmit** *interval* [ **instance** *instance-id* ]

**undo ospfv3 timer retransmit** [ *interval* ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which LSAs are retransmitted on an interface. | The value is an integer ranging from 1 to 3600, in seconds. |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer that ranges from 0 to 255. The default value is <b>0</b>. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After sending an LSA to its neighbor, a device needs to wait for the LSAck packet from the neighbor. If the user does not receive the LSAck packet from the neighbor within the nth retransmission interval, the user retransmits the LSA to the neighbor. In the preceding information,Interval at which LSAs are retransmitted for the first time = Configured interval at which LSAs are retransmitted;Interval at which LSAs are retransmitted for the second time = Configured interval at which LSAs are retransmitted;Interval at which LSAs are retransmitted for the third time = Configured interval at which LSAs are retransmitted;Interval for retransmitting LSAs for the fourth time = Configured interval for retransmitting LSAs, that is, interval\*2;Interval for retransmitting LSAs for the fifth time = Configured interval for retransmitting LSAs, that is, interval\*2^2;Interval for retransmitting LSAs for the nth time = Configured interval for retransmitting LSAs, that is, interval\*2^(n-3);If interval\*2^(n-3) is greater than 30, the interval for retransmitting LSAs for the nth time is 30.If the configured interval for retransmitting LSAs is greater than 30s, the interval for retransmitting LSAs for the nth time is equal to the configured interval.The interval for retransmitting LSAs between neighboring devices should not be set too small. Otherwise, unnecessary retransmission occurs.


Example
-------

# Set the interval at which LSAs are retransmitted between a specified interface in instance 1 and its neighboring device to 12 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 timer retransmit 12 instance 1

```