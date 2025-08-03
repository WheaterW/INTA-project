dfs-group
=========

dfs-group

Function
--------



The **dfs-group** command creates a Dynamic Fabric Service (DFS) group.

The **undo dfs-group** command deletes a DFS group.



By default, no DFS group is created.


Format
------

**dfs-group** *dfs-group-id*

**undo dfs-group** *dfs-group-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A DFS group is used for device pairing. Before configuring M-LAG on a dual-active network, you must run the **dfs-group** command to create a DFS group.

**Precautions**

* The dfs-group and **ipv4 source check user-bind enable** commands are mutually exclusive.
* On the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, the **dfs-group** command and the **authentication-profile** command in the interface view are mutually exclusive.


Example
-------

# Delete a DFS group.
```
<HUAWEI> system-view
[~HUAWEI] undo dfs-group 1

```

# Configure a DFS group.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1

```