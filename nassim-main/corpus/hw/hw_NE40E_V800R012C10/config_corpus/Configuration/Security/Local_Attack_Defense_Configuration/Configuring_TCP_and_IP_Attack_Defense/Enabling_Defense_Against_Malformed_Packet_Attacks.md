Enabling Defense Against Malformed Packet Attacks
=================================================

With defense against malformed packet attacks, the Router checks the validity of received packets and filters out illegal packets, thus defending the CPU against attacks of IP packets with null load, null IGMP packets, LAND attack packets, Smurf attack packets, and packets with invalid TCP flag bits.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Perform either of the following operations as required:
   * Run the [**abnormal-packet-defend enable**](cmdqueryname=abnormal-packet-defend+enable) command to enable defense against IPv4 malformed packet attacks.
   * Run the [**ipv6-abnormal-packet-defend enable**](cmdqueryname=ipv6-abnormal-packet-defend+enable) command to enable defense against IPv6 malformed packet attacks.
   
   
   
   Defense against IPv4 malformed packet attacks can defend against attacks of various malformed packets, including IP packets with null load, null IGMP packets, LAND attack packets, Smurf attack packets, and packets with invalid TCP flag bits.
   
   Defense against IPv6 malformed packet attacks can defend against attacks of various malformed packets, including LAND attack packets, and packets with invalid TCP flag bits.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.