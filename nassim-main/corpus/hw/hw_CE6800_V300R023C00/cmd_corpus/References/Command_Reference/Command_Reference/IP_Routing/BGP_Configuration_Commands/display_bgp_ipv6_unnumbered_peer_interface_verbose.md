display bgp ipv6 unnumbered peer interface verbose
==================================================

display bgp ipv6 unnumbered peer interface verbose

Function
--------



The **display bgp ipv6 unnumbered peer interface verbose** command displays detailed BGP IPv6 unnumbered peer information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
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

To check detailed BGP IPv6 unnumbered peer information, run the **display bgp ipv6 unnumbered peer interface verbose** command. The command output can be used for troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed IPv6 peer information on interface 100GE 1/0/8.
```
<HUAWEI> display bgp ipv6 unnumbered peer interface 100GE 1/0/8 verbose

 BGP Peer is FE80::3A9C:B2FF:FE21:300,  remote AS 100
 Type: IBGP link
 Unnumbered peer
 Belong to peer-group: ii
 BGP version 4, Remote router ID 10.3.3.3
 Update-group ID: 3
 BGP current state: Established, Up for 00h34m42s
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
                  Total  messages                44
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             41
                  Notification messages          0
                  Refresh messages               0
 Sent    :
                  Total  messages                43
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             40
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received: 2021-04-15 11:23:10+00:00
  Last keepalive sent    : 2021-04-15 11:23:09+00:00
  Last update received   : 2021-04-15 10:48:51+00:00
  Last update sent       : 2021-04-15 10:48:51+00:00
  No refresh received since peer has been configured
  Last refresh sended    : 2021-04-15 07:55:23+00:00
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp ipv6 unnumbered peer interface verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing further actions. * If the TCP connection is successfully established, BGP stops the ConnectRetry Timer, sends an Open message to the peer, and changes its state to Opensent. * If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state. * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP. * If the TCP connection is successfully established, BGP resets the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. * If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. * If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state. * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer. * If BGP receives a correct Open message, BGP enters the OpenConfirm state. * If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. * OpenConfirm: BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message or a TCP connection teardown message, BGP enters the Idle state. * If BGP receives a Keepalive message, BGP enters the Established state. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or Keepalive message, BGP remains in the Established state. * If BGP receives a Notification message, BGP enters the Idle state. * No neg: address family is not enabled on the BGP peer. In this state, other successfully negotiated address families can exchange Update messages normally. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage. Possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Flapping count of a BGP peer in a specified period of time. |
| BGP Peer is | BGP peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Peer Preferred Value | PrefVal of the peer. |
| Unnumbered peer | Unnumbered peer. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the update-group to which the peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of received active route prefixes. |
| Received : Active Hold Time | Hold time on the peer. |
| Received | Number of packets received from peers:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Notification messages: number of Notification messages. * Refresh messages: number of Route-refresh messages. |
| Advertised total routes | Number of sent route prefixes. |
| Keepalive Time | Interval at which Keepalive messages are sent to the peer. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family IPv6 Unicast | IPv6 unicast address family. |
| Sent | Number of packets sent to peers:   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive messages. * Notification messages: number of Notification messages. * Refresh messages: number of Route-refresh messages. |
| Authentication type configured | Authentication type that is configured. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Last time when an Update message is received. |
| Last refresh sended | Last time when a Refresh message is sent. |
| Last update sent | Last time when an Update message is sent. |
| No routing policy is configured | There is no routing policy configured. |
| Minimum route advertisement interval is 15 seconds | Minimum route advertisement interval. |
| Optional capabilities | (Optional) Peer-supported capabilities. |
| Route refresh capability has been enabled | Route refreshing has been enabled. |
| Routing policy configured | Configured routing policy. |
| Type | BGP link type: IBGP or EBGP. |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and has a fixed port number of 179. * Remote: port number of the peer. |
| Configured | Locally configured timers.   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from the peer in the hold time, BGP considers that the peer is Down and then instructs other peers to remove the routes that are sent from the peer. * Keep Alive Time: indicates the interval at which Keepalive messages are sent to the peer. BGP peers exchange Keepalive messages periodically to maintain their relationships. |
| Negotiated : Active Hold Time | Hold time agreed between the BGP peers after capability negotiation. |
| Negotiated | Negotiated value of the timer. |