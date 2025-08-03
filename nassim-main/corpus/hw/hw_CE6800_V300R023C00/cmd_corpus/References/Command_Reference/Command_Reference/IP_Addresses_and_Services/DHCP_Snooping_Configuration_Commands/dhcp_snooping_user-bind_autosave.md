dhcp snooping user-bind autosave
================================

dhcp snooping user-bind autosave

Function
--------



The **dhcp snooping user-bind autosave** command enables local automatic backup of the DHCP snooping binding table and configures the file to be saved.

The **undo dhcp snooping user-bind autosave** command disables local automatic backup of the DHCP snooping binding table and deletes the configured file.



By default, local automatic backup of the DHCP snooping binding table is disabled.


Format
------

**dhcp snooping user-bind autosave** *file-name* [ **write-delay** *delay-time* ]

**undo dhcp snooping user-bind autosave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the path for storing the file that backs up the binding table and the file name. The file path and name supported by the device must be both entered. | The value is a string of 12 to 51 case-insensitive characters, spaces not supported. The file name with a full path must be flash:/\*.tbl. The file name without a path or format can contain only digits, letters, and special characters ('\_' and'-'). |
| **write-delay** *delay-time* | Specifies the interval for local automatic backup of the DHCP snooping binding table.  If this parameter is not specified, the backup interval is the default value. | The value is an integer that ranges from 60 to 4294967295. The default value is 3600. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device generates DHCP snooping binding entries for DHCP users, you can run the **dhcp snooping user-bind autosave** command to enable local automatic backup of the DHCP snooping binding table to prevent the binding entries from being lost after the device restarts.

**Prerequisites**

DHCP snooping has been enabled on the device using the **dhcp snooping enable** command.

**Precautions**

The extension of the backup binding table file must be .tbl, which contains all DHCPv4 and DHCPv6 binding tables on the current device.When the system time is changed or the user binding table is changed, if the device restarts within the configured update interval (1 hour by default), the time for automatically updating binding entries is not reached. In this case, you need to run the undo command and then the same command to trigger the backup of the latest binding entries, otherwise, after the switch restarts, the restored binding entries are different from the actual entries before the restart.If a device where the DHCP snooping binding table is backed up is powered off and then restarted after the lease of DHCP snooping binding table expires, the DHCP snooping entries cannot be restored.After this function is configured, if an interface goes Down, DHCP snooping binding entries on the interface are deleted from the backup binding table file.When a new file name is configured or the undo command is run, the old configuration file is deleted.


Example
-------

# Configure the device to back up the DHCP snooping binding table to the file backup.tbl in the flash every 5000 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp snooping enable
[*HUAWEI] dhcp snooping user-bind autosave flash:/backup.tbl write-delay 5000

```