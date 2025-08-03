display bgp unnumbered peer
===========================

display bgp unnumbered peer

Function
--------



The **display bgp unnumbered peer** command displays information about BGP unnumbered peers.




Format
------

**display bgp unnumbered peer**


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



To check information about BGP unnumbered peers, run the **display bgp unnumbered peer** command.



**Precautions**



When dynamic BGP peer relationships are being established or disconnected, statistics about the BGP peers may be inconsistent with the actual number of BGP peers. Therefore, you are advised to query statistics after the BGP peer status is stable.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP unnumbered peer information.
```
<HUAWEI> display bgp unnumbered peer
 BGP local router ID        : 10.4.4.4
 Local AS number            : 100
 Total number of peers      : 2
 Peers in established state : 2

  Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv       Interface
  FE80::3A9C:B2FF:FE21:300         4         100      294      297     0 04:12:09 Established        0         100GE1/0/8
  FE80::3A9C:B2FF:FE21:301         4         200     1699     1709     0 24:34:46 Established        0         100GE1/0/1

```

**Table 1** Description of the **display bgp unnumbered peer** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the BGP local device.  If two ends have the same BGP local router ID, no BGP peer relationship can be established between them. In this situation, run the router id command in the BGP view on either end to change the BGP local router ID. Changing it to the IP address of a loopback interface is recommended. |
| Local AS number | Local AS number. |
| AS | AS number. |
| Total number of peers | Total number of BGP peers. |
| Peers in established state | Number of BGP peers in Established state. |
| Peer | IP address of the peer. |
| V | BGP version used on the peer. |
| MsgRcvd | Number of received messages. |
| MsgSent | Number of sent messages. |
| OutQ | Message to be sent to the specified peer. |
| Up/Down | Duration of the BGP session staying in the current state.   * If the duration is less than 24 hours, it is displayed in the format of xx:xx:xx, indicating xx hours, xx minutes, and xx seconds. * If the duration is greater than 24 hours, it is displayed in the format of xxxxhxxm, indicating xxxx hours and xx minutes. If the duration exceeds 9999 hours, it is displayed in the format of \*\*\*\*hxxm. |
| State | Status of the peer:   * Idle: indicates that BGP denies any request of entering. This is the initiatory status of BGP.   Upon receiving a Start event, BGP initiates a TCP connection request to the remote BGP peer, starts the ConnectRetry Timer with the initial value, listens for a TCP connection request initiated by the remote BGP peer, and changes its state to Connect.   * Connect: indicates that BGP is waiting for the TCP connection to be set up before it determines whether to perform other operations. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value, initiates a TCP connection request to the remote BGP peer, and stays in the Connect state. * Active: indicates that BGP tries to set up a TCP connection. This is the intermediate status of BGP. * If the TCP connection succeeds, BGP stops the ConnectRetry Timer, sends an Open message to the remote peer, and changes its state to OpenSent. * If the ConnectRetry Timer has expired before a TCP connection is established, BGP restarts the timer with the initial value and changes its state to Connect. * If BGP initiates a TCP connection request with an unknown IP address, the TCP connection fails. When this occurs, BGP restarts the ConnectRetry Timer with the initial value and stays in the Active state. * OpenSent: indicates that BGP has sent one Open message to its peer and is waiting for the other Open message from the peer. * If there are no errors in the Open message received, BGP changes its state to OpenConfirm. * If there are errors in the Open message received, BGP sends a Notification message to the remote peer and changes its state to Idle. * If the TCP connection fails, BGP restarts the ConnectRetry Timer with the initial value, continues to listen for a TCP connection request initiated by the remote peer, and changes its state to Active. * OpenConfirm: indicates that BGP is waiting for a Notification or Keepalive message. * If BGP receives a Notification message, or the TCP connection fails, BGP changes its state to Idle. * If BGP receives a Keepalive message, BGP changes its state to Established. * Established: indicates that BGP peers can exchange Update, Notification, and Keepalive messages. * If BGP receives an Update or a Keepalive message, its state stays in Established. * If BGP receives a Notification message, BGP changes its state to Idle. * No neg: The address family is not enabled for the BGP peer. In this state, Update messages can be exchanged in other address families whose capabilities have been successfully negotiated. If the address family is enabled for the BGP peer, the local BGP peer receives a Notification message, and the peer relationship is disconnected. Then, the BGP peer changes to the Idle state and re-establishes the peer relationship. |
| PrefRcv | Number of route prefixes sent from the peer. |
| Interface | Unnumbered interface. |