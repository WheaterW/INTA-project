display trace information
=========================

display trace information

Function
--------



The **display trace information** command displays information about service diagnosis.




Format
------

**display trace information**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After configuring service diagnosis, you can run this command to view global information about service diagnosis, for example, the counts of diagnosis instances and objects created on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about service diagnosis.
```
<HUAWEI> display trace information
Trace Information:
------------------------------------------------------------
Trace Enable                            : Enable
Debug info level                        : Brief
Debug fill-instance                     : Off
Debug quit-instance                     : Off
Debug output information                : Off
Syslog Source IP Address                : -

The sum of all the instances            : 0
The startID of the instance table       : -
Alloc instance times                    : 9
Free instance times                     : 9
The sum of all the objects              : 2
------------------------------------------------------------

```

**Table 1** Description of the **display trace information** command output
| Item | Description |
| --- | --- |
| Trace Information | Information about service diagnosis. |
| Trace Enable | Status of service diagnosis.   * Disable: Service diagnosis is disabled. * Enable: Service diagnosis is enabled.   This field can be modified using the trace enable command. |
| Debug info level | Output level of service diagnosis information.   * Brief: brief service diagnosis information. * Detail: detailed service diagnosis information.   This field can be modified using the trace enable command. |
| Debug fill-instance | Debugging status of the fill-instance module.   * Off: disabled. * On: enabled. |
| Debug quit-instance | Debugging status of the quit-instance module.   * Off: disabled. * On: enabled. |
| Debug output information | Debugging status of the output information module.   * Off: disabled. * On: enabled. |
| Syslog Source IP Address | Source IP address of the interface for exporting diagnosis information to the log server. To set the IP address of the interface for exporting diagnosis information to a log server, run the trace syslog source command. |
| The sum of all the instances | Total number of diagnosis instances. |
| The startID of the instance table | Start ID of the instance table. |
| The sum of all the objects | Total number of diagnosis objects. |
| Alloc instance times | Number of allocated service diagnosis instances. The creation of a diagnosis instance is irrelevant to the diagnosis object. After the service diagnosis function is enabled, the service triggers the creation of a diagnosis instance, and the number of allocated instances increases. |
| Free instance times | Number of the release diagnosis instances. |