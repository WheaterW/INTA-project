display ip interface description
================================

display ip interface description

Function
--------



The **display ip interface description** command displays brief information on and descriptions of IP-related interfaces.

If no parameter is specified, brief IP configurations of all interfaces are displayed.




Format
------

**display ip interface description** [ *interface-type* *interface-number* | **slot** *slot-number* [ **card** *card-number* ] ]

**display ip interface description** *interface-type*

**display ip interface description ip-configured** [ **except** *interface-type* ]

**display ip interface description** *interface-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Displays IP description configurations of a specified type of interface.  If no interface type is specified, the system displays IP configurations of and statistics on all interfaces. | The value is of the enumerated type. |
| *interface-number* | Displays IP description configurations of a specified interface.  ifNum and ifType define an interface. If an interface type is specified but no interface number is specified, statistics on and IP description configurations of all the interfaces of the specified type are displayed. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **slot** *slot-number* | Displays the IP configuration and statistics of interfaces on the specified slot.  If the slot number is not specified, description IP configurations of the interfaces on all interface boards and main control boards are displayed. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **card** *card-number* | Displays the IP configuration and statistics of interfaces on the specified slot.  If the slot number is not specified, description IP configurations of the interfaces on all interface boards and main control boards are displayed. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **ip-configured** | Displays the IP configuration of interfaces assigned IP addresses. | - |
| **except** | Displays the IP configuration of interfaces, excluding the interfaces of the specified type. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view brief information on and descriptions of IP-related interfaces, run the **display ip interface description** command.



**Implementation Procedure**

* Run the display interface description command to view the description of the interface.
* Run the display interface command to view detailed information about the operation and statistics of the interface.

**Precautions**

You can run the display ip interface brief command to view the following:

* IP configurations of all interfaces
* IP configurations of interfaces of the specified type, specified interfaces, interfaces in the specified slot, or interfaces on the specified board in the slot
* IP configurations of interfaces assigned IP addressesThis command, however, cannot be used to display the IP configurations of member interfaces of a Trunk.If an interface is used for services exclude IP services, no information about the interface is displayed with this command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information on and descriptions of IP-related interfaces.
```
<HUAWEI> display ip interface description
Codes:
      Ana(Analogmodem),       Asy(Async),             Cell(Cellular),
      Dia(Dialer),            GE(GigabitEthernet),    H(Hssi),
      Loop(LoopBack),         Tun(Tunnel)

      d(dampened),            D(down),                *D(administratively down),
      !D(FIB overload down),  ^D(standby),            l(loopback),
      s(spoofing),            U(up)
------------------------------------------------------------------------------
Number of interfaces whose physical status is Up: 5
Number of interfaces whose physical status is Down: 0
Number of interfaces whose protocol status is Up: 4
Number of interfaces whose protocol status is Down: 1

Interface                      IP Address/Mask    Phy  Prot Description
100GE1/0/2                     1.1.1.1/16         U    U
100GE1/0/1                     1.1.1.1/16         U    U
100GE1/0/1                     1.1.1.1/16         U    U
MEth0/0/0                      unassigned         U    D
NULL0                          unassigned         U    U(s)

```

**Table 1** Description of the **display ip interface description** command output
| Item | Description |
| --- | --- |
| Number of interfaces whose physical status is Up/Down | Number of interfaces with the physical status of Up/Down. |
| Number of interfaces whose protocol status is Up/Down | Number of interfaces with the link layer protocol of Up/Down. |
| Interface | Type and number of an interface. |
| IP Address/Mask | IP address and subnet mask of a Layer 3 interface. |
| Phy | Physical status of an interface. |
| Prot | Link layer protocol status of an interface. |
| Codes | The following information provides the full spelling and explanation of the abbreviated interface names, physical status, and link layer protocols. |