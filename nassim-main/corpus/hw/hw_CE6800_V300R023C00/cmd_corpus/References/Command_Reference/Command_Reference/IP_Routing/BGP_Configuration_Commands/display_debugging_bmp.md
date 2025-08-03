display debugging bmp
=====================

display debugging bmp

Function
--------



The **display debugging bmp** command displays information about enabled BGP Monitoring Protocol (BMP) debugging functions.




Format
------

**display debugging bmp**


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



When a large amount of information is output, you can run the **display debugging bmp** command to view information about enabled BMP debugging functions and disable some unnecessary debugging functions to minimize the debugging information output.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about enabled BMP debugging functions.
```
<HUAWEI> display debugging bmp
[BMP] :session-msg(NULL) debugging switch is on
[BMP] :peer-notification(NULL) debugging switch is on
[BMP] :state-report(NULL) debugging switch is on
[BMP] :route-monitor(NULL) debugging switch is on

```

**Table 1** Description of the **display debugging bmp** command output
| Item | Description |
| --- | --- |
| session-msg(NULL) debugging switch is on | BMP session message debugging is enabled. |
| peer-notification(NULL) debugging switch is on | BMP Peer-Notification message debugging. |
| state-report(NULL) debugging switch is on | BMP Status-Report message debugging. |
| route-monitor(NULL) debugging switch is on | BMP Route-Monitor message debugging. |