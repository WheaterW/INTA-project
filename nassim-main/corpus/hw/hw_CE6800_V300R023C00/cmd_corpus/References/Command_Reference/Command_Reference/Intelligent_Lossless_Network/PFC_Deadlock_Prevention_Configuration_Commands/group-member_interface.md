group-member interface
======================

group-member interface

Function
--------



The **group-member interface** command adds specified interfaces to a PFC uplink interface group.

The **undo group-member interface** command removes specified interfaces from a PFC uplink interface group.



By default, no interface is added to a PFC uplink interface group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**group-member interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ] &<1-32>

**undo group-member interface** { *interface-name* | *interface-type* *interface-number* } [ **to** { *interface-name* | *interface-type* *interface-number* } ] &<1-32>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface to be added to a PFC uplink interface group. | - |
| *interface-type* | Specifies the type of interfaces to be added to a PFC uplink interface group. | - |
| *interface-number* | Specifies the number of the interface to be added to a PFC uplink interface group. | - |
| **to** | The to keyword specifies an interface range that includes all interfaces between these two interfaces. | - |



Views
-----

PFC uplink group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a PFC uplink interface group is created on a leaf switch, you can add the leaf switch's interfaces connecting to a spine switch to the PFC uplink interface group. If the system detects that a service flow enters and exits through interfaces in the interface group, the service flow is a high-risk hook-shaped flow that may cause a PFC deadlock.

**Precautions**

* If you run this command multiple times, all the configurations take effect.
* Only physical interfaces can be added to a PFC uplink interface group.
* A maximum of 96 member interfaces can be configured for all PFC uplink interface groups in the system.
* If the to keyword is specified, pay attention to the following points:
  + The start and end interfaces must be of the same type and have the same attribute. For example, they are both interfaces resulting from a split. If they are interfaces resulting from a split, they must belong to the same physical interface.
  + If to is not specified, the preceding limitations do not apply.

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:If you add a physical interface that has been added to an Eth-Trunk to a PFC uplink interface group, PFC deadlock prevention takes effect on the Eth-Trunk.For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:PFC deadlock prevention takes effect on physical interfaces.



Example
-------

# Add 100GE1/0/1 and 100GE1/0/4 to the PFC uplink interface group myuplink.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc uplink group myuplink
[*HUAWEI-dcb-pfc-uplink-group-myuplink] group-member interface 100GE 1/0/1 to 100GE 1/0/4

```