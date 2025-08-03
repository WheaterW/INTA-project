display vrrp admin-vrrp
=======================

display vrrp admin-vrrp

Function
--------



The **display vrrp admin-vrrp** command displays all the configured management Virtual Router Redundancy Protocol (mVRRP) backup groups and their status on the current device.




Format
------

**display vrrp admin-vrrp**


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

The display vrrp admin-vrrp command can be used to display information about all mVRRP groups. The information includes the VRRP-enabled interface, ID of the mVRRP group, and mVRRP status.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all mVRRP groups and their status on the device.
```
<HUAWEI> display vrrp admin-vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:1     Master:0    Backup:0    Non-active:1    
VRID State       Interface                                       Type    Virtual IP
--------------------------------------------------------------------------------------   
   1 Initialize  Vlanif1                                         A       192.168.1.1

```

**Table 1** Description of the **display vrrp admin-vrrp** command output
| Item | Description |
| --- | --- |
| VRID | ID of the VRRP group. |
| State | Status of the device in the mVRRP group. The values are as follows:   * Master: The device is the master device in the mVRRP group. * Backup: The device is the backup device in the mVRRP group. * Initialize: The initial status of all devices in an mVRRP group is Initialize. When the status of an interface is Down or administratively Down, the status of the device in the mVRRP group on the interface switches to Initialize. |
| Interface | Interface on which the mVRRP group is configured. |
| Type | Type of the VRRP group. The value is Admin. |
| Virtual IP | Virtual IP address of the mVRRP group. |
| Total | Total number of mVRRP groups. |
| Master | Number of mVRRP groups in the Master state. |
| Backup | Number of mVRRP groups in the Backup state. |
| Non-active | Number of mVRRP groups in the Non-active state. |