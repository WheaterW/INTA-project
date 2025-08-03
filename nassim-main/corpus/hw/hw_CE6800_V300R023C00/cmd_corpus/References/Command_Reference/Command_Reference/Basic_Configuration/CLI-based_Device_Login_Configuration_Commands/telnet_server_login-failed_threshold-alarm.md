telnet server login-failed threshold-alarm
==========================================

telnet server login-failed threshold-alarm

Function
--------



The **telnet server login-failed threshold-alarm** command configures alarm generation and clearance thresholds for Telnet server login failures within a specified period.

The **undo telnet server login-failed threshold-alarm** command restores the default alarm generation and clearance thresholds.



By default, an alarm is generated if the number of login failures reaches 30 within 5 minutes and is cleared if the number of login failures falls below 20 within the same period.


Format
------

**telnet server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*

**undo telnet server login-failed threshold-alarm**

**undo telnet server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lower-limit** *resume-times* | Specifies an alarm clearance threshold. | The value is an integer ranging from 0 to report-times. It varies with report-times. The default value is 20, and the maximum value is 45. If resume-times is 0, it functions the same as the value is set to 1, which means that a clear alarm is generated if no login failures occur. |
| **period** *period-time* | Specifies a statistics collection period. | The value is an integer ranging from 1 to 120, in minutes. The default value is 5. If report-times is 0, the period-time value specified does not take effect. |
| **upper-limit** *report-times* | Specifies an alarm generation threshold. | The value is an integer ranging from 0 to 100. The default value is 30. If the value is 0, no alarms are generated upon Telnet server login failures. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To manage frequent Telnet server login failures within a specified period, run the **telnet server login-failed threshold-alarm** command to configure alarm generation and clearance thresholds for the login failures.This command takes effect for both ipv4 and ipv6 Telnet servers.

**Precautions**

The Telnet protocol has security risks. You are advised to use the SSH v2 protocol.


Example
-------

# Configure the device to generate an alarm when the number of Telnet server login failures within 3 minutes reaches 20 and clear the alarm when the number of Telnet server login failures within 3 minutes is less than 10.
```
<HUAWEI> system-view
[~HUAWEI] telnet server login-failed threshold-alarm upper-limit 20 lower-limit 10 period 3

```