peer description(BGP-VPN instance IPv6 address family view)(group)
==================================================================

peer description(BGP-VPN instance IPv6 address family view)(group)

Function
--------



The **peer description** command configures a description for a peer group.

The **undo peer description** command deletes the description of a peer group.



By default, no description is configured for a peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **description** *description-text*

**undo peer** *group-name* **description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *description-text* | Specifies a description. | The value is a string of 1 to 255 characters. Letters, digits, and spaces are supported. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The peer description can be used to configure a description for a peer group, which facilitates management of peers or peer groups. The description records information about the peer group, such as the VPN instance to which the peer group belongs, and devices that establish peer relationships with the peer group.

**Implementation Procedure**

The description configured by using the **peer description** command for a peer is displayed from the first non-space character.

**Configuration Impact**



If the **peer description** command is run multiple times to configure a description for a peer group, the latest configuration overwrites the previous one.



**Follow-up Procedure**



You can run display bgp peer verbose command can be used to view the description of a peer.




Example
-------

# Configure a description for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test description ISP1

```