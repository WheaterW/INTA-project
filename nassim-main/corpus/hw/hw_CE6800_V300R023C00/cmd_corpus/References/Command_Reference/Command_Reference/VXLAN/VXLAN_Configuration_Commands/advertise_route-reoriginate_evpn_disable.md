advertise route-reoriginate evpn disable
========================================

advertise route-reoriginate evpn disable

Function
--------



The **advertise route-reoriginate evpn disable** command disables a device from re-originating EVPN routes in a specified VPN instance as VPN or EVPN routes or re-originating VPN routes in a specified VPN instance as EVPN routes.

The **undo advertise route-reoriginate evpn disable** command restores the default configuration.



By default, the function to re-originate EVPN routes in a specified VPN instance as EVPN or VPN routes or to re-originate VPN routes in a specified VPN instance as EVPN routes is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise route-reoriginate evpn disable**

**undo advertise route-reoriginate evpn disable**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A device can be configured to re-originate IP prefix routes and IRB routes received from an EVPN peer and then advertise them to a VPN or EVPN peer. A device can also be configured to re-originate routes received from a VPN peer and then advertise them to an EVPN peer. You can run the advertise route-reoriginate evpn disable command to disable the function to re-originate EVPN routes as EVPN or VPN routes or to re-originate VPN routes as EVPN routes in a specified VPN instance.


Example
-------

# Disable a device from re-originating EVPN routes in a specified VPN instance as EVPN or VPN routes or re-originating VPN routes in a specified VPN instance as EVPN routes .
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpn-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] advertise route-reoriginate evpn disable
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] advertise route-reoriginate evpn disable

```