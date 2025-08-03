info-center log-storage-time
============================

info-center log-storage-time

Function
--------



The **info-center log-storage-time** command configures the log retention period.

The **undo info-center log-storage-time** command deletes the log retention period.



By default, the log retention period is disabled, and management logs cannot be maintained by time.


Format
------

**info-center log-storage-time** *day-value*

**undo info-center log-storage-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *day-value* | Specifies the log retention period. | The value is an integer ranging from 30 to 1095, in days. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* After the log retention period is configured, expired logs are not deleted immediately. They are deleted only after the configured number of days.
* Only security logs, event logs, operation logs, and security service logs are involved in retention period management.

Example
-------

# Set the log retention period to 180 days.
```
<HUAWEI> system-view
[~HUAWEI] info-center log-storage-time 180

```