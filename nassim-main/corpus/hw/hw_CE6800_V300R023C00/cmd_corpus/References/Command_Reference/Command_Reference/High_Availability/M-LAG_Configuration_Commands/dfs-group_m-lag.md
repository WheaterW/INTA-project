dfs-group m-lag
===============

dfs-group m-lag

Function
--------



The **dfs-group m-lag** command binds a user-side interface to a DFS group.

The **undo dfs-group m-lag** command unbinds a user-side interface from a DFS group.



By default, no user-side interface is bound to a DFS group.


Format
------

**dfs-group** *dfs-group-id* **m-lag** *m-lag-id* [ **active-standby** ]

**undo dfs-group** [ *dfs-group-id* [ **m-lag** *m-lag-id* [ **active-standby** ] ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Indicates the ID of a DFS group. | The value must be 1. |
| *m-lag-id* | Specifies the ID of a user-side interface. The specification is the same as that of an Eth-Trunk. | The value is an integer ranging from 1 to 2048. |
| **active-standby** | Indicates the active/standby mode. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Ensure that the bound Eth-Trunk interface is connected to a device that needs to be dual-homed to the M-LAG, and the two M-LAG devices must be configured with the same m-lag-id.If the active-standby parameter is not specified when this command is run, M-LAG member interfaces work in active/active mode.If the active-standby parameter is specified when this command is run, M-LAG member interfaces work in active/standby mode.Before configuring M-LAG member interfaces in active/standby mode, configure the packet type for active/standby interface election.

**Precautions**



A Layer 3 Eth-Trunk interface cannot be configured as an M-LAG member interface.When VBST is enabled, the default STP configuration must be used on M-LAG interfaces. The configuration includes the port cost, port priority, and point-to-point setting.




Example
-------

# Bind Eth-Trunk interface 2 to DFS group 1 and set the value of m-lag-id to 3.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] dfs-group 1 m-lag 3

```