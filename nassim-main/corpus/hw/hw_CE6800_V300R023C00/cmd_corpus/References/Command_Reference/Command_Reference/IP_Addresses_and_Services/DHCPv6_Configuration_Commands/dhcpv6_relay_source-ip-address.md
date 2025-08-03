dhcpv6 relay source-ip-address
==============================

dhcpv6 relay source-ip-address

Function
--------



The **dhcpv6 relay source-ip-address** command configures the source IPv6 address for DHCPv6 messages relayed by a DHCPv6 relay agent.

The **undo dhcpv6 relay source-ip-address** command restores the default source IPv6 address of DHCPv6 messages relayed by a DHCPv6 relay agent.



By default, a DHCPv6 relay agent uses the IPv6 address of the gateway as the source IPv6 address for DHCPv6 messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay source-ip-address** *ipv6-address*

**undo dhcpv6 relay source-ip-address** [ *ipv6-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies a source IPv6 address for DHCPv6 messages relayed by a DHCPv6 relay agent. The address must be the IPv6 address to which a local interface is bound. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To help a DHCPv6 server know the forwarding path of DHCPv6 messages sent from a client and facilitate address allocation and parameter configuration, run the **dhcpv6 relay source-ip-address** command so that DHCPv6 messages relayed by a DHCPv6 relay agent carry the specified source IPv6 address.


Example
-------

# 100GE1/0/1 receives DHCPv6 packets with 2001:db8::1 as the source address.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcpv6 relay destination 2001:db8::1
[*HUAWEI-100GE1/0/1] dhcpv6 relay source-ip-address 2001:db8::1

```