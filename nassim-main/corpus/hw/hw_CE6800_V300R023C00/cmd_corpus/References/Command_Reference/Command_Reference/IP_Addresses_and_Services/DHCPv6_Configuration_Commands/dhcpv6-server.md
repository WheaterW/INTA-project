dhcpv6-server
=============

dhcpv6-server

Function
--------



The **dhcpv6-server** command adds a DHCPv6 server or a next-hop relay agent to a DHCPv6 server group.

The **undo dhcpv6-server** command deletes a DHCPv6 server or a next-hop relay agent that is configured in a DHCPv6 server group.



By default, no DHCPv6 server or next-hop relay agent is configured in a DHCPv6 server group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6-server** *ipv6-address* [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**undo dhcpv6-server** *ipv6-address* [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a DHCPv6 server or a next-hop relay agent. | The value has 128 bits. It is represented as eight groups of four hexadecimal digits with the groups being separated by colons, in the format of X:X:X:X:X:X:X:X. |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an outbound interface for DHCPv6 packets. | - |
| *interface-name* | Specifies the name of an outbound interface for DHCPv6 packets. | - |



Views
-----

DHCPv6 server group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dhcpv6-server** command is used on DHCPv6 relay agents. To ensure that the DHCPv6 relay agent can send DHCPv6 packets to multiple DHCPv6 servers, you can configure multiple DHCPv6 servers in a DHCPv6 server group. Multiple DHCPv6 servers can allocate IPv6 addresses and other network configuration information to DHCPv6 clients through the DHCPv6 relay agent.A DHCPv6 client and a DHCPv6 server can have multiple DHCPv6 relay agents connected in between. A device functions as a DHCPv6 relay agent. If the device is connected to a DHCPv6 server, you need to specify the IPv6 address for the DHCPv6 server. If the device is connected to a next-hop relay agent, you need to specify the IPv6 address for the next-hop relay agent and specify the IPv6 address of the remote DHCPv6 server or the next-hop relay agent on the next-hop relay agent.

**Prerequisites**

A DHCPv6 server group has been created using the **dhcpv6 server group** command.

**Precautions**

If a DHCPv6 relay agent is connected to multiple DHCPv6 servers or next-hop relay agents, repeat this step. A maximum of 20 DHCPv6 servers or next-hop relay agents can be connected to the device.If the IPv6 address of a DHCPv6 server or next-hop relay agent is set to a multicast address or a link-local address, an outbound interface must be specified in the **dhcpv6-server** command. Otherwise, it cannot be specified.


Example
-------

# Add the DHCPv6 server at fc00:1::1 to the DHCPv6 server group named dhcp-srv1.
```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 server group dhcp-srv1
Info: It is successful to create a DHCPv6 server group.
[*HUAWEI-dhcpv6-server-group-dhcp-srv1] dhcpv6-server fc00:1::1

```