dhcp server database
====================

dhcp server database

Function
--------



The **dhcp server database** command enables the function to save the current DHCP data to storage devices.

The **undo dhcp server database** command disables the function to save the DHCP data to storage devices.



By default, the function of saving DHCP data to storage devices is disabled.


Format
------

**dhcp server database** { **enable** | **write-delay** *interval* }

**undo dhcp server database** { **enable** | **write-delay** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables the function of storing DHCP data. | - |
| **write-delay** *interval* | Specifies the interval at which DHCP data is saved. | The value is an integer ranging from 300 to 86400, in seconds. The default value is 3600 seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device functions as a DHCP server, run the **dhcp server database enable** command to enable the device to save DHCP data to storage devices. This avoids data loss caused by device faults. Then the system generates lease.txt and conflict.txt files in the storage device. The two files save address lease information and address conflict information respectively. After the **dhcp server database enable** command is run, current DHCP data is automatically saved at the specified interval, and previous data files are overwritten. The interval can be set using the **dhcp server database write-delay interval** command.If a fault occurs on the device, DHCP data can be restored from storage devices after the system restarts.Run the **display dhcp server database** command to check the storage device for saving DHCP data.

**Prerequisites**

The **dhcp server database enable** command has been run to enable the device to save DHCP data to storage devices and recover automatically, and ensure that the storage devices work properly.

**Precautions**

* The lease.txt and conflict.txt files are overwritten periodically; therefore, you are advised to back up and save the two files to other locations.
* The time displayed in the lease.txt and conflict.txt files is the UTC time rather than the system time, and you do not need to pay attention to time zone information.

Example
-------

# Enable the device to save the current DHCP data to storage devices and to recover automatically, and set the interval at which DHCP data is saved to 3600s.
```
<HUAWEI> system-view
[~HUAWEI] dhcp server database enable
[*HUAWEI] dhcp server database write-delay 3600

```