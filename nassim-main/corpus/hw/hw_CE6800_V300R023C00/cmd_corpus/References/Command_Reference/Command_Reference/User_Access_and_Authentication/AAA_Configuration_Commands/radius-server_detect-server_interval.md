radius-server detect-server interval
====================================

radius-server detect-server interval

Function
--------

The **radius-server detect-server interval** command configures an automatic detection interval for RADIUS servers in Down status.

The **undo radius-server detect-server interval** command restores the default settings.

The default automatic detection interval is 60 seconds.



Format
------

**radius-server detect-server interval** *interval*

**undo radius-server detect-server interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the automatic detection interval for RADIUS servers in Down status. | The value is an integer that ranges from 5 to 3600. The default value is 60. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After the automatic detection function is enabled using the **radius-server testuser** command, you can run the **radius-server detect-server interval** command to adjust the automatic detection interval for RADIUS servers in Down status.



Example
-------

# Set the automatic detection interval for RADIUS servers in Down status to 100 seconds in the RADIUS server template acs.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template acs
[*HUAWEI-radius-acs] radius-server detect-server interval 100

```