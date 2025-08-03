display msdp brief
==================

display msdp brief

Function
--------



The **display msdp brief** command displays brief information about Multicast Source Discovery Protocol (MSDP) peers.




Format
------

**display msdp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **brief** [ **state** { **connect** | **down** | **listen** | **shutdown** | **up** } ]

**display msdp brief** [ **state** { **connect** | **down** | **listen** | **shutdown** | **up** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays brief information about MSDP peers in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |
| **all-instance** | Displays brief information about MSDP peers in all instances. | - |
| **state** | State. | - |
| **connect** | Displays brief information about MSDP peers that act as servers of the local device and have not set up connections with the local device. | - |
| **down** | Displays brief information about MSDP peers that fail to set up connections with the local device. | - |
| **listen** | Displays brief information about MSDP peers that act as clients of the local device and have set up connections with the local device. | - |
| **shutdown** | Displays brief information about MSDP peers that have been shut down. | - |
| **up** | Displays brief information about MSDP peers that have set up connections and sessions with the local device. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

In an MSDP peer relationship, the peer with the higher IP address acts as the server, and the peer with the lower IP address acts as the client. The server listens the client using the port 639, and the client is responsible for initiating connection requests. If a connection fails, the client initiates a connection request again after a specified period.After MSDP peers establish TCP connections, you can run the **display msdp brief** command to display brief information about the remote MSDP peers, such as the peer address, autonomous system (AS) number, number of (S, G) entries, and TCP connection status.

**Prerequisites**

MSDP peer relationships have been set up.

**Precautions**

If neither vpn-instance nor all-instance is specified, the command displays brief information about MSDP peers in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about MSDP peers in the public network instance.
```
<HUAWEI> display msdp brief
MSDP Peer Brief Information of VPN-Instance: public net
  Configured   Up           Listen       Connect      Shutdown     Down
  2            2            0            0            0            0
  Peer's Address     State     Up/Down time    AS     SA Count   Reset Count
  192.168.3.2        Up        01:07:08        ?      8          0
  192.168.5.1        Up        00:16:39        ?      13         0

```

**Table 1** Description of the **display msdp brief** command output
| Item | Description |
| --- | --- |
| MSDP Peer Brief Information of VPN-Instance | Instance in which brief information about MSDP peers is displayed. |
| Configured | Total number of configured MSDP peers. |
| Up | Number of MSDP peers in the Up state. |
| Listen | Number of MSDP peers in the Listen state. |
| Connect | Number of MSDP peers in the Connect state. |
| Shutdown | Number of MSDP peers in the Shutdown state. |
| Down | Number of MSDP peers in the Down state. |
| Peer's Address | Address of a peer. |
| State | MSDP connection state.   * Up: The connection is set up and is in the Up state. * Listen: The connection is set up, and the local device acts as the server that is listening the clients. * Connect: The connection is not set up, and the local device acts as the client that has initiated a connection request. * Shutdown: The MSDP peer is shut down. * Down: The connection fails. |
| Up/Down time | Time when the session becomes Up or Down. The time format is as follows:   * Time that is shorter than or equal to 24 hours: hour: minute: second. * Time that is longer than 24 hours but shorter than or equal to one week: day: hour. * Time that is longer than one week: week: day. |
| AS | AS number of the MSDP peer.  "?" indicates that the AS number is not obtained. |
| SA Count | Number of (S, G) entries in the source active (SA) cache. |
| Reset Count | Number of MSDP reset times, including reset caused by timeout when the Notification or Holdtimer message is received. |