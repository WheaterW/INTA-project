peer advertise-large-community (BGP-IPv4 unicast address family view)
=====================================================================

peer advertise-large-community (BGP-IPv4 unicast address family view)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a BGP peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its BGP peer.


Format
------

**peer** *peerIpv4Addr* **advertise-large-community** [ **disable** ]

**undo peer** *peerIpv4Addr* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**

A route-policy has been used to define the large-community attribute.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix 1 permit 10.1.1.0 24
[*HUAWEI] route-policy RP permit node 10
[*HUAWEI-route-policy] if-match ip-prefix 1
[*HUAWEI-route-policy] apply large-community 35551:100:65552 additive
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.2 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 1.1.1.2 advertise-large-community

```