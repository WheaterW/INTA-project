display eth-trunk
=================

display eth-trunk

Function
--------



The **display eth-trunk** command displays configurations of an Eth-Trunk interface.




Format
------

**display eth-trunk** [ *trunk-id* [ **interface** { *interface-type* *interface-number* | *interface-name* } | **verbose** ] ]

**display eth-trunk brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer in the range from 0 to 1023. |
| *interface-type* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies an interface name. | - |
| **verbose** | Displays detailed Eth-Trunk information. | - |
| **brief** | Displays brief Eth-Trunk information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



After configuring an Eth-Trunk interface on a device, you can run the display eth-trunk command to check whether the configurations of the Eth-Trunk interface are correct.



**Prerequisites**



The interface specified in this command must be an existing one. This ensures that valid entries are displayed after you execute the command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about a specified Eth-Trunk interface.
```
<HUAWEI> display eth-trunk brief
Status: Operate status
Role: E-Trunk status
Act: Active link number
Inact: Inactive link number
Cfgd: Configured link number
BW: Bandwidth
Interface              Mode      Status    Role      Act/Inact/Cfgd   BW(Mbps)    
Eth-Trunk1             NORMAL    Up        M         0/1/2            200           
Eth-Trunk2             NORMAL    Up        S         0/1/3            100

```

# Display the configurations of Eth-Trunk 10 in static LACP mode.
```
<HUAWEI> display eth-trunk 10
Eth-Trunk10's state information is:
(h): high priority
(r): reference port
Local:
LAG ID: 10                  WorkingMode: STATIC
Preempt Delay Time: 10      Hash arithmetic: According to flow
System Priority: 120        System ID: 00e0-fc12-3456
Least Active-linknumber: 1  Max Active-linknumber: 8
Operate status: up          Ports: 2
Timeout Period: Slow
PortKeyMode: Auto
------------------------------------------------------------------------------------
ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/2(hr)             Selected 1GE      10      262    2609    10111100  1
100GE1/0/3(h)              Selected 1GE      10      263    2609    10111100  1
100GE1/0/4(h)              Unselect 1GE      32768   264    2609    10100000  1

Partner:
------------------------------------------------------------------------------------
ActorPortName              SysPri    SystemID  PortPri PortNo  PortKey   PortState
100GE1/0/2                 32768  00e0-fc12-3460  32768  262   2609      10111100
100GE1/0/3                 32768  00e0-fc12-3460  32768  263   2609      10111100
100GE1/0/4                 32768  00e0-fc12-3460  32768  264   2609      10110000

```

# Display the detailed configurations of Eth-Trunk 10 in static LACP mode.
```
<HUAWEI> display eth-trunk 10 verbose
Eth-Trunk10's state information is:
(h): high priority
(r): reference port
Local:
LAG ID: 10                  WorkingMode: STATIC
Preempt Delay Time: 10      Hash arithmetic: According to flow
System Priority: 120        System ID: 00e0-fc12-3456
Least Active-linknumber: 1  Max Active-linknumber: 8
Operate status: up          Number Of Up Ports In Trunk: 2
Timeout Period: Slow
PortKeyMode: Auto
------------------------------------------------------------------------------------
ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/2(hr)             Selected 1GE      10      262    2609    10111100  1
100GE1/0/3(h)              Selected 1GE      10      263    2609    10111100  1
100GE1/0/4(h)              Unselect 1GE      32768   264    2609    10100000  1

Partner:
------------------------------------------------------------------------------------
ActorPortName              SysPri    SystemID  PortPri PortNo  PortKey   PortState
100GE1/0/2                 32768  00e0-fc12-3460  32768  262   2609      10111100
100GE1/0/3                 32768  00e0-fc12-3460  32768  263   2609      10111100
100GE1/0/4                 32768  00e0-fc12-3460  32768  264   2609      10110000

Flow statistic
 Interface 100GE1/0/2,
    Last 300 seconds input rate 32 bits/sec, 0 packets/sec
    Last 300 seconds output rate 32 bits/sec, 0 packets/sec
    148 packets input, 18944 bytes, 0 drops
    246 packets output, 31488 bytes, 0 drops
 Interface 100GE1/0/3,
    Last 300 seconds input rate 32 bits/sec, 0 packets/sec
    Last 300 seconds output rate 32 bits/sec, 0 packets/sec
    147 packets input, 18816 bytes, 0 drops
    246 packets output, 31488 bytes, 0 drops
 Interface 100GE1/0/4,
    Last 300 seconds input rate 56 bits/sec, 0 packets/sec
    Last 300 seconds output rate 48 bits/sec, 0 packets/sec
    144 packets input, 18432 bytes, 0 drops
    174 packets output, 22272 bytes, 0 drops
 Interface Eth-Trunk10
    Last 300 seconds input rate 96 bits/sec, 0 packets/sec
    Last 300 seconds output rate 96 bits/sec, 0 packets/sec
    439 packets input, 56192 bytes, 0 drops
    666 packets output, 85248 bytes, 0 drops

```

