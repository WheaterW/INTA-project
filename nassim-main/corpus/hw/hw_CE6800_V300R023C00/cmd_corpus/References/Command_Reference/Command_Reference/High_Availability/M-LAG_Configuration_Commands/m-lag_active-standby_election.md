m-lag active-standby election
=============================

m-lag active-standby election

Function
--------



The **m-lag active-standby election** command configures the packet type for active/standby interface election when M-LAG member interfaces work in active/standby mode.

The **undo m-lag active-standby election** command deletes the configured packet type for active/standby interface election when M-LAG member interfaces work in active/standby mode.



By default, active/standby status election is disabled for M-LAG member interfaces in active/standby mode.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**m-lag active-standby election** { **arp** | **nd** | **igmp** | **dhcp** | **mld** }

**undo m-lag active-standby election** { **arp** | **nd** | **igmp** | **dhcp** | **mld** }

For CE6885-LL (low latency mode):

**m-lag active-standby election** { **arp** | **igmp** | **dhcp** }

**undo m-lag active-standby election** { **arp** | **igmp** | **dhcp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **arp** | M-LAG active/standby interface election is performed based on ARP packets. | - |
| **nd** | M-LAG active/standby interface election is performed based on ND packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **igmp** | M-LAG active/standby interface election is performed based on IGMP packets. | - |
| **dhcp** | M-LAG active/standby interface election is performed based on DHCP packets. | - |
| **mld** | M-LAG active/standby interface election is performed based on MLD packets.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

M-LAG member interfaces in active/standby mode perform active/standby interface election based on protocol packets received from servers. ARP/ND/IGMP/DHCP/MLD packets are supported. You can run this command to configure the packet type for active/standby interface election.

**Precautions**

When M-LAG member interfaces work in active/standby mode, at least one packet type must be configured for active/standby interface election.


Example
-------

# Configure M-LAG member interfaces in active/standby mode to support active/standby interface election through ND packets.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] m-lag active-standby election nd

```

# Configure M-LAG member interfaces in active/standby mode to support active/standby interface election through ARP packets.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] m-lag active-standby election arp

```