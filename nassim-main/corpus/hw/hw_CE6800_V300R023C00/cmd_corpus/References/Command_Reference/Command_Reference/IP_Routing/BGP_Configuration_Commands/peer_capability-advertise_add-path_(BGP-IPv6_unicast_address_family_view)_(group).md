peer capability-advertise add-path (BGP-IPv6 unicast address family view) (group)
=================================================================================

peer capability-advertise add-path (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer capability-advertise add-path** command enables the Add-Path function.

The **undo peer capability-advertise add-path** command restores the default setting.



By default, Add-Path function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *group-name* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
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

This command is used to configure BGP Add-Path. After BGP Add-Path is configured, a device can advertise two or more routes with the same prefix to a BGP peer. These routes can back up each other or load-balance traffic, thereby ensuring data transmission reliability.When deploying BGP Add-Path, run the **peer capability-advertise add-path** command to enable the device to advertise Add-Path routes to a specified BGP peer or receive Add-Path routes from a specified BGP peer. In addition, you need to run the **peer advertise add-path** command to configure the number of routes that the device can advertise to a specified peer.

**Precautions**

If the **peer capability-advertise add-path** command is run for a specified peer and the **peer advertise best-external** command is run for a specified peer group, the peer cannot inherit the function of the **peer advertise best-external** command configured for the peer group when the peer is added to the peer group.Enabling or disabling Add-Path will disconnect and then re-establish the peer session. This operation will cause temporary network interruption. Therefore, exercise caution when performing this operation.


Example
-------

# Enable the device to accept the Add-Path routes received from a peer.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[~HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test capability-advertise add-path both

```