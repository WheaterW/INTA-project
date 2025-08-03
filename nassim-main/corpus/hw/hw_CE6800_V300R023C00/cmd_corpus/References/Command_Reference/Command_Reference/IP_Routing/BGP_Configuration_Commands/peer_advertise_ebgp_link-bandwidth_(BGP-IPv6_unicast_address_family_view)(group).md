peer advertise ebgp link-bandwidth (BGP-IPv6 unicast address family view)(group)
================================================================================

peer advertise ebgp link-bandwidth (BGP-IPv6 unicast address family view)(group)

Function
--------



The **peer advertise ebgp link-bandwidth** command enables a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer group.

The **undo peer advertise ebgp link-bandwidth** command cancels the existing configuration.

The **peer advertise link-bandwidth transitive** command enables a device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP routes into an optional transitive attribute before advertising the BGP routes to a specified peer group.

The **undo peer advertise link-bandwidth transitive** command cancels the existing configuration.



By default, if the peer advertise ebgp link-bandwidth command is run, the device does not advertise the Link Bandwidth extended community attribute to an EBGP peer group; if the peer advertise link-bandwidth transitive command is run, the device does not convert the Link Bandwidth extended community attribute (optional non-transitive) carried in a BGP route into an optional transitive attribute before advertising the route to other peer groups.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **advertise** **ebgp** **link-bandwidth**

**peer** *peerGroupName* **advertise** **link-bandwidth** **transitive**

**undo peer** *peerGroupName* **advertise** **ebgp** **link-bandwidth**

**undo peer** *peerGroupName* **advertise** **link-bandwidth** **transitive**


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

**Usage Scenario**

To enable a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer group, run the **peer advertise ebgp link-bandwidth** command.To enable a device to convert the Link Bandwidth extended community attribute (optional non-transitive) carried in BGP routes into an optional transitive attribute before advertising the BGP routes to a specified peer group, run the **peer advertise link-bandwidth transitive** command.

**Precautions**

Before running the peer advertise ebgp link-bandwidth or **peer advertise link-bandwidth transitive** command to advertise the link bandwidth extended community attribute, you need to use a route-policy to add the link bandwidth attribute. Currently, this command can process only one Link Bandwidth extended community attribute. If a device changes the next-hop address of a received route carrying the Link Bandwidth extended community attribute to its own address, the device deletes this attribute before advertising it to other peers.


Example
-------

# Enable a device to advertise the Link Bandwidth extended community attribute to a specified EBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] ext-community-change enable
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test advertise-ext-community
[*HUAWEI-bgp-af-ipv6] peer test advertise ebgp link-bandwidth

```