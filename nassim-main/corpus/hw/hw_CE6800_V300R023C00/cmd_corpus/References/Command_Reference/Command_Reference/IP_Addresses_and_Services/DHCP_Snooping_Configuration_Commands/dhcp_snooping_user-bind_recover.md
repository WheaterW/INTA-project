dhcp snooping user-bind recover
===============================

dhcp snooping user-bind recover

Function
--------



The **dhcp snooping user-bind recover** command triggers the function of restoring binding tables from a specified file.




Format
------

**dhcp snooping user-bind recover** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *file-name* | Specifies the path and name of the file used to restore DHCP snooping binding table, and the path and name of the file supported by the device must be entered at the same time. | The value is a string of 12 to 51 case-sensitive characters without spaces. The file name with a full path must be flash:/\*.tbl. The file name without a path or format can contain only digits, letters, and special characters ('\_' and '-'). |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To manually restore DHCP snooping binding tables from a specified file, run the **dhcp snooping user-bind recover** command.

**Prerequisites**

Before running this command, local automatic backup of DHCP snooping binding tables has been enabled using the **dhcp snooping user-bind autosave** command.

**Precautions**

The extension of the specified binding table file must be .tbl.This command is used to restore all DHCPv4 and DHCPv6 binding entries. If the binding entry to be restored already exists on the device, the binding entry cannot be restored.


Example
-------

# Manually restore the user binding table from the specified backup file.
```
<HUAWEI> system-view
[~HUAWEI] dhcp snooping user-bind autosave flash:/dhcpsnp.tbl
[~HUAWEI] dhcp snooping  user-bind recover flash:/dhcpsnp.tbl

```