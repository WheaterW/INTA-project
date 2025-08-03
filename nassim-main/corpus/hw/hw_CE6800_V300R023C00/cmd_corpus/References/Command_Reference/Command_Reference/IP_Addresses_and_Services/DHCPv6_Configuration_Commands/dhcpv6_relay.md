dhcpv6 relay
============

dhcpv6 relay

Function
--------



The **dhcpv6 relay** command enables the DHCPv6 relay function on interfaces and configures the IPv6 address of the DHCPv6 server or next-hop relay agent.

The **undo dhcpv6 relay** command disables the DHCPv6 relay function on an interface.



By default, the DHCPv6 relay function is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay** { **destination** *ipv6-address* [ **vpn-instance** *vpn-instance-name* | **public-net** ] | **interface** { *interface-type* *interface-number* | *interface-name* } }

**undo dhcpv6 relay** { **destination** *ipv6-address* [ **vpn-instance** *vpn-instance-name* | **public-net** ] | **interface** { *interface-type* *interface-number* | *interface-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **destination** *ipv6-address* | Specifies the destination address of relay messages, which can be the IPv6 address of the DHCPv6 server or next hop relay agent. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance-name* | Specifies a destination VPN instance for DHCPv6 relay messages. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **public-net** | Indicates that the destination VPN instance of the DHCPv6 messages is the public VPN instance. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of the outbound interface of relay messages. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-name* | Specifies the name of the outbound interface of relay packets. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a client applies to a DHCPv6 server on a different network segment for an IPv6 address, you need to deploy a relay agent between the client and the DHCPv6 server. In this manner, the relay agent transmits DHCPv6 messages exchanged between the client and the DHCPv6 server.You can use the **dhcpv6 relay destination** command to enable the DHCPv6 relay function on an interface.


Example
-------

# Enable the DHCPv6 relay function on 100GE1/0/1 and set the destination address of relay messages to fc00:1::1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] dhcpv6 relay destination fc00:1::1

```