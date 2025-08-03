Configuring Basic NTP Functions
===============================

This section describes how to configure basic NTP functions.

#### Usage Scenario

Select a proper mode based on the networking topology to meet various clock synchronization requirements.

In mode and peer mode, NTP packets can have the same source IP address.

[Table 1](#EN-US_TASK_0000001800928882__tab_dc_vrp_ntp_cfg_000301) shows the NTP operating modes that the NE40E supports.

**Table 1** NTP operating mode
| Operating Mode | Location and Synchronization Direction | Working Principle |
| --- | --- | --- |
| Client/server mode | Configure NTP only on the client. The server needs to be configured only with an NTP master clock and listening interfaces.  The client can be synchronized with the server but the server cannot be synchronized with the client. | 1. The client sends a synchronization request packet to the server, with the mode field set to 3. The value 3 indicates the client mode. 2. Upon receiving the request packet, the server automatically works in the server mode and sends a response packet with the mode field being set to 4. The value 4 indicates the server mode. 3. After receiving the response packet, the client performs clock filtering and selection, and finally, is synchronized with the optimal server. |
| Peer mode | Configure NTP only on the proactive peer end. The proactive peer end and passive peer end can be synchronized.  The end with a lower stratum (larger stratum number) is synchronized to the end with a higher stratum (smaller stratum number). | 1. The proactive peer end sends a synchronization request packet to the passive peer end with the mode field being set to 1. The value 1 indicates the proactive peer mode. 2. Upon receiving the request packet, the passive peer end automatically works in passive peer mode and sends a response packet with the mode field being set to 2. The value 2 indicates the passive peer mode. The passive peer end also forms a dynamic session with proactive peer end. |
| Broadcast mode | Configure NTP on both the server and the client.  The client can be synchronized with the server but the server cannot be synchronized with the client. | 1. The server periodically sends clock-synchronization packets to the broadcast address 255.255.255.255. 2. The client listens to the broadcast packets from the server. 3. After receiving the first broadcast packet, the client temporarily starts in the client/server mode to exchange packets with the server. This allows the client to estimate the network delay. 4. The client then reverts to the broadcast mode, continues to listen to the broadcast packets, and re-synchronizes the local clock according to the received broadcast packets. |
| Multicast mode | Configure NTP on both the server and the client.  The client can be synchronized with the server but the server cannot be synchronized with the client. | 1. The server periodically sends clock-synchronization packets to the configured multicast IP address. 2. The client listens to the multicast packets sent from the server. 3. After receiving the first multicast packet, the client temporarily starts in the client/server mode to exchange packets with the server. This allows the client to estimate the network delay. 4. The client then reverts to the multicast mode, continues to listen to the multicast packets, and re-synchronizes the local clock according to the received multicast packets. |
| Manycast mode | Configure NTP on both the server and the client.  The client can be synchronized with the server but the server cannot be synchronized with the client. | 1. A client operating in manycast mode periodically sends request packets to a designated IPv4/IPv6 multicast address in order to search for a minimum number of connections. The search process starts with a time to live (TTL) value of 1 and value increases in increments of 1 until the minimum number of connections are invoked or the TTL reaches its upper limit. If the TTL reaches its upper limit but the associations invoked by the client are still not enough, the client stops transmission for a timeout period to clear all connections, and then repeats the search process. If the minimum number of associations have been invoked, then the client starts transmitting one packet per timeout period to maintain the connections. 2. A designated manycast server within range of the TTL field in the packet header listens for packets with that address. If server synchronization is possible, the server will return a packet with the Mode field set to 4 using the unicast address of the client as the destination address. |



#### Pre-configuration Tasks

Before configuring basic NTP functions, complete the following tasks:

* Configure the link layer protocol for the interface.
* Configure an IP address and a routing protocol for the interface to ensure that NTP packets can reach destinations.


[Configuring the NTP Master Clock and Listening Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0005.html)

The master clock on the server must have a smaller stratum number (higher stratum) than that of the clock on the client. Otherwise, the clock on the client cannot synchronize with the master clock on the server. Perform the following steps on the server.

[Configuring Time Parameters for Synchronizing the Client Clock](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0035.html)

If the server clock changes or multiple NTP servers are available, you need to set clock synchronization parameters on the client clock, such as the interval and the maximum synchronization distance threshold for synchronizing the client clock. The client clock synchronizes with the clock source based on the configured clock synchronization parameters.

[(Optional) Configuring the Client/Server Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0006.html)

In client/server mode, the clock on the client synchronizes with the master clock on the server.

[(Optional) Configuring the Peer Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0007.html)

In peer mode, the two peers synchronize clocks with each other. One end can send the clock synchronization request message to the other and respond to the clock synchronization request message from the peer. 

[(Optional) Configuring the Broadcast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0008.html)

The NTP broadcast mode can be configured on a LAN to synchronize clocks on the LAN.

[(Optional) Configuring the Multicast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0009.html)

The NTP multicast mode can be configured to synchronize clocks in a multicast domain.

[(Optional) Configuring the Manycast Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0033.html)

The NTP manycast mode can be configured to synchronize clocks in a manycast domain.

[(Optional) Disabling the Interface From Receiving NTP Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0010.html)

To prevent a host on the LAN from synchronizing the clock on the specified server, you can disable the specified interface on the host from receiving NTP packets.

[(Optional) Setting the Port Number for Sending NTP Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0045.html)



[Enabling the NTP Service Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0042.html)

This section describes how to use NTP IPv4 or IPv6 services.

[Verifying the Configuration of Basic NTP Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ntp_cfg_0011.html)

After configuring basic NTP functions, check details about the configured and dynamic NTP sessions and the status of the NTP service.