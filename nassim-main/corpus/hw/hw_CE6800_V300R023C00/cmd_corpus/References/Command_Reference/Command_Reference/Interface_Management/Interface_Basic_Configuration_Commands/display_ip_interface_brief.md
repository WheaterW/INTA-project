display ip interface brief
==========================

display ip interface brief

Function
--------



The **display ip interface brief** command displays brief interface IP configurations, including the IP address, mask, status of the physical link and protocol, and interface description.

If no parameter is specified, brief IP configurations of all interfaces are displayed.




Format
------

**display ip interface brief** [ *interface-type* *interface-number* | **slot** *slot-number* [ **card** *card-number* ] ]

**display ip interface brief** *interface-type*

**display ip interface brief ip-configured** [ **except** *interface-type* ]

**display ip interface brief** *interface-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays brief IP configurations of a specified type of interface.  If no interface type is specified, the system displays IP configurations of and statistics on all interfaces. | The value is of the enumerated type. |
| *interface-number* | Displays brief IP configurations of a specified interface.  ifNum and ifType define an interface. If an interface type is specified but no interface number is specified, statistics on and IP configurations of all the interfaces of the specified type are displayed. | - |
| **slot** *slot-number* | Displays the IP configuration and statistics of interfaces on the specified slot.  If the slot number is not specified, brief IP configurations of the interfaces on all interface boards and main control boards are displayed. | - |
| **card** *card-number* | Displays the IP configuration and statistics of interfaces on the specified slot.  If the slot number is not specified, brief IP configurations of the interfaces on all interface boards and main control boards are displayed. | - |
| **ip-configured** | Displays the IP configuration of interfaces assigned IP addresses. | - |
| **except** | Displays the IP configuration of interfaces, excluding the interfaces of the specified type. | - |
| *interface-name* | Displays brief IP-related information about a specified interface.  If no interface is specified, IP-related configurations and statistics on all interfaces are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view the physical status, protocol status, and IP address of an interface, run the **display ip interface brief** command. The obtained information about interface status and configurations helps you diagnose interface faults.



**Precautions**

You can run the **display ip interface brief** command to view the following:

* IP configurations of all interfaces
* IP configurations of interfaces of the specified type, specified interfaces, interfaces in the specified slot, or interfaces on the specified board in the slot
* IP configurations of interfaces assigned IP addressesThis command, however, cannot be used to display the IP configurations of member interfaces of a Trunk.If an interface is used for services exclude IP services, no information about the interface is displayed with this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief IP configurations of all interfaces on the device.
```
<HUAWEI> display ip interface brief
*down: administratively down
!down: FIB overload down
^down: standby
(l): loopback
(s): spoofing
(d): Dampening Suppressed
(ed): error down
The number of interface that is UP in Physical is 3
The number of interface that is DOWN in Physical is 0
The number of interface that is UP in Protocol is 3
The number of interface that is DOWN in Protocol is 0
Interface                   IP Address/Mask    Physical Protocol VPN
100GE1/0/1                  10.2.1.1/16         up       up       --
MEth0/0/0                   192.168.190.129/16  up       up       --
NULL0                       unassigned          up       up(s)    --

```

**Table 1** Description of the **display ip interface brief** command output
| Item | Description |
| --- | --- |
| (l): loopback | The loopback function is configured on the interface. |
| (s): spoofing | The spoofing feature of the link protocol status of the interface. That is, the link protocol status of the interface is always Up.  This is the build-in attribute of an interface. When this interface is assigned an IP address, (s) is still displayed. |
| (d): Dampening Suppressed | Protocol of the interface is suppressed. |
| The number of interface that is UP/DOWN in Physical is | Status (Up or Down) of a physical link and number of interfaces in different states. |
| The number of interface that is UP/DOWN in Protocol is | Status (Up or Down) of a protocol and number of interfaces in different states. |
| Physical | Physical status of an interface:   * Up: The interface is running normally. * Down: The interface becomes faulty. * \*down: An administrator runs the shutdown command on the interface. * !down: The forwarding information base (FIB) module is in the overload suspension state. In this case, the link protocol status of the interface is Down. |
| Protocol | Link protocol status of the interface:   * Up: The link protocol status of the interface is normal. * Down: The link protocol status of the interface is abnormal, or the interface is not assigned an IP address. * \*down: refers to administratively Down, indicating that the administrator runs the shutdown network-layer command on the interface. |
| Interface | Interface type and number.  Bandwidth identifier displayed in the brackets after an interface: Actual bandwidth of the interface. For example, the name of a 10 Gbit/s main interface or sub-interface is tagged with the 10G bandwidth identifier. For a main interface or sub-interface whose bandwidth is limited by a license, the bandwidth identifier is displayed after the interface name. For a main interface or sub-interface with adaptive bandwidth, the bandwidth identifier is displayed after the interface name. |
| IP Address/Mask | IP address and subnet mask of a Layer 3 interface. |
| VPN | VPN configured for the current interface. The possible states are as follows:   * --: No VPN is configured. * huawei: indicates the name of a VPN instance. |
| (ed): error down | The physical layer of the interface is in the Error Down state. |
| \*down | Reason that interface is physically Down.  Administratively DOWN: The network administrator runs the shutdown command on the interface. |
| !down | The interface goes Down because the number of route prefixes in the FIB exceeds the upper limit. |
| ^down | The interface is a backup interface. |