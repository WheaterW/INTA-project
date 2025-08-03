access-user syslog-restrain period
==================================

access-user syslog-restrain period

Function
--------

The **access-user syslog-restrain period** command sets a period for system log suppression.

The **undo access-user syslog-restrain period** command restores the default period for system log suppression.

By default, the period of system log suppression is 300s.



Format
------

**access-user syslog-restrain period** *period*

**undo access-user syslog-restrain period**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *period* | Specifies the period for system log suppression. | The value is an integer that ranges from 60 to 604800, in seconds. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After the system log suppression function is enabled using the **access-user syslog-restrain enable** command, use this command to set the system log suppression period. After generating a system log, the device will not generate the same log within the suppression period.



Example
-------

# Set the period for system log suppression to 600s.
```
<HUAWEI> system-view
[~HUAWEI] access-user syslog-restrain period 600

```