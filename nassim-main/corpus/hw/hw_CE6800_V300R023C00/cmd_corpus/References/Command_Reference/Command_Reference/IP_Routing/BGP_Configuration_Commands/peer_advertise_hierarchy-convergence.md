peer advertise hierarchy-convergence
====================================

peer advertise hierarchy-convergence

Function
--------



The **peer advertise hierarchy-convergence enable** command enables the function of advertising the hierarchical convergence attribute to a peer.

The **undo peer advertise hierarchy-convergence enable** command removes the configuration of enabling the function of advertising the hierarchical convergence attribute to a peer.

The **peer advertise hierarchy-convergence disable** command disables a device from advertising the hierarchical convergence attribute to a peer.

The **undo peer advertise hierarchy-convergence disable** command removes the configuration of disabling the function of advertising hierarchical convergence attributes to a peer.



By default, the function of advertising the hierarchical convergence attribute to a peer is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **advertise** **hierarchy-convergence** { **enable** | **disable** }

**undo peer** *ipv6-address* **advertise** **hierarchy-convergence** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is in the format X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **peer advertise hierarchy-convergence** command to control whether to advertise the hierarchical convergence attribute to the peer.


Example
-------

# Enable the function of advertising the hierarchical convergence attribute to a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 advertise hierarchy-convergence enable

```