dhcpv6 relay server-select
==========================

dhcpv6 relay server-select

Function
--------



The **dhcpv6 relay server-select** command configures a DHCPv6 server group for a DHCPv6 relay agent.

The **undo dhcpv6 relay server-select** command deletes a DHCPv6 server group for a DHCPv6 relay agent.



By default, no DHCPv6 server group is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay server-select** *group-name*

**undo dhcpv6 relay server-select**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a DHCPv6 server group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported, can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot be "-" or "--". |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used on a DHCPv6 relay agent. When a DHCPv6 client sends DHCPv6 request packets to a DHCPv6 server through a DHCPv6 relay agent, you can run the **dhcpv6 relay server-select** command to specify a DHCPv6 server group for the DHCPv6 relay agent and configure the DHCPv6 server address for the DHCPv6 relay agent.

**Prerequisites**

A DHCPv6 server group has been created using the **dhcpv6 server group** command.The IPv6 function has been enabled using the **ipv6 enable** command in the interface view.

**Precautions**

Each DHCPv6 server group can be bound to multiple interfaces, but each interface can only be bound to one DHCPv6 server group.IP addresses of servers in a DHCPv6 server group cannot be on the same network segment with IP addresses of interfaces on the DHCPv6 relay agent.If you run the **dhcpv6 relay server-select** command multiple times in the same interface view, only the latest configuration takes effect.


Example
-------

# Configure the DHCPv6 server group named group1 for the DHCPv6 relay agent on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcpv6 server group group1
Info: It is successful to create a DHCPv6 server group.
[*HUAWEI-dhcpv6-server-group-group1] dhcpv6-server fc00:1::1
[*HUAWEI-dhcpv6-server-group-group1] quit
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] dhcpv6 relay server-select group1

```