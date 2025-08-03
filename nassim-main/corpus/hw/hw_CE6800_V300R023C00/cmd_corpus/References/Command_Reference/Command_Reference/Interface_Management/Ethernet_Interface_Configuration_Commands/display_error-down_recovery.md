display error-down recovery
===========================

display error-down recovery

Function
--------



The **display error-down recovery** command displays information about the interface in the error-down state, including the interface name, cause of the error-down event, delay for the transition from Down to Up, and remaining time for the Up event.




Format
------

**display error-down recovery** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | Interface number: The value is a string of 1 to 63 characters without spaces. |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



The auto recovery function is configured and the delay for the transition from Down to Up is set on an interface using the **error-down auto-recovery** command. If the interface is now in the error-down state, run the **display error-down recovery** command to view the remaining time for an Up event.An interface enters the error-down state after being shut down due to an error.



**Prerequisites**



The auto recovery function has been configured on an interface using the **error-down auto-recovery** command.



**Configuration Impact**



If interface is not configured in this command, the system displays information about all interfaces in the error-down state.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the delay for the transition from Down to Up and the remaining time for the Up event.
```
<HUAWEI> display error-down recovery
interface                    error-down cause         recovery   remainder 
                                                      time(sec)  time(sec)
----------------------------------------------------------------------------
100GE1/0/1                   bpdu-protection          30         10

```

**Table 1** Description of the **display error-down recovery** command output
| Item | Description |
| --- | --- |
| error-down cause | Cause of the error-down event. |
| recovery time | Delay (in seconds) for a transition from Down to Up.  If the auto recovery function is not configured, it needs to recovery from Down to Up using undo shutdown command. In this case, hyphens (--) are displayed in this field. |
| interface | Interface name. |
| remainder time | Remaining time for an Up event.  If the auto recovery function is not configured, it needs to recovery from Down to Up using undo shutdown command. In this case, hyphens (--) are displayed in this field. |