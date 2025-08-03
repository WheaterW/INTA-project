display vrrp6 admin-vrrp
========================

display vrrp6 admin-vrrp

Function
--------



The **display vrrp6 admin-vrrp** command displays information about all management Virtual Router Redundancy Protocol for IPv6 (mVRRP6) backup groups.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6 admin-vrrp**


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

To view information about all mVRRP6 backup groups, run this command. The information includes the interface on which an mVRRP6 backup group is configured, ID of an mVRRP6 backup group, and status of the device in an mVRRP6 backup group.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all mVRRP6 backup groups.
```
<HUAWEI> display vrrp6 admin-vrrp
Type:
  N: Normal
  A: Administrator
  M: Member
  L: Load-Balance
  LM: Load-Balance-Member
Total:1     Master:1    Backup:0    Non-active:0
VRID State       Interface               Type    Virtual IP
----------------------------------------------------------------
  2  Master      Vlanif34                A       FE80::218:82FF:FED3:2AF1

```

**Table 1** Description of the **display vrrp6 admin-vrrp** command output
| Item | Description |
| --- | --- |
| VRID | ID of the mVRRP6 backup group. |
| State | Status of the device in the mVRRP6 backup group:   * Master: The device is the master device in the mVRRP6 backup group. * Backup: The device is the backup device in the mVRRP6 backup group. * Initialize: The initial status of all devices in an mVRRP6 backup group is Initialize. When the status of an interface is Down or administratively Down, the status of the device in the mVRRP6 backup group on the interface switches to Initialize. |
| Interface | Interface on which the mVRRP6 backup group is configured. |
| Type | Type of the VRRP6 backup group. The value is Admin. |
| Virtual IP | Virtual IPv6 address of the mVRRP6 backup group. |
| Master | Number of mVRRP6 backup groups in the Master state. |
| Total | Total number of mVRRP6 backup groups. |
| Backup | Number of mVRRP6 backup groups in the Backup state. |
| Non-active | Number of mVRRP6 backup groups in the Non-active state. |