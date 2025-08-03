peer capability-advertise add-path (BGP view)
=============================================

peer capability-advertise add-path (BGP view)

Function
--------



The **peer capability-advertise add-path** command enables BGP Add-Path function.

The **undo peer capability-advertise add-path** command restores the default setting.



By default, the Add-Path function is disabled.


Format
------

**peer** *ipv4-address* **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** *ipv4-address* **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| **add-path** | Indicates the Add-Path function. | - |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to configure BGP Add-Path. After BGP Add-Path is configured, a device can advertise two or more routes with the same prefix to a BGP peer. These routes can back up each other or load-balance traffic, thereby ensuring data transmission reliability.When deploying BGP Add-Path, run the **peer capability-advertise add-path** command to enable the device to advertise Add-Path routes to a specified BGP peer or receive Add-Path routes from a specified BGP peer. In addition, you need to run the **peer advertise add-path** command to configure the number of routes that the device can advertise to a specified peer.

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
[*HUAWEI-bgp] peer 10.2.3.4 as-number 100
[*HUAWEI-bgp] peer 10.2.3.4 capability-advertise add-path receive

```