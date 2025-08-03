vrf-route-distribute disable (BGP view)
=======================================

vrf-route-distribute disable (BGP view)

Function
--------



The **vrf-route-distribute vpnv4 disable** command prevents BGP unicast VPN routes from being sent to BGP VPNv4.

The **undo vrf-route-distribute vpnv4 disable** command restores the default configuration. BGP unicast VPN routes are sent to BGP VPNv4.

The **vrf-route-distribute vpnv6 disable** command prevents BGP unicast VPN routes from being sent to BGP VPNv6.

The **undo vrf-route-distribute vpnv6 disable** command restores the default configuration. BGP unicast VPN routes are sent to BGP VPNv6.



By default, BGP unicast VPN routes can be sent to BGP VPNv4 or BGP VPNv6.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**vrf-route-distribute** { **vpnv4** | **vpnv6** } **disable**

**undo vrf-route-distribute** { **vpnv4** | **vpnv6** } **disable**

For CE6885-LL (low latency mode):

**vrf-route-distribute vpnv4 disable**

**undo vrf-route-distribute vpnv4 disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Configures the device not to send BGP unicast VPN routes to BGP VPNv4. | - |
| **vpnv6** | Configures the device not to send BGP unicast VPN routes to BGP VPNv6.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When EVPN is used to replace L3VPN, BGP unicast VPN routes are still copied to the BGP VPNv4 or BGP VPNv6 routing table by default, consuming system resources. You can run this command to disable replication of BGP unicast VPN routes to the BGP VPNv4 or BGP VPNv6 routing table to save system resources.

**Precautions**

In an L3VPN scenario, after this command is run, BGP unicast VPN routes cannot be leaked to BGP VPNv4 or BGP VPNv6 routes. Therefore, exercise caution when running this command.


Example
-------

# Prevent BGP unicast VPN routes from being sent to BGP VPNv6.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] vrf-route-distribute vpnv6 disable

```

# Prevent BGP unicast VPN routes from being sent to BGP VPNv4.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] vrf-route-distribute vpnv4 disable

```