display vrrp6
=============

display vrrp6

Function
--------



The **display vrrp6** command displays information about a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ]

**display vrrp6** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| *virtual-id* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |
| **verbose** | Displays detailed information about the current VRRP6 backup group. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view detailed information about a VRRP6 backup group, run the display vrrp6 verbose command.

**Precautions**

Before you run the display vrrp6 command, ensure that a VRRP6 backup group has been configured. Otherwise, no information is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all VRRP6 backup groups.
```
<HUAWEI> display vrrp6
Type:
  N: Normal
  A: Administrator
  M: Member
  L: Load-Balance
  LM: Load-Balance-Member
Total:2     Master:1    Backup:0    Non-active:1
VRID State       Interface               Type    Virtual IP
----------------------------------------------------------------
   1 Master      Vlanif2                 N       FE80::1:2
   2 Initialize  Vlanif3                 N       FE80::218:82FF:FED3:2AF1

```

# Display detailed information about VRRP6 backup group 1.
```
<HUAWEI> display vrrp6 interface 100GE 1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:db8::2
Master IP       : FE80::3A51:BBFF:FE11:100
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 100
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 3
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-56
Check hop limit : YES
Config Type     : Normal
Create Time       : 2019-08-05 03:14:17
Last Change Time  : 2019-08-05 03:14:23

```

# Display detailed information about the IPv4 and IPv6 protocol status tracked by VRRP6 group 1.
```
<HUAWEI> display vrrp6 interface 100GE 1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:db8::2
Master IP       : FE80::3A51:BBFF:FE11:100
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 100
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 3
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-56
Check hop limit : YES
Config Type     : Normal
Track IF          : 100GE 1/0/1       Priority Increased : 10
IF State          : UP 
Track IF(IPv6)    : 100GE 1/0/1       Priority Reduced : 10
IF State          : UP 
Create Time       : 2019-08-05 03:14:17
Last Change Time  : 2019-08-05 03:14:23

```

**Table 1** Description of the **display vrrp6** command output
| Item | Description |
| --- | --- |
| VRID | ID of the VRRP6 backup group. |
| State | Status of the device in the VRRP6 backup group:   * Master: The device is the master device in the VRRP6 backup group. * Backup: The device is the backup device in the VRRP6 backup group. * Initialize: The initial status of all devices in a VRRP6 backup group is Initialize. When the status of an interface is Down or administratively Down, the status of the device in the VRRP6 backup group on the interface switches to Initialize. |
| Interface | Interface on which the VRRP6 backup group is configured. |
| Type | Type of the VRRP6 backup group:   * N (Normal): indicates the normal VRRP6 backup group. * A (Administrator): indicates the mVRRP6 backup group. * M (Member): indicates the member VRRP6 backup group. * L (Load-Balance): indicates the load-balance redundancy group (LBRG). * LM (Load-Balance-Member): indicates the LBRG member group. |
| Virtual IP | Virtual IPv6 address of the VRRP6 backup group. |
| Virtual MAC | Virtual MAC address of the VRRP6 backup group. |
| Master | Number of VRRP6 backup groups in the Master state. |
| Master IP | Primary IPv6 address of the VRRP6 backup group.   * :: is displayed in this field if the service VRRP6 state is backup. |
| PriorityRun | Running priority of the device in the VRRP6 backup group, that is, the current priority.  If the device is an IP address owner, its running priority is displayed as 255. |
| PriorityConfig | Priority configured for the device in the VRRP6 backup group.  You can run the vrrp6 vrid priority command to configure a priority for a device in a VRRP6 backup group. |
| MasterPriority | Priority of the master device in the VRRP6 backup group. |
| Preempt | Flag for the working mode of the backup device:   * YES: The backup device works in preemption mode. * NO: The backup device works in non-preemption mode. |
| Delay Time | Preemption delay of the backup device in preemption mode, in seconds.  You can run the vrrp6 vrid preempt timer delay command to configure a preemption delay for a backup device. |
| Remain | Remaining time of the preemption delay for the backup device, in seconds. |
| Hold Multiplier | Number of VRRP heartbeat timeouts. |
| TimerRun | Current interval at which the master device in the VRRP6 backup group sends Advertisement packets, in centiseconds. |
| TimerConfig | Configured interval at which the master device in the VRRP6 backup group sends Advertisement packets, in centiseconds.  You can run the vrrp6 vrid timer advertise command to configure an interval at which the master device in a VRRP6 backup group sends Advertisement packets. |
| Check hop limit | Flag for checking the hop count in a received VRRP6 packet:   * YES: The device checks the hop count in a received VRRP6 packet. * NO: The device does not check the hop count in a received VRRP6 packet. |
| Config Type | Type of the VRRP6 backup group:   * Normal: indicates the normal VRRP6 backup group. * Administrator: indicates the mVRRP6 backup group. * Member: indicates the member VRRP6 backup group. * Load-Balance: indicates the load-balance redundancy group (LBRG). * Load-Balance-Member: indicates the LBRG member group. |
| Create Time | Time when the VRRP6 backup group was created. |
| Last Change Time | Time when the status of the VRRP6 backup group last changed. |
| 100GE1/0/1 | Virtual Router 1 | Interface on which the VRRP6 backup group is configured and ID of the VRRP6 backup group. |
| Track IF | Name of the interface whose IPv4 protocol status is tracked by the VRRP6 group. |
| Track IF(IPv6) | Name of the interface whose IPv6 protocol status is tracked by the VRRP6 group. |
| IF State | IPv6 or IPv4 protocol status of the interface tracked by the VRRP6 group. |
| Priority Increased | Priority increased when the IPv4 or IPv6 protocol status of the interface associated with the VRRP6 group goes down. |
| Priority Reduced | Priority reduced when the IPv4 or IPv6 protocol status of the interface associated with the VRRP6 group goes down. |
| Total | Total number of VRRP6 backup groups. |
| Backup | Number of VRRP6 backup groups in the Backup state. |
| Non-active | Number of VRRP6 backup groups in the Non-active state. |