(Optional) Setting an IPv4 ToS Value
====================================

When an IPv6 packet is translated into an IPv4 packet, the ToS value in the IPv4 packet is copied from the Traffic-Class field in the IPv6 packet by default. To change the ToS value in the IPv4 packet, set the ToS value of the IPv4 packet in an instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-t instance**](cmdqueryname=map-t+instance) *map-t-instance-name* [ **id** *id* ]
   
   
   
   The MAP-T instance view is displayed.
3. Run [**map ipv4-tos**](cmdqueryname=map+ipv4-tos) *tos-value*
   
   
   
   An IPv4 ToS value is set for IPv4 traffic after private network-to-public network IPv6 traffic is converted to IPv4 traffic.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.