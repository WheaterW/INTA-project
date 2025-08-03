ssl certificate alarm-threshold
===============================

ssl certificate alarm-threshold

Function
--------



The **ssl certificate alarm-threshold** command sets the time when an alarm is generated before the certificate expires and the certificate expiration check interval.

The **undo ssl certificate alarm-threshold** command restores the default time when an alarm is generated before the certificate expires and the default certificate expiration check interval.



By default, the alarm threshold for certificate expiration is 90 days and the alarm check period is 24 hour.


Format
------

**ssl certificate alarm-threshold early-alarm** *time* **check-interval** *check-period*

**undo ssl certificate alarm-threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **check-interval** *check-period* | Specifies an interval at which certificate expiration alarms are checked. | The value is an integer data type. The value range is from 1 to 168 hours. Default value is 24 hours. |
| **early-alarm** *time* | Specifies an early alarm time of certificates. | The value is an integer data type. The value range is from 7 to 180 days. Default value is 90 days. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To change the alarm threshold or check interval, run this command.


Example
-------

# Set the time when an alarm is generated before the certificate expires to 15 days and the certificate expiration check interval to 10 hours.
```
<HUAWEI> system-view
[~HUAWEI] ssl certificate alarm-threshold early-alarm 15 check-interval 10

```