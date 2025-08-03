auto-defend threshold
=====================

auto-defend threshold

Function
--------



The **auto-defend threshold** command sets the checking threshold for attack source tracing.

The **undo auto-defend threshold** command restores the default checking threshold for attack source tracing.



By default, you can view the checking threshold for attack source tracing in the auto-defend threshold field of the display auto-defend configuration cpu-defend policy default command output.


Format
------

**auto-defend threshold** *threshold-value*

**undo auto-defend threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Specifies the threshold for checking attack source tracing. | The value is an integer that ranges from 1 to 65535. The default value is 128. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After attack source tracing is enabled, you can set the checking threshold for attack source tracing. When the number of sent protocol packets from an attack source in a specified period exceeds the checking threshold, the device traces and logs the attack source.

**Prerequisites**

Attack source tracing has been enabled using the **auto-defend enable** command.

**Precautions**

If you run the **auto-defend threshold** command in the same attack defense policy view multiple times, only the latest configuration takes effect.After the **auto-defend enable** command is executed, the device traces the attack source based on the default threshold even if the **auto-defend threshold** command is not used.


Example
-------

# Set the checking threshold for attack source tracing in the attack defense policy named test to 200 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] auto-defend enable
[*HUAWEI-cpu-defend-policy-test] auto-defend threshold 200

```