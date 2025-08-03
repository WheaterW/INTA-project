consistency-check whitelist module stp service-type
===================================================

consistency-check whitelist module stp service-type

Function
--------



The **consistency-check whitelist module stp service-type** command configures the M-LAG consistency check whitelist for the STP module.

The **undo consistency-check whitelist module stp service-type** command cancels the M-LAG consistency check whitelist configured for the STP module.



By default, the M-LAG consistency check whitelist is not configured for the STP module.


Format
------

**consistency-check whitelist module stp service-type stp-m-lag-priority**

**undo consistency-check whitelist module stp service-type stp-m-lag-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **stp-m-lag-priority** | STP priority of the M-LAG interface. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if the configuration consistency check function is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the STP module to the configuration consistency check whitelist to disable the consistency check function for the configuration.


Example
-------

# Add the STP priority of the M-LAG interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module stp service-type stp-m-lag-priority

```