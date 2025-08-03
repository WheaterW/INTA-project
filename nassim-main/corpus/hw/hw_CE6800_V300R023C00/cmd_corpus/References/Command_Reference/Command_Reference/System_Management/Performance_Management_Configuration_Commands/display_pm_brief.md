display pm brief
================

display pm brief

Function
--------



The **display pm brief** command displays brief PM information.




Format
------

**display pm brief**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After PM is configured, run the display pm brief command to view brief PM information, such as the PM status, interval at which performance statistics are collected, number of performance statistics tasks, number of performance statistics instances, number of PM servers, number of performance statistics files.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief PM information globally.
```
<HUAWEI> display pm brief
Statistics Status                   : enable
Statistics Start Time               : 2012-01-06 07:32:11
Current Statistics Cycles           : 15 minutes
Number of Statistics Tasks          : 1
Number of Statistics Objects        : 0
Number of Configured Pm Servers       : 0
Number of Statistics Files          : 0
Statistics Files Saved Directory    : /pmdata/

```

**Table 1** Description of the **display pm brief** command output
| Item | Description |
| --- | --- |
| Statistics Status | Whether PM is enabled:   * enable. * disable. |
| Statistics Start Time | Date and time when the performance statistics function starts. |
| Statistics Files Saved Directory | Path where performance statistics files are saved. |
| Current Statistics Cycles | Interval at which performance statistics are collected. |
| Number of Statistics Tasks | Number of performance statistics tasks. |
| Number of Statistics Objects | Number of performance statistics objects. |
| Number of Configured Pm Servers | Number of configured PM servers. |
| Number of Statistics Files | Number of performance statistics files. |