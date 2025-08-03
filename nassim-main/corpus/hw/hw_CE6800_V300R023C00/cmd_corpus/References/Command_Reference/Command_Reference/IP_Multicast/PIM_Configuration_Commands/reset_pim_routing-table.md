reset pim routing-table
=======================

reset pim routing-table

Function
--------



The **reset pim routing-table** command clears interface status of the specified PIM routing entry.




Format
------

**reset pim routing-table group** *groupAddr* **mask** { *group-mask-length* | *group-mask-addr* } **source** *sourceAddr* **interface** { *oif-port-type* *oif-port-num* | *oif-port-name* }

**reset pim vpn-instance** *vpn-instance-name* **routing-table** **group** *groupAddr* **mask** { *group-mask-length* | *group-mask-addr* } **source** *sourceAddr* **interface** { *oif-port-type* *oif-port-num* | *oif-port-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mask** | Specifies mask. | - |
| *group-mask-length* | Specifies the mask length of a multicast group address. | The value is an integer ranging from 4 to 32. |
| *group-mask-addr* | Specifies the mask of a multicast group address. | The value ranges from 128.0.0.0 to 255.255.255.255, in dotted decimal notation. |
| **source** *sourceAddr* | Specifies the source address of a PIM entry. | The value is in dotted decimal notation. If the specified PIM entry is a (\*, G) entry, the source address is 0.0.0.0. |
| **interface** *oif-port-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *oif-port-type* | Specifies the type of an interface. | - |
| *oif-port-num* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **group** *groupAddr* | Specifies the group address of a PIM entry. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Clearing PIM status of the downstream interfaces may trigger the sending of corresponding Join/Prune messages, which affects multicast services.Using this command can clear join information about illegal users and stop data forwarding on the specified downstream interfaces.Using this command only can clear the PIM status of the specified interface in a specified PIM entry. The command cannot be used to clear the IGMP and static group join status on a specified interface and the status of the entries generated through the BGP protocol.If vpn-instance is not specified, PIM status of the downstream interface of a specified PIM entry in the public network instance is cleared.


Example
-------

# In the public network instance, clear PIM status of the downstream interface vlanif 1 of the (S, G) entry (1.1.1.1, 225.0.0.1).
```
<HUAWEI> reset pim routing-table group 225.0.0.1 mask 255.255.255.0 source 1.1.1.1 interface Vlanif 1

```