peer advertise link-bandwidth transitive (BGP-IPv4 unicast address family view)(IPv6)
=====================================================================================

peer advertise link-bandwidth transitive (BGP-IPv4 unicast address family view)(IPv6)

Function
--------



The **peer advertise link-bandwidth transitive** command enables a device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP routes into an optional transitive attribute before advertising the BGP routes to a specified peer.

The **undo peer advertise link-bandwidth transitive** command cancels the existing configuration.



By default, a device cannot convert the Link Bandwidth extended community attribute (optional non-transitive) carried in a BGP route into an optional transitive attribute before advertising the route to a BGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **advertise** **link-bandwidth** **transitive**

**peer** *peerIpv6Addr* **advertise** **link-bandwidth** **transitive** **disable**

**undo peer** *peerIpv6Addr* **advertise** **link-bandwidth** **transitive**

**undo peer** *peerIpv6Addr* **advertise** **link-bandwidth** **transitive** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **disable** | Disables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP routes into an optional transitive attribute before advertising the BGP routes to a specified peer, run the **peer advertise link-bandwidth transitive** command.After a peer is added to a peer group, the peer inherits the configuration of the peer group. If the **peer advertise link-bandwidth transitive** command is run on the local device for the peer group and the newly added peer does not need to inherit this configuration, you need to run the **peer advertise link-bandwidth transitive disable** command on the local device for the peer.

**Precautions**

Before using the **peer advertise link-bandwidth transitive** command to advertise the Link Bandwidth extended community attribute, you need to use a route-policy to add the Link Bandwidth attribute.Currently, this command can process only one Link Bandwidth extended community attribute.After a device receives a route carrying the Link Bandwidth extended community attribute and changes the next hop of the route before advertising the route to other peers, the device deletes the Link Bandwidth extended community attribute and advertises the route to other peers.


Example
-------

# Enable a device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP routes into an optional transitive attribute before advertising the BGP routes to a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] ext-community-change enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 advertise-ext-community
[*HUAWEI-bgp-af-ipv4] peer FE80::1 advertise link-bandwidth transitive

```