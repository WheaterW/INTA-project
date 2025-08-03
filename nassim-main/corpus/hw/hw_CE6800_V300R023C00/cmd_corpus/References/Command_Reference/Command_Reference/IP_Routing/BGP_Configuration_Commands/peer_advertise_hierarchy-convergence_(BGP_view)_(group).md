peer advertise hierarchy-convergence (BGP view) (group)
=======================================================

peer advertise hierarchy-convergence (BGP view) (group)

Function
--------



The **peer advertise hierarchy-convergence disable** command disables a device from advertising the hierarchical convergence attribute to a peer group.

The **undo peer advertise hierarchy-convergence disable** command restores the default configuration.

The **peer advertise hierarchy-convergence enable** command enables a device to advertise the hierarchical convergence attribute to a peer group.

The **undo peer advertise hierarchy-convergence enable** command disables the function of advertising the hierarchical convergence attribute to a peer group and restores the default configuration.



By default, a BGP device is enabled to advertise the hierarchical convergence attribute to its peer group.


Format
------

**peer** *group-name* **advertise** **hierarchy-convergence** { **disable** | **enable** }

**undo peer** *group-name* **advertise** **hierarchy-convergence** { **disable** | **enable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **disable** | Disables the capability of advertising the hierarchical convergence attribute. | - |
| **enable** | Enables the capability of advertising the hierarchical convergence attribute. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To disable a BGP device from advertising the hierarchical convergence attribute to its peer group, run the **peer advertise hierarchy-convergence disable** command. If a device advertises the attribute to its peer group, all the members of the peer group will inherit the configuration. This facilitates route maintenance and management.




Example
-------

# Disable a BGP device from advertising the hierarchical convergence attribute to its peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group a
[*HUAWEI-bgp] peer a advertise hierarchy-convergence disable

```