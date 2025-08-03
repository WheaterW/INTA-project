display bgp all summary
=======================

display bgp all summary

Function
--------



The **display bgp all summary** command displays information about BGP peers in the address family, including the peer status and route statistics.




Format
------

**display bgp all summary**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

During fault location, you can run the **display bgp all summary** command to view information about BGP peers in the address family, including the peer status and route statistics. The supported address family depends on the actual device.

**Precautions**

If no peers exist in an address family view, information about the address family is not displayed in the command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about peers in all BGP address family views.
```
<HUAWEI> display bgp all summary
 
 BGP local router ID : 10.1.1.1
 Local AS number : 100
 Address Family:Ipv4 Unicast
 --------------------------------------------------------------------------------------------
 Total number of peers : 3                 Peers in established state : 2

  Peer                                     AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.1.1.2                                200     1842     1844     0 0026h40m Established        2        3
  10.2.1.1                                100        0        0     0 0026h40m     Connect        0        0
  10.3.1.2                                200     1837     1840     0 0026h40m Established        2        3

 Address Family:Ipv6 Unicast
 --------------------------------------------------------------------------------------------
 Total number of peers : 1                 Peers in established state : 0

  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  2001:DB8:1::1                            200        0        0     0 0026h40m        Idle        0        0

 Address Family:Vpnv4 All
 --------------------------------------------------------------------------------------------
 Total number of peers : 4                 Peers in established state : 1

  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.2.1.1                                 100        0        0     0 0026h40m     Connect        0        0
   
  Peer of IPv4-family for vpn instance :
  VPN-Instance kkk, Router ID 10.1.1.1:
  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.4.1.2                                 200     1840     1830     0 0026h34m Established        3        0
  VPN-Instance vrf1, Router ID 10.1.1.1:
  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.2.3.4                                 100        0        0     0 0026h40m      Active        0        0
  VPN-Instance vrf2, Router ID 10.1.1.1:
  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.6.6.6                                 200        0        0     0 0026h40m        Idle        0        0

 Address Family:Vpnv6 All
 --------------------------------------------------------------------------------------------
 Total number of peers : 2                 Peers in established state : 0

  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.2.1.1                                 100        0        0     0 0026h40m     Connect        0        0
                
  Peer of IPv6-family for vpn instance :
  VPN-Instance vrf1, Router ID 10.1.1.1:
  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  2001:DB8:4::5                            300        0        0     0 0026h40m        Idle        0        0

 Address Family:Ipv4 Mvpn
 --------------------------------------------------------------------------------------------
 Total number of peers : 1                 Peers in established state : 0

  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.2.1.1                                 100        0        0     0 0026h40m     Connect        0        0

 Address Family:Evpn
 --------------------------------------------------------------------------------------------
 Total number of peers : 2                 Peers in established state : 0

  Peer                                      AS  MsgRcvd  MsgSent  OutQ  Up/Down       State    RtRcv    RtAdv
  10.1.1.2                                 100        0        0     0 00:00:07 Idle(Admin)        0        0
  2001:DB8:10::2                           100        0        0     0 00:00:07 Idle(Admin)        0        0

```

