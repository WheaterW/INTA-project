consistency-check whitelist module m-lag service-type
=====================================================

consistency-check whitelist module m-lag service-type

Function
--------



The **consistency-check whitelist module m-lag service-type** command configures an M-LAG consistency check whitelist of the M-LAG module.

The **undo consistency-check whitelist module m-lag service-type** command cancels the configured M-LAG consistency check whitelist of the M-LAG module.



By default, no M-LAG consistency check whitelist is configured for the M-LAG module.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**consistency-check whitelist module m-lag service-type** { **m-lag-member-num** | **m-lag-id** | **peer-link-exclude-vlan** | **m-lag-ipv4-address** | **m-lag-ipv6-address** | **m-lag-election-mode** } \*

**undo consistency-check whitelist module m-lag service-type** { **m-lag-member-num** | **m-lag-id** | **peer-link-exclude-vlan** | **m-lag-ipv4-address** | **m-lag-ipv6-address** | **m-lag-election-mode** } \*

For CE6885-LL (low latency mode):

**consistency-check whitelist module m-lag service-type** { **m-lag-member-num** | **m-lag-id** | **peer-link-exclude-vlan** | **m-lag-ipv4-address** | **m-lag-election-mode** } \*

**undo consistency-check whitelist module m-lag service-type** { **m-lag-member-num** | **m-lag-id** | **peer-link-exclude-vlan** | **m-lag-ipv4-address** | **m-lag-election-mode** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **m-lag-member-num** | Number of M-LAG member interfaces. | - |
| **m-lag-id** | M-LAG interface number. | - |
| **peer-link-exclude-vlan** | Configuration of removing a peer-link interface from a VLAN. | - |
| **m-lag-ipv4-address** | IPv4 address for a dynamic routing protocol over M-LAG. | - |
| **m-lag-ipv6-address** | IPv6 address for a dynamic routing protocol over M-LAG.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **m-lag-election-mode** | Active/standby election mode. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if the configuration consistency check function is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the M-LAG module to the configuration consistency check whitelist to disable the consistency check function for the configuration.


Example
-------

# Add the M-LAG interface number to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type m-lag-id

```

# Add the configuration of removing a peer-link interface from a VLAN to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type peer-link-exclude-vlan

```

# Add the IPv4 address for a dynamic routing protocol over M-LAG to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type m-lag-ipv4-address

```

# Add the IPv6 address for a dynamic routing protocol over M-LAG to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type m-lag-ipv6-address

```

# Add the M-LAG active/standby election mode to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type m-lag-election-mode

```

# Add the number of M-LAG member interfaces to the configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module m-lag service-type m-lag-member-num

```