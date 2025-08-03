condition syslog pattern
========================

condition syslog pattern

Function
--------



The **condition syslog pattern** command configures Syslogs as the triggering condition for a maintenance assistant.



By default, no triggering condition is configured for a maintenance assistant.


Format
------

**condition syslog pattern** *reg-express* [ **occurs** *occur-number* [ **period** *period-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reg-express* | Specifies the formula expression of a Syslog. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **occurs** *occur-number* | Specifies the number of times a Syslog is generated. | The value is an integer ranging from 1 to 32. |
| **period** *period-value* | Specifies the period during which a Syslog is generated. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a maintenance assistant is created, a triggering condition must be specified so that the maintenance assistant can be automatically operated as long as the triggering condition is met.To trigger a maintenance assistant based on a Syslog, run the condition syslog pattern command.

**Prerequisites**

The **assistant** command has been run in the system view to create a maintenance assistant.

**Precautions**

A maintenance assistant can be configured with only one triggering condition.


Example
-------

# Configure the maintenance assistant to be triggered based on Syslog hwClockChanged.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition syslog pattern .*hwClockChanged.*

```