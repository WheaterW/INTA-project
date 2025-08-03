peer advertise ebgp link-bandwidth (BGP-IPv6 unicast address family view)(IPv6)
===============================================================================

peer advertise ebgp link-bandwidth (BGP-IPv6 unicast address family view)(IPv6)

Function
--------



The **peer advertise ebgp link-bandwidth** command enables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer.

The **undo peer advertise ebgp link-bandwidth** command cancels the existing configuration.



By default, a device cannot advertise the Link Bandwidth extended community attribute to any EBGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **advertise** **ebgp** **link-bandwidth**

**peer** *peerIpv6Addr* **advertise** **ebgp** **link-bandwidth** **disable**

**undo peer** *peerIpv6Addr* **advertise** **ebgp** **link-bandwidth**

**undo peer** *peerIpv6Addr* **advertise** **ebgp** **link-bandwidth** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **disable** | Disables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer, run the **peer advertise ebgp link-bandwidth** command.After a peer is added to a peer group, the peer inherits the configuration of the peer group. If the **peer advertise ebgp link-bandwidth** command is run on the local device for the peer group and the newly added peer does not need to inherit this configuration, you need to run the **peer advertise ebgp link-bandwidth disable** command on the local device for the peer.

**Precautions**

Before using the **peer advertise ebgp link-bandwidth** command to advertise the Link Bandwidth extended community attribute, you need to use a route-policy to add the Link Bandwidth attribute.Currently, this command can process only one Link Bandwidth extended community attribute.If a device changes the next-hop address of a received route carrying the Link Bandwidth extended community attribute to its own address, the device deletes this attribute before advertising it to other peers.


Example
-------

# Enable a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] ext-community-change enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 advertise-ext-community
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 advertise ebgp link-bandwidth

```