configuration current backup-to-file
====================================

configuration current backup-to-file

Function
--------



The **configuration current backup-to-file** command enables and sets the configuration for periodically backing up the configuration file. If interval and from are not specified, the system uses the default values. The default start time of the periodic backup is 05:00, and the default interval is one day.

The **undo configuration current backup-to-file** command disables the function of periodically backing up the configuration file.



By default, the periodic configuration backup function is enabled.


Format
------

**configuration current backup-to-file** [ **interval** *interval-time* | **from** *time* ] \*

**undo configuration current backup-to-file**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval-time* | Interval for periodic backup. | The value is an integer ranging from 1 to 7, in days. |
| **from** *time* | Start time of periodic backup. | The value is time format, ranging from 00:00 to 23:59. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



After this function is enabled, if a configuration error occurs, you can use the local backup configuration file to roll back the configuration. The backup configuration file is automatically saved to the $\_autobackup directory in the flash memory. The file name contains the time when the configuration file is saved. The default file name extension is .zip.




Example
-------

# Enable or set the configuration for the periodic backup.
```
<HUAWEI> system-view
[~HUAWEI] configuration current backup-to-file interval 2 from 22:00

```