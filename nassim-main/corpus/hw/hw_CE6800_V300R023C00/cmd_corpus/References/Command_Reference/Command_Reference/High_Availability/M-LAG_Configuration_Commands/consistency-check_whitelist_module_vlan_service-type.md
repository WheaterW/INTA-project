consistency-check whitelist module vlan service-type
====================================================

consistency-check whitelist module vlan service-type

Function
--------



The **consistency-check whitelist module vlan service-type** command configures the M-LAG consistency check whitelist for the VLAN module.

The **undo consistency-check whitelist module vlan service-type** command cancels the M-LAG consistency check whitelist configured for the VLAN module.



By default, the M-LAG consistency check whitelist is not configured for the VLAN module.


Format
------

**consistency-check whitelist module vlan service-type** { **vlan-configuration** | **port-vlan-relation** } \*

**undo consistency-check whitelist module vlan service-type** { **vlan-configuration** | **port-vlan-relation** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan-configuration** | VLAN configuration. | - |
| **port-vlan-relation** | VLANs of packets allowed to pass through interfaces. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if configuration consistency check is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the VLAN module to the configuration consistency check whitelist to disable the consistency check function for the configuration.


Example
-------

# Add the VLAN configuration to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlan service-type vlan-configuration

```

# Add the VLANs of packets allowed to pass through interfaces to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlan service-type port-vlan-relation

```