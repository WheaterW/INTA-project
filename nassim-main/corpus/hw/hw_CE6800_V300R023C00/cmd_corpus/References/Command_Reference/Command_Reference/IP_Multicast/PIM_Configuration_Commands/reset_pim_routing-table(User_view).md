reset pim routing-table(User view)
==================================

reset pim routing-table(User view)

Function
--------



The **reset pim routing-table** command clears PIM status information in PIM routing entries.




Format
------

**reset pim routing-table all**

**reset pim vpn-instance** *vpn-instance-name* **routing-table** **all**

**reset pim routing-table group** *groupAddr* **mask** { *group-mask-length* | *group-mask-addr* } **source** *sourceAddr*

**reset pim vpn-instance** *vpn-instance-name* **routing-table** **group** *groupAddr* **mask** { *group-mask-length* | *group-mask-addr* } **source** *sourceAddr*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which a PIM routing entry belongs. If this parameter is not specified, the command deletes PIM entries of the public network instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all** | Indicates all routing entries. | - |
| **group** *groupAddr* | Specifies the group address of a PIM routing entry. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |
| **mask** { *group-mask-length* | *group-mask-addr* } | Specifies the mask length or mask address of a PIM routing entry group address. | Mask length: The value is an integer that ranges from 4 to 32.  Mask address: The value ranges from 240.0.0.0 to 255.255.255.255, in dotted decimal notation. |
| **source** *sourceAddr* | Specifies the source address of a PIM routing entry. | The value is in dotted decimal notation. If the specified PIM entry is an (\*, G) entry, the source address is 0.0.0.0. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to clear PIM status information in all PIM routing entries or a specified PIM routing entry. After this command is run, data forwarding of the corresponding PIM routing entry is stopped.

**Precautions**

This command clears only the PIM status information of PIM routing entries, but does not clear the IGMP and static group join status information or BGP report entry information.


Example
-------

# Delete PIM status information from all IPv4 PIM routing entries in the public network instance.
```
<HUAWEI> reset pim routing-table all

```