dfs-group port-group
====================

dfs-group port-group

Function
--------



The **dfs-group port-group** command binds a DFS group to a user-side protection group.

The **undo dfs-group port-group** command unbinds a DFS group from a user-side protection group.



By default, no DFS group is bound to a user-side protection group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dfs-group** *dfs-group-id* **port-group** *port-group-id*

**undo dfs-group** *dfs-group-id* **port-group** *port-group-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |
| *port-group-id* | Specifies the ID of the active/standby protection group. | The value is an integer that ranges from 1 to 1024. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **dfs-group port-group** command needs to be configured only when the active and standby network adapters of the access device are connected to two M-LAG devices for multicast traffic forwarding. In addition, the port-group IDs configured on the two M-LAG devices must be the same. In other scenarios, only the **dfs-group m-lag** command needs to be configured.

**Precautions**

* The dfs-group port-group and **dfs-group m-lag** commands are mutually exclusive and cannot be configured on the same interface.
* The dfs-group port-group and **peer-link** commands are mutually exclusive and cannot be configured on the same interface.
* You are advised not to use ports in a protection group to connect to active and standby NICs. You are advised to use the M-LAG active/standby mode.

Example
-------

# Bind the DFS group with ID 1 to user-side Eth-Trunk 2 and set the port-group-id to 2.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] dfs-group 1 port-group 2

```