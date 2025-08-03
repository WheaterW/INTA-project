consistency-check whitelist module vxlan service-type
=====================================================

consistency-check whitelist module vxlan service-type

Function
--------



The **consistency-check whitelist module vxlan service-type** command configures an M-LAG consistency check whitelist for the VXLAN module.

The **undo consistency-check whitelist module vxlan service-type** command deletes the whitelist for the M-LAG consistency check of the VXLAN module.



By default, the M-LAG consistency check whitelist is not configured for the VXLAN module.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**consistency-check whitelist module vxlan service-type** { **bd-configuration** | **vbdif-configuration** | **ipv4-address** | **ipv6-address** | **virtual-mac** | **vbdif-status** } \*

**undo consistency-check whitelist module vxlan service-type** { **bd-configuration** | **vbdif-configuration** | **ipv4-address** | **ipv6-address** | **virtual-mac** | **vbdif-status** } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bd-configuration** | Specifies the BD configuration. | - |
| **vbdif-configuration** | Specifies the VBDIF interface configuration. | - |
| **ipv4-address** | Specifies the IPv4 address of a VBDIF interface. | - |
| **ipv6-address** | Specifies the IPv6 address of a VBDIF interface. | - |
| **virtual-mac** | Specifies the virtual MAC address of a VBDIF interface. | - |
| **vbdif-status** | Specifies the VBDIF interface status. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG scenario, if the configuration consistency check function is enabled but some configurations are not required to be checked, you can run this command to add the specified configuration of the VXLAN module to the configuration consistency check whitelist to disable the consistency check function for the configuration.


Example
-------

# Add the IPv6 address of a VBDIF interface to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type ipv6-address

```

# Add the virtual MAC address of a VBDIF interface to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type virtual-mac

```

# Add the BD configuration to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type bd-configuration

```

# Add the VBDIF interface status to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type vbdif-status

```

# Add the VBDIF interface configuration to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type vbdif-configuration

```

# Add the IPv4 address of a VBDIF interface to the M-LAG configuration consistency check whitelist.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check whitelist module vxlan service-type ipv4-address

```