display smart-link group
========================

display smart-link group

Function
--------



The **display smart-link group** command displays information about all Smart Link groups or a specified Smart Link group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display smart-link group** { *group-id* | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-id* | Displays information about a specified Smart Link group. | The value is an integer ranging from 1 to 48. |
| **all** | Displays information about all Smart Link groups. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view Smart Link group information, including information about member interfaces and links, run the **display smart-link group** command. The command output helps locate faults in a Smart Link group.

**Prerequisites**

A Smart Link group has been created using the **smart-link group** command, and the master and slave interfaces have been configured using the port command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about Smart Link group 1.
```
<HUAWEI> display smart-link group 1
Smart Link group 1 information :                                                
  Smart Link group: enabled
  Link status: Lock
  Wtr-time is: 60 sec                                                  
  Load-Balance Instance: 10
  Protected-VLAN reference-instance: 1                                 
  DeviceID: 00e0-fc12-3456  Control-VLAN ID: 505                                
  Member                          Role    InstanceID  State      FlushCount   LastFlushTime
  ------------------------------------------------------------------------------------
  100GE1/0/1            Master           0  active              0   0000/00/00 00:00:00 UTC+00:00 
  100GE1/0/2            Slave            0  Inactive            0   0000/00/00 00:00:00 UTC+00:00

```

**Table 1** Description of the **display smart-link group** command output
| Item | Description |
| --- | --- |
| Smart Link group | Whether the Smart Link group is enabled:   * enabled. * disabled. |
| Link status | Interface on which traffic is locked:   * lock: Traffic is locked on the master interface. * force: Traffic is locked on the slave interface.   The interface on which traffic is locked can be configured using the smart-link command. |
| Wtr-time | Switchback time.  The switchback time can be set using the timer wtr command. |
| Load-Balance Instance | Load-balancing instance ID.  The load-balancing instance ID can be set using the load-balance instance command. |
| Protected-VLAN reference-instance | ID of a protection instance.  The protection instance ID can be set using the protected-vlan reference-instance command. |
| Control-VLAN ID | Control VLAN ID of a Smart Link group.  The control VLAN ID can be set using the flush send command. |
| Member | Member interface in the Smart Link group. |
| Role | Role of the member interface in the Smart Link group:   * Master. * Slave. |
| InstanceID | Instance ID. |
| State | State of the member interface:   * Active. The interface forwards traffic. * Inactive. The interface does not forward traffic.   Unknown. The Smart Link group may be disabled, or the interface is not detected. |
| FlushCount | Number of sent Flush packets. |
| LastFlushTime | Time that the latest Flush packet was sent. The time is displayed in the format of YYYY/MM/DD HH:MM:SS UTC+HH:MM. If no Flush packets are ever sent, the time is displayed as 0000/00/00 00:00:00 UTC+00:00. |
| DeviceID | MAC address of the device. |