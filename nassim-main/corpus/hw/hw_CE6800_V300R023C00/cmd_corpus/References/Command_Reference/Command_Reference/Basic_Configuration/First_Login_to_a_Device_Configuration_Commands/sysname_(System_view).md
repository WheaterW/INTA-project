sysname (System view)
=====================

sysname (System view)

Function
--------



The **sysname** command sets the host name of the device.

The **undo sysname** command restores the default host name of the device.



By default, the host name of the device is HUAWEI.


Format
------

**sysname** *host-name*

**undo sysname**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *host-name* | Specifies a host name. | The value is a string of 1 to 246 case-sensitive characters, with spaces supported.  When configuring a system name, do not use the following special characters: \ " , ! @ [ ] ' If these characters are used, the save-as function and NE explorer of an NMS are opened slowly after the name is synchronized to the NMS. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can change the displayed host name. After the configuration is complete, the host name is updated immediately.


Example
-------

# Set the host name of the device to DeviceA.
```
<HUAWEI> system-view
[~HUAWEI] sysname DeviceA
[*HUAWEI] commit
[~DeviceA]

```