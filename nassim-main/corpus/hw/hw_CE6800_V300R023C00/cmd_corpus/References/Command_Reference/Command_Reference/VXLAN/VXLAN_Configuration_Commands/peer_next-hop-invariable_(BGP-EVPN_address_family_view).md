peer next-hop-invariable (BGP-EVPN address family view)
=======================================================

peer next-hop-invariable (BGP-EVPN address family view)

Function
--------



The **peer next-hop-invariable** command enables a BGP EVPN speaker to keep the next hops of routes unchanged when the speaker advertises these routes to EBGP EVPN peers and to apply the original next hops of locally imported routes when the speaker advertises these routes to IBGP EVPN peers.

The **undo peer next-hop-invariable** command restores the default configuration.



By default, the function of keeping the next hops of routes unchanged is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **next-hop-invariable**

**undo peer** *peerIpv4Addr* **next-hop-invariable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default:

* A BGP EVPN speaker changes the next hops of routes to the interface that it uses to establish EBGP EVPN peer relationships before advertising these routes to EBGP EVPN peers.
* A BGP EVPN speaker changes the next hops of routes imported from EBGP EVPN to the interface that it uses to establish IBGP EVPN peer relationships before advertising these routes to IBGP EVPN peers.
* An RR does not change the next hops of routes imported from IBGP EVPN when advertising these routes to IBGP EVPN peers.
* A BGP EVPN speaker changes the next hops of routes to the interface that it uses to establish IBGP EVPN peer relationships before advertising these routes to IBGP EVPN peers.In an inter-AS scenario where an EVPN Route Reflector (RR) is used, the **peer next-hop-invariable** command needs to be run on the RR to prevent the RR from modifying the Next\_Hops of routes before advertising the routes to EBGP peers. This ensures that the remote PE recurses routes to the LSP destined for the local PE during traffic transmission.In an EVPN VXLAN scenario, the **peer next-hop-invariable** command must be run if a device needs to advertise routes received from an EBGP EVPN peer to IBGP EVPN peers or advertise routes to EBGP EVPN peers.

**Prerequisites**

The specified peer has been enabled in the BGP-EVPN address family view.

**Precautions**

If both the peer next-hop-invariable and peer next-hop-local commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP device not to change the Next\_Hop of a route when the BGP device advertises it to its EBGP peer in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.9 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.9 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.9 next-hop-invariable

```