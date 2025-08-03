peer advertise-large-community (BGP-MVPN address family view) (BGPMVPN)
=======================================================================

peer advertise-large-community (BGP-MVPN address family view) (BGPMVPN)

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
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer, run the **peer advertise-large-community** command.

**Prerequisites**

A route-policy has been used to define the large-community attribute.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 10
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 advertise-large-community

```