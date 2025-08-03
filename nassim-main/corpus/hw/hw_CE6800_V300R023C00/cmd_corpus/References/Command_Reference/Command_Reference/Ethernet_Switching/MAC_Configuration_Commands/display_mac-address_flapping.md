display mac-address flapping
============================

display mac-address flapping

Function
--------



The **display mac-address flapping** command displays the MAC address flapping configuration, active MAC address flapping records and aged MAC address flapping records.




Format
------

**display mac-address flapping** [ **slot** *slot-id* ] [ **begin** *datetime* *hourtime* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays the MAC address flapping configuration of the specified board.  If this parameter is not specified, the command displays the MAC address flapping configurations of all boards. | - |
| **begin** | Indicates the start time of MAC address flapping. | - |
| *datetime* | Specifies the start date. | The format of the start date is YYYY/MM/DD. |
| *hourtime* | Specifies the start time. | The format of the start time is HH:MM:SS. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display mac-address flapping** command to display the MAC address flapping configuration, active MAC address flapping records and aged MAC address flapping records in the system.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the MAC address flapping configuration when the security level of MAC address flapping is set.
```
<HUAWEI> display mac-address flapping
MAC Address Flapping Configurations :
-------------------------------------------------------------------------------
  Flapping detection          : Enable
  Aging time(s)               : 300
  Quit-VLAN Recover time(m)   : --
  Exclude VLAN-list           : 10
  Security level              : Middle
  Exclude BD-list             : --
-------------------------------------------------------------------------------

```

# Display the MAC address flapping configuration when the security threshold for MAC address flapping detection is set.
```
<HUAWEI> display mac-address flapping
MAC Address Flapping Configurations :
-------------------------------------------------------------------------------
  Flapping detection          : Enable
  Aging  time(s)              : 300
  Quit-VLAN Recover time(m)   : --
  Exclude VLAN-list           : --
  Security threshold          : 200
  Exclude BD-list             : --
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display mac-address flapping** command output
| Item | Description |
| --- | --- |
| MAC Address Flapping Configurations | MAC address flapping configuration. |
| Flapping detection | Whether MAC address flapping detection is enabled:   * Enable: MAC address flapping detection is enabled. * Disable: MAC address flapping detection is disabled. |
| Aging time(s) | Aging time of a MAC address flapping entry. |
| Quit-VLAN Recover time(m) | Recover time of an interface after the interface was deleted from a VLAN. |
| Exclude VLAN-list | VLAN added to the whitelist. |
| Exclude BD-list | BD for which the whitelist is configured. |
| Security level | Security level.   * High. * Middle. * Low. By default, the security level is middle. |
| Security threshold | Security threshold for MAC address flapping detection. |