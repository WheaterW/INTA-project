bestroute add-path (BGP-IPv6 unicast address family view)
=========================================================

bestroute add-path (BGP-IPv6 unicast address family view)

Function
--------



The **bestroute add-path** command enables BGP Add-Path and configures the number of routes that the device can select.

The **undo bestroute add-path** command restores the default configuration.



By default, BGP Add-Path is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute add-path path-number** *path-number*

**undo bestroute add-path**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **path-number** *path-number* | Specifies the number of routes that the device can select. | The value is an integer that ranges from 2 to 64. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a scenario with an RR and clients, if the RR has multiple routes to the same destination (with the same prefix), the RR selects an optimal route from these routes and then sends only the optimal route to its clients. Therefore, the clients have only one route to the destination. If a link along this route fails, route convergence takes a long time, which cannot meet the requirements for high reliability. To address this issue, deploy the BGP Add-Path feature on the RR. With BGP Add-Path, the RR can send two or more routes with the same prefix to a specified peer. These routes can back up each other or load-balance traffic, which ensures high reliability in data transmission.

**Follow-up Procedure**

Run the **peer capability-advertise add-path send** command to enable the device to advertise Add-Path routes to a specified peer.Run the **peer advertise add-path** command to specify the number of routes to be advertised to a peer.

**Precautions**

The **bestroute add-path** command can be configured and takes effect on any device, but it is mainly configured on an RR. After this command is run, BGP can select multiple routes.The selected Add-Path routes may not work in load balancing mode. They can work in load balancing mode only when they meet load balancing conditions.If the optimal route is a labeled route, only labeled routes are selected as Add-Path routes. If the optimal route is a common route, only common routes are selected as Add-Path routes.To enable the device to accept the Add-Path routes received from the specified peer, you need to run the **peer capability-advertise add-path receive** command on the device.BGP Add-Path advertises multiple routes with the same prefix. Therefore, in specific scenarios, two devices may select each other as the next hop, causing a traffic loop. Avoid such scenarios when deploying BGP Add-Path.The bestroute add-path and **deterministic-med** commands are mutually exclusive. Do not run them together.


Example
-------

# Configure BGP to select six optimal routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] bestroute add-path path-number 6

```