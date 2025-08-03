peer advertise hierarchy-convergence (BGP view)
===============================================

peer advertise hierarchy-convergence (BGP view)

Function
--------



The **peer advertise hierarchy-convergence enable** command enables a BGP device to advertise the hierarchical convergence attribute to a peer.

The **undo peer advertise hierarchy-convergence enable** command cancels the configuration of enabling a BGP device to advertise the hierarchical convergence attribute to a peer.

The **peer advertise hierarchy-convergence disable** command disables a BGP device from advertising the hierarchical convergence attribute to a peer.

The **undo peer advertise hierarchy-convergence disable** command cancels the configuration of disabling a BGP device from advertising the hierarchical convergence attribute to a peer.



By default, a BGP device is enabled to advertise the hierarchical convergence attribute to a peer.


Format
------

**peer** *ip-address* **advertise** **hierarchy-convergence** { **enable** | **disable** }

**undo peer** *ip-address* **advertise** **hierarchy-convergence** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To control whether a device advertises the hierarchical convergence attribute to a peer, run the **peer advertise hierarchy-convergence** command.




Example
-------

# Enable a BGP device to advertise the hierarchical convergence attribute to a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] peer 10.1.1.1 advertise hierarchy-convergence enable

```