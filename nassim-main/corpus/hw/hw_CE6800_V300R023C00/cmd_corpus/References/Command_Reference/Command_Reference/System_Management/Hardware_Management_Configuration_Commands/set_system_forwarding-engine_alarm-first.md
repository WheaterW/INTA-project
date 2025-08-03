set system forwarding-engine alarm-first
========================================

set system forwarding-engine alarm-first

Function
--------



The **set system forwarding-engine alarm-first** command configures the device to only generate an alarm in case of faults.

The **undo set system forwarding-engine alarm-first** command restores the default configuration.



By default, an alarm is generated and the device or board is reset in case of faults.


Format
------

**set system forwarding-engine alarm-first**

**undo set system forwarding-engine alarm-first**


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



You can configure different actions for forwarding chip events. If the alarm-first function is disabled and related major failures occur, the corresponding board restarts according to the handling policy. If the alarm-first function is enabled and related major failures occur, an alarm is generated, but the corresponding board does not restart.



**Precautions**

If the alarm-first function is enabled and a critical fault occurs on the device, the device does not reset even if the alarm-first priority function is disabled. The device resets only after the previous critical alarm is cleared and a new critical fault occurs.


Example
-------

# Configure the device to only generate an alarm in case of faults.
```
<HUAWEI> system-view
[~HUAWEI] set system forwarding-engine alarm-first

```