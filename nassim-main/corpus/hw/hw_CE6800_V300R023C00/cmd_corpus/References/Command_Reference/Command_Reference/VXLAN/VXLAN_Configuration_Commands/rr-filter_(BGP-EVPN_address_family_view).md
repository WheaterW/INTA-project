rr-filter (BGP-EVPN address family view)
========================================

rr-filter (BGP-EVPN address family view)

Function
--------



The **rr-filter** command configures a reflection policy for an RR.

The **undo rr-filter** command cancels the configuration.



By default, there is no reflection policy for an RR.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rr-filter** *extended-list-number*

**undo rr-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *extended-list-number* | * Specifies the VPN-Target extended community filter name. Only one extended community filter can be specified each time. * Specifies the number of the extended community filter that an RR group supports. Only one extended community filter can be specified each time. | * Name of an extended community filter: The name is a string of 1 to 51 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks. * Number of an extended community filter: The value is an integer ranging from 1 to 399. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Full-mesh connections need to be established between IBGP peers in an AS to ensure the connectivity between the IBGP peers. When there are many IBGP peers, it is costly to establish a fully-meshed network. An RR or a confederation can be used to solve the problem. Only the IBGP route of which route-target extended community attribute meets the matching rules can be reflected. This allows load balancing among RRs.


Example
-------

# Create an RR group on a BGP device and enable the BGP device to filter incoming VPNv4 routing updates automatically based on the configured route-target extended community.
```
<HUAWEI> system-view
[~HUAWEI] ip extcommunity-filter 10 deny rt 200:200
[*HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] rr-filter 10

```