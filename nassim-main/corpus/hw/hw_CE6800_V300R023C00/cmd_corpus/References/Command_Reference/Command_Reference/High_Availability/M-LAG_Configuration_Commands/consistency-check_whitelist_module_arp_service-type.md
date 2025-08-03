consistency-check whitelist module arp service-type
===================================================

consistency-check whitelist module arp service-type

Function
--------



The **consistency-check whitelist module arp service-type** command configures the M-LAG consistency check whitelist for the ARP module.

The **undo consistency-check whitelist module arp service-type** command cancels the M-LAG consistency check whitelist configured for the ARP module.



By default, the M-LAG consistency check whitelist is not configured for the ARP module.


Format
------

**consistency-check whitelist module arp service-type** { **arp-aging-time** | **static-arp** } \*

**undo consistency-check whitelist module arp service-type** { **arp-aging-time** | **static-arp** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp-aging-time** | ARP aging time. | - |
| **static-arp** | Static ARP. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if configuration consistency check is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the ARP module to the configuration consistency check whitelist to disable the configuration consistency check function.


Example
-------

# Add the ARP aging time to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module arp service-type arp-aging-time

```

# Add static ARP entries to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module arp service-type static-arp

```