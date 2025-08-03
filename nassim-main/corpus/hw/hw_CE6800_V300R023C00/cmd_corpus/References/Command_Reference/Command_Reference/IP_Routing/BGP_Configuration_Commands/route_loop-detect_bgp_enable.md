route loop-detect bgp enable
============================

route loop-detect bgp enable

Function
--------



The **route loop-detect bgp enable** command enables BGP loop detection.

The **undo route loop-detect bgp enable** command disables BGP loop detection.



By default, BGP loop detection is disabled.


Format
------

**route loop-detect bgp enable**

**undo route loop-detect bgp enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If BGP loop detection is incorrectly reported or other problems are caused by BGP loop detection, run the **undo route loop-detect bgp enable** command to disable BGP loop detection. To enable BGP loop detection again, run the **route loop-detect bgp enable** command.

**Precautions**

If BGP loop detection is disabled, the routes that caused a routing loop may form another loop after the existing loop is resolved. Therefore, exercise caution when running the **undo route loop-detect bgp enable** command.


Example
-------

# Disable BGP loop detection.
```
<HUAWEI> system-view
[~HUAWEI] undo route loop-detect bgp enable

```

# Enable BGP loop detection.
```
<HUAWEI> system-view
[~HUAWEI] route loop-detect bgp enable

```