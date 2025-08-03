display bgp peer verbose
========================

display bgp peer verbose

Function
--------



The **display bgp peer verbose** command displays detailed information about BGP peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp peer** *ipv4-address* **verbose**

**display bgp peer verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp peer** *ipv6-address* **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp peer verbose** command displays BGP peer detailed information. This command can be used for troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the peer 10.2.2.9.
```
<HUAWEI> display bgp peer 10.2.2.9 verbose
BGP Peer is 10.2.2.9,  remote AS 100
 Type: IBGP link
 BGP version 4, Remote router ID 10.1.1.1
 Update-group ID: 1 
 BGP current state: Established, Up for 00h57m53s
 BGP current event: RecvKeepalive
 BGP last state: Established
 BGP Peer Up count: 1
 Received total routes: 0
 Received active routes total: 0
 Advertised total routes: 2
 Port: Local - 42796        Remote - 179
 Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Received  : Active Hold Time: 180 sec
 Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
 Peer optional capabilities:
  Peer supports bgp multi-protocol extension
  Peer supports bgp route refresh capability
 Peer supports bgp 4-byte-as capability
  Address family IPv4 Unicast: advertised and received
  Some BGP capabilities have not been negotiated for incomplete open message
 Received:
                  Total                          60
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             58
                  Notification messages          0
                  Refresh messages               0
 Sent:
                  Total                          61
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             58
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
  Last keepalive received:2011-05-24 08:48:36
 Minimum route advertisement interval is 15 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 Listen-only has been configured
 Send best-external has been configured
 Add-path number : 3
 Peer Preferred Value: 0 
 Peer limit state: true
 Pipe limit percent: 10
 Pipe limit count: 3
 Pipe last limit time: 2020-11-21 08:48:36
 Routing policy configured:
 Peer's BFD has been enabled
 No routing policy is configured
 TCP-MSS configured value: 200
 Rely-state interface has been enabled
 Peer-as-check has been configured

```

**Table 1** Description of the **display bgp peer verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | State of BGP:   * Idle: indicates that BGP denies any connection request. This is the initial status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Peer Preferred Value | PrefVal of the peer. |
| Peer limit state | Suppression status of the pipe for receiving packets from peers:   * true: suppressed. * false: not suppressed. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of prefixes of received active BGP routes (optimal BGP routes). |
| Received : Active Hold Time | Hold time of the peer. |
| Received | Number of messages received from the peerr:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Advertised total routes | Number of route prefixes sent. |
| Keepalive Time | Interval for sending Keepalive messages to the peer. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Authentication type configured | Authentication type that is configured. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Minimum route advertisement interval is 15 seconds | Minimum interval at which routes are advertised. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Listen-only has been configured | The device detects connection requests but does not initiate any connection. |
| Send best-external has been configured | The local device has been enabled to advertise Best External routes to a specified peer. |
| Add-path number | Number of optimal routes that the local device can send to the peer. |
| Pipe limit percent | Rate limit percentage of the pipe for receiving neighbor packets. |
| Pipe limit count | Number of times rate limiting is performed on the pipe for receiving neighbor packets. |
| Pipe last limit time | Last time when the rate of the pipe for receiving neighbor packets was limited. |
| Routing policy configured | Configured routing policy. |
| Peer's BFD has been enabled | BFD has been enabled on the peer. |
| No routing policy is configured | No routing policy is configured. |
| TCP-MSS configured value | TCP MSS value used during TCP connection establishment. This field is displayed only after the peer tcp-mss command is configured. |
| Type | BGP link type (IBGP or EBGP). |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and uses the fixed port number 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timers.   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from the peer in the hold time, BGP considers that the peer is Down and then instructs other peers to remove the routes that are sent from the peer. * Keep Alive Time: indicates the interval at which Keepalive messages are sent to the peer. BGP peers exchange Keepalive messages periodically to maintain their relationships. |
| Negotiated : Active Hold Time | Hold time negotiated by BGP peers. |
| Sent | Number of packets sent to peers:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Negotiated | Negotiated timer value. |