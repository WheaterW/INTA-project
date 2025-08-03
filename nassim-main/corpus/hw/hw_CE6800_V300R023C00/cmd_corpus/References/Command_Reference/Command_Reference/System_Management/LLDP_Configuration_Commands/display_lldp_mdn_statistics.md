display lldp mdn statistics
===========================

display lldp mdn statistics

Function
--------



The **display lldp mdn statistics** command displays statistics about non-LLDP packets received by a specific or all interfaces on a device.




Format
------

**display lldp mdn statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays statistics about non-LLDP packets that a specified interface receives.  If this parameter is not specified, statistics about non-LLDP packets that all interfaces on the device receive are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



In an MDN failure scenario, before you analyze faults based on statistics about non-LLDP packets that the device receives, run the display lldp mdn statistics command.To view statistics about non-LLDP packets that a device receives during a specific period, run the **reset lldp mdn statistics** command to delete existing statistics about non-LLDP packets. Then run the display lldp mdn statistics command after the specified time elapses.



**Prerequisites**



LLDP has been enabled using the lldp enable command in the system view, and MDN has been enabled on interfaces using the lldp mdn enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about non-LLDP packets that all interfaces on a device receive.
```
<HUAWEI> display lldp mdn statistics
MDN statistics global Information:
Statistics for 10GE1/0/1:
Received Frames Total:        4056
Frames Discarded Total:       0
Frames Error Total:           0
Frames Checksum Error Total:  0
Last cleared Time:           never

```

**Table 1** Description of the **display lldp mdn statistics** command output
| Item | Description |
| --- | --- |
| MDN statistics global Information | Statistics about non-LLDP packets that a device transmits. |
| Received Frames Total | Number of received non-LLDP packets. |
| Frames Discarded Total | Number of discarded non-LLDP packets. |
| Frames Error Total | Number of received error non-LLDP packets. |
| Frames Checksum Error Total | Number of received packets with incorrect checksums of non-standard discovery protocols. |
| Last cleared Time | Date and time when the latest statistics about non-LLDP packets were deleted. |