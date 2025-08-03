display bgp evpn peer
=====================

display bgp evpn peer

Function
--------



The **display bgp evpn slow-peer** command displays information about slow BGP EVPN peers.

The **display bgp evpn peer** command displays information about BGP EVPN peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp** [ **instance** *instance-name* ] **evpn** **peer**

**display bgp** [ **instance** *instance-name* ] **evpn** **slow-peer**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Displays the information about BGP EVPN peers of a specified BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check the following information about BGP EVPN peers, run the **display bgp evpn peer** command:

* Status of connections between BGP EVPN peers
* Configuration information about BGP EVPN peers
* Whether BGP EVPN peers are successfully configured using the **peer enable** command
* Whether BGP EVPN peers are successfully deleted using the **undo peer enable** commandTo check information about slow BGP EVPN peers, run the display bgp evpn slow-peer command. The information includes the time when a peer began to be identified as a slow peer, the time when a peer last exited from the slow peer state, the number of times a peer has been identified as a slow peer, and the remaining time for a peer to exit from the slow peer state.

**Precautions**



When dynamic BGP EVPN peer relationships are being established or disconnected, statistics about the BGP EVPN peers may be inconsistent with the actual number of BGP EVPN peers. Therefore, you are advised to query statistics after the BGP EVPN peer status is stable.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about slow BGP EVPN peers.
```
<HUAWEI> display bgp evpn slow-peer
Total number of peers : 2                 
 Switchback detection timer: Remaining 3581 Second(s)
 Peer                             LastSlowEndTime              SlowStartTime                SlowCount 
 10.1.1.1                          2016-04-10 20:41:33+00:00    2016-04-12 00:02:33+00:00    3 
 10.2.2.1                          2016-04-11 23:02:40+00:00    2016-04-12 00:02:40+00:00    5

```

# display information about BGP peers.
```
<HUAWEI> display bgp evpn peer
BGP local router ID        : 10.3.3.3
 Local AS number            : 100
 Total number of peers      : 3
 Peers in established state : 3

  Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
  10.1.1.1                          4         100     4456     3196     0 0045h29m Established        5
  10.2.2.2                          4         100     4447     3202     0 0045h29m Established        5
  10.4.4.4                          4         100     4452     3206     0 0045h29m Established        4

```

**Table 1** Description of the **display bgp evpn peer** command output
| Item | Description |
| --- | --- |
| Total number of peers | Number of peers. |
| Switchback detection timer | Remaining time for a peer to exit from the slow peer state. |
| Peer | Peer IP address. |
| LastSlowEndTime | Time when a peer last exited from the slow peer state. |
| SlowStartTime | Time when a peer began to be identified as a slow peer. |
| SlowCount | Number of times a peer has been identified as a slow peer. |
| BGP local router ID | Local BGP EVPN router ID. |
| Local AS number | Local AS number. |
| AS | Autonomous system number. |
| Peers in established state | Number of peers in the Established state. |
| V | BGP version. |
| MsgRcvd | BGP version of a peer. |
| MsgSent | Number of messages sent. |
| OutQ | Number of messages waiting to be sent to a specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Current BGP EVPN status:   * Idle: BGP EVPN denies any connection request. This is the initial state of BGP EVPN.   After BGP EVPN receives a start event, BGP EVPN initiates a TCP connection to a peer, starts the ConnectRetry timer, and listens to the TCP messages from the peer. BGP EVPN then enters the Connect state.   * Connect: BGP EVPN is waiting for the TCP connection establishment to complete before performing further actions.   If the TCP connection is successfully established, BGP EVPN stops the ConnectRetry timer and sends an Open message to the peer. BGP EVPN then enters the Opensent state.  If the TCP connection fails to be established, BGP EVPN resets the ConnectRetry timer and listens to the TCP connection initiated by the peer. BGP EVPN then enters the Active state.  If the ConnectRetry timer expires, BGP EVPN restarts the ConnectRetry timer and attempts to establish a TCP connection with the peer again. At this time, BGP EVPN remains in the Connect state.   * Active: BGP EVPN attempts to establish a TCP connection. This is the intermediate state of BGP EVPN.   If the TCP connection is successfully established, BGP EVPN resets the ConnectRetry timer and sends an Open message to the peer. BGP EVPN then enters the Opensent state.  If the ConnectRetry timer expires, BGP EVPN restarts the ConnectRetry timer and enters the Connect state.  If BGP EVPN attempts to establish a TCP connection with an unknown IP address but fails, BGP EVPN resets the ConnectRetry timer and remains in the Active state.   * OpenSent: BGP EVPN has sent an Open message to the peer and is now waiting for an Open message from the peer.   If BGP EVPN receives a correct Open message, BGP EVPN enters the OpenConfirm state.  If BGP EVPN receives an incorrect Open message, BGP EVPN sends a Notification message to the peer and enters the Idle state.  If BGP EVPN receives a TCP connection teardown message, BGP EVPN resets the ConnectRetry timer and listens to the TCP connection initiated by the peer. BGP EVPN then enters the Active state.   * OpenConfirm: BGP EVPN is waiting for a Notification or Keepalive message.   If BGP EVPN receives a Notification or TCP connection teardown message, BGP EVPN enters the Idle state.  If BGP EVPN receives a Keepalive message, BGP EVPN enters the Established state.   * Established: Peers can exchange Update, Notification, and Keepalive messages.   If BGP EVPN receives an Update or Keepalive message, BGP EVPN remains in the Established state.  If BGP EVPN receives a Notification message, BGP EVPN enters the Idle state.   * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes sent from the peer. |