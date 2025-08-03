display stp vlan
================

display stp vlan

Function
--------



The **display stp vlan** command displays the STP status of an interface added to a specified VLAN.




Format
------

**display stp vlan** *vlan-id*

**display stp vlan** *vlan-id* **blocked-interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays the spanning tree status of an interface that joins a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **blocked-interface** | Displays information about the spanning tree protocol blocked interfaces of a specified VLAN. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an interface is added to a VLAN, run the display stp vlan command to view the STP status of the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the STP status of an interface added to a specified VLAN.
```
<HUAWEI> display stp vlan 1
 ProcessId   InstanceId   Port                        Role  State
 ----------------------------------------------------------------------
         0            0   100GE1/0/1                  DESI  discarding

```

**Table 1** Description of the **display stp vlan** command output
| Item | Description |
| --- | --- |
| ProcessId | Process ID. |
| InstanceId | Instance ID. |
| Port | Interface. |
| Role | Interface role:   * DESI: Designated port. * ROOT: Root port. * ALTE: Alternate port. * BACK: Backup port. * MAST: Master port. |
| State | Interface status:   * FORWARDING. * DISCARDING. |