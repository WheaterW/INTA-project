display dhcpv6 server group
===========================

display dhcpv6 server group

Function
--------



The **display dhcpv6 server group** command displays the configuration of a DHCPv6 server group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 server group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Displays the configuration of a specified DHCPv6 server group.  If this parameter is not specified, the configuration of all DHCPv6 server groups is displayed. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, and can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" and "--" as names. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCPv6 relay devices. You can run the **display dhcpv6 server group** command to check the configuration of the DHCPv6 server group created on the DHCPv6 relay agent.

**Prerequisites**

DHCPv6 server groups have been configured on the DHCPv6 relay agent using the **dhcpv6 server group** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# View the configuration of the DHCPv6 server group named group1 on the DHCPv6 relay agent.
```
<HUAWEI> display dhcpv6 server group group1
  DHCPv6 Group-name   : group1
    (0)   server-ip   : FC00:1::1
    VPN instance      : vpn1

```

# View the configuration of all the DHCPv6 server groups on the DHCPv6 relay agent.
```
<HUAWEI> display dhcpv6 server group
DHCPv6 server group
--------------------------------------------------------------------------------
  DHCPv6 Group-name   : g1
    (0)   server-ip   : FC00:2::1
    (1)   server-ip   : FC00:2::2
    (2)   server-ip   : FC00:2::3
    (3)   server-ip   : FC00:2::4
    (4)   server-ip   : FC00:2::5
    (5)   server-ip   : FC00:4::1
    VPN instance      : vpn1
  DHCPv6 Group-name   : g2
    (0)   server-ip   : FC00:3::111
    (1)   server-ip   : FC00:3::122
    (2)   server-ip   : FC00:3::123
    (3)   server-ip   : FC00:3::124
    (4)   server-ip   : FC00:3::125
    (5)   server-ip   : FC00:3::126
    (6)   server-ip   : FC00:3::127
    VPN instance      : vpn2
  DHCPv6 Group-name   : g3
    (0)   server-ip   : FC00:3::1
    (1)   server-ip   : FC00:3::2
    (2)   server-ip   : FC00:3::3
    (3)   server-ip   : FC00:3::4
    (4)   server-ip   : FC00:3::5
    (5)   server-ip   : FC00:3::6
    (6)   server-ip   : FC00:3::7
    VPN instance      : vpn3

```

**Table 1** Description of the **display dhcpv6 server group** command output
| Item | Description |
| --- | --- |
| DHCPv6 Group-name | Name of a DHCPv6 server group.  To set this parameter, run the dhcpv6 server group command. |
| server-ip | IPv6 address of a DHCPv6 server in a DHCPv6 server group.  To set this parameter, run the dhcpv6-server command. |
| VPN instance | VPN instance of a DHCPv6 server in a DHCPv6 server group.  To set this parameter, run the vpn-instance command. |