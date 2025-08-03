Setting a Minimum TTL Value for IPv6 Multicast Packets
======================================================

Multicast data for each multicast group on an IPv6 network needs to be transmitted in a certain range. You can control the IPv6 multicast forwarding range by setting a minimum TTL value for IPv6 multicast packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The IPv6 PIM interface view is displayed.
3. Run [**multicast ipv6 minimum-ttl**](cmdqueryname=multicast+ipv6+minimum-ttl) *ttl-value*
   
   
   
   A minimum TTL value is set for IPv6 multicast packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display multicast ipv6 minimum-ttl**](cmdqueryname=display+multicast+ipv6+minimum-ttl) [ *interface-type* *interface-number* ] command to check the set minimum TTL value of IPv6 multicast packets that an interface is allowed to send.