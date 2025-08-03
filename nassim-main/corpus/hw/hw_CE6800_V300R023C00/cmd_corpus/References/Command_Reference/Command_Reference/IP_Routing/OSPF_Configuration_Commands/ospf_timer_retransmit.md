ospf timer retransmit
=====================

ospf timer retransmit

Function
--------



The **ospf timer retransmit** command sets the interval at which LSAs are retransmitted on an interface.

The **undo ospf timer retransmit** command restores the default value.



The default interval is 5 seconds.


Format
------

**ospf timer retransmit** *interval*

**undo ospf timer retransmit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which LSAs are retransmitted on an interface. | The value is an integer ranging from 1 to 3600, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After sending an LSA to its neighbor, a device needs to wait for the LSAck packet from the neighbor. If the user does not receive the LSAck packet from the neighbor within the nth retransmission interval, the user retransmits the LSA to the neighbor. In the preceding information,Interval at which LSAs are retransmitted for the first time = Configured interval at which LSAs are retransmitted,Interval at which LSAs are retransmitted for the second time = Configured interval at which LSAs are retransmitted,Interval at which LSAs are retransmitted for the third time = Configured interval at which LSAs are retransmitted,Interval for retransmitting LSAs for the fourth time = Configured interval for retransmitting LSAs x 2,Interval at which LSAs are retransmitted for the fifth time = Configured interval at which LSAs are retransmitted x 2^2,...Interval for retransmitting LSAs for the nth time = Configured interval for retransmitting LSAs, that is, interval x 2^(n-3)If interval x 2^(n-3) is greater than 30, the interval for retransmitting LSAs for the nth time is 30.If the configured interval for retransmitting LSAs is greater than 30s, the interval for retransmitting LSAs for the nth time is equal to the configured interval.The interval for retransmitting LSAs between neighboring devices should not be set too small. Otherwise, LSAs are retransmitted unnecessarily.

**Precautions**

The command cannot be run on a null interface.


Example
-------

# Specify the interval at which LSAs are retransmitted between the interface and the adjacent routers to 8 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ospf timer retransmit 8

```