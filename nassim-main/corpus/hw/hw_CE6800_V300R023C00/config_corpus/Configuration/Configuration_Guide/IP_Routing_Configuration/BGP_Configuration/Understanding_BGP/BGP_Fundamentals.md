BGP Fundamentals
================

BGP Fundamentals

#### BGP Characteristics

BGP has the following characteristics:

* Unlike an Interior Gateway Protocol (IGP), such as Open Shortest Path First (OSPF), BGP functioning as an Exterior Gateway Protocol (EGP) controls route advertisement and selects optimal routes between ASs, rather than discovering or calculating routes.
* BGP uses Transmission Control Protocol (TCP) as the transport layer protocol to improve reliability.
  
  + BGP selects optimal routes among inter-AS routes, which requires high stability on protocols. As such, TCP is used to enhance BGP due to its high reliability.
  + BGP peers must be logically connected, and TCP connections must be established between them. The destination port number is fixed at 179, while the local port number is a random value.
* BGP supports classless inter-domain routing (CIDR).
* During route update, BGP advertises only the changed routes, which greatly reduces bandwidth consumption. Therefore, BGP is suitable when a large number of routes are transmitted on the Internet.
* BGP is a distance-vector routing protocol.
* The design of BGP includes the capability to prevent routing loops.
  
  + Between ASs: BGP routes carry information about the full AS path (as specified in the AS\_Path attribute) that the routes have traversed. To prevent inter-AS loops, a device discards received routes that carry the local AS number.
  + Within an AS: BGP does not advertise the routes learned within an AS to BGP peers in the same AS, thereby preventing intra-AS loops.
* BGP uses various routing policies to filter and select routes flexibly.
* BGP provides a mechanism for preventing route flapping, improving Internet stability.
* BGP can be easily extended to adapt to network development.

#### BGP Operating Modes

BGP operates in either of the following modes:

* Internal BGP (IBGP)
* External BGP (EBGP)

When BGP runs within an AS, it is called IBGP; however, when it runs between ASs, it is called EBGP.


#### BGP Roles

* Speaker: device that sends BGP messages. The BGP speaker receives or generates new routing information, and advertises it to other BGP speakers. After receiving a route from another AS, the BGP speaker compares the route with its local routes. If the route is better than its local routes, or the route is new, the speaker advertises it to all its other remote BGP speakers except the one that has advertised the route.
* Peer: BGP speakers that exchange messages with each other are called peers.

#### BGP Messages

BGP runs by sending five types of messages: Open, Update, Notification, Keepalive, and Route-refresh.

* Open: first message sent after a TCP connection is set up. An Open message is used to set up a BGP peer relationship. After a peer receives the Open message and negotiation between the local device and peer succeeds, the peer sends a Keepalive message to confirm and maintain the peer relationship. Then, the peers can exchange Update, Notification, Keepalive, and Route-refresh messages.
* Update: This type of message is used to exchange routes between BGP peers. Update messages can be used as follows:
  
  + An Update message can be used to advertise multiple reachable routes that share the same set of attributes. These attributes are applicable to all destinations (expressed by IP prefixes) in the network layer reachability information (NLRI) field of the Update message.
  + An Update message can be used to withdraw multiple unreachable routes. Each route is identified by its destination (expressed by an IP prefix), and a list of IP prefixes carried in the Update message indicates the routes previously advertised by the local BGP speaker to the remote BGP speaker.
  + An Update message can be used to advertise reachable routes, withdraw unreachable routes, or advertise reachable routes and withdraw unreachable routes simultaneously. When an Update message is used only to withdraw routes, it does not need to carry path attributes or NLRI. When an Update message is used only to advertise reachable routes, it does not need to carry information about routes to be withdrawn.
