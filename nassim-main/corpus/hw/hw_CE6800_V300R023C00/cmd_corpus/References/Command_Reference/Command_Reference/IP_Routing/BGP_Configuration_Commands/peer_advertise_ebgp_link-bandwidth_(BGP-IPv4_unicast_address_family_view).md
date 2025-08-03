peer advertise ebgp link-bandwidth (BGP-IPv4 unicast address family view)
=========================================================================

peer advertise ebgp link-bandwidth (BGP-IPv4 unicast address family view)

Function
--------



The **peer advertise ebgp link-bandwidth** command enables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer.

The **undo peer advertise ebgp link-bandwidth** command cancels the existing configuration.



By default, a device cannot advertise the Link Bandwidth extended community attribute to any EBGP peer.


Format
------

**peer** *peerIpv4Addr* **advertise** **ebgp** **link-bandwidth**

**peer** *peerIpv4Addr* **advertise** **ebgp** **link-bandwidth** **disable**

**undo peer** *peerIpv4Addr* **advertise** **ebgp** **link-bandwidth**

**undo peer** *peerIpv4Addr* **advertise** **ebgp** **link-bandwidth** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **disable** | Disables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


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
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] ext-community-change enable
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 advertise-ext-community
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 advertise ebgp link-bandwidth

```