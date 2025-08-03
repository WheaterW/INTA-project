(Optional) Setting the Traffic Class of IPv6 Packets
====================================================

When an IPv4 packet is translated into an IPv6 packet, the Traffic-Class field value in the IPv6 packet is copied from the ToS field in the IPv4 packet. To modify the traffic class of IPv6 packets, set the traffic class value of IPv6 packets in an instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**map traffic-class**](cmdqueryname=map+traffic-class) *class-value*
   
   
   
   The Traffic-Class field is set for public network-to-private network IPv6 traffic.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.