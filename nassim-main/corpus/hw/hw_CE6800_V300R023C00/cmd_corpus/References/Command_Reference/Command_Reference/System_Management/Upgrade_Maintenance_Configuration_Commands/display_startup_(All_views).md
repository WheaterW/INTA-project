display startup (All views)
===========================

display startup (All views)

Function
--------



The **display startup** command displays the names of the system software, configuration file, and PAF file loaded at the current startup and to be loaded for the next startup.




Format
------

**display startup** [ **slot** *slot-num* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-num* | Specifies the slot ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Before upgrading or downgrading the system, you can run this command to check whether the system software, configuration file name and PAF file name for the next startup are correct. Only when these parameters are correct, the system can be upgraded or downgraded successfully. You can also run this command to view the names of the system software, configuration file and PAF file loaded for the current startup.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display startup information.
```
<HUAWEI> display startup
MainBoard:
  Configured startup system software:        flash:/XXXXXXXXXX.cc
  Startup system software:                   flash:/XXXXXXXXXX.cc
  Next startup system software:              flash:/XXXXXXXXXX.cc
  Startup saved-configuration file:          flash:/vrpcfg.zip
  Next startup saved-configuration file:     flash:/vrpcfg.zip
  Startup paf file:                          default
  Next startup paf file:                     default
  Startup patch package:                     NULL
  Next startup patch package:                NULL
  Startup feature software:                  NULL
  Next startup feature software:             NULL
  Startup extended-system software:          flash:/XXXXXXXXXX.cch
  Next startup extended-system software:     flash:/XXXXXXXXXX.cch

```

**Table 1** Description of the **display startup (All views)** command output
| Item | Description |
| --- | --- |
| Configured startup system software | Configured startup software package. |
| Startup saved-configuration file | Configuration file for the current startup. |
| Startup paf file | PAF file for the current startup. |
| Startup patch package | Patch package for the current startup. |
| Startup extended-system software | Displays the current startup hardware package. |
| Startup feature software | Feature package for the current startup. |
| Next startup saved-configuration file | Configuration file for the next startup. |
| Next startup paf file | PAF file for the next startup. |
| Next startup patch package | Patch package for the next startup. |
| Next startup extended-system software | Displays the hardware package for the next startup. |
| Next startup feature software | Displays the feature package for the next startup. |
| Next startup system software | Display the system software package for the next startup. |
| MainBoard | Active board. |