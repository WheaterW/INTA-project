display multicast statistics
============================

display multicast statistics

Function
--------



The **display multicast statistics** command displays global PIM entry statistics.




Format
------

**display multicast global** { **pim** **sm** | **pim** **dm** | **all** } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pim** | Indicates the PIM entry. | - |
| **sm** | Indicates the PIM-SM mode. | - |
| **dm** | Indicates the PIM-DM mode. | - |
| **all** | Indicates all modes. | - |
| **global** | Displays the global configuration. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check PIM entry restriction and statistics in PIM-SM mode, run the display multicast global pim sm statistics command.To check PIM entry restriction and statistics in PIM-DM mode, run the display multicast global pim dm statistics command.To check PIM entry restriction and statistics in all modes, run the display multicast global all statistics command.

**Prerequisites**

Before running the **display multicast statistics** command to view the limit and statistics on PIM entries, run the **multicast global limit** command in the system view or the **multicast limit** command in the VPN view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display PIM entry restriction and statistics in the PIM-SM mode.
```
<HUAWEI> display multicast global pim sm statistics
------------------------------------------------------------------
PIM-SM        Number        Limit         Threshold(Upper%/Lower%)
------------------------------------------------------------------
(*, G)        0             2000          80/70                   
(S, G)        0             1000          80/70                   
------------------------------------------------------------------

```

**Table 1** Description of the **display multicast statistics** command output
| Item | Description |
| --- | --- |
| PIM-SM | Type of PIM-SM entry for which a limit takes effect. The value can be (\*, G) or (S, G). |
| Number | Number of created PIM entries. |
| Limit | Limit on the number of PIM entries. If no limit is set, -- is displayed. |
| Threshold(Upper%/Lower%) | Alarm trigger and clear thresholds. If they are not set, -- is displayed. |