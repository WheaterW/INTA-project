vpn-instance (DHCP server group view)
=====================================

vpn-instance (DHCP server group view)

Function
--------



The **vpn-instance** command binds a DHCP server group to a VPN instance.

The **undo vpn-instance** command unbinds a DHCP server group from a VPN instance.



By default, no DHCP server group is bound to a VPN instance.


Format
------

**vpn-instance** *vpn-instance-name*

**undo vpn-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

DHCP server group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP relay agents. To apply DHCP services in a VPN instance, you need to run the **vpn-instance** command to bind the created DHCP server group to the VPN instance.

**Prerequisites**

A VPN instance has been created using the **ip vpn-instance** command.

**Configuration Impact**

After the **undo vpn-instance** command is run to unbind a DHCP server from a VPN instance, the assigned IP addresses will be released from the DHCP server address pool.

**Precautions**

The VPN instance bound to the DHCP server group on the DHCP relay agent must be the same as the VPN instance bound to the IP address pool on the DHCP server; otherwise, users in the IP address pool cannot go online.


Example
-------

# Bind the DHCP server group dhcp-srv1 to the VPN instance vpn-1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-dhcp-vpn1] ipv4-family
[*HUAWEI-vpn-instance-dhcp-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-dhcp-vpn1] quit
[*HUAWEI] dhcp relay server group dhcp-srv1
[*HUAWEI-dhcp-server-group-dhcp-srv1] vpn-instance vpn1

```