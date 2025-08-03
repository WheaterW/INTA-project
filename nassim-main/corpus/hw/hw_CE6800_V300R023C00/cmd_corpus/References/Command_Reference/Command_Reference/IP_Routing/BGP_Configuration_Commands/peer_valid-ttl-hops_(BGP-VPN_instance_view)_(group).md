peer valid-ttl-hops (BGP-VPN instance view) (group)
===================================================

peer valid-ttl-hops (BGP-VPN instance view) (group)

Function
--------



The **peer valid-ttl-hops** command applies the GTSM on a BGP peer or a BGP peer group.

The **undo peer valid-ttl-hops** command cancels the GTSM configured on a BGP peer or a BGP peer group.



By default, GTSM is not configured on any BGP peer group.


Format
------

**peer** *group-name* **valid-ttl-hops** [ *hops* ]

**undo peer** *group-name* **valid-ttl-hops**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *hops* | Specifies the number of TTL hops to be checked. | The value is an integer that ranges from 1 to 255. The default value is 255. If you specify the parameter hops, the valid range of the TTL value in the packet to be checked is [ 255-hops+1, 255 ]. |



Views
-----

BGP-VPN instance view,BGP multi-instance VPN instance session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a device against the attacks by the forged BGP or BGP4+ packets, you can configure GTSM to check whether the TTL value in the IP packet header is within the valid range.

**Prerequisites**

Before configuring GTSM for a peer group, you need to run the **peer group** command to add peers to the peer group.

**Implementation Procedure**

If you run the **undo peer valid-ttl-hops** command without specifying any parameter, all the GTSM configurations on a peer or a peer group are deleted.

**Precautions**

When this command is used in the BGP view, it is also applicable to MP-BGP extensions because they use the same TCP connection.The GTSM configurations are symmetrical, that is, GTSM must be enabled on both ends of the BGP connection.NOTE:

* GTSM and EBGP-MAX-HOP are mutually exclusive because both of them affect the TTL of the sent BGP messages. Therefore, only one of the two functions can be enabled on a peer or peer group.
* If GTSM is enabled on two directly connected EBGP peers, the fast sensing function on the interfaces directly connecting the EBGP peers is invalid. This is because BGP regards the EBGP peers as indirectly connected when GTSM is enabled on the EBGP peers.

Example
-------

# Configure GTSM for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test
[*HUAWEI-bgp-instance-vpn1] peer test valid-ttl-hops 5

```