# Display the configurations of all Eth-Trunk interfaces.
```
<HUAWEI> display eth-trunk
Eth-Trunk10's state information is:
(h): high priority
(r): reference port
Local:
LAG ID: 10                  WorkingMode: STATIC
Preempt Delay Time: 10      Hash arithmetic: According to flow
System Priority: 120        System ID: 00e0-fc12-3456
Least Active-linknumber: 1  Max Active-linknumber: 8
Operate status: up          Number Of Up Ports In Trunk: 2
Timeout Period: Slow
PortKeyMode: Auto
------------------------------------------------------------------------------------
ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/2(hr)             Selected 1GE      10      262    2609    10111100  1
100GE1/0/3(h)              Selected 1GE      10      263    2609    10111100  1
100GE1/0/4(h)              Unselect 1GE      32768   264    2609    10100000  1

Partner:
------------------------------------------------------------------------------------
ActorPortName              SysPri    SystemID  PortPri PortNo  PortKey   PortState
100GE1/0/2                 32768  00e0-fc12-3460  32768  262   2609      10111100
100GE1/0/3                 32768  00e0-fc12-3460  32768  263   2609      10111100
100GE1/0/4                 32768  00e0-fc12-3460  32768  264   2609      10110000

Eth-Trunk20's state information is:
WorkingMode: NORMAL         Hash arithmetic: According to flow
Least Active-linknumber: 1  Max Bandwidth-affected-linknumber: 16
Operate status: up          Number Of Up Ports In Trunk: 1
--------------------------------------------------------------------------------
PortName                      Status      Weight
100GE1/0/1                    Up          1
100GE1/0/2                    Offline     1

```

# Display the configurations of Eth-Trunk 20 in manual load balancing mode.
```
<HUAWEI> display eth-trunk 20
Eth-Trunk20's state information is:
WorkingMode: NORMAL         Hash arithmetic: According to flow
Least Active-linknumber: 1  Max Bandwidth-affected-linknumber: 16
Operate status: up          Number Of Up Ports In Trunk: 1
--------------------------------------------------------------------------------
PortName                      Status      Weight
100GE1/0/1                    Up          1
100GE1/0/2                    Offline     1

```

# Display the detailed configurations of Eth-Trunk 20 in manual load balancing mode.
```
<HUAWEI> display eth-trunk 20 verbose
Eth-Trunk20's state information is:
WorkingMode: NORMAL         Hash arithmetic: According to flow
Least Active-linknumber: 1  Max Bandwidth-affected-linknumber: 16
Operate status: up          Number Of Up Ports In Trunk: 1
--------------------------------------------------------------------------------
PortName                      Status      Weight
100GE1/0/1                    Up          1
100GE1/0/2                    Offline     1

Flow statistic
 Interface 100GE1/0/1,
    Last 300 seconds input rate 0 bits/sec, 0 packets/sec
    Last 300 seconds output rate 0 bits/sec, 0 packets/sec
    0 packets input, 0 bytes, 0 drops
    0 packets output, 0 bytes, 0 drops
 Interface Eth-Trunk20
    Last 300 seconds input rate 0 bits/sec, 0 packets/sec
    Last 300 seconds output rate 0 bits/sec, 0 packets/sec
    0 packets input, 0 bytes, 0 drops
    0 packets output, 0 bytes, 0 drops

```