* Notification: If error conditions are detected, BGP sends Notification messages to its peers. The BGP connections are then torn down immediately.
* Keepalive: BGP periodically sends Keepalive messages to peers to ensure the validity of BGP connections.
* Route-refresh: This type of message is used to request that BGP peers re-send all reachable routes to the local device.
  
  If all BGP devices are enabled with the route-refresh capability and an import routing policy changes, the local device sends Route-refresh messages to its peers. Upon receipt, the peers re-send their routing information to the local device. Route-refresh ensures that the local BGP routing table is dynamically updated and the new routing policy is used without tearing down BGP connections.

#### BGP Finite State Machine

The BGP finite state machine (FSM) has six states: Idle, Connect, Active, OpenSent, OpenConfirm, and Established, as shown in [Figure 1](#EN-US_CONCEPT_0000001130624148__fig_dc_feature_bgp_000401). Idle, Active, and Established are the three common states involved in BGP peer relationship establishment.

**Figure 1** BGP FSM  
![](figure/en-us_image_0000001176663767.png)

1. Idle is the initial state of BGP. In this state, BGP denies all connection requests from peers. BGP attempts to establish TCP connections with other BGP peers and enters the Connect state only after receiving a Start event from the local device.![](public_sys-resources/note_3.0-en-us.png) 
   * The Start event occurs when an operator configures a BGP process or resets an existing BGP process or when the device software resets a BGP process.
   * If an error event such as a Notification message or a TCP link disconnection notification is received in any state, BGP enters the Idle state.
2. In the Connect state, BGP starts the Connect Retry timer and waits for a TCP connection to be established:
   
   * If the TCP connection is established, BGP sends an Open message to the peer and transitions to the OpenSent state.
   * If the TCP connection fails to be established, BGP transitions to the Active state.
   * If BGP does not receive any response from the peer when the Connect Retry timer expires, BGP attempts to establish a TCP connection with this peer again and stays in the Connect state.
3. In the Active state, BGP keeps trying to establish a TCP connection with a peer:
   
   * If the TCP connection is established, BGP sends an Open message to the peer, terminates the Connect Retry timer, and transitions to the OpenSent state.
   * If the TCP connection fails to be established, BGP stays in the Active state.
   * If BGP does not receive any response from the peer when the Connect Retry timer expires, BGP transitions to the Connect state.
4. In the OpenSent state, BGP waits for an Open message from a peer. Upon receipt, BGP checks the validity of the Open message, including the AS number, version, and authentication password:
   
   * If the received Open message is valid, BGP sends a Keepalive message and transitions to the OpenConfirm state.
   * If the received Open message is invalid, BGP sends a Notification message to the peer and returns to the Idle state.
5. In the OpenConfirm state, the BGP device waits for a Keepalive or Notification message from a peer. If BGP receives a Keepalive message, it transitions to the Established state; however, if BGP receives a Notification message, it returns to the Idle state.
6. In the Established state, BGP can exchange Update, Keepalive, Route-refresh, and Notification messages with a peer:
   
   * If BGP receives a valid Update or Keepalive message, it considers that the peer is working properly and maintains the BGP connection with the peer.
   * If BGP receives an invalid Update or Keepalive message, it sends a Notification message to the peer and returns to the Idle state.
   * If BGP receives a Route-refresh message, it does not change its state.
   * If BGP receives a Notification message, it returns to the Idle state.
   * If BGP receives a TCP disconnect notification, it terminates the TCP connection with the peer and returns to the Idle state.

A BGP peer relationship can be established successfully only when both BGP peers are in the Established state. The BGP peers exchange routing information through Update messages.


#### BGP Processing

* After a BGP peer relationship is established, the BGP peers exchange information about their BGP routing tables with each other. BGP does not require a periodic update of its routing table. Instead, incremental Update messages are exchanged between peers to update their routing tables if BGP routes change.
* BGP sends Keepalive messages to maintain the BGP connection between peers.
* If BGP detects an error (for example, it receives an error message), BGP sends a Notification message to report the error, and the BGP connection is torn down accordingly.