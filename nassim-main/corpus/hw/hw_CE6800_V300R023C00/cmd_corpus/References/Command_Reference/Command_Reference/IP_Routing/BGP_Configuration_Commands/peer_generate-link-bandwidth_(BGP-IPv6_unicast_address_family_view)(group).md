peer generate-link-bandwidth (BGP-IPv6 unicast address family view)(group)
==========================================================================

peer generate-link-bandwidth (BGP-IPv6 unicast address family view)(group)

Function
--------



The **peer generate-link-bandwidth** command enables an EBGP peer group on the local device to obtain the link bandwidth of directly connected EBGP peers.

The undo peer generate link-bandwidthcommand cancels the existing configuration.



By default, an EBGP peer group is disabled from obtaining the link bandwidth of directly connected EBGP peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **generate-link-bandwidth**

**undo peer** *peerGroupName* **generate-link-bandwidth**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To obtain the actual link bandwidth <S1> link bandwidth <S1> link bandwidth <S1> link bandwidth, run the following command: When the peer connect-interface, peer ebgp-max-hop, or ttl command is not run, the bandwidth is dynamically updated with the actual bandwidth, you can run the **peer generate-link-bandwidth** command to enable a BGP peer group to obtain the <S1> link bandwidth of a directly connected BGP peer, in addition, the EBGP peers in the peer group inherit the configuration of the peer group.


Example
-------

# Configure an EBGP peer group to obtain the link bandwidth of directly connected EBGP peers.
```
<HUAWEI> system
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test generate-link-bandwidth

```