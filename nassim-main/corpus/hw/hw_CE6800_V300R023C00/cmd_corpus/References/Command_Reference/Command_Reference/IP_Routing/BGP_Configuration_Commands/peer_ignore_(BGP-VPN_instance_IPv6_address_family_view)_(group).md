peer ignore (BGP-VPN instance IPv6 address family view) (group)
===============================================================

peer ignore (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer ignore** command prevents a BGP device from establishing a session with a peer group.

The **undo peer ignore** command cancels the configuration.



By default, a BGP device is allowed to establish a session with a BGP peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **ignore**

**undo peer** *group-name* **ignore**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a peer session needs to be interrupted temporarily and a large number of configurations exist on the peer, you can run the **peer ignore** command to reduce the reconfiguration workload. For example, if the peer relationship is frequently established due to the upgrade or link adjustment of the peer end within a period of time, you can run this command on the stable end to temporarily interrupt the BGP peer relationship to prevent frequent route or peer relationship flapping.You can run this command to terminate the session with a specified peer group and clear all related routing information. For a peer group, this means that a large number of sessions with the peers are terminated suddenly.

**Configuration Impact**



After a BGP session is successfully established, running the **peer ignore** command interrupts the BGP session. The interrupted BGP session cannot be established again, and the status of the corresponding BGP peer relationship is displayed as Idle.




Example
-------

# Prohibit a device from establishing any session with peer group.
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
[*HUAWEI-bgp-6-vpn1] peer test ignore

```