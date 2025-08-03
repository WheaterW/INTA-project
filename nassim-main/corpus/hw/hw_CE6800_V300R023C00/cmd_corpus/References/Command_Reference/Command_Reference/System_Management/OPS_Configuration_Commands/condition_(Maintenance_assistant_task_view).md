condition (Maintenance assistant task view)
===========================================

condition (Maintenance assistant task view)

Function
--------



The **condition alarm level** command configures the severity of an alarm as a triggering condition for a maintenance assistant.

The **condition name** command configures a triggering condition for a maintenance assistant.

The **undo condition** command cancels the configuration.



By default, no triggering condition is configured for a maintenance assistant.


Format
------

**condition** { **alarm** [ *alarm-type* ] | **event** } **feature** *feature-name* **name** *event-name* [ *para-name* *para-optype* *para-value* ] &<1-4> [ **occurs** *occur-number* [ **period** *period-value* ] ]

**condition alarm level** { **eq** | **ge** | **gt** | **le** | **lt** | **ne** } { **critical** | **major** | **minor** | **warning** }

**undo condition**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **alarm** | Indicates an alarm as the triggering condition. | - |
| *alarm-type* | Specify the type of alarm as the triggering condition. | The value is of the enumerated type and can be start or end. |
| **event** | Indicates an event as the triggering condition. | - |
| **feature** *feature-name* | Specifies a feature as the triggering condition. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **name** *event-name* | Specifies the alarm or event name. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *para-name* | Specifies the name of an alarm or event. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *para-optype* | Specify parameter comparing method. | The value is of the enumerated type and can be eq, ge, gt, le, lt or ne. |
| *para-value* | Specifies the parameter value of an alarm or event. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **occurs** *occur-number* | Specifies the number of times an alarm or event is generated. | The value is an integer ranging from 1 to 32. |
| **period** *period-value* | Specifies the period during which alarms or events are generated. | The value is an integer ranging from 1 to 4294967295. |
| **eq** | Specifies eq as the comparing operation. | - |
| **ge** | Specifies ge as the comparing operation. | - |
| **gt** | Specifies gt as the comparing operation. | - |
| **le** | Specifies le as the comparing operation. | - |
| **lt** | Specifies lt as the comparing operation. | - |
| **ne** | Specifies ne as the comparing operation. | - |
| **critical** | Sets the alarm severity to critical. | - |
| **major** | Sets the alarm severity to major. | - |
| **minor** | Sets the alarm severity to minor. | - |
| **warning** | Sets the alarm severity to warning. | - |



Views
-----

Maintenance assistant task view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure the severity of an alarm as a triggering condition for a maintenance assistant, run the **condition alarm level** command.This command does not specify an alarm but specifies the severity of an alarm as a triggering condition. For example, you can configure a maintenance assistant to perform a task if a critical alarm is generated.

After an alarm or event is generated, the maintenance assistant can be executed.Configuring a task-related alarm or event as the triggering condition is recommended. For example, the task of a maintenance assistant is to restart the power module. You can configure the alarm indicating a power module failure as the triggering condition.

**Prerequisites**

The **assistant** command has been run in the system view to create a maintenance assistant.

**Precautions**

Only one trigger condition can be configured for one task of the maintenance assistant.When an alarm is generated or cleared, the maintenance assistant is triggered to perform the task.If the alarm or event in the trigger condition is not supported in the current version, the maintenance assistant will not be triggered.


Example
-------

# Configure an ifnet alarm named linkdown as the triggering condition for a maintenance assistant.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition alarm start feature ifnet name linkdown

```

# Configure an ifnet alarm named linkdown as the triggering condition.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant task
[*HUAWEI-ops-assistant-task] condition alarm feature ifnet name linkdown

```

# Execute the maintenance assistant config if a critical alarm is generated.
```
<HUAWEI> system-view
[~HUAWEI] ops
[~HUAWEI-ops] assistant config
[*HUAWEI-ops-assistant-config] condition alarm level eq critical

```