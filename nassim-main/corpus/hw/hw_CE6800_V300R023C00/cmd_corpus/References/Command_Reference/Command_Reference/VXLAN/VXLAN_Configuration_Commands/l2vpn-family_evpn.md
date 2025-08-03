l2vpn-family evpn
=================

l2vpn-family evpn

Function
--------



The **l2vpn-family evpn** command enables the BGP-EVPN address family and displays the BGP-EVPN address family view.

The **undo l2vpn-family evpn** command deletes the BGP-EVPN address family view.



By default, the BGP-EVPN address family is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**l2vpn-family evpn**

**undo l2vpn-family evpn**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before you perform configurations in the BGP-EVPN address family view, run the **l2vpn-family evpn** command to enable the BGP-EVPN address family and display the BGP-EVPN address family view.


Example
-------

# Enable the BGP-EVPN address family and display the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn]

```