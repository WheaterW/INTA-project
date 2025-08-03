c-multicast ad-route-ignore
===========================

c-multicast ad-route-ignore

Function
--------



The **c-multicast ad-route-ignore** command configures a device not to check whether local A-D routes exist after the device.

receives C-multicast routes from its BGP MVPN peers.

The undo c-multicast ad-route-ignore command restores the default configuration.



By default, after a device receives C-multicast routes from its BGP MVPN peers, the device checks whether local A-D routes exist.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**c-multicast ad-route-ignore**

**undo c-multicast ad-route-ignore**


Parameters
----------

None

Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the scenario where the IPv4 Layer 3 multicast Over VXLAN is deployed, when the BGP MVPN neighbor receives the C-multicast route, it ignores whether the local A-D route exists during the route validity check, so that the received C-multicast route is valid. In this way, the M-LAG implements the active-active gateway.

**Configuration Impact**

When the configuration of the c-multicast ad-route-ignore command changes on a device, the device re-checks the validity ofreceived C-multicast routes and re-selects routes. If the optimalroute changes, the device re-advertises routes to its BGP MVPN peers.


Example
-------

# Configure a device not to check whether local A-D routes exist after the device receives C-multicast routes from its BGP MVPN peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] c-multicast ad-route-ignore

```