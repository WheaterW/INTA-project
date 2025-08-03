display bgp vpnv6 peer
======================

display bgp vpnv6 peer

Function
--------



The **display bgp vpnv6 peer** command is used to display the information of the BGP VPNv6 peer.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *bgpName* ] **vpnv6** **all** **peer**

**display bgp** [ **instance** *bgpName* ] **vpnv6** **vpn-instance** *vpn-instance-name* **peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies the BGP multi-instance name. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Display all information on VPNv6 routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display bgp vpnv6 peer** command is used to display the information of the BGP VPNv6 peer.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about VPNv6 peers.
```
<HUAWEI> display bgp vpnv6 all peer
BGP local router ID : 10.1.1.1
 Local AS number : 100
 Total number of peers : 2                 Peers in established state : 2

  Peer              V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv

  10.2.2.2          4   100      210      220     0   02:42:55     Established    1

  Peer of IPv6-family for vpn instance :

  VPN-Instance vpn1 :
  2001:DB8:2000::2  4   65410    205      178     0   02:42:53     Established    0

```

**Table 1** Description of the **display bgp vpnv6 peer** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the BGP local device.  If two ends have the same BGP local router ID, no BGP peer relationship can be established between them. In this situation, run the router id command in the BGP view on either end to change the BGP local router ID. Changing it to the IP address of a loopback interface is recommended. |
| Local AS number | Local AS number. |
| AS | Autonomous system number. |
| Total number of peers | Number of BGP peers. |
| Peers in established state | Number of BGP peers in the Established state. |
| Peer | Peer IP address. |
| V | BGP version. |
| MsgRcvd | BGP version of a peer. |
| MsgSent | Number of messages sent. |
| OutQ | Number of messages waiting to be sent to a specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Status of the peer:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection request initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes sent from the peer. |