display bgp vpn-target peer verbose
===================================

display bgp vpn-target peer verbose

Function
--------



The **display bgp vpn-target peer verbose** command displays detailed information about BGP peers.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display bgp vpn-target peer verbose**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display bgp vpn-target peer** { *ipv4-address* | *ipv6-address* } **verbose**

For CE6885-LL (low latency mode):

**display bgp vpn-target peer** *ipv4-address* **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 address. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpn-target peer verbose** command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, specify log-info in the command to check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about peers in the BGP VPN-target address family.
```
<HUAWEI> display bgp vpn-target peer verbose

         BGP Peer is 2.2.2.2,  remote AS 200
         Type: EBGP link
         BGP version 4, Remote router ID 2.2.2.2
         Update-group ID: 7
         BGP current state: Established, Up for 00h12m10s
         BGP current event: RecvKeepalive
         BGP last state: OpenConfirm
         BGP Peer Up count: 3
         Received total routes: 0
         Received active routes total: 0
         Advertised total routes: 0
         Port: Local - 53198        Remote - 179
         Configured: Connect-retry Time: 32 sec
         Configured: Min Hold Time: 0 sec
         Configured: Active Hold Time: 30 sec   Keepalive Time:10 sec
         Received  : Active Hold Time: 30 sec
         Negotiated: Active Hold Time: 30 sec   Keepalive Time:10 sec
         Peer optional capabilities:
         Peer supports bgp multi-protocol extension
         Peer supports bgp route refresh capability
         Peer supports bgp 4-byte-as capability
         Address family IPv4 Unicast: advertised and received
         Address family VPN-Target: advertised and received
 Received: Total 93 messages
                  Update messages                2
                  Open messages                  1
                  KeepAlive messages             90
                  Notification messages          0
                  Refresh messages               0
 Sent: Total 93 messages
                  Update messages                3
                  Open messages                  1
                  KeepAlive messages             89
                  Notification messages          0
                  Refresh messages               0
 Authentication type configured: None
 Last keepalive received: 2019-09-17 05:12:10+00:00
 Last keepalive sent    : 2019-09-17 05:12:08+00:00
 Last update received: 2019-09-17 05:00:02+00:00
 Last update sent    : 2019-09-17 05:00:02+00:00
 No refresh received since peer has been configured
 No refresh sent since peer has been configured
 Minimum route advertisement interval is 30 seconds
 Optional capabilities:
 Route refresh capability has been enabled
 4-byte-as capability has been enabled
 Connect-interface has been configured
 Multi-hop ebgp has been enabled
 Peer Preferred Value: 0
 Routing policy configured:
 No routing policy is configured

```

**Table 1** Description of the **display bgp vpn-target peer verbose** command output
| Item | Description |
| --- | --- |
| BGP Peer | Peer IP address. |
| BGP version | BGP version used on the peer. |
| BGP current state | Status the BGP peer:   * Idle: BGP denies any connection request. This is the initial status of BGP. * Active: BGP tries to establish a TCP connection. This is the intermediate status of BGP. * Connect: BGP is waiting for the establishment of the TCP connection to complete before performing further actions. * OpenSent: BGP is waiting for an Open message from the peer. * OpenConfirm: BGP is waiting for a Notification message or a Keepalive message. * Established: BGP peers can exchange Update, Notification, and Keepalive messages. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| BGP current event | Current BGP event. |
| BGP Peer Up count | Number of times the BGP peer flaps. |
| BGP last state | State of last BGP stage, The possible states are Idle, Connect, Active, OpenSent, OpenConfirm, Established, and No neg. |
| Peer supports bgp multi-protocol extension | The BGP peer supports MP-BGP. |
| Peer supports bgp route refresh capability | The BGP peer supports route-refresh. |
| Peer Preferred Value | PrefVal of the peer. |
| Peer optional capabilities | Optional capabilities supported by the peer. |
| remote AS | Peer AS number. |
| Remote router ID | Router ID of a peer. |
| Update-group ID | Update group ID of the BGP peer. |
| Received | * Active Hold Time indicates the hold time of the peer. * Keepalive Time indicates the interval for sending Keepalive messages to the peer.   Number of packets received from the peer.   * Total: total number of records. * Update messages: number of Update messages. * Open messages: number of Open messages. * KeepAlive messages: number of Keepalive packets. * Notification messages: number of Notification messages. * Refresh messages: number of Route-refresh messages. |
| Received total routes | Number of received route prefixes. |
| Received active routes total | Number of active route prefixes received. |
| Advertised total routes | Number of route prefixes sent. |
| Address family IPv4 Unicast | IPv4 unicast address family. |
| Address family VPN-Target | VPN-Target address family. |
| Authentication type configured | Authentication type. |
| Last keepalive received | Last time when a Keepalive message is received. |
| Last keepalive sent | Time when a Keepalive message was last sent. |
| Last update received | Time at which the last update message is received. |
| Last update sent | Time at which the last update message is sent. |
| Minimum route advertisement interval is 30 seconds | Minimum route advertisement interval:   * EBGP: 30s. * IBGP: 15s. |
| Optional capabilities | Optional capabilities of the peer. |
| Route refresh capability has been enabled | Route-refresh enabled. |
| Routing policy configured | Configured routing policy. |
| Type | BGP link type (IBGP or EBGP). |
| Port | Port No.   * Local: indicates the local port number. BGP uses TCP as the transport layer protocol. The fixed port number is 179. * Remote: peer port number. |
| Configured | Locally configured timers.   * Active Hold Time: indicates the hold time. If BGP does not receive any Keepalive message from a BGP peer within the hold time, BGP considers that the peer is Down. In this case, BGP instructs other peers to withdraw the routes received from the peer in the Down state. * Keepalive Time: indicates the interval for sending Keepalive messages to BGP peers. BGP peers periodically send Keepalive messages to each other to notify each other that they are working properly. |
| Negotiated | * Active Hold Time indicates the hold time determined by BGP peers after capability negotiation. * Keepalive Time indicates the interval for sending Keepalive messages to the peer. |
| Sent | Number of messages sent to the BGP peer:   * Total: indicates the total number of messages. * Update messages: indicates the number of Update messages. * Open messages: indicates the number of Open messages. * KeepAlive messages: indicates the number of Keepalive messages. * Notification messages: indicates the number of Notification messages. * Refresh messages: indicates the number of route-refresh messages. |