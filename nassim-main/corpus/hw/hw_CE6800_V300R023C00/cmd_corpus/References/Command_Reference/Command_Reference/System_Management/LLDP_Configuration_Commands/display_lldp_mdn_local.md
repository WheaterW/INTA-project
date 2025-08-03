display lldp mdn local
======================

display lldp mdn local

Function
--------



The **display lldp mdn local** command displays configurations and status information about MAC address discovery neighbor (MDN) on a specific or all interfaces.




Format
------

**display lldp mdn local** [ **interface** { *interface-name* | *interface-type* *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-name* | Displays MDN information about a specified interface.  If this parameter is not specified, MDN information about all interfaces is displayed.  Displays configuration and status information about MDN on a specified interface.  If this parameter is not specified, configurations and status information about MDN on all interfaces are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view configurations and status information about MDN on a specific or all interfaces, run the display lldp mdn local command.



**Prerequisites**



LLDP has been enabled using the lldp enable command in the system view, and MDN has been enabled on interfaces using the lldp mdn enable command in the interface view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations and status information about MDN on all interfaces.
```
<HUAWEI> display lldp mdn local
System configuration
--------------------------------------------------------------------------
MDN Notification Interval          :5                (default is 5s)
MDN Notification Enable            :disabled         (default is disabled)

Remote Table Statistics:
--------------------------------------------------------------------------
Remote Table Last Change Time      :0 days, 0 hours, 1 minutes, 56 seconds
Remote Neighbors Added             :4
Remote Neighbors Deleted           :0
Remote Neighbors Dropped           :0
Remote Neighbors Aged              :0
Total Neighbors                    :4

Port information:
--------------------------------------------------------------------------
Interface 10GE1/0/1:
MDN Status                         :rxOnly           (default is disabled)
Total Neighbors                    :4

Interface 10GE1/0/1:
MDN Status                         :rxOnly           (default is disabled)
Total Neighbors                    :0

```

**Table 1** Description of the **display lldp mdn local** command output
| Item | Description |
| --- | --- |
| MDN Notification Interval | Delay time for sending alarms about MDN neighbor information changes.  The delay value can be changed using the lldp mdn trap-interval command. |
| MDN Notification Enable | Whether the alarm function about MDN neighbor information changes is enabled:   * enabled. * disabled. |
| MDN Status | Whether MDN is enabled on the local interface:   * rxOnly: Only MDN packets can be received. * disabled: MDN is disabled. |
| Remote Table Last Change Time | Duration between last change in MDN neighbor statistics and when the display lldp mdn local command is run. |
| Remote Neighbors Added | Number of increased MDN neighbors. |
| Remote Neighbors Deleted | Number of deleted MDN neighbors. |
| Remote Neighbors Dropped | Number of MDN neighbors that are deleted due to insufficient storage space. |
| Remote Neighbors Aged | Number of MDN neighbors that are deleted due to information aging. |
| Remote Table Statistics | MDN neighbor statistics. |
| Total Neighbors | Total number of MDN neighbors. |
| Port information | Interface information. |