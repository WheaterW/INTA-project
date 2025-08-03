display control-flap
====================

display control-flap

Function
--------



The **display control-flap** command displays the running status and statistics of control-flap on an interface. You can adjust parameters about control-flap based on the statistics.

If no interface is specified, the running status and statistics of control-flap on all interfaces are displayed.




Format
------

**display control-flap** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Interface type. | The value is of the enumerated type. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



Before you monitor interface status or locate an interface fault, run the **display control-flap** command to view the running status and statistics of control-flap on the interface. The command output helps you adjust control-flap parameters, collect traffic statistics, and troubleshoot the interface.



**Configuration Impact**



If interface-type interface-number is not specified, the running status and statistics of control-flap on all interfaces are displayed.



**Follow-up Procedure**



If you find that the parameters about control-flap are not proper based on the output of the **display control-flap** command, adjust the parameters by using the **control-flap** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the control-flap running status and statistics on an interface.
```
<HUAWEI> display control-flap
Interface 100GE1/0/1
Control flap status: unsuppressed
Flap count: 0 
Current penalty: 0.000 
Control flap parameter:  suppress   reuse    decay-ok   decay-ng   ceiling
                         2.000      0.750    15         15         16.000

```

**Table 1** Description of the **display control-flap** command output
| Item | Description |
| --- | --- |
| Control flap status | Whether the interface is suppressed:   * suppressed: The interface is suppressed. * unsuppressed: The interface is not suppressed. |
| Control flap parameter | Parameters about control-flap on an interface. |
| Flap count | Total number of times that the interface is suppressed. |
| Current penalty | Current suppression penalty value of the interface. |
| suppress | Suppression threshold on an interface. |
| reuse | Interface reuse threshold. |
| decay-ok | Time to decrease the penalty to half when the interface is Up. |
| decay-ng | Time to decrease the penalty to half when the interface is Down. |
| ceiling | Maximum suppression penalty value. |