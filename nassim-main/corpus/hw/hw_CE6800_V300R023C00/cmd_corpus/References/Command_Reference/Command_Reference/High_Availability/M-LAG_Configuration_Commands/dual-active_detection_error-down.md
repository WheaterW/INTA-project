dual-active detection error-down
================================

dual-active detection error-down

Function
--------



The **dual-active detection error-down** command disables or delays the action of setting interfaces except the management interface and peer-link interface on one device to error-down state when the peer-link fails but the DAD heartbeat status is normal.

The **undo dual-active detection error-down** command restores the default action when the peer-link fails but the DAD heartbeat status is normal.



By default, interfaces except the management interface and peer-link interface on one device enter the error-down state when the peer-link fails but the DAD heartbeat status is normal.


Format
------

**dual-active detection error-down** { **disable** | **delay** *delaytime* }

**undo dual-active detection error-down** { **disable** | **delay** | **delay** *delaytime* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables the action of setting interfaces except the management interface and peer-link interface on one device to error-down state when the peer-link fails but the DAD heartbeat status is normal. | - |
| **delay** *delaytime* | Specifies the time to delay the action of setting interfaces except the management interface and peer-link interface on one device to error-down state when the peer-link fails but the DAD heartbeat status is normal. | The value is an integer that ranges from 0 to 7200. The default value is 0. |



Views
-----

DFS group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an access device is single-homed to M-LAG master and backup devices at Layer 3, traffic forwarding on the device is not affected in a dual-active scenario where the peer-link fails but the DAD heartbeat status is normal. To prevent packet loss, you can run the **dual-active detection error-down** command to disable or delay the action of setting interfaces except the management interface and peer-link interface on one M-LAG device to error-down state when the peer-link fails but the DAD heartbeat status is normal.If delay-time is set to 0, the system does not delay the action of setting interfaces except the management interface and peer-link interface on one M-LAG device to error-down state when the peer-link fails but the DAD heartbeat status is normal.

**Precautions**

When an access device is connected to M-LAG master and backup devices using M-LAG dual-homing access mode or Layer 2 access mode, you cannot disable or delay the Error-Down action.


Example
-------

# Disable the action of setting interfaces except the management interface and peer-link interface on one device to error-down state when the peer-link fails but the DAD heartbeat status is normal.
```
<HUAWEI> system-view
[~HUAWEI] dfs-group 1
[*HUAWEI-dfs-group-1] dual-active detection error-down disable

```