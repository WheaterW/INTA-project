reset pim ipv6 routing-table(User View)
=======================================

reset pim ipv6 routing-table(User View)

Function
--------



The **reset pim ipv6 routing-table** command clears PIM status information in IPv6 PIM routing entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset pim ipv6 routing-table all**

**reset pim ipv6 vpn-instance** *instance-name* **routing-table** **all**

**reset pim ipv6 routing-table group** *groupAddr* **mask** *group-mask-length* **source** *sourceAddr*

**reset pim ipv6 vpn-instance** *instance-name* **routing-table** **group** *groupAddr* **mask** *group-mask-length* **source** *sourceAddr*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance to which an IPv6 PIM routing entry belongs. If this parameter is not specified, the command deletes PIM entries of the public network instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Indicates all routing entries. | - |
| **group** *groupAddr* | Specifies the group address of an IPv6 PIM routing entry. | The value is in hexadecimal notation and in the format FFxA:xxxx:xxxx::xxxx, in which x ranges from 0 to F and A is 0 or ranges from 3 to F. |
| **mask** *group-mask-length* | Specifies the mask length of the group address in an IPv6 PIM routing entry. | The value is an integer ranging from 0 to 128. |
| **source** *sourceAddr* | Specifies the source address of an IPv6 PIM routing entry. | The value is in hexadecimal notation. If the specified PIM entry is an (\*, G) entry, the source address is 0::0. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to clear PIM status information in all IPv6 PIM routing entries or a specified IPv6 PIM routing entry. After this command is run, data forwarding of the corresponding PIM routing entry is stopped.


Example
-------

# Delete PIM status information from all IPv6 PIM routing entries.
```
<HUAWEI> reset pim ipv6 routing-table all

```