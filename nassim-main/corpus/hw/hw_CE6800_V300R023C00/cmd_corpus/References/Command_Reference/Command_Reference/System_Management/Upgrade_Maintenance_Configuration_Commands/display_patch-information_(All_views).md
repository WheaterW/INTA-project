display patch-information (All views)
=====================================

display patch-information (All views)

Function
--------



The **display patch-information** command displays information about the current patches.




Format
------

**display patch-information** [ **verbose** | **history** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Details about a loaded patch. | - |
| **history** | Displays historical information about the patch status change. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can view patch information, including information about the running patch unit, activated patch unit, and deactivated patch unit, to facilitate fault locating and analysis.The **display patch-information verbose** command displays detailed information about the current patch, including information about the running patch units, activated patch units, deactivated patch units, boards with patch instances, type and status of patch processes, and name of patch instance.The **display patch-information history** command displays history information about the patch status change.

**Precautions**

If no patch is loaded to the system, the system displays a message indicating that no patch exists when you run the **display patch-information** command to view information about the current patch package.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display patch information (with patches).
```
<HUAWEI> display patch-information verbose
Patch Package Name    :flash:/RPG_PNFV600R021SPH001.PAT
Patch Package Version :V600R021SPH001
Patch Package State   :Running
Patch Package Run Time:2020-05-29 10:03:14
****************************************************************************
*             Information about patch errors is as follows:                *
****************************************************************************

SlotID/CpuID   CurrentVersion
----------------------------------------------------------------------------
No patch error occurs on any board
----------------------------------------------------------------------------
Total = 0
Board Info :
--------------------------------------------------------------------------------------------------------------------
SlotID/CpuID   ProcName            State   PatchType Valid     PatchEffectiveTime            PatchUnitName  PatchFileName
--------------------------------------------------------------------------------------------------------------------
1/0            swm_daemon_master   Running C         YES       2020-05-29 10:03:11.991       HPN000001.pat  RPG_PNFV600R021SPH001.PAT
--------------------------------------------------------------------------------------------------------------------
Total = 1

```

# Display information about the patch package in the system (when patch information is available).
```
<HUAWEI> display patch-information
Patch Package Name    :flash:/RPG_PNFV600R021SPH001.PAT
Patch Package Version :V600R021SPH001
Patch Package State   :Running
Patch Package Run Time:2022-04-06 10:00:17

```

# Display historical information about patch status changes.
```
<HUAWEI> display patch-information history
********************************************************************************
*                    The patch command history, as follows:                    *
********************************************************************************
time                           state      size          PatchFileName
-----------------------------------------------------------------------------------
2020-05-29 10:03:15            Running    141658        RPG_PNFV600R021SPH001.PAT
2020-05-29 05:47:51            Idle       141658        RPG_PNFV600R021SPH002.PAT

```

**Table 1** Description of the **display patch-information (All views)** command output
| Item | Description |
| --- | --- |
| Patch Package Version | Version of the patch package. |
| Patch Package State | Status of the patch package. |
| Patch Package Run Time | Running time of a patch package. |
| Patch Package Name | Patch package name. |
| State | Patch status and patch instance status:   * Idle: The patch is in the idle state. * Deactive: The patch is not activated. * Active: The patch is activated. * Running: The patch is running. * Startup: The patch is specified for next startup. * @Idle: The idle state of the patch for the next startup is cleared. |
| SlotID/CpuID | Slot ID and CPU ID for the board where a patch instance resides. |
| Board Info | Board information. |
| ProcName | ID of the process where the patch instance resides. |
| PatchType | Type of the patch instance. |
| Valid | Patch validity. |
| PatchEffectiveTime | Time when a patch package takes effect. |
| PatchUnitName | Patch unit name. |
| PatchFileName | Patch package name. |
| time | Time when a patch takes effect in the patch history. |
| state | Patch status:   * Idle: The patch is in the idle state. * Deactive: The patch is not activated. * Active: The patch is activated. * Running: The patch is running. * Startup: The patch is specified for next startup. * @Idle: The idle state of the patch for the next startup is cleared. |
| size | Size of the patch package. |