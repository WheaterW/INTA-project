user-interface vty available-vty-threshold
==========================================

user-interface vty available-vty-threshold

Function
--------



The **user-interface vty available-vty-threshold** command sets the alarm threshold for the number of VTY channels.

The **undo user-interface vty available-vty-threshold** command restores the default alarm threshold for the number of VTY channels.



By default,the alarm threshold for the number of VTY channels is 4.


Format
------

**user-interface vty available-vty-threshold** *threshold-value*

**undo user-interface vty available-vty-threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Alarm threshold for the number of VTY channels. | The value is an integer that ranges from 0 to 21. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When the number of available VTYs in the system is less than the threshold, the device reports an alarm. When the number of available VTYs in the system is greater than or equal to the threshold, the device does not generate or clear the alarm. When the number of available VTYs in the system is greater than the threshold, the alarm is cleared.


Example
-------

# Set the alarm threshold for the number of VTY channels to 7.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty available-vty-threshold 7

```