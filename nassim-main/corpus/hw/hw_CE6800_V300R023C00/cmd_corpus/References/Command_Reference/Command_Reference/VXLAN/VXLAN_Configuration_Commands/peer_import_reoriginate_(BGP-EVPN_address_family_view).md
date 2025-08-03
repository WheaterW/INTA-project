peer import reoriginate (BGP-EVPN address family view)
======================================================

peer import reoriginate (BGP-EVPN address family view)

Function
--------



The **peer import reoriginate** command enables a device to add a regeneration flag to the routes received from BGP EVPN peers.

The **undo peer import reoriginate** command restores the default configuration.



By default, a device does not add a regeneration flag to the routes received from BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **import** **reoriginate**

**peer** *peerIpv6Addr* **import** **reoriginate**

**undo peer** *peerIpv4Addr* **import** **reoriginate**

**undo peer** *peerIpv6Addr* **import** **reoriginate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP EVPN peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP EVPN peer. This parameter applies only to the BGP-EVPN address family view. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Data Center Interconnect (DCI) refers to the definition of various solutions for interconnecting data centers. In a DCI solution, a DCI-PE re-originates received EVPN routes before sending them to peers. By default, the function of re-originating labeled routes is disabled. That is, a DCI-PE does not re-encapsulate the routes received from peers. To enable a DCI-PE to re-encapsulate EVPN routes, run the **peer import reoriginate** command to enable the function of re-originating labeled routes.You can query the BGP VPN routing table to check whether a route carries the REGEN capability flag in its attributes. If the route carries this flag, it can be re-originated and re-advertised to the BGP public network.

**Prerequisites**

The device has been enabled to exchange routing information with the specified peer using the **peer enable** command.


Example
-------

# Configure the device to add the regeneration flag to the routes to be received from a BGP EVPN peer in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 import reoriginate

```

# Configure the device to re-originate the routes received from a BGP EVPN IPv6 peer in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:db8:1::1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:db8:1::1 import reoriginate

```