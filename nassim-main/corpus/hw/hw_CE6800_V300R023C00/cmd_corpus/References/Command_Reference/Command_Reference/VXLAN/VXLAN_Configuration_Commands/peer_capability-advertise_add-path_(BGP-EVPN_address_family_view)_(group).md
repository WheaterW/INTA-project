peer capability-advertise add-path (BGP-EVPN address family view) (group)
=========================================================================

peer capability-advertise add-path (BGP-EVPN address family view) (group)

Function
--------



The **peer capability-advertise add-path** command enables a device to send Add-Path routes to or receive Add-Path routes from a BGP EVPN peer group.

The **undo peer capability-advertise add-path** command restores the default configuration.



By default, a device is disabled from sending Add-Path routes to or receiving Add-Path routes from a BGP EVPN peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *peerGroupName* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to configure BGP Add-Path. After BGP Add-Path is configured, a device can advertise two or more routes with the same prefix to a BGP peer. These routes can back up each other or load-balance traffic, thereby ensuring data transmission reliability.When deploying BGP Add-Path, run the **peer capability-advertise add-path** command to enable the device to advertise Add-Path routes to a specified BGP peer or receive Add-Path routes from a specified BGP peer. In addition, you need to run the **peer advertise add-path** command to configure the number of routes that the device can advertise to a specified peer.

**Prerequisites**

Enable the peer group in current view using **peer enable** command.

**Precautions**

If you enable or disable the Add-Path function, the BGP peer relationship will be re-established, which can lead to a temporary network interruption. Therefore, exercise caution when running the related commands.


Example
-------

# Enable the device to receive Add-Path routes from a BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.1 as-number 100
[*HUAWEI-bgp] peer 2.2.2.2 as-number 100
[*HUAWEI-bgp] group gp1
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer gp1 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.1 group gp1
[*HUAWEI-bgp-af-evpn] peer 2.2.2.2 group gp1
[*HUAWEI-bgp-af-evpn] peer gp1 capability-advertise add-path receive

```