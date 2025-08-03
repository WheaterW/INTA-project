peer vpn-orf disable (BGP-EVPN address family view) (group)
===========================================================

peer vpn-orf disable (BGP-EVPN address family view) (group)

Function
--------



The **peer vpn-orf disable** command disables EVPN ORF for a BGP EVPN peer group.

The **undo peer vpn-orf disable** command restores the default configuration.



By default, a device with EVPN ORF enabled performs EVPN ORF for all its BGP EVPN peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **vpn-orf** **disable**

**undo peer** *peerGroupName* **vpn-orf** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On a network where both EVPN and L3VPN services are deployed, if a PE does not support EVPN ORF due to an earlier version, after BGP-VT peer relationships are established on the entire network and EVPN ORF is enabled on other PEs and RRs, PEs of earlier versions cannot exchange EVPN routes with RRs. As a result, EVPN services cannot run properly. In this case, you can run the **peer vpn-orf disable** command to disable the RR from filtering routes related to the IRT so that the RR can send and receive EVPN routes properly. This ensures that EVPN services run properly.


Example
-------

# Disable EVPN ORF for a specified BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 vpn-orf disable

```