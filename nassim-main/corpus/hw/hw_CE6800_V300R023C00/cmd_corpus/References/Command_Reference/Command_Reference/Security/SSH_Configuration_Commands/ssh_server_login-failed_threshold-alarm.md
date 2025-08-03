ssh server login-failed threshold-alarm
=======================================

ssh server login-failed threshold-alarm

Function
--------



The **ssh server login-failed threshold-alarm** command configures alarm generation and clearance thresholds for SSH server login failures within a specified period.

The **undo ssh server login-failed threshold-alarm** command restores the default alarm generation and clearance thresholds.



By default, an alarm is generated if the number of login failures reaches 30 within 5 minutes and is cleared if the number of login failures falls below 20 within the same period.


Format
------

**ssh server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*

**undo ssh server login-failed threshold-alarm**

**undo ssh server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lower-limit** *resume-times* | Specifies an alarm clearance threshold. | The value is an integer ranging from 0 to report-times and varies with report-times. The default value is 20, and the maximum value is 45. If resume-times is 0, the function is the same as that when the value is set to 1, which means that a clear alarm is generated if no login failures occur. |
| **period** *period-time* | Specifies a statistics collection period. | The value is an integer ranging from 1 to 120, in minutes. The default value is 5. If report-times is 0, the period-time value specified does not take effect. |
| **upper-limit** *report-times* | Specifies an alarm generation threshold. | The value is an integer ranging from 0 to 100. The default value is 30. If the value is 0, no alarms are generated upon SSH server login failures. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To manage frequent SSH server login failures within a specified period, run the **ssh server login-failed threshold-alarm** command to configure alarm generation and clearance thresholds for the login failures. This configuration enables the device to generate alarms for administrators to promptly handle associated events. The alarm SSH\_1.3.6.1.4.1.2011.5.25.207.2.8 hwSSHLoginFailed is generated when the number of login failures reaches report-times within period-time, and the clear alarm SSH\_1.3.6.1.4.1.2011.5.25.207.2.10 hwSSHLoginFailedClear is generated when the number of login failures falls below resume-times within the same period.This command takes effect for both IPv4 and IPv6 SSH servers.




Example
-------

# Configure the device to generate an alarm when the number of SSH server login failures within 3 minutes reaches 20 and clear the alarm when the number of SSH server login failures within 3 minutes is less than 10.
```
<HUAWEI> system-view
[~HUAWEI] ssh server login-failed threshold-alarm upper-limit 20 lower-limit 10 period 3

```