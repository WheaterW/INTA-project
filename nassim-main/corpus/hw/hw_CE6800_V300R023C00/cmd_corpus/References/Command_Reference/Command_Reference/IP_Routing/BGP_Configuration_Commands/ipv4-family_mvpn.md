ipv4-family mvpn
================

ipv4-family mvpn

Function
--------



The **ipv4-family mvpn** command enables the BGP-MVPN address family and displays the address family view.

The **undo ipv4-family mvpn** command deletes the configurations in the BGP-MVPN address family.



By default, the address family view of MVPN is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv4-family mvpn**

**undo ipv4-family mvpn**


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

To enable the BGP-MVPN address family and enter this address family view, run this command.


Example
-------

# Enter the BGP-MVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn]

```