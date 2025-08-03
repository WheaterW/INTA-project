irb-reoriginated without-split-group disable(Global EVPN configuration view)
============================================================================

irb-reoriginated without-split-group disable(Global EVPN configuration view)

Function
--------



The **irb-reoriginated without-split-group disable** command disables the function to advertise re-originated IRB routes without being restricted by a split horizon group (SHG).

The **undo irb-reoriginated without-split-group disable** command restores the default configuration.



By default, re-originated IRB routes are advertised without being restricted by an SHG.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**irb-reoriginated without-split-group disable**

**undo irb-reoriginated without-split-group disable**


Parameters
----------

None

Views
-----

Global EVPN configuration view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In scenarios where segment VXLAN tunnels are used to implement DC interconnections, to prevent forwarding BUM traffic from causing a loop during Layer 2 interconnection, BGP EVPN peer-based SHG is introduced. If no BGP EVPN peer-based SHGs are specified (using the peer split-group command) on transit leaf nodes (edge devices interconnecting DCs), all BGP EVPN peers belong to the default system SHG. In this case, after a transit leaf node re-originates IRB routes received from an intra-DC device, the transit leaf node cannot advertise the re-originated IRB routes to the peer DC's transit leaf node because the transit leaf nodes both belong to the default system SHG. As a result, Layer 3 traffic forwarding is affected.To prevent this problem, a device advertises re-originated IRB routes without being restricted by an SHG by default. If SHGs are specified for all BGP EVPN peers on transit leaf nodes, to disable the function to advertise re-originated IRB routes without being restricted by an SHG, run the **irb-reoriginated without-split-group disable** command.


Example
-------

# Disable the function to advertise re-originated IRB routes without being restricted by an SHG.
```
<HUAWEI> system-view
[~HUAWEI] evpn
[*HUAWEI-evpn] irb-reoriginated without-split-group disable

```