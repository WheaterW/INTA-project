display module-information (All views)
======================================

display module-information (All views)

Function
--------



The **display module-information** command displays information about dynamically installed modules in the system.




Format
------

**display module-information** [ [ *moduleName* ] **verbose** | **next-startup** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *moduleName* | Specifies a module name. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |
| **verbose** | Specifies details about a loaded module. | - |
| **next-startup** | Displays detailed information about the module for the next startup. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view information about dynamically installed modules in the system, run the display module-information command. The information helps to monitor whether modules are successfully installed or uninstalled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display details about all modules in the system.
```
<HUAWEI> display module-information verbose
                       Module Information
--------------------------------------------------------------------------------------------------------
Module               Version             InstallTime                   PackageName
--------------------------------------------------------------------------------------------------------
semls                xxxxxx              2020-05-29 09:57:32           xxxxxx.MOD
--------------------------------------------------------------------------------------------------------
Total = 1
****************************************************************************
*             Information about patch errors is as follows:                *
****************************************************************************

SlotID/CpuID   CurrentVersion
----------------------------------------------------------------------------
No patch error occurs on any board
----------------------------------------------------------------------------
Total = 0
Board Info :
--------------------------------------------------------------------------------------------------------------
SlotID/CpuID    ProcName            Type     FileName      EffectiveTime                      Module
--------------------------------------------------------------------------------------------------------------
1/0             swm_daemon_master   C        HM780000.mod  2020-05-29 09:57:28.050            semls
--------------------------------------------------------------------------------------------------------------
Total = 1

```

# Display information about the loaded module configured for the next startup.
```
<HUAWEI> display module-information next-startup
                    Next startup module packages
------------------------------------------------------------------------------
No.    PackageName
------------------------------------------------------------------------------
1      flash:/$_install_mod/xxxxxx.MOD
------------------------------------------------------------------------------
Total = 1

```

# Display details about a specified module in the system.
```
<HUAWEI> display module-information xxxxxx.MOD verbose
                       Module Information
--------------------------------------------------------------------------------------------------------
Module               Version             InstallTime                   PackageName
--------------------------------------------------------------------------------------------------------
semls                xxxxxx              2020-05-29 09:57:32           xxxxxx.MOD
--------------------------------------------------------------------------------------------------------
Total = 1
****************************************************************************
*             Information about patch errors is as follows:                *
****************************************************************************

SlotID/CpuID   CurrentVersion
----------------------------------------------------------------------------
No patch error occurs on any board
----------------------------------------------------------------------------
Total = 0
Board Info :
--------------------------------------------------------------------------------------------------------------
SlotID/CpuID    ProcName            Type     FileName      EffectiveTime                      Module
--------------------------------------------------------------------------------------------------------------
1/0            swm_daemon_master   C        HM780000.mod  2020-05-29 09:57:28.050            semls
1/0            swm_daemon_master   C        HM780000.mod  2020-05-29 09:57:28.023            semls
--------------------------------------------------------------------------------------------------------------
Total = 2

```

**Table 1** Description of the **display module-information (All views)** command output
| Item | Description |
| --- | --- |
| Module Information | Module information. |
| Module | Module name. |
| Version | Module version. |
| InstallTime | Loading time. |
| PackageName | File name. |
| Total | Total number of displayed records. |
| Board Info | Board information. |
| ProcName | Process name. |
| Type | File type. |
| FileName | File name. |
| EffectiveTime | Time when the patch file takes effect. |
| SlotID/CpuID | Board ID or CPU ID. |
| No. | File ID. |