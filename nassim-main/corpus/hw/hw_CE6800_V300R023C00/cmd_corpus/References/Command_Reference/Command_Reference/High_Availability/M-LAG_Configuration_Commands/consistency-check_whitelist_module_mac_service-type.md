consistency-check whitelist module mac service-type
===================================================

consistency-check whitelist module mac service-type

Function
--------



The **consistency-check whitelist module mac service-type** command configures the M-LAG consistency check whitelist for the MAC module.

The **undo consistency-check whitelist module mac service-type** command cancels the M-LAG consistency check whitelist configured for the MAC module.



By default, the M-LAG consistency check whitelist is not configured for the MAC module.


Format
------

**consistency-check whitelist module mac service-type** { **mac-aging-time** | **static-mac** } \*

**undo consistency-check whitelist module mac service-type** { **mac-aging-time** | **static-mac** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-aging-time** | Specifies the MAC address aging time. | - |
| **static-mac** | Indicates the static MAC address. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if the configuration consistency check function is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the MAC module to the configuration consistency check whitelist to disable the consistency check function for the configuration.


Example
-------

# Add the MAC address aging time to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module mac service-type mac-aging-time

```

# Add static MAC addresses to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module mac service-type static-mac

```