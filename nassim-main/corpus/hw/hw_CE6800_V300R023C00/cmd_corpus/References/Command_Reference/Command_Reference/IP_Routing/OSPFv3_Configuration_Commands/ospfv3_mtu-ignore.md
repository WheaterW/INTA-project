ospfv3 mtu-ignore
=================

ospfv3 mtu-ignore

Function
--------



The **ospfv3 mtu-ignore** command disables the MTU check on DD packets.

The **undo ospfv3 mtu-ignore** command restores the default configuration.



By default, the MTU check on DD packets is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ospfv3 mtu-ignore** [ **instance** *instance-id* ]

**undo ospfv3 mtu-ignore** [ **instance** *instance-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-id* | Specifies the interface instance ID. | The value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, OSPFv3 checks whether the MTU carried in the DD packet from the neighbor exceeds the local MTU. If the interface MTUs configured on the two devices are different, the OSPF neighbor relationship cannot enter the Full state. In this way, the problem of interface MTU inconsistency can be identified in advance.Non-Huawei devices may use different default MTU settings. If the default MTU check is used, neighbor relationships may fail to be established. To improve device compatibility, run the ospfv3 mtu-ignore command to disable MTU check for DD packets.


Example
-------

# Disable OSPFv3 from checking the MTU of DD packets.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ospfv3 1 area 0 instance 1
[*HUAWEI-100GE1/0/1] ospfv3 mtu-ignore instance 1

```