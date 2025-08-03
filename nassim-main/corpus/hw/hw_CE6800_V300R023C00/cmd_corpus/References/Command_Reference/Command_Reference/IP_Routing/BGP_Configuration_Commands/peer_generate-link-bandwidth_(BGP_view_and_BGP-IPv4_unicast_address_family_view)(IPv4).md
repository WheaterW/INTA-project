peer generate-link-bandwidth (BGP view/BGP-IPv4 unicast address family view)(IPv4)
==================================================================================

peer generate-link-bandwidth (BGP view/BGP-IPv4 unicast address family view)(IPv4)

Function
--------



The **peer generate-link-bandwidth** command configures the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate an extended community attribute.

The **undo peer generate-link-bandwidth** command cancels the existing configuration.



By default, the local device is disabled from obtaining the link bandwidth of a specified directly connected EBGP peer.


Format
------

**peer** *peerIpv4Addr* **generate-link-bandwidth**

**peer** *peerIpv4Addr* **generate-link-bandwidth** **disable**

**undo peer** *peerIpv4Addr* **generate-link-bandwidth**

**undo peer** *peerIpv4Addr* **generate-link-bandwidth** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **disable** | Disables a device to obtaining the bandwidth of directly connected EBGP neighbor interfaces. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the actual link bandwidth needs to be obtained and dynamically updated based on the actual bandwidth when routes are available for load balancing, run the **peer generate-link-bandwidth** command to obtain the link bandwidth of directly connected EBGP peer, generate the extended community attribute, and update route information.After a peer is added to a peer group, if the local device is enabled to obtain the link bandwidth of directly connected EBGP peers for the peer group, the peer inherits the configuration of the peer group. If the peer does not need to inherit the configuration of the peer group, disable the function of obtaining the link bandwidth of the directly connected EBGP peer.



**Precautions**



If the peer connect-interface, peer ebgp-max-hop, or ttl command is not run, you can run the **peer generate-link-bandwidth** command to obtain the link bandwidth of the directly connected EBGP peer.




Example
-------

# Configure the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate an extended community attribute.
```
<HUAWEI> system
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.2.1 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.2.1 generate-link-bandwidth

```