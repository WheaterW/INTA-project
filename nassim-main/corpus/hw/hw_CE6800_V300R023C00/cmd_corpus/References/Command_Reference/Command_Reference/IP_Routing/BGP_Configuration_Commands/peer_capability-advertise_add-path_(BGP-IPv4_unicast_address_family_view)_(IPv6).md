peer capability-advertise add-path (BGP-IPv4 unicast address family view) (IPv6)
================================================================================

peer capability-advertise add-path (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer capability-advertise add-path** command enables optional BGP functions when a BGP peer advertises routes to its peer. The optional BGP functions include route-refresh, general function, 4-byte AS number, and Add-Path.

The **undo peer capability-advertise add-path** command restores the default setting.



By default, Add-Path function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *peerIpv6Addr* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When BGP advertises routes, optional functions include Add-Path. Using the **peer capability-advertise add-path** command, you can enable or disable the ADD-PATH function as required.

**Precautions**

If the **peer capability-advertise add-path** command is run for a specified peer and the **peer advertise best-external** command is run for a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command configured for the peer group when the peer is added to the peer group.peer capability-advertise add-path takes effect only on the routes received from BGP peers.

* If the route received from a BGP peer is preferred, the local BGP routes imported using the network command are not preferred or advertised.
* If the local routes imported using the network command are preferred, the routes received from the BGP peer are not preferred. After the add-path command is run, the routes can be advertised.Enabling or disabling Add-Path will disconnect and then re-establish the peer session. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.

Example
-------

# Enable the RR to receive Add-Path routes from a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 capability-advertise add-path receive

```