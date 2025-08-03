peer capability-advertise add-path (bgp-muli-instance-af-evpn view)
===================================================================

peer capability-advertise add-path (bgp-muli-instance-af-evpn view)

Function
--------



The **peer capability-advertise add-path** command enables a device to send Add-Path routes to or receive Add-Path routes from a specified peer.

The **undo peer capability-advertise add-path** command restores the default configuration.



By default, a device is disabled from sending Add-Path routes to or receiving Add-Path routes from a specified peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** { *ipv4-address* | *ipv6-address* } **capability-advertise** **add-path** { **both** | **receive** | **send** }

**undo peer** { *ipv4-address* | *ipv6-address* } **capability-advertise** **add-path** { **both** | **receive** | **send** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **both** | Enables the RR to receive Add-Path routes from and send Add-Path routes to a specified IBGP peer. | - |
| **receive** | Enables the RR to receive Add-Path routes from a specified IBGP peer. | - |
| **send** | Enables the RR to send Add-Path routes to a specified IBGP peer. | - |



Views
-----

bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is used to configure BGP Add-Path. After BGP Add-Path is configured, a device can advertise two or more routes with the same prefix to a BGP peer. These routes can back up each other or load-balance traffic, thereby ensuring data transmission reliability.When deploying BGP Add-Path, run the **peer capability-advertise add-path** command to enable the device to advertise Add-Path routes to a specified BGP peer or receive Add-Path routes from a specified BGP peer. In addition, you need to run the **peer advertise add-path** command to configure the number of routes that the device can advertise to a specified peer.

**Prerequisites**

Enable the peer in current view using **peer enable** command.

**Precautions**

If you enable or disable the Add-Path function, the BGP peer relationship will be re-established, which can lead to a temporary network interruption. Therefore, exercise caution when running the related commands.


Example
-------

# Enable the device to receive Add-Path routes from a BGP EVPN peer.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a] l2vpn-family evpn
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a-af-evpn] peer 10.1.1.1 capability-advertise add-path receive

```