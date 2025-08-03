display monitor-link group
==========================

display monitor-link group

Function
--------



The **display monitor-link group** command displays information about all Monitor Link groups or a specified Monitor Link group.




Format
------

**display monitor-link group** *group-id*

**display monitor-link group all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Displays information about a specified Monitor Link group. | The value is an integer ranging from 1 to 24. |
| **all** | Displays information about all Monitor Link groups. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display monitor-link group** command to view information about a Monitor Link group. The displayed information includes the name and status of each member interface.



**Prerequisites**



A Monitor Link group has been created using the **monitor-link group** command, and uplink and downlink interfaces have been added to the Monitor Link group using the port (Monitor Link group view) command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about Monitor Link group 1.
```
<HUAWEI> display monitor-link group 1
  Monitor Link group 1 information                                             
  Status: Enable
  Recover-timer: 3 second(s)
  Remain-time: 0 second(s)
  Member       Role         State Remain-time(s) Last-change-time             
  100GE1/0/1   Uplink       UP    --             0000/00/00 00:00:00 UTC+00:00                 
  100GE1/0/2   Downlink[1]  UP    --             0000/00/00 00:00:00 UTC+00:00

```

**Table 1** Description of the **display monitor-link group** command output
| Item | Description |
| --- | --- |
| Member | Member interface in a Monitor Link group. |
| Role | Role of a member interface, which can be:   * Uplink: an uplink interface. * Downlink[1]: a downlink interface. The figure within the square brackets is the ID of the downlink interface. |
| State | Physical status of a member interface, which can be:   * UP. * DOWN. |
| Remain-time(s) | Remaining delay after which the downlink interface in the Monitor Link group goes Up, in seconds. |
| Last-change-time | Time when the status of a member interface changes for the last time. The format is YYYY/MM/DD HH:MM:SS UTC+HH:MM. If the status of a member interface does not change after the member interface is added to a Monitor Link group, the time is displayed as 0000/00/00 00:00:00 UTC+00:00. |
| Recover-timer | WTR time of the Monitor Link group, in seconds.  The WTR time can be configured using the timer recover-time command. |
| Status | Status of association between uplink and downlink interfaces in a Monitor Link group:   * Enable. * Disable. |
| Remain-time | Remaining WTR time of the Monitor Link group, in seconds. |