**Table 1** Description of the **display bgp all summary** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local BGP device, in the same format as an IPv4 address. |
| Local AS number | Local AS number. |
| AS | AS number of the BGP peer. |
| Address Family | Address family (The address family information depends on the address family supported by the device.) The address family information is only an example.   * Ipv4 Unicast: BGP-IPv4 unicast address family. * Ipv6 Unicast: BGP-IPv6 unicast address family. * Vpnv4 All: BGP-VPNv4 address family. * Vpnv6 All: BGP-VPNv6 address family. * Ipv4 Mvpn: BGP-MVPN address family. * Ipv4 Flow: BGP-IPv4 Flow address family. * Ipv6 Flow: BGP-IPv6 Flow address family. * Vpnv4 Flow: BGP-VPNv4 Flow address family. * Vpnv6 Flow: BGP-VPNv6 Flow address family. * L2vpn Evpn: BGP-L2VPN-EVPN address family. * Link-State Unicast: BGP-Link-State Unicast unicast address family. * Ipv6 Sr-Policy: BGP-IPv6 SR-Policy address family. * Ipv4 Multicast: BGP-IPv4 Multicast address family. * Ipv4 Labeled All: BGP-IPv4 labeled address family. * Vpnv4 Multicast: BGP-VPNv4 Multicast address family. * L2vpn-AD: BGP-L2VPN-AD address family. * Ipv4 VPN-Target: BGP-IPv4 VPN-Target address family. * Ipv4 MDT: BGP-IPv4 MDT address family. * Ipv4 RPD: BGP-IPv4 RPD address family. * Ipv4 Sr-Policy: BGP-IPv4 SR-Policy address family. * Ipv4 SD-WAN: BGP-IPv4 SD-WAN address family. |
| Total number of peers | Total number of BGP peers. |
| Peers in established state | Number of BGP peers in Established state. |
| Peer | IP address of the BGP peer. |
| Peer of IPv4-family for vpn instance | Peers in the BGP-VPN instance IPv4 address family. |
| Peer of IPv6-family for vpn instance | Peers in the BGP-VPN instance IPv6 address family. |
| MsgRcvd | Statistics about messages received from peers. The received messages are defined in BGP, such as Update and Open messages. |
| MsgSent | Statistics about messages sent to the peer. The sent messages are defined in BGP, such as Update and Open messages. |
| OutQ | Number of route prefixes that have been packed and are waiting to be sent to the peer. The statistics cover the prefixes of updated and withdrawn routes. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Current BGP status:   * Idle: BGP denies any connection request. This is the initial status of BGP.   After receiving a Start event, BGP initiates a TCP connection to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection initiated by the remote BGP peer, and changes its state to Connect.   * Connect: BGP is waiting for the TCP connection to be established before performing further actions.  1. If the TCP connection is successfully established, BGP stops the ConnectRetry Timer, sends an Open message to the peer, and changes its state to Opensent. 2. If the TCP connection fails to be established, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection initiated by the remote peer, and changes its state to Active. 3. If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP remains in the Connect state.  * Active: BGP attempts to establish a TCP connection. This is the intermediate state of BGP.  1. If the TCP connection is successfully established, BGP resets the ConnectRetry timer and sends an Open message to the peer. BGP then enters the Opensent state. 2. If the ConnectRetry timer expires, BGP restarts the ConnectRetry timer and enters the Connect state. 3. If BGP attempts to establish a TCP connection with an unknown IP address, the TCP connection fails, the ConnectRetry Timer is reset, and BGP remains in the Active state.  * OpenSent: BGP has sent an Open message to the peer and is now waiting for an Open message from the peer.  1. If BGP receives a correct Open message, BGP enters the OpenConfirm state. 2. If the Open message received by BGP is incorrect, BGP sends a Notification message to the peer and changes its state to Idle. 3. If BGP receives a TCP connection teardown message, BGP resets the ConnectRetry timer and listens to the TCP connection initiated by the peer. BGP then enters the Active state.  * OpenConfirm: BGP is waiting for a Notification or Keepalive message.  1. If BGP receives a Notification message or a TCP connection teardown message, BGP enters the Idle state. 2. If BGP receives a Keepalive message, BGP enters the Established state.  * Established: BGP peers can exchange Update, Notification, and Keepalive messages.  1. If BGP receives an Update or Keepalive message, BGP remains in the Established state. 2. If BGP receives a Notification message, BGP enters the Idle state.  * No neg: address family is not enabled on the BGP peer. In this state, other successfully negotiated address families can exchange Update messages normally. If the address family is enabled on the remote BGP peer, the local BGP peer receives a Notification message, disconnects from the remote BGP peer, changes to the Idle state, and re-establishes a connection with the remote BGP peer. |
| RtRcv | Statistics about route prefixes received from peers. The value indicates the number of Ribin routes of the peers, excluding the routes denied by a policy. |
| RtAdv | Statistics of route prefixes advertised to peers. The statistics increase when routes are advertised to peers for the first time and decrease when routes are withdrawn. The statistics are reset when the export policy of a peer changes or a slow peer is detected. |
| VPN-Instance kkk | VPN instance name. |
| Router ID | Router ID of the device. |