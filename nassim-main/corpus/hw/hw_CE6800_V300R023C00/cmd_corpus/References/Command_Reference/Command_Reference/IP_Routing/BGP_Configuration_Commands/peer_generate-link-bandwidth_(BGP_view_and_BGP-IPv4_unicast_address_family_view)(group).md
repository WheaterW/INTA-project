peer generate-link-bandwidth (BGP view/BGP-IPv4 unicast address family view)(group)
===================================================================================

peer generate-link-bandwidth (BGP view/BGP-IPv4 unicast address family view)(group)

Function
--------



The **peer generate-link-bandwidth** command enables an EBGP peer group on the local device to obtain the link bandwidth of directly connected EBGP peers.

The undo peer generate link-bandwidth command cancels the existing configuration.



By default, an EBGP peer group is disabled from obtaining the link bandwidth of directly connected EBGP peers.


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

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To obtain the actual link bandwidth <S1> link bandwidth <S1> link bandwidth <S1> link bandwidth, run the following command: When the peer connect-interface, peer ebgp-max-hop, or ttl command is not run, the bandwidth is dynamically updated with the actual bandwidth, you can run the **peer generate-link-bandwidth** command to enable a BGP peer group to obtain the <S1> link bandwidth of a directly connected BGP peer, in addition, the EBGP peers in the peer group inherit the configuration of the peer group.




Example
-------

# Configure an EBGP peer group to obtain the link bandwidth of directly connected EBGP peers.
```
<HUAWEI> system
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test generate-link-bandwidth

```