reset statistics(Alarm management view)
=======================================

reset statistics(Alarm management view)

Function
--------



The **reset statistics** command clears alarm statistics.




Format
------

**reset statistics name** *alarm-name*

**reset statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *alarm-name* | Specifies the name of an alarm. This alarm must exist. | The value is a string of 1 to 63 characters, spaces not supported. |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics to simplify statistics display, run this command.The reset statistics name <alarm-name> command clears statistics about a specific alarm. The **reset statistics** command clears statistics about all alarms.

**Configuration Impact**

The **reset statistics** command clears alarm statistics but cannot clear the active alarm list, previously generated alarm list, or log data.

**Precautions**

Alarm statistics are maintenance data. After the device is reset or the statistics are cleared, the previous statistics cannot be obtained. Therefore, before clearing the statistics, you are advised to run the **display alarm statistics** command to obtain the alarm statistics and back up the statistics.


Example
-------

# Display statistics about a specific alarm.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] reset statistics name linkDown

```

# Display statistics about all alarms.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] reset statistics

```