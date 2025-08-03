reset pim ipv6 routing-table
============================

reset pim ipv6 routing-table

Function
--------



The **reset pim ipv6 routing-table** command clears PIM status of the specified downstream interface of the specified IPv6 PIM entry.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset pim ipv6 routing-table group** *groupAddr* **mask** *group-mask-length* **source** *sourceAddr* **interface** { *oif-port-type* *oif-port-num* | *oif-port-name* }

**reset pim ipv6 vpn-instance** *vpn-instance-name* **routing-table** **group** *groupAddr* **mask** *group-mask-length* **source** *sourceAddr* **interface** { *oif-port-type* *oif-port-num* | *oif-port-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mask** *group-mask-length* | Specifies the mask length of an IPv6 multicast group address. | It is an integer ranging from 0 to 128. |
| **source** *sourceAddr* | Specifies the source address of an IPv6 PIM entry. | If the specified PIM entry is an (\*, G) entry, the source address is 0::0. |
| **interface** *oif-port-type* *oif-port-num* | Specifies the type and number of an interface. | - |
| *oif-port-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **group** *groupAddr* | Specifies the group address of an IPv6 PIM entry. | The value is in hexadecimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Clearing PIM status of the downstream interfaces may trigger the sending of corresponding Join/Prune messages, which affects multicast services.Using this command can clear join information about illegal users and stop data forwarding on the specified downstream interfaces of the specified PIM entry.Using this command only can clear the PIM status of the specified interface in a specified PIM entry. The command cannot be used to clear the MLD and static group join status on a specified interface.


Example
-------

# In the public network instance, clear PIM status of the downstream interface 100GE1/0/1 of the (S, G) entry (2001:db8:4::4,FF25::1).
```
<HUAWEI> reset pim ipv6 routing-table group ff25::1 mask 128 source 2001:db8:4::4 interface 100GE 1/0/1

```