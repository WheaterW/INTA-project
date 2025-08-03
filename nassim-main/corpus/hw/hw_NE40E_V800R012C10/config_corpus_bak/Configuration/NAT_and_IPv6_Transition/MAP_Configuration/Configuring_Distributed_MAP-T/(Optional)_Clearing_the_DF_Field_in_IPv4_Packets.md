(Optional) Clearing the DF Field in IPv4 Packets
================================================

The default implementation is as follows. Before a device translates an IPv6 packet into an IPv4 packet, if the IPv6 packet does not carry the fragment extension header and the packet length is less than or equal to 1280 bytes, the DF field in the IPv4 packet is set to 0 (can be fragmented). If the IPv6 packet does not carry the fragment extension header and the packet length is greater than 1280 bytes, the DF field in the IPv4 packet is set to 1 (cannot be fragmented). If the IPv6 packet carries the fragment extension header, the DF field in the IPv4 packet is set to 0 (can be fragmented). After the DF field clearing function is enabled, the device sets the DF field in IPv4 packets to 0.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-t instance**](cmdqueryname=map-t+instance) *map-t-instance-name* [ **id** *id* ]
   
   
   
   The MAP-T instance view is displayed.
3. Run [**map ipv6 df-override enable**](cmdqueryname=map+ipv6+df-override+enable)
   
   
   
   The device is enabled to set the DF field to 0 for IPv4 packets after IPv6 packets are converted to IPv4 packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.