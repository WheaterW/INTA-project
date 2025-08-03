consistency-check enable
========================

consistency-check enable

Function
--------



The **consistency-check enable mode** command enables M-LAG consistency check and specifies a check mode.

The **undo consistency-check enable mode** command restores the default settings for M-LAG configuration consistency check.

The **consistency-check disable** command disables M-LAG consistency check.



By default, M-LAG consistency check is disabled.


Format
------

**consistency-check** { **enable** **mode** { **loose** | **strict** } | **disable** }

**undo consistency-check** [ **enable** **mode** { **loose** | **strict** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mode** | Specifies an M-LAG consistency check mode. | - |
| **loose** | Specifies the loose mode. | - |
| **strict** | Specifies the strict mode. | - |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The M-LAG configuration falls into two types: key configuration (Type 1) and common configuration (Type 2). There are two consistency check modes available for the key configuration: strict and loose.

* Key configuration (Type 1): If the configurations of the two M-LAG member devices are inconsistent, certain problems can occur, such as loops and long-period packet loss, even if the M-LAG status is normal.

In strict mode, if the key configurations of the two M-LAG member devices are inconsistent, the M-LAG member interface on the M-LAG backup device will enter the error-down state and an alarm that indicates key configuration inconsistency will be generated.In loose mode, if the key configurations of the two M-LAG member devices are inconsistent, an alarm that indicates key and common configuration inconsistencies will be generated.

* Common configuration (Type 2): If the configurations of the two M-LAG member devices are inconsistent, the M-LAG status may be abnormal. However, this problem, compared to that of the key configuration, has less impact on the live network.

Regardless of the chosen mode, if any common configuration inconsistencies are detected between the M-LAG member devices, an alarm that indicates key and common configuration inconsistencies will be generated.


Example
-------

# Enable M-LAG consistency check and specify the strict mode.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] consistency-check enable mode strict

```