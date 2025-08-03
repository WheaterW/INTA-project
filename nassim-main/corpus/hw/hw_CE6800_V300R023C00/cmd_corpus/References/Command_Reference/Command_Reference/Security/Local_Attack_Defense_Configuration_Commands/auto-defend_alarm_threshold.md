auto-defend alarm threshold
===========================

auto-defend alarm threshold

Function
--------



The **auto-defend alarm threshold** command sets the event reporting threshold for attack source tracing.

The **undo auto-defend alarm threshold** command restores the default event reporting threshold for attack source tracing.



By default, the event reporting threshold for attack source tracing is 128 pps.


Format
------

**auto-defend alarm threshold** *alarm-threshold*

**undo auto-defend alarm threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *alarm-threshold* | Specifies the event reporting threshold for attack source tracing. | The value is an integer that ranges from 1 to 65535. The default value is 128. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the number of packets of a specified protocol from an attack source exceeds the threshold in a specified period, the device reports an event to the administrator so that the administrator can take measures to protect the device.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command, and the alarm source tracing function has been enabled using the **auto-defend alarm enable** command.

**Precautions**

If you run the **auto-defend alarm threshold** command in the same attack defense policy view multiple times, only the latest configuration takes effect.


Example
-------

# Set the event reporting threshold for attack source tracing in the attack defense policy named test to 300 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend alarm enable
[*HUAWEI-cpu-defend-policy-test] auto-defend alarm threshold 300

```