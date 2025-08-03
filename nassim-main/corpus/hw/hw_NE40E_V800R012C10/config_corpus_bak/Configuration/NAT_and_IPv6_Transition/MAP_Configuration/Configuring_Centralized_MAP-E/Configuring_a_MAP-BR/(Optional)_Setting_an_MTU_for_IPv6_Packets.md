(Optional) Setting an MTU for IPv6 Packets
==========================================

This section describes how to set a maximum transmission unit. Whether to fragment translated packets depends on the smaller value between the MTU configured in an instance and the interface MTU. To customize the MTU value of the IPv6 packets in a MAP instance, set the MTU value in the MAP instance.

#### Context

* If the size of packets is greater than the configured MTU value, the packets are broken into a great number of fragments.
* If the MTU is set too large, packets may be transmitted at a low speed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**map-e instance**](cmdqueryname=map-e+instance) *map-e-instance-name* [ **id** *id* ]
   
   
   
   The MAP-E instance view is displayed.
3. Run [**map mtu**](cmdqueryname=map+mtu) *mtu-value*
   
   
   
   An MTU value is set for IPv6 packets in a MAP instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.