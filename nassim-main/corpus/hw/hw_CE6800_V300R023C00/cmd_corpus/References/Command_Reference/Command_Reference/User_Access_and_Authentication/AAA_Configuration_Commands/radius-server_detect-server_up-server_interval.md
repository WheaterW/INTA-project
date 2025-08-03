radius-server detect-server up-server interval
==============================================

radius-server detect-server up-server interval

Function
--------

The **radius-server detect-server up-server interval** command enables automatic detection for RADIUS servers in Up status and configures the automatic detection interval.

The **undo radius-server detect-server up-server interval** command restores the default settings.

By default, a device does not automatically detect RADIUS servers in Up status.



Format
------

**radius-server detect-server up-server interval** *interval*

**undo radius-server detect-server up-server interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the automatic detection interval for RADIUS servers in Up status. | The value is an integer that ranges from 0 or 2 to 3600, in seconds. The value 0 indicates that the device does not automatically detect RADIUS servers in Up status. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After automatic detection is enabled using the **radius-server testuser** command, the device automatically detects only RADIUS servers in Down status by default. To make the device automatically detect RADIUS servers in Up status, run the **radius-server detect-server up-server interval** command to enable automatic detection for RADIUS servers in Up status and configure the automatic detection interval.



Example
-------

# Enable automatic detection for RADIUS servers in Up status and set the automatic detection interval to 100 seconds in the RADIUS server template acs.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template acs
[*HUAWEI-radius-acs] radius-server detect-server up-server interval 100

```