**Table 1** Description of the **display eth-trunk** command output
| Item | Description |
| --- | --- |
| Operate status | Eth-Trunk status:   * UP: The interface is up and can forward traffic. * DOWN: The interface is down and cannot forward traffic. |
| Interface | Interface name and number. |
| Status | Status of the local member interface in LACP mode:   * Indep: A member interface in this state can forward data but cannot receive LACPDUs from a remote device. * Selected: The member interface is selected as an active interface. * Unselect: The member interface is not selected. * Unknown: The member interface is offline.   Status of a local member interface in manual load balancing mode:   * Up: The interface is started normally. * Down: The interface is physically faulty. * Offline: The interface is offline. |
| Role | Role of an Eth-Trunk member interface in static LACP mode:   * MASTER. * SLAVE. * NONE.   You can run the lacp port-role command to configure or change the role of an Eth-Trunk member interface in static LACP mode. |
| (h): high priority | ID of the high-priority end. The Actor of LACP member interfaces is elected by comparing the system priorities and system IDs of the local and peer ends. |
| (r): reference port | LACP reference interface.  After static LACP is enabled on a trunk interface, the interface with the highest priority is selected as the reference interface by comparing the interface priority and interface number of the Actor.  If a trunk has multiple member interfaces, only the interface with the same system priority, system ID, and key as the LACP reference interface is selected. |
| LAG ID | ID of the Eth-Trunk. |
| Preempt Delay | Preemption delay of an Eth-Trunk interface in static LACP mode.  You can configure and change the preemption delay of an Eth-Trunk interface in static LACP mode using the lacp preempt delay command. |
| Preempt Delay Time | Preemption delay. |
| Hash arithmetic | Hash algorithm type of the Eth-Trunk interface. |
| System Priority | System LACP priority. |
| System ID | System ID. |
| Least Active-linknumber | Minimum number of active member links.  If the number of Eth-Trunk member interfaces that are in the Up state is less than the Least Active-linknumber value, the Eth-Trunk interface goes Down.  You can change the Least Active-linknumber value by running the least active-linknumber (Eth-Trunk interface view) command. |
| Max Active-linknumber | Maximum number of active member links.  You can configure and change the maximum number of active member links using the max active-linknumber command. |
| Max Bandwidth-affected-linknumber | Maximum number of member interfaces that affect the actual bandwidth of the Layer 2 Eth-Trunk interface. |
| Timeout Period | Timeout period during which an Eth-Trunk interface in static LACP mode fails to receive LACPDUs.  You can configure or modify the timeout period using the lacp timeout command. |
| ActorPortName | Name of a member interface. |
| PortType | Type of the local member interface. |
| PortPri | LACP priority of the member interface in an Eth-Trunk interface in static LACP mode.  You can configure and change the LACP priority of the member interface using the lacp priority command. |
| PortNo | LACP number of the member interface in an Eth-Trunk interface in static LACP mode. |
| PortKey | LACP key of the member interface in an Eth-Trunk interface in static LACP mode. |
| PortState | Status variable of the member interface in an Eth-Trunk interface in static LACP mode.  The status variable is an 8-bit binary number, such as 10111100. The descriptions of each bit from left to right are as follows:   * First bit: whether the member interface is an Actor. This bit has a fixed value 1. * Second bit: whether the member interface uses a long or short timeout period to receive LACPDUs. 1: The member interface uses a short timeout period. 0: The member interface uses a long timeout period.   By default, an Eth-Trunk member interface uses the long timeout (90 seconds) period to receive LACPDUs. The value can be changed using the lacp timeout command.   * Third bit: whether the system allows the member interface to be aggregated. 1: The system allows the member interface to be aggregated. 0: The system does not allow the member interface to be aggregated. * Fourth bit: whether the member interface is added to the link aggregation group (LAG). 1: The member interface is added to the LAG. 0: The member interface is not added to the LAG. * Fifth bit: whether the member interface can receive packets. 1: The member interface can receive packets. 0: The member interface cannot receive packets. * Sixth bit: whether the member interface can send packets. 1: The member interface can send packets. 0: The member interface cannot send packets. * Seventh bit: whether the packets have default contents. 1: The packets have default contents. 0: The packets do not have default contents. * Eighth bit: whether the receive state machine of the Actor is in the Expired state. 1: It is in the Expired state. 0: It is not in the Expired state. |
| Weight | Weight of a member interface in an Eth-Trunk interface. |
| PortName | Eth-Trunk member interface name. |
| Number Of Up Ports In Trunk | Number of member interfaces in the up state in an Eth-Trunk interface. |
| Ports | Port number. |
| Flow statistic | Interface traffic statistics. |
| Last 300 seconds input rate Last 300 seconds output rate | The rates at which bits and packets are sent and received by the interface in the last 300 seconds.  Each time this command is run, the rates at which bits and packets are sent and received by the interface within the last 300s are re-collected and displayed. The statistics are measured in the number of bits/300s and the number of packets/300s.  The interval at which traffic statistics are collected can be changed using the set flow-stat interval command. |
| Local | Configuration of the local Eth-Trunk. |
| WorkingMode | Working mode of an Eth-Trunk interface:   * Normal: manual load balancing mode. * Static: static LACP mode. * Dynamic: dynamic LACP mode. |
| Partner | Information about member interfaces of the remote Eth-Trunk interface. |
| Input | Total number of received packets and bytes:   * packets: total number of packets.   The total number of packets received by an Eth-Trunk interface is the total number of packets received by all Eth-Trunk member interfaces.   * bytes: total number of bytes.   The total number of bytes received by an Eth-Trunk interface is the total number of bytes received by all Eth-Trunk member interfaces.   * drops: number of discarded packets. |
| Output | Number of packets and bytes sent by an interface:   * packets: total number of packets.   The total number of packets sent by an Eth-Trunk interface is the total number of packets sent by all Eth-Trunk member interfaces.   * bytes: total number of bytes.   The total number of bytes sent by an Eth-Trunk interface is the total number of bytes sent by all Eth-Trunk member interfaces.   * drops: number of discarded packets. |
| Act | Number of activated links. |
| Inact | Number of deactivated links. |
| Cfgd | Number of configured links. |
| BW | Link bandwidth. |
| PortKeyMode | LACP member interface's PortKey generation mode:   * Auto: The system automatically generates a value. * Manual: The configuration is generated manually. |