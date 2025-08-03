display vrrp
============

display vrrp

Function
--------



The **display vrrp** command displays the status and parameters of a VRRP group.




Format
------

**display vrrp** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ]

**display vrrp** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-id* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| *virtual-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **verbose** | Displays detailed information about the current VRRP group. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The display vrrp command displays information about VRRP groups.

* If you do not specify the interface-type, interface-number nor virtual-id parameter, detailed information about all VRRP groups on the device is displayed.
* If you specify only the interface-type and interface-number parameters, detailed information about all VRRP groups on the specified interface is displayed.
* If you specify the interface-type, interface-number and virtual-id parameters, detailed information about the specified VRRP group on the specified interface is displayed.

**Precautions**

At least one VRRP group must be configured before you run the display vrrp command; otherwise, no information is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information about backup groups on 100GE1/0/1.
```
<HUAWEI> display vrrp interface 100GE 1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State          : Master
Virtual IP     : 10.1.1.2
Master IP      : 10.1.1.1
PriorityRun    : 100
PriorityConfig : 100
MasterPriority : 100
Preempt        : YES   Delay Time : 0s   Remain : --
Hold Multiplier: 4
TimerRun       : 1s
TimerConfig    : 1s
Auth Type      : MD5
Virtual MAC    : xxxx-xxxx-xxxx
Check TTL      : YES
Config Type    : Normal
Create Time       : 2019-08-05 02:21:25
Last Change Time  : 2019-08-05 02:21:31

```

# Display brief information about all the VRRP groups.
```
<HUAWEI> display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:1     Master:0    Backup:0    Non-active:1    
VRID State       Interface                                       Type    Virtual IP
--------------------------------------------------------------------------------------
   1 Initialize  Vlanif1                                         N       192.168.1.1

```

**Table 1** Description of the **display vrrp** command output
| Item | Description |
| --- | --- |
| Virtual IP | Virtual IP address of the VRRP group. |
| Virtual MAC | Virtual MAC address of the VRRP group. |
| State | Status of the device in the VRRP group. When VRRP works normally, the values are as follows:   * Master: The device functions as the master device in the VRRP group. * Backup: The device functions as the backup device in the VRRP group. * Initialize: All devices in the VRRP group start with the Initialize state. When an interface goes down or AdminDown, the status of the VRRP group changes to Initialize. |
| Master IP | IP address of the primary interface on the master device.   * 0.0.0.0 is displayed in this field if the service VRRP state is backup. |
| Master | Number of VRRP groups in the Master state. |
| PriorityRun | Running priority of the device in the VRRP group, that is, the current priority. If the device is an IP address owner in a VRRP group, the device running priority is displayed as 255 in the VRRP group. |
| PriorityConfig | Priority configured using the vrrp vrid priority command for the device. For an IP address owner, the default priority 100 but not 255 is displayed. |
| MasterPriority | Priority of the master device in the VRRP group. If the Router is an IP address owner in a VRRP group, the device master priority is displayed as 255 in the VRRP group. |
| Preempt | Preemption flag. YES indicates that the preemption mode is used. |
| Delay Time | Preemption delay, in seconds. |
| Remain | Remaining time before preemption, in seconds. |
| Hold Multiplier | Number of VRRP heartbeat timeouts. |
| TimerRun | Timer value of the VRRP group, in seconds. |
| TimerConfig | Interval at which VRRP packets are sent, in seconds. |
| Auth Type | VRRP packet authentication mode, which can be:   * NONE: No authentication is configured. * SIMPLE TEXT: Simple authentication is configured. * MD5: MD5 authentication is configured. |
| Check TTL | Whether to check the TTL of a VRRP packet. It can be YES or NO. |
| Config Type | Type of the VRRP group, which can be:   * Normal: common VRRP group. * Administrator: admin VRRP group. * Member: member VRRP group. * Load-Balance: VRRP LB admin group. * Load-Balance-Member: VRRP LB member group. |
| Create Time | Time when the VRRP group was created. |
| Last Change Time | Time when the state of the VRRP group last changed. |
| VRID | ID of the VRRP group. |
| Interface | Name of the interface on which a VRRP group is configured. |
| GE1/0/1 | Virtual Router 1 | Interface on which the VRRP group is configured and ID of the VRRP group. |
| Total | Total number of VRRP groups. |
| Backup | Number of the VRRP groups in the backup state. |
| Non-active | Number of VRRP groups in the non-active state. |
| Backup-forward | Function of service traffic forwarding by the backup device in a VRRP group:   * disabled. * enabled. |