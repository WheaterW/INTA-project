ftp server login-failed threshold-alarm
=======================================

ftp server login-failed threshold-alarm

Function
--------



The **ftp server login-failed threshold-alarm** command configures alarm generation and clearance thresholds for FTP server login failures within a specified period.

The **undo ftp server login-failed threshold-alarm** command restores the default alarm generation and clearance thresholds.



By default, an alarm is generated if the number of login failures reaches 30 within 5 minutes and is cleared if the number of login failures falls below 20 within the same period.


Format
------

**ftp server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*

**undo ftp server login-failed threshold-alarm**

**undo ftp server login-failed threshold-alarm upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lower-limit** *resume-times* | Specifies the number of times authentication failure clear alarms are reported. | The value is an integer that ranges from 0 to 45. If this parameter is set to 0, the alarm is cleared when no login failure occurs within the specified period. |
| **period** *period-time* | Specifies the period in which failure alarms are counted. | The value is an integer ranging from 1 to 120, in minute. |
| **upper-limit** *report-times* | Specifies the number of times authentication failure alarms are reported. | The value is an integer ranging from 0 to 100. If the value is 0, no authentication failure alarm is reported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an FTP management user frequently fails to log in within a short period, the device generates a management security alarm and reports it to administrators for their intervention. To configure alarm reporting and clearance thresholds within a specified period, run the ftp server login-failed threshold-alarm command.The command takes effect for both ipv4 and ipv6 FTP servers.


Example
-------

# Configure 40 as the alarm reporting threshold and 25 as the alarm clearance threshold within 10 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ftp server login-failed threshold-alarm upper-limit 40 lower-limit 25 period 10

```