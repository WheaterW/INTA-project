set system next-work-mode
=========================

set system next-work-mode

Function
--------



The **set system next-work-mode** command configures the system working mode.



By default, the device starts in low-latency mode.


Format
------

**set system next-work-mode** { **standard-forward** | **low-latency** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **standard-forward** | The system works in common forwarding mode. | - |
| **low-latency** | The system works in low-delay mode. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



The device can work in low-latency mode or common forwarding mode. You can manually configure the next working mode by running commands.



**Precautions**

* After configuring the working mode for the next startup, restart the device for the configuration to take effect.
* Only the CE6885-LL-56F supports this command.


Example
-------

# Set the working mode for the next startup to standard-forward.
```
<HUAWEI> system-view
[~HUAWEI] set system next-work-mode standard-forward
Warning: The setting will take effect after the system reboots. Ensure that the next startup mode is supported by the board. Continue? [Y/N]:y
Info: The setting succeeded. The new system working mode is standard-forward.

```