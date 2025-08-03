display isis last-peer-change
=============================

display isis last-peer-change

Function
--------



The **display isis last-peer-change** command displays information about IS-IS neighbor status changes.




Format
------

**display isis** *process-id* **last-peer-change**

**display isis last-peer-change** [ *process-id* | **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check IS-IS neighbor status changes, you can run the **display isis last-peer-change** command. By viewing information about IS-IS neighbor status changes, you can determine the network status.After a master/slave device switchover, if the command is run when no neighbor relationship flapping exists, nothing will be displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IS-IS neighbor status changes.
```
<HUAWEI> display isis last-peer-change
Peer change information for ISIS(1)
----------------------------------------

Time      : 2012-03-13 14:33:08+00:00
System ID : 0000.0000.0002
Type      : L2 LAN
Interface : 100GE1/0/1 (4)
State     : Init -> Up
Details   : New adjacency created

Time      : 2012-03-13 14:33:08+00:00
System ID : 0000.0000.0002
Type      : L2 LAN
Interface : 100GE1/0/1 (4)
State     : Up -> Init
Details   : Peer state change

Time      : 2012-03-13 14:33:08+00:00
System ID : 0000.0000.0002
Type      : L1 LAN
Interface : 100GE1/0/1 (4)
State     : Up -> Down
Details   : Area mismatch

Time      : 2012-03-13 14:32:23+00:00
System ID : 0000.0000.0002
Type      : L2 LAN
Interface : 100GE1/0/1 (4)
State     : Init -> Up
Details   : New adjacency created

Time      : 2012-03-13 14:32:23+00:00
System ID : 0000.0000.0002
Type      : L1 LAN
Interface : 100GE1/0/1 (4)
State     : Init -> Up
Details   : New adjacency created

```

**Table 1** Description of the **display isis last-peer-change** command output
| Item | Description |
| --- | --- |
| Time | Neighbor change interval. |
| System ID | System ID of the host. |
| Type | Neighbor type:   * L1 LAN. * L2 LAN. * P2P. |
| Interface | Interface where the neighbor resides and the interface index. |
| State | Status of the neighbor change. The options are as follows:   * Init -> Up. * Up -> Down. * Up -> Init. * Down -> Up. * Up -> Up. * IPv4/IPv6 -> IPv4. * IPv4/IPv6 -> IPv6. * IPv4 -> IPv4/IPv6. * IPv6 -> IPv4/IPv6. * IPv4 -> IPv6. * IPv6 -> IPv4. |
| Details | Cause of the neighbor change:   * Circuit down: The interface is Down. * BFD down: The BFD session becomes Down. * BFD6 down: The IPv6 BFD session becomes Down. * Hold timer expired: The holding time of a neighbor times out. * New adjacency created: A new adjacency is created. * Adjacency usage mismatch: The level of a P2P neighbor changes, causing level mismatch. * Memory low: The system has consumed the maximum number of memory resources allowed and can no longer apply for new memory resources. * P2P circuit ID conflict: The circuit ID negotiated by the two ends is inconsistent, or the packet is modified. * Area mismatch: The area ID of a router does not match that of its neighboring router. * Three way down: The three-way handshake status becomes Down. * Three way init: The three-way handshake status becomes initializing. * Three way up: The three-way handshake status becomes Up. * Protocol change: The protocol is changed. * Mt usage mismatch: The MTID carried by the P2P neighbor is not the same as that configured on the local end. * Peer state change: The neighbor status changes. * Peer level change: The neighbor level changes. |