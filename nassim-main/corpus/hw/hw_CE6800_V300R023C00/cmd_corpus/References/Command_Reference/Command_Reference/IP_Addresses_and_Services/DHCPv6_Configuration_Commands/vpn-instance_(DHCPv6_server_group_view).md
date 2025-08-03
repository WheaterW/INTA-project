vpn-instance (DHCPv6 server group view)
=======================================

vpn-instance (DHCPv6 server group view)

Function
--------



The **vpn-instance** command binds a DHCPv6 server group to a VPN instance.

The **undo vpn-instance** command unbinds a DHCPv6 server group from a VPN instance.



By default, no DHCPv6 server group is bound to a VPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

DHCPv6 server group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCPv6 relay agents. To apply DHCPv6 services in a VPN instance, you need to run the **vpn-instance** command to bind the created DHCPv6 server group to the VPN instance.

**Prerequisites**

A VPN instance has been created using the **ip vpn-instance** command.

**Configuration Impact**

After the **undo vpn-instance** command is run to unbind a DHCPv6 server from a VPN instance, the assigned IP addresses will be released from the DHCPv6 server address pool.

**Precautions**

The VPN instance bound to the DHCPv6 server group on the DHCP relay agent must be the same as the VPN instance bound to the IP address pool on the DHCPv6 server; otherwise, users in the IP address pool cannot go online.


Example
-------

# Bind the DHCPv6 server group dhcp-srv1 to the VPN instance vpn-1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn-1
[*HUAWEI-vpn-instance-vpn-1] ipv6-family
[*HUAWEI-vpn-instance-vpn-1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn-1] quit
[*HUAWEI] dhcpv6 server group dhcp-srv1
Info: It is successful to create a DHCPv6 server group.
[*HUAWEI-dhcpv6-server-group-dhcp-srv1] vpn-instance vpn-1

```