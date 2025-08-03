Operating Modes of NTP
======================

Operating Modes of NTP

#### Overview

[Table 1](#EN-US_CONCEPT_0000001563755697__table7322201312131) lists the operating modes of NTP.

**Table 1** Operating modes of NTP
| Operating Mode | Description | Usage Scenario |
| --- | --- | --- |
| Client/Server mode | The client synchronizes its clock with the clock on the server. | In this mode, the server and client run at a high stratum level on the synchronization subnet. In this mode, the IP address of the server needs to be obtained in advance. |
| Peer mode | The symmetric active peer and symmetric passive peer can synchronize with each other. The peer with a lower stratum level (larger stratum value) is synchronized with the peer with a higher stratum level (smaller stratum value). | In this mode, the host runs at a relatively low stratum level on the synchronization subnet. |
| Broadcast mode | The server periodically sends clock synchronization packets to a broadcast address. | This mode applies to high-speed networks that have numerous workstations but lower requirements on synchronization accuracy. In typical scenarios, one or more time servers periodically send broadcast packets to workstations, which then determine the time based on a millisecond-level delay. |
| Multicast mode | The server periodically sends clock synchronization packets to a multicast address. | This mode applies to scenarios where a large number of clients are distributed on the network. In this mode, the NTP server multicasts an NTP packet to all clients, thereby lowering the number of NTP packets sent on the network. |
| Manycast mode | Manycast servers continuously listen for request packets that manycast clients periodically send to a multicast address in search of a server with the fewest number of hops. | This mode applies to scenarios where multiple servers are sparsely distributed on the network. Clients can discover and synchronize with the closest manycast server. This mode applies to networks where servers are not stable and clients do not need to be reconfigured if a server fails. |



#### Client/Server Mode

[Figure 1](#EN-US_CONCEPT_0000001563755697__fig_dc_fd_ntp_000601) shows the packet exchange process in client/server mode. The client synchronizes its clock with the clock on the server. The server provides synchronization information for the client but does not alter its own clock. In client/server mode, the server is also called a unicast server to distinguish it from the broadcast server, multicast server, and manycast server in other modes.

**Figure 1** Client/Server mode  
![](figure/en-us_image_0000001512676254.png)

The packet exchange process in client/server mode is as follows:

1. The client periodically sends packets to the server. The value of the Mode field in the packets is set to 3 (client mode). A client will not verify the reachability and stratum of the server.
2. After receiving the request packet, the server sends a response packet in which the Mode field is set to 4 (server mode). The server fills in the required information to the response packet before sending it to the client. The server does not need to retain any status information.
3. After receiving the response packet, the client performs the clock filter and selection procedure and then synchronizes its clock to the server that provides the optimal clock.

#### Peer Mode

[Figure 2](#EN-US_CONCEPT_0000001563755697__fig_dc_fd_ntp_000602) shows the packet exchange process in peer mode.

**Figure 2** Peer mode  
![](figure/en-us_image_0000001513035398.png)

The packet exchange process in peer mode is as follows:

1. The symmetric active peer sends an NTP request packet to the symmetric passive peer, with the Mode field being 3 (client mode). The symmetric passive peer replies with an NTP response packet, in which the Mode field is set to 4 (server mode).
2. The active peer periodically sends packets to the passive peer. The value of the Mode field in a packet is set to 1, indicating that the packet is sent by the active peer. Whether the peer is reachable and the number of layers of the peer are not considered.
3. After receiving the request packet, the symmetric passive peer sends a response packet in which the Mode field is set to 2 (symmetric passive peer). The symmetric passive peer does not need to be configured. A host establishes a connection and sets relevant state variables only after an NTP packet is received.
4. After the peer relationship is set up, the symmetric active and passive peers can synchronize with each other. The peer with a lower stratum level (larger stratum value) is synchronized with the peer with a higher stratum level (smaller stratum value).

#### Broadcast Mode

[Figure 3](#EN-US_CONCEPT_0000001563755697__fig_dc_fd_ntp_000603) shows the packet exchange process in broadcast mode. In this mode, servers typically run high-speed broadcast media over the network. They provide synchronization information to all clients, but do not alter their own clocks.

**Figure 3** Broadcast mode  
![](figure/en-us_image_0000001513035402.png)

The packet exchange process in broadcast mode is as follows:

1. The broadcast server periodically sends clock synchronization packets to the broadcast address 255.255.255.255. The Mode field in the packets is set to 5 (broadcast mode or multicast mode), regardless of whether the client is reachable or the number of layers.
2. The client listens for the broadcast packets sent from the server. After receiving the first broadcast packet, the client temporarily starts in client/server mode to exchange packets with the server. This allows the client to estimate the network delay.
3. The client then enters the broadcast mode, continues to listen for the subsequent broadcast packets, and synchronizes the local clock according to the subsequent broadcast packets.

#### Multicast Mode

[Figure 4](#EN-US_CONCEPT_0000001563755697__fig_dc_fd_ntp_000604) shows the packet exchange process in multicast mode. In this mode, servers typically run high-speed broadcast media over the network. They provide synchronization information to all clients, but do not alter their own clocks.

**Figure 4** Multicast mode  
![](figure/en-us_image_0000001563755741.png)

The packet exchange process in multicast mode is as follows:

1. The multicast server periodically sends clock synchronization packets to an IPv4 or IPv6 multicast address. The Mode field in the packets is set to 5 (broadcast or multicast mode).
2. The client listens for the multicast packets sent from the server. After receiving the first multicast packet, the client temporarily starts in client/server mode to exchange packets with the server. This allows the client to estimate the network delay.
3. The client then enters the multicast mode, continues to listen for the subsequent multicast packets, and synchronizes the local clock according to the subsequent multicast packets.

#### Manycast Mode

[Figure 5](#EN-US_CONCEPT_0000001563755697__fig_dc_fd_ntp_000605) shows the packet exchange process in manycast mode. In this mode, servers provide synchronization information to all clients and do not alter their own clocks.

**Figure 5** Manycast mode  
![](figure/en-us_image_0000001564115473.png)

The packet exchange process in manycast mode is as follows:

1. The manycast client periodically sends request packets to an IPv4 or IPv6 multicast address to search for the closest manycast server (smallest TTL). The value of the Mode field is set to 3 (client mode).
   
   The initial TTL value of a request packet sent by the client is 1. The value increases by 1 each time a request packet is sent until either the client receives a response packet or the TTL value reaches the upper limit. Receipt of a response packet indicates that the client has found the closest manycast server. To subsequently maintain the connection with this server, the client sends a packet every time a timeout period expires. If the client does not receive a response packet when the TTL reaches the upper limit, the client stops sending request packets for a certain period of time (a timeout period). This timeout period allows all connections to be cleared. After the timeout period expires, the client repeats the preceding process.
2. The manycast server continuously listens for packets. If server synchronization is possible, the server unicasts a response packet to the client, with the Mode field set to 4 (server mode).
3. After receiving the response packet, the client performs the clock filter and selection procedure and then synchronizes its clock to the server that provides the optimal clock.