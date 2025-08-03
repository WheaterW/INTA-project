peer ignore (BGP multi-instance VPN instance IPv4 address family view)(IPv4)
============================================================================

peer ignore (BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer ignore** command prevents a BGP device from establishing a session with a peer.

The **undo peer ignore** command cancels the configuration.



By default, a BGP device is allowed to establish a session with a BGP peer.


Format
------

**peer** *ipv4-address* **ignore**

**undo peer** *ipv4-address* **ignore**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vrf1] peer 10.1.1.1 ignore

```