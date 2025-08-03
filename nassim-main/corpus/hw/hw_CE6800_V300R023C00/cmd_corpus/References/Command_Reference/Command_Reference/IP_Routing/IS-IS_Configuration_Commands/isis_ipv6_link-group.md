isis ipv6 link-group
====================

isis ipv6 link-group

Function
--------



The **isis ipv6 link-group** command binds an IS-IS IPv6 interface to an existing link group.

The **undo isis ipv6 link-group** command unbinds an IS-IS IPv6 interface from a link group.



By default, an IS-IS IPv6 interface is not bound to any link group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**isis ipv6 link-group** *group-name* [ **level-1** | **level-2** ]

**undo isis ipv6 link-group** [ *group-name* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a link group. | The value is a string of 1 to 32 case-sensitive characters. When quotation marks are used around the string, spaces are allowed in the string. |
| **level-1** | Binds a Level-1 IPv6 interface to the link group. | - |
| **level-2** | Binds a Level-2 IPv6 interface to the link group.  If neither level-1 nor level-2 is specified in the command, both Level-1 and Level-2 IPv6 interfaces are bound to the link group. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a link group is created in the IS-IS view, run the **isis link-group** or **isis ipv6 link-group** command to bind a specified interface to the link group for the link group to take effect.

**Prerequisites**

IPv6 IS-IS has been enabled using the isis ipv6 enable command, and a link group has been created using the link-group command.


Example
-------

# Bind 100GE1/0/1 to the link group named link-a.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] link-group link-a
[*HUAWEI-isis-1-link-group-link-a] quit
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-isis-100GE1/0/1] undo portswitch
[*HUAWEI-isis-100GE1/0/1] ipv6 enable
[*HUAWEI-isis-100GE1/0/1] isis ipv6 enable
[*HUAWEI-isis-100GE1/0/1] isis ipv6 link-group link-a

```