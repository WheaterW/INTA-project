black-hole-dup-mac(BD-EVPN mac-duplication view)
================================================

black-hole-dup-mac(BD-EVPN mac-duplication view)

Function
--------



The **black-hole-dup-mac** command configures flapping MAC routes as black-hole routes.

The **undo black-hole-dup-mac** command restores the default configuration.



By default, flapping MAC routes are not configured as blackhole routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**black-hole-dup-mac**

**undo black-hole-dup-mac**


Parameters
----------

None

Views
-----

BD-EVPN mac-duplication view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an EVPN VXLAN, two PEs may be interconnected through both network-side and access-side links. The network will encounter both BUM traffic loops and MAC route flapping. When such problems occur on a local PE, the PE will use the MAC duplication suppression function to resolve the problems. By default, the system checks the number of times a MAC entry flaps within a detection period (180s by default). If the number of MAC flaps exceeds the upper threshold (5 by default), the system considers MAC route flapping to be occurring on the network and consequently suppresses the flapping MAC routes. The suppressed MAC routes cannot be sent to a remote PE through a BGP EVPN peer relationship. To set flapping MAC routes as blackhole routes, run the **black-hole-dup-mac** command. After this configuration is performed, if the source or destination MAC address of the forwarded traffic is the same as the MAC address of a blackhole MAC route, the traffic is discarded.


Example
-------

# Configure flapping MAC routes as blackhole routes.
```
<HUAWEI> system-view
[~HUAWEI] evpn-overlay enable
[*HUAWEI] bridge-domain 2
[*HUAWEI-bd2] vxlan vni 2
[*HUAWEI-bd2] evpn
[*HUAWEI-bd2-evpn] mac-duplication
[*HUAWEI-bd2-evpn-mac-dup] black-hole-dup-mac

```