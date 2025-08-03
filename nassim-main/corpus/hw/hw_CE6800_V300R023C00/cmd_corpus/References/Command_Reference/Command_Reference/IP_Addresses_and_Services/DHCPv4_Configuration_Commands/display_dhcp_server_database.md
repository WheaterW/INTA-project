display dhcp server database
============================

display dhcp server database

Function
--------



The **display dhcp server database** command displays information about the DHCP database.




Format
------

**display dhcp server database**


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

The **display dhcp server database** command displays the storage path and file name of DHCP data on a DHCP server. This information helps to check:

* Whether the function that saves DHCP data to the storage device is enabled. If this function is not enabled, run the **dhcp server database** command to enable it.
* Whether the interval at which DHCP data is saved is proper.
* Whether the function that recovers DHCP data from the storage device after the system restarts is enabled.

**Precautions**

The function that saves DHCP data to storage devices and the function that recovers DHCP data from storage devices can be enabled in any sequence.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DHCP database storage information.
```
<HUAWEI> display dhcp server database
 Status: disable
 Recover from files after reboot: disable
 File saving lease items: flash:/dhcp/lease.txt
 File saving conflict items: flash:/dhcp/conflict.txt
 Save Interval: 300 (seconds)

```

**Table 1** Description of the **display dhcp server database** command output
| Item | Description |
| --- | --- |
| Recover from files after reboot | Whether to recover data from the file on the storage device after the system restarts:   * disable. * enable.   The value is set using the dhcp server database command. |
| File saving lease items | File name and path in which address lease information is saved. |
| File saving conflict items | File name and path in which address conflict information is saved. |
| Save Interval | Interval at which DHCP data is saved, in seconds.  The value is set using the dhcp server database command. |
| Status | Whether to save the data to the storage device:   * disable. * enable.   The value is set using the dhcp server database command. |