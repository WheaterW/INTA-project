dhcpv6 relay advertise prefix-delegation route
==============================================

dhcpv6 relay advertise prefix-delegation route

Function
--------



The **dhcpv6 relay advertise prefix-delegation route** command enables a DHCPv6 relay agent to forward routing information of DHCPv6 prefix delegation (DHCPv6 PD) terminals.

The **undo dhcpv6 relay advertise prefix-delegation route** command disables a DHCPv6 relay agent from forwarding routing information of DHCPv6 PD terminals.



By default, a DHCPv6 relay agent does not forward routing information of DHCPv6 PD terminals.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay advertise prefix-delegation route**

**undo dhcpv6 relay advertise prefix-delegation route**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dhcpv6 relay advertise prefix-delegation route** command is used on DHCPv6 relay agents. DHCPv6 PD terminals cannot advertise IPv6 routes. This command enables a DHCPv6 relay agent to add routes of DHCPv6 PD terminals to the routing table when DHCPv6 PD terminals apply for IP addresses from the DHCPv6 server through the DHCPv6 relay agent. The DHCPv6 relay agent then forwards the routing information to the DHCPv6 server.

**Prerequisites**

The DHCPv6 relay function has been enabled on the interface using the **dhcpv6 relay destination** or **dhcpv6 relay server-select** command.

**Precautions**

This command takes effect only for the first-hop DHCPv6 relay agent connected to DHCPv6 PD terminals.


Example
-------

# Enable 100GE1/0/1 to forward routing information of DHCPv6 PD terminals.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] dhcpv6 relay destination FC00::1:3
[*HUAWEI-100GE1/0/1] dhcpv6 relay advertise prefix-delegation route

```