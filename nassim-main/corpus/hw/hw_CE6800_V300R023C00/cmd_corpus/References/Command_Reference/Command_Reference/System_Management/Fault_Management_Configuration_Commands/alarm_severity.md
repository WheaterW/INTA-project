alarm severity
==============

alarm severity

Function
--------



The **alarm severity** command changes the severity of a specific alarm.

The **undo alarm severity** command restores the default severity.



By default, the severity of an alarm is determined when the alarm is defined.


Format
------

**alarm** *alarm-name* **severity** { **critical** | **major** | **minor** | **warning** } [ **instance** *instance-name* ]

**undo alarm** *alarm-name* **severity** [ **instance** *instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alarm-name* | Specifies the name of an alarm. It is configured when an alarm is defined. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **severity** | Specifies the severity of an alarm. | - |
| **critical** | Specifies the severity of an alarm to be critical. | - |
| **major** | Specifies the severity of an alarm to be major. | - |
| **minor** | Specifies the severity of an alarm to be minor. | - |
| **warning** | Specifies the severity of an alarm to be warning. | - |
| **instance** *instance-name* | Alarm object instance name. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to change the severity of an alarm when the actual service requirement is not met.The descriptions of alarm severities are as follows:

* Critical: A service affecting condition has occurred, and an immediate corrective action is required. For example, a managed node fails and it must be repaired.
* Major: A service affecting condition has developed, and an urgent corrective action is required. For example, the capabilities of a managed node are seriously weakened, and all capabilities must be restored.
* Minor: A non-service affecting fault condition exists, and a corrective action should be taken in order to prevent more serious fault (for example, service affecting). For example, the capabilities of a managed node are not weakened at present.
* Warning: A potential or impending service affecting fault is deleted, before any significant effects have been sensed. Relevant measures must be taken for further fault diagnosis and fault repair to prevent the fault from getting worse.

**Prerequisites**

The alarm has been defined.

**Configuration Impact**

The severity of the alarm is changed.

**Follow-up Procedure**

Run the **display alarm information** command and check whether the changed configuration takes effect. You can run the undo alarm severity command to restore the default severity.

**Precautions**

Changing the severity of an alarm does not trigger the generation of new alarms. The NMS host can be configured to synchronize alarms with that on the device.


Example
-------

# Set the severity of the alarm named linkdown to critical.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] alarm linkdown severity critical

```