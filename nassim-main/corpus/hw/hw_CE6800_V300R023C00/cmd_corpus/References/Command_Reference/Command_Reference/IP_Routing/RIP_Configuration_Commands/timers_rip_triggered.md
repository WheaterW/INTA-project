timers rip triggered
====================

timers rip triggered

Function
--------



The **timers rip triggered** command sets the value of the triggered timer.

The **undo timers rip triggered** command disables the triggered timer or restores the default value of the triggered timer.



By default, the triggered timer is disabled.


Format
------

**timers rip triggered** { **minimum-interval** *minimum-interval* | **incremental-interval** *incremental-interval* | **maximum-interval** *maximum-interval* } \*

**undo timers rip triggered** [ **minimum-interval** [ *minimum-interval* ] | **incremental-interval** [ *incremental-interval* ] | **maximum-interval** [ *maximum-interval* ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **minimum-interval** *minimum-interval* | Specifies the minimum interval for triggering Update packets. | The value is an integer ranging from 100 to 5000, in milliseconds. The default value is 100. |
| **incremental-interval** *incremental-interval* | Specifies the incremental interval for triggering Update packets. | The value is an integer ranging from 100 to 1000, in milliseconds. The default value is 100. |
| **maximum-interval** *maximum-interval* | Specifies the maximum interval for triggering Update packets. | The value is an integer ranging from 200 to 5000, in milliseconds. The default value is 5000. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a stable network, you can set a large value for the triggered timer. On a network whose topology frequently changes, do not set the value of the triggered timer too small; otherwise devices will send Update packets frequently.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.

**Precautions**

If no parameter is specified or all parameters are specified in the **undo timers rip triggered** command, the triggered timer is disabled. If other parameters are specified (not all parameters are specified), the triggered timer is enabled, but the specified parameters are restored to the default values.


Example
-------

# set the triggered timer value to 1000 ms.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] timers rip triggered minimum-interval 1000

```