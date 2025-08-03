peer vpn-orf disable (BGP-EVPN address family view)
===================================================

peer vpn-orf disable (BGP-EVPN address family view)

Function
--------



The **peer vpn-orf disable** command disables EVPN ORF for a BGP EVPN peer.

The **undo peer vpn-orf disable** command restores the default configuration.



By default, a device with EVPN ORF enabled performs EVPN ORF for all its BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *peerIpv4Addr* | *peerIpv6Addr* } **vpn-orf** **disable**

**undo peer** { *peerIpv4Addr* | *peerIpv6Addr* } **vpn-orf** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP peer. | The value is in dotted decimal notation. |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network where both EVPN and L3VPN services are deployed, if a PE does not support EVPN ORF due to an earlier version, after BGP-VT peer relationships are established on the entire network and EVPN ORF is enabled on other PEs and RRs, PEs of earlier versions cannot exchange EVPN routes with RRs. As a result, EVPN services cannot run properly. In this case, you can run the **peer vpn-orf disable** command to disable the RR from filtering routes related to the IRT so that the RR can send and receive EVPN routes properly. This ensures that EVPN services run properly.

**Precautions**

In a scenario where a Huawei device is connected to a non-Huawei device, VPN ORF is configured on the non-Huawei device. VPN ORF is enabled in all VPN-related address families on the non-Huawei device and enabled by address family on the Huawei device. To enable the non-Huawei device to send all required routes to the Huawei device, ensure that the import VPN targets of all VPNs are the same, or different address families are deployed over different BGP sessions.


Example
-------

# Disable EVPN ORF for a specified BGP EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 200
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-af-evpn] peer 1.1.1.1 enable
[*HUAWEI-af-evpn] peer 1.1.1.1 vpn-orf disable

```