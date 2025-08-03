condition timer (Maintenance assistant task view)
=================================================

condition timer (Maintenance assistant task view)

Function
--------



The **condition timer** command sets the time at which a maintenance assistant is to be executed.



By default, the time when a maintenance assistant is executed is not configured.


Format
------

**condition timer** *cron* *minutes* *hours* *daysOfMonth* *months* *daysOfWeek* [ *years* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cron* | Specifies the format of cron time. | Currently, only cron is supported. |
| *minutes* | Specifies the minute information. | The value is a string of characters in the format of cron time. The value ranges from 0 to 59. |
| *hours* | Specifies the hour information. | The value is a string of characters in the format of cron time. The value ranges from 0 to 23. |
| *daysOfMonth* | Specifies the day of a month. | The value is a string of characters in the format of cron time. The value ranges from 1 to 28, 29, 30, or 31 based on the specific month. The value and daysOfWeek are mutually exclusive. Either of them must be configured as \*. |
| *months* | Specifies the month information. | The value is a string of characters in the format of cron time. The value ranges from 1 to 12. |
| *daysOfWeek* | Specifies the day of a week. | The value is a string of characters in the format of cron time. The value ranges from 0 to 7. Both 0 and 7 indicate Sunday. The value 1 to 6 indicate Monday to Saturday. The value and daysOfMonth are mutually exclusive. Either of them must be configured as \*. |
| *years* | Specifies the year information. | The value is a string of characters in the format of cron time. The value ranges from 2000 to 2099. This parameter is optional. If this parameter is not specified, all years from 2000 to 2099 are covered. |



Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure the time when a maintenance assistant is executed, run the **condition timer cron** command.After an alarm is generated, an event occurs, or a timer expires, the maintenance assistant can be executed.To trigger a maintenance assistant based on a timer, run this command. The time is expressed using the syntax in Unix or Linux cron program.The common time format hh:mm:ss dd-mm-yyyy usually represents a fixed moment. The time in the cron format is more flexible and can represent a single moment, multiple moments, time range, or interval in a simplified manner. The value can contain 10 numbers (0 to 9) and four special characters (\*, -, / and ,).

**Prerequisites**

The **assistant** command has been run in the system view to create a maintenance assistant.

**Precautions**

* If both days-of-month and days-of-week are configured as \*, all days are covered.
* The tasks are executed in sequence, and the period that each task lasts is not fixed and may be longer than the period during which the subsequent task instance is generated. Therefore, the time when a task instance is executed may vary from the time when a task instance is generated. The **condition timer cron** command configures the time when a task instance is generated but not the time when the task instance is executed.
* A maintenance assistant can be configured with only one condition.

Example
-------

# Configure a maintenance assistant named task to be executed at 20:00 on May 4, 2020.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition timer cron 0 20 4 5 * 2020

```

# Configure a maintenance assistant named task to be executed at each minute.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition timer cron * * * * * *

```