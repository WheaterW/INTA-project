peer transit-med-to-ebgp(BGP-EVPN address family view) (IPv6)
=============================================================

peer transit-med-to-ebgp(BGP-EVPN address family view) (IPv6)

Function
--------



The **peer transit-med-to-ebgp** command enables a device to advertise the MED attribute to its EBGP-EVPN peers.

The **undo peer transit-med-to-ebgp** command cancels the existing configuration.

The **peer transit-med-to-ebgp disable** command disables a device from advertising the MED attribute to a specified peer in an EBGP-EVPN peer group.

The **undo peer transit-med-to-ebgp disable** command cancels the existing configuration.



By default, the MED attribute is not forcibly advertised to any EBGP EVPN peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **transit-med-to-ebgp** [ **disable** ]

**undo peer** *peerIpv6Addr* **transit-med-to-ebgp** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MED attribute is an optional non-transitive attribute. When EBGP EVPN peers are established between devices in two data centers in different BGP ASs, the MED attributes of EVPN routes are not transmitted between the EBGP EVPN peers by default. If a DC has active and standby gateways and the cost needs to be changed to trigger an active/standby switchover of service flows, you can configure peer transit-med-to-ebgp to enable the local gateway to advertise the MED attribute of received EVPN routes to the peer.

**Precautions**

By default, the MED attribute can be transmitted in an AS. Therefore, if the peer ip-address command is run to specify the address of a peer as an AS address, the command does not take effect.


Example
-------

# Advertise the MED attribute to EBGP EVPN peers.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-evpn] peer 2001:DB8:1::1 transit-med-to-ebgp

```