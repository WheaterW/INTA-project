ospfv3 timer wait
=================

ospfv3 timer wait

Function
--------



The **ospfv3 timer wait** command sets the wait timer on an OSPFv3 interface.

The **undo ospfv3 timer wait** command restores the default value.



By default, on broadcast interfaces, the wait interval is 40 seconds; on NBMA interfaces, it is 120 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 timer wait** *interval* [ **instance** *instance-id* ]

**undo ospfv3 timer wait** [ *interval* ] [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the wait timer on an OSPFv3 interface. | The value is an integer ranging from 1 to 65535. |
| **instance** *instance-id* | Specifies an interface instance ID. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To change the wait timer, run this command. If no Backup Seen event is received within the timer, the designated router (DR) election starts. Setting a proper value for the wait timer can slow down changes of the DR and the backup designated router (BDR) on the network, reducing network flapping. When setting the wait timer, note the following points:

* The wait timer takes effect only on broadcast and NBMA interfaces.
* The value of the wait timer cannot be greater than the value of the dead timer.

**Precautions**

The command cannot be run on a null interface.


Example
-------

# Set the wait timer on an interface to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0
[*HUAWEI-100GE1/0/1] ospfv3 timer wait 30

```