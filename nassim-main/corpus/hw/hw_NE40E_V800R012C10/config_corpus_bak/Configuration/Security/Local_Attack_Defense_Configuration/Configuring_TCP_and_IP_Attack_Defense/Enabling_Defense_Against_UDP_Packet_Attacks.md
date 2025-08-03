Enabling Defense Against UDP Packet Attacks
===========================================

With defense against UDP packet attacks, the Router can identify packets in Fraggle attacks and attack packets on UDP diagnosis ports according to the destination port of the received UDP packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Perform either of the following operations as required:
   * Run the [**udp-packet-defend enable**](cmdqueryname=udp-packet-defend+enable) command to enable defense against IPv4 UDP packet attacks.
   * Run the [**ipv6-udp-packet-defend enable**](cmdqueryname=ipv6-udp-packet-defend+enable) command to enable defense against IPv6 UDP packet attacks.
   
   
   
   Defense against UDP packet attacks protects the Router against Fraggle attacks and UDP diagnosis port attacks. UDP packets with the destination port number being 7, 13, or 19 are regarded as malformed packets and directly discarded by the Router.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.