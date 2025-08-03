display bgp unnumbered peer interface verbose
=============================================

display bgp unnumbered peer interface verbose

Function
--------



The **display bgp unnumbered peer interface verbose** command displays detailed BGP unnumbered peer information.




Format
------

**display bgp unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | - |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check detailed BGP unnumbered peer information, run the **display bgp unnumbered peer interface verbose** command. The command output can be used for troubleshooting.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed peer information on interface 100GE 1/0/8.
```
<HUAWEI> display bgp unnumbered peer interface 100GE 1/0/8 verbose

 BGP Peer is FE80::3A9C:B2FF:FE21:300,  remote AS 100
 Type: IBGP link
 Unnumbered peer
 Belong to peer-group: ii
 BGP version 4, Remote router ID 10.3.3.3
 Update-group ID: 3
 BGP current state: Established, Up for 01h14m17s
 BGP current event: RecvKeepalive
 BGP last state: OpenConfirm
 BGP Peer Up count: 6
 Received total routes: 0
 Received active routes total: 0
 Advertised total routes: 0
 Port: Local - 50992        Remote - 179
 Configured: Connect-retry Time: 32 sec
 Configured: Min Hold Time: 0 sec
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Address family IPv6 Unicast: advertised and received
 Received:
                  Total  messages                90
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             87
                  Notification messages          0
                  Refresh messages               0
 Sent    :
                  Total  messages                89
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             86
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2021-04-15 12:02:33+00:00
  Last keepalive sent    : 2021-04-15 12:02:31+00:00
  Last update received   : 2021-04-15 10:48:51+00:00
  Last update sent       : 2021-04-15 10:48:51+00:00
  No refresh received since peer has been configured
  Last refresh sended    : 2021-04-15 07:55:23+00:00
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 Extended Next Hop Encoding capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp unnumbered peer interface verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing further actions. * If the TCP connection is successfully established, BGP stops the ConnectRetry Timer, sends an Open message to the peer, and changes its state to Opensent. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * If the TCP connection is successfully established, BGP resets the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer. * If BGP receives a correct Open message, BGP enters the OpenConfirm state. * If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * OpenConfirm: BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP enters the Idle state. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP enters the Idle state. * No neg: address family is not enabled on the BGP peer. In this state, other successfully negotiated address families can exchange Update messages normally. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, which can be Idle, Connect, Active, OpenSent, OpenConfirm, Established, or No neg. |
| BGP Peer Up count | Flapping count of a BGP peer in a specified period of time. |
| BGP Peer is | BGP peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Peer Preferred Value | Preferred value of the peer. |
| Unnumbered peer | Unnumbered peer. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the update-group to which the peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Indicates the number of received active route prefixes. |
| Received : Active Hold Time | Hold time of the peer. |
| Received | Number of packets received from peers:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Notification messages: number of Notification messages. * Refresh messages: number of Route-refresh messages. |
| Advertised total routes | Number of sent route prefixes. |
| Keepalive Time | Interval for sending Keepalive messages to the peer. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family IPv6 Unicast | IPv6 unicast address family. |
| Sent | Number of packets sent to peers:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Notification messages: number of Notification messages. * Refresh messages: number of Route-refresh messages. |
| Authentication type configured | Authentication type. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Last time when an Update message is received. |
| Last update sent | Last time when an Update message is sent. |
| Last refresh sended | Last time when a Refresh message is sent. |
| No routing policy is configured | No routing policy is configured. |
| Minimum route advertisement interval is 15 seconds | Minimum route advertisement interval. |
| Optional capabilities | Capabilities supported by the peer (optional). |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Routing policy configured | Indicates the configured routing policy. |
| Type | BGP link type, which can be IBGP or EBGP. |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and has a fixed port number of 179. * Remote: port number of the peer. |
| Configured | Locally configured timers:   * Active Hold Time: If a BGP device does not receive a Keepalive message from its peer within the Hold Time, the BGP device considers the peer Down. In this case, the BGP device instructs other peers to withdraw the routes received from the peer that is Down. * Keep Alive Time: interval for sending KeepAlive messages to the peer. BGP peers send KeepAlive messages to each other periodically to notify each other that they are working normally. |
| Negotiated : Active Hold Time | Hold time negotiated by BGP peers. |
| Negotiated | Negotiated value of the timer. |