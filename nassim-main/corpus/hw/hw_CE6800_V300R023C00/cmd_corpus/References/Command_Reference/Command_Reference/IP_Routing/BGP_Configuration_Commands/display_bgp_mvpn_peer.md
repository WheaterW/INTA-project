display bgp mvpn peer
=====================

display bgp mvpn peer

Function
--------



The **display bgp mvpn peer** command displays information about MVPN BGP peers.

The **display bgp mvpn slow-peer** command displays information about slow MVPN BGP peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp mvpn all peer**

**display bgp mvpn slow-peer**


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

The **display bgp mvpn peer** command displays BGP MVPN peer information. You can implement the following operations based on the command output:

* To check the status of BGP connections
* To check information about a BGP peer
* To check whether a BGP peer is configured using the **peer as-number** command
* To check whether a BGP peer is deleted using the **undo peer as-number** commandThe **display bgp mvpn peer** command can be used for troubleshooting, with details as follows: If BGP peers are disconnected, specify log-info in the command to check the log information of the specified peer. In the command output, Date/Time indicates the time when the peers were disconnected, and Error Code and Error Subcode indicate the cause of the disconnection.To check information about slow MVPN BGP peers, run the display mvpn bgp slow-peer command. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited from the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit from the slow peer state.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about peers in the BGP-MVPN address family.
```
<HUAWEI> display bgp mvpn all peer
BGP local router ID : 2.2.2.2
 Local AS number : 100
 Total number of peers : 2                 Peers in established state : 2

  Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv

  3.3.3.3         4         100      482      484     0 07:58:05 Established       1
  4.4.4.4         4         100      439      439     0 07:13:16 Established       3

```

**Table 1** Description of the **display bgp mvpn peer** command output
| Item | Description |
| --- | --- |
| BGP local router ID | ID of the BGP local router. If two ends have the same BGP local router ID, no BGP peer relationship can be established between them. In this situation, run the router id command in the BGP view on either end to change the BGP local router ID. Changing it to the IP address of a loopback interface is recommended. |
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
| State | Status of the peer:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP. Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection request initiated by the remote BGP peer, and changes its state to Connect. * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations.   + If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent.   + If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active.   + If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP.   + If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent.   + If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect.   + If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer.   + If there are no errors in the Open message received, BGP changes its state to OpenConfirm.   + If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle.   + If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message.   + If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle.   + If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages.If BGP receives an Update or a Keepalive message, its state stays in Established.If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes sent from the peer. |