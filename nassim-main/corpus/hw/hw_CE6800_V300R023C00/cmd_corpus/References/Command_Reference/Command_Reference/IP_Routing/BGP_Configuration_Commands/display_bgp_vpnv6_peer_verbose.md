display bgp vpnv6 peer verbose
==============================

display bgp vpnv6 peer verbose

Function
--------



The **display bgp vpnv6 peer verbose** command displays detailed information about BGP VPNv6 peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **peer** **verbose**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **peer** *ipv6-address* **verbose**

**display bgp vpnv6 vpn-instance** *vpn-instance-name* **peer** *ipv4-address* **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 peer verbose** command displays detailed information about BGP VPNv6 peers.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about BGP VPNv6 peers.
```
<HUAWEI> display bgp vpnv6 vpn-instance vrf1 peer 2001:DB8:12::2 verbose

         BGP Peer is 2001:DB8:12::2,  remote AS 200
         Type: EBGP link
         BGP version 4, Remote router ID 10.1.1.2
         Update-group ID: 6
         BGP current state: Established, Up for 00h05m02s
         BGP current event: RecvKeepalive
         BGP last state: OpenConfirm
         BGP Peer Up count: 1
         Received total routes: 0
         Received active routes total: 0
         Advertised total routes: 0
         Port: Local - 179        Remote - 54463
         Configured: Connect-retry Time: 32 sec
         Configured: Min Hold Time: 0 sec
         Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
         Received  : Active Hold Time: 180 sec
         Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
         Peer optional capabilities:
         Peer supports bgp multi-protocol extension
         Peer supports bgp route refresh capability
         Peer supports bgp 4-byte-as capability
         Address family IPv6 Unicast: advertised and received
 Received: Total 8 messages
                  Update messages                1
                  Open messages                  1
                  KeepAlive messages             6
                  Notification messages          0
                  Refresh messages               0
 Sent: Total 10 messages
                  Update messages                1
                  Open messages                  3
                  KeepAlive messages             6
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
 Last keepalive received: 2020-01-28 17:24:31+00:00
 Last keepalive sent    : 2020-01-28 17:24:12+00:00
 Last update    received: 2020-01-28 17:20:03+00:00
 Last update    sent    : 2020-01-28 17:20:03+00:00
 No refresh received since peer has been configured
 No refresh sent since peer has been configured
 Minimum route advertisement interval is 30 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp vpnv6 peer verbose** command output
| Item | Description |
| --- | --- |
| BGP version | BGP version. |
| BGP current state | State of BGP:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| BGP current event | Current BGP event. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| BGP Peer is | IP address of a BGP peer. |
| Peer Preferred Value | PrefVal of the peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| Remote router ID | Router ID of the peer. |
| Update-group ID | ID of the Update group to which a peer belongs. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of active route prefixes received. |
| Received | Number of messages received from the peerr:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Advertised total routes | Number of route prefixes sent. |
| Keepalive Time | Interval for sending Keepalive messages to the peer. |
| 4-byte-as capability has been enabled | 4-byte-As is enabled. |
| Address family IPv6 Unicast | IPv6 unicast address family. |
| Notification | Notification message sent or received by a peer. |
| Authentication type configured | Authentication type that is configured. |
| Last keepalive received | Time when a Keepalive message was last received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Last time when an Update message is received. |
| Last update sent | Last time when an Update message is sent. |
| No refresh received since peer has been configured | No Route-Refresh messages are received from the peer after the peer relationship is established. |
| No refresh sent since peer has been configured | No Route-Refresh messages are sent to the peer after the peer relationship is established. |
| Minimum route advertisement interval is 30 seconds | Minimum interval at which routes are advertised. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Routing policy configured | Configured routing policy. |
| Type | BGP link type (IBGP or EBGP). |
| Port | Port number.   * Local: local port number. BGP uses TCP as the transport layer protocol and uses the fixed port number 179. * Remote: indicates the port number of the peer. |
| Configured | Locally configured timers.   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from the peer in the hold time, BGP considers that the peer is Down and then instructs other peers to remove the routes that are sent from the peer. * Keep Alive Time: indicates the interval at which Keepalive messages are sent to the peer. BGP peers exchange Keepalive messages periodically to maintain their relationships. |
| Sent | Number of packets sent to peers:   * Total: total number of records. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of Route-refresh messages. |
| Negotiated | Negotiated timer value. |