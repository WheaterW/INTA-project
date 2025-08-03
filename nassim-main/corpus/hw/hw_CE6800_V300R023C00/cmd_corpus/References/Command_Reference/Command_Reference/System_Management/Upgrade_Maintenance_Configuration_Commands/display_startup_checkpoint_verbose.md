display startup checkpoint verbose
==================================

display startup checkpoint verbose

Function
--------



The **display startup checkpoint verbose** command displays detailed information about a specified checkpoint.




Format
------

**display startup checkpoint** [ *checkpoint\_name* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *checkpoint\_name* | Checkpoint name. | The value is a string of 5 to 32 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Before you roll back the system to a specified checkpoint, run this command to view detailed information about the checkpoint.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the specified rollback point chkpnt\_auto. The hardware package is displayed only when the model supports the hardware package and the hardware package exists on the device.
```
<HUAWEI> display startup checkpoint @chkpnt_auto_0705210735 verbose
-----------------------------------------------------------------------------------
  Startup checkpoint name:                   @chkpnt_auto_0705210735
  Startup system software:                   flash:/XXXXXXXXX.cc
  Startup saved-configuration file:          config_@chkpnt_auto_0705210735.dat
  Startup paf file:                          NULL
  Startup patch package:                     NULL
  Startup module package:                    NULL
  Startup feature software:                  NULL
  Startup extended-system software:          flash:/xxxxxxxx.cch

```

**Table 1** Description of the **display startup checkpoint verbose** command output
| Item | Description |
| --- | --- |
| Startup checkpoint name | Checkpoint name. |
| Startup system software | Checkpoint system software. |
| Startup patch package | Checkpoint patch package. |
| Startup module package | Checkpoint module package. |
| Startup feature software | Checkpoint feature software. |
| Startup paf file | Checkpoint paf file. |
| Startup saved-configuration file | Checkpoint saved-configuration file. |
| Startup extended-system software | Information about the system extended package at the rollback point. This parameter is displayed only when there is a system extended package. |