peer ignore (BGP-VPN instance IPv6 address family view) (IPv6)
==============================================================

peer ignore (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer ignore** command prevents a BGP device from establishing a session with a peer.

The **undo peer ignore** command cancels the configuration.



By default, a BGP device is allowed to establish a session with a BGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **ignore**

**undo peer** *ipv6-address* **ignore**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the peer session needs to be interrupted temporarily and a large number of configurations exist on the peer, you can run the **peer ignore** command to reduce the reconfiguration workload. For example, if the peer relationship is frequently established due to the upgrade or link adjustment of the peer end within a period of time, you can run this command on the stable end to temporarily interrupt the BGP peer relationship to prevent frequent route or peer relationship flapping.You can run this command to terminate the session with a specified peer and clear all related routing information. For a peer group, this means that a large number of sessions with the peers are terminated suddenly.

**Configuration Impact**



After a BGP session is successfully established, running the **peer ignore** command interrupts the BGP session. The interrupted BGP session cannot be established again, and the status of the corresponding BGP peer relationship is displayed as Idle.




Example
-------

# Prohibit a device from establishing any session with the peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 ignore

```