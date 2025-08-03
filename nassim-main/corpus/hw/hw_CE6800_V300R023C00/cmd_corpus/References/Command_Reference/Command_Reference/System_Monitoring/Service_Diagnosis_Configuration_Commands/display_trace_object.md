display trace object
====================

display trace object

Function
--------



The **display trace object** command displays the configuration about a service diagnosis object.




Format
------

**display trace object** [ *service-object-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *service-object-id* | Specifies the ID of a diagnosis object. | The value is an integer that ranges from 0 to 3. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Display the configuration about a service diagnosis object.If you do not specify the parameters service-object-id, configurations about all diagnosis objects are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations about all diagnosis objects.
```
<HUAWEI> display trace object
Trace Object:
------------------------------------------------------------
  Object ID      : 0
  Slot           : -
  MAC Address    : -
  IP Flag        : -
  Session ID     : -
  IP Address     : 10.1.1.1
  VRF Index      : -
  CID            : -
  Calling Number : -
  SubCallingNum  : -
  User Name      : -
  Interface      : -
  QinQ VLAN ID   : -
  User VLAN ID   : -
  Access Mode    : -
  User Tunnel ID : -
  Output         : command line


------------------------------------------------------------
  Total 1, 1 printed

```

**Table 1** Description of the **display trace object** command output
| Item | Description |
| --- | --- |
| Trace Object | The diagnosis object. |
| Object ID | ID of the diagnosis object. This parameter is automatically generated from 0 in sequence of creation time. |
| Slot | Slot ID of the interface board device. |
| MAC Address | MAC address of the interface. To set the MAC address of an interface, run the trace object command. |
| IP Flag | Flag of the IP address. |
| IP Address | IP address of the interface. To set the IP address of an interface, run the trace object command. |
| Session ID | ID of the session. |
| VRF Index | User VRF index. |
| CID | User connect ID. |
| Calling Number | User calling number. To set the calling number, run the trace object command. |
| SubCallingNum | Whether fuzzy matching is supported. To set the calling number, run the trace object command. |
| User Name | User name. To set the user name, run the trace object command. |
| User VLAN ID | User VLAN ID. To set the user VLAN ID, run the trace object command. |
| User Tunnel ID | User tunnel ID. To set the user tunnel ID, run the trace object command. |
| Interface | Interface index. To set the interface index, run the trace object command. |
| QinQ VLAN ID | QinQ VLAN ID. To set the QinQ VLAN ID, run the trace object command. |
| Access Mode | User access mode, including dot1x, mac-authen. To set the user access mode, run the trace object command. |
| Output | Direction in which diagnostic information is exported. This parameter is defined using the trace object command.  command line: Diagnostic information is exported to a command line configuration terminal. The prerequisite for displaying diagnostic information on the CLI terminal is that the trace enable command is configured. The trace enable command is equivalent to the debugging function of the diagnostic information exported in the current terminal window. After the trace enable command is run in multiple terminal windows, if the undo trace enable command is run in one of the terminal windows, the diagnostic information exported in all the terminal windows is affected. After the trace enable command is run again, diagnostic information exported in the current window and other windows where the trace enable command has been run is restored, and diagnostic information cannot be exported in the windows where the undo trace enable command has been run.  file: Diagnostic information is exported to a file.  server: Diagnostic information is exported to a log server. |
| Total 1, 1 printed | Total number of created diagnosis objects and count of displayed objects. |