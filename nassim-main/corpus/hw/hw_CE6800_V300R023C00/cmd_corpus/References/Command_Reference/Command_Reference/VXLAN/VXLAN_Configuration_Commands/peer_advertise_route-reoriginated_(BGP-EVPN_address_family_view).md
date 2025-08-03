peer advertise route-reoriginated (BGP-EVPN address family view)
================================================================

peer advertise route-reoriginated (BGP-EVPN address family view)

Function
--------



The **peer advertise route-reoriginated** command configures a device to send the routes that are regenerated in the EVPN or VPNv4/v6 address family to a BGP EVPN peer.

The **undo peer advertise route-reoriginated** command restores the default configuration.



By default, a device does not send the routes that are regenerated in the EVPN or VPNv4/v6 address family to a BGP EVPN peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** }

**peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** **ip**

**peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** }

**peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** **ip**

**peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** **ipv6**

**peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** { **mac** | **mac-ip** | **mac-ipv6** }

**undo peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** { **mac-ip** | **mac** }

**undo peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** **ip**

**undo peer** *peerIpv4Addr* **advertise** **route-reoriginated** **evpn** { **mac-ipv6** | **ipv6** }

**undo peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** **ipv6**

**undo peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** **ip**

**undo peer** *peerIpv6Addr* **advertise** **route-reoriginated** **evpn** { **mac** | **mac-ip** | **mac-ipv6** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| **evpn** | Re-encapsulates the received EVPN routes. | - |
| **mac-ip** | Re-encapsulates the IRB or ARP routes in received EVPN routes. | - |
| **mac** | Re-encapsulates MAC routes in received EVPN routes. | - |
| **ip** | Re-encapsulates received prefix routes. | - |
| **mac-ipv6** | Re-encapsulates the IRBv6 or ND routes in received EVPN routes. | - |
| **ipv6** | Re-encapsulates received IPv6 prefix routes. | - |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The format is X:X:X:X:X:X:X:X. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Data Center Interconnect (DCI) is an umbrella term for various solutions used to interconnect data centers. In a DCI solution, a DCI-PE re-originates received EVPN or VPNv4/v6 routes before sending them to peers.

* After a DCI-PE receives EVPN routes with the VXLAN encapsulation attribute from a data center, the DCI-PE re-originates these EVPN routes and advertises them with the MPLS encapsulation attribute to its BGP EVPN peers on the DCI backbone network.
* After receiving EVPN, VPNv4, or VPNv6 routes with the MPLS encapsulation attribute from BGP EVPN, VPNv4, or VPNv6 peers on the DCI backbone network, the local DCI-PE re-originates these routes and then advertises EVPN routes with the VXLAN encapsulation attribute to the data center side.

You can query the BGP EVPN routing table to check whether a re-originated EVPN route carries the reoriginated flag.

**Prerequisites**

Route information exchange has been enabled between the local device and a specified peer using the **peer enable** command.


Example
-------

# Configure the DCI-PE to send the MAC routes that are regenerated to a BGP EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2.2.2.2 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2.2.2.2 enable
[*HUAWEI-bgp-af-evpn] peer 2.2.2.2 advertise route-reoriginated evpn mac

```

# Configure the border leaf to send the EVPN IPv6 routes that are re-originated to the BGP EVPN IPv6 peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 advertise route-reoriginated evpn ipv6

```

# Configure the DCI-PE to send the ARP routes that are regenerated to a BGP EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn mac-ip

```

# Configure the border leaf to send the EVPN IP routes that are re-originated to the BGP EVPN IPv6 peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 advertise route-reoriginated evpn ip

```