display isis peer
=================

display isis peer

Function
--------



The **display isis peer** command displays IS-IS neighbor information.




Format
------

**display isis peer** [ **verbose** ] [ [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] | [ **interface** { *interface-name* | *interfacetype* *interfacenumber* } ] ] [ **peer-system-id** *peer-system-id-value* ]

**display isis** *process-id* **peer** [ **verbose** ]

**display isis** *process-id* **peer** [ **verbose** ] **interface** { *interface-name* | *interfacetype* *interfacenumber* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed information about an IS-IS neighbor, including its area address, duration during which the neighbor stays Up, and IP address of its directly connected interface. | - |
| *process-id* | Displays neighbor information about the specified IS-IS process. | The value is an integer ranging from 1 to 4294967295.  By default, information about all IS-IS neighbors in all IS-IS processes is displayed. |
| **vpn-instance** *vpn-instance-name* | Displays neighbor information about a specified VPN instance to which an IS-IS process belongs. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **interface** *interfacetype* *interfacenumber* | Specifies the interface type and interface number. | - |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| **peer-system-id** *peer-system-id-value* | Displays information about the neighbor with a specified system ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

In an IS-IS area, if you need to check whether two devices can communicate with each other, run the **display isis peer** command to view information about the neighbor, such as its status, duration during which the neighbor stays Up, and the neighbor type.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed neighbor information.
```
<HUAWEI> display isis peer verbose
Peer information for ISIS(1)
---------------------------------------------------------------------------------------
                          
System Id       Interface         Circuit Id           State  HoldTime   Type       PRI
---------------------------------------------------------------------------------------
0000.0000.0001  100GE1/0/1           0000.0000.0001.01    Up     26s        L1(L1L2)    64
  MT IDs supported     : 0(UP)  2(DOWN)  100(UP)  200(DOWN)
  Local MT IDs         : 0  100  110
  Area Address(es)     : 10
  Peer IP Address(es)  : 10.10.10.1
  Uptime               : 00h00m19s
  Peer Up Time         : 2018-06-08 01:41:57
  Adj Protocol         : IPV4
  Restart Capable      : YES
  Suppressed Adj       : NO
  Peer System Id       : 0000.0000.0002
  MT IDs BFD Required  : 0(IPv4:TRUE IPv6:TRUE) 2(IPv6:TRUE)
  BFD Incr-Cost State  : MT0 : NO / MT2 : NO

0000.0000.0001  100GE1/0/1           0000.0000.0001.01      Up     27s     L2(L1L2)    64
  MT IDs supported     : 0(UP)  2(DOWN)  100(UP)  200(DOWN)
  Local MT IDs         : 0  100  110
  Area Address(es)     : 10
  Peer IP Address(es)  : 10.10.10.1
  Uptime               : 00h00m19s
  Peer Up Time         : 2018-06-08 01:41:57
  Adj Protocol         : IPV4
  Restart Capable      : YES
  Suppressed Adj       : NO
  Peer System Id       : 0000.0000.0002
  MT IDs BFD Required  : 0(IPv4:TRUE IPv6:TRUE) 2(IPv6:TRUE)
  BFD Incr-Cost State  : MT0 : NO / MT2 : NO

Total Peer(s): 2

```

# Display detailed neighbor information after the verbose parameter is used.
```
<HUAWEI> display isis peer verbose

Peer Verbose Information for ISIS(1)
--------------------------------------------------------------------------------
                         
  System Id     Interface       Circuit Id        State HoldTime Type     PRI
-----------------------------------------------------------------------------
0000.0000.0002  100GE1/0/1      0000.0000.0002.01  Up   7s       L1(L1L2) 64 

  MT IDs supported     : 0(UP) 
  Local MT IDs         : 0 
  Area Address(es)     : 10     
  Peer IP Address(es)  : 1.1.1.2           
  Peer IPV6 Address(es): FE80::3AF2:B2FF:FE21:300
  Peer IPV6 GlbAddr(es): 2001:db8:1::1
  Uptime               : 00h01m21s
  Peer Up Time         : 2021-02-27 02:34:51
  Adj Protocol         : IPV4  IPV6
  Restart Capable      : YES
  Suppressed Adj       : NO
  Peer System Id       : 0000.0000.0002
  BFD Incr-Cost State  : MT0 : NO / MT2 : NO
  MT IDs BFD Required  : 0(IPv4:FALSE IPv6:FALSE) 2(IPv6:FALSE)

0000.0000.0002  100GE1/0/1      0000.0000.0002.01  Up   7s       L2(L1L2) 64 
                
  MT IDs supported     : 0(UP) 
  Local MT IDs         : 0 
  Area Address(es)     : 10     
  Peer IP Address(es)  : 1.1.1.2           
  Peer IPV6 Address(es): FE80::3AF2:B2FF:FE21:300
  Peer IPV6 GlbAddr(es): 2001:db8:1::1
  Uptime               : 00h01m21s
  Peer Up Time         : 2021-02-27 02:34:51
  Adj Protocol         : IPV4  IPV6
  Restart Capable      : YES
  Suppressed Adj       : NO
  Peer System Id       : 0000.0000.0002
  BFD Incr-Cost State  : MT0 : NO / MT2 : NO
  MT IDs BFD Required  : 0(IPv4:FALSE IPv6:FALSE) 2(IPv6:FALSE)


Total Peer(s): 2

```

# Display IS-IS neighbor information.
```
<HUAWEI> display isis peer
Peer information for ISIS(1)
----------------------------------------------------------------------------------
                                                                
System Id        Interface        Circuit Id          State HoldTime Type      PRI
----------------------------------------------------------------------------------
0000.0000.0001   100GE1/0/1          0000.0000.0001.01   Up    24s      L1(L1L2)   64
0000.0000.0001   100GE1/0/1          0000.0000.0001.01   Up    24s      L2(L1L2)   64

Total Peer(s): 2

```

**Table 1** Description of the **display isis peer** command output
| Item | Description |
| --- | --- |
| Peer Up Time | Time when the peer went Up. |
| Peer System Id | System ID of a neighbor. If the value contains an asterisk (\*), an IPv6 multi-topology neighbor exists. |
| Peer IP Address(es) | Peer IP addresses. |
| Peer IPV6 GlbAddr(es) | Peer interface IPv6 address. |
| Peer IPV6 Address(es) | Neighbor IPv6 link local address. |
| System Id | System ID of a neighbor.  If an IPv6 IS-IS neighbor relationship is established, an asterisk (\*) is added behind the system ID. |
| Interface | Interface type and number. |
| Circuit Id | Link ID of a P2P neighbor interface, and LSP ID of a broadcast neighbor interface. |
| State | Status of the neighbor:   * Up: indicates that the neighbor is Up, and the two ends can exchange messages. * Init: indicates that only the local end can receive packets from the remote end. It is displayed when authentication is configured on the remote end. * Down: indicates that the neighbor is Down. This is the initial status, indicating that no message is received from the neighbor. The status is not displayed in most cases. |
| HoldTime | Holdtime of the adjacency. |
| Type | Neighbor type:   * L1: indicates that the neighbor type is Level-1 and that interfaces at both ends are Level-1. * L2: indicates that the neighbor type is Level-2 and that interfaces at both ends are Level-2. * L1(L1L2): indicates that the neighbor type is Level-1 and that interfaces at both ends are Level-1-2. * L2(L1L2): indicates that the neighbor type is Level-2 and that interfaces at both ends are Level-1-2. |
| PRI | Priority of a neighbor that runs for DIS. |
| MT IDs supported | IDs of topology instances supported by the remote interface. |
| MT IDs BFD Required | Whether a neighbor can go up only if the BFD status is up. |
| Local MT IDs | IDs of topology instances supported by the local interface. |
| Area Address(es) | Area address of the neighbor. |
| Uptime | Duration during which the adjacency stays Up. |
| Adj Protocol | Protocol used for setting up the adjacency (IPv4 or IPv6). |
| Restart Capable | Whether GR is supported:   * YES. * No. |
| Suppressed Adj | Whether neighbor suppression is supported:   * YES. * No. |
| BFD Incr-Cost State | Adjust the interface cost based on the status of an associated BFD session. |
| Total Peer(s) | Neighbor quantity. |