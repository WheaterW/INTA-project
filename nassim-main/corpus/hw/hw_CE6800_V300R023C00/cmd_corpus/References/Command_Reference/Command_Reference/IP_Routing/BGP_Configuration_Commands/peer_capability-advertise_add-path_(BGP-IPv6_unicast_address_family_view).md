peer capability-advertise add-path (BGP-IPv6 unicast address family view)
=========================================================================

peer capability-advertise add-path (BGP-IPv6 unicast address family view)

Function
--------



The **peer capability-advertise add-path** command enables optional functions for BGP to advertise routes, including route-refresh, common functions, 4-byte AS number, and Add-Path.

The **undo peer capability-advertise add-path** command restores the default configuration.



By default, the route-refresh and 4-byte AS number functions are enabled, but the general function and Add-Path are disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *ipv4-address* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **add-path** | Indicates the Add-Path function. | - |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

There are multiple optional BGP functions when a BGP peer advertises routes to its peer. The optional BGP functions include route-refresh, general function, 4-byte AS number, and Add-Path. You can run the **peer capability-advertise** command to select one of the functions based on the needs on the live network.

**Precautions**

If the **peer capability-advertise add-path** command is run for a specified peer and the **peer advertise best-external** command is run for a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command configured for the peer group when the peer is added to the peer group.Enabling or disabling Add-Path will disconnect and then re-establish the peer session. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Enable the RR to receive Add-Path routes from a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 capability-advertise add-path receive

```