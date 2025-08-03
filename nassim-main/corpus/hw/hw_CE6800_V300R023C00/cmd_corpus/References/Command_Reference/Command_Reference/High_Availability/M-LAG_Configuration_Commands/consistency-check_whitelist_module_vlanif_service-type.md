consistency-check whitelist module vlanif service-type
======================================================

consistency-check whitelist module vlanif service-type

Function
--------



The **consistency-check whitelist module vlanif service-type** command configures the M-LAG consistency check whitelist for the VLANIF module.

The **undo consistency-check whitelist module vlanif service-type** command cancels the M-LAG consistency check whitelist configured for the VLANIF module.



By default, the M-LAG consistency check whitelist is not configured for the VLANIF module.


Format
------

For CE6820H, CE6820H-K, CE6820S:

**consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **ipv6-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **arp-timeout** } \*

**undo consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **ipv6-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **arp-timeout** } \*

For CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **ipv6-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **vlanif-bypass** | **arp-timeout** } \*

**undo consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **ipv6-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **vlanif-bypass** | **arp-timeout** } \*

For CE6885-LL (low latency mode):

**consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **arp-timeout** } \*

**undo consistency-check whitelist module vlanif service-type** { **vlanif-configuration** | **ipv4-address** | **vrrp4** | **virtual-mac** | **vlanif-status** | **arp-timeout** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlanif-configuration** | VLANIF interface configuration. | - |
| **ipv4-address** | IPv4 address of a VLANIF interface. | - |
| **ipv6-address** | IPv6 address of a VLANIF interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **vrrp4** | IPv4 VRRP group configured on a VLANIF interface. | - |
| **virtual-mac** | Virtual MAC address of a VLANIF interface. | - |
| **vlanif-status** | Status of a VLANIF interface. | - |
| **vlanif-bypass** | Bypass tunnel configuration of a VLANIF interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **arp-timeout** | Sets the aging time of ARP entries on a VLANIF interface. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if configuration consistency check is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the VLANIF module to the configuration consistency check whitelist to disable the configuration consistency check function.


Example
-------

# Add the VLANIF interface status to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type vlanif-status

```

# Add the bypass tunnel configuration of a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type vlanif-bypass

```

# Add the IPv4 VRRP group on a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type vrrp4

```

# Add the IPv6 address of a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type ipv6-address

```

# Add the IPv4 address of a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type ipv4-address

```

# Add the VLANIF interface configuration to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type vlanif-configuration

```

# Add the virtual MAC address of a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type virtual-mac

```

# Add the ARP timeout configuration of a VLANIF interface to the M-LAG consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vlanif service-type arp-timeout

```