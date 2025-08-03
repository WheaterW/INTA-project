(Optional) Configuring Other Parameters of an IPv4 over IPv6 Tunnel
===================================================================

This section describes how to configure an IPv6 packet header for an IPv4 packet so that the packet can be transmitted over an IPv4 over IPv6 tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration in the tunnel interface view is similar to that in the system view, and therefore is not described here.
   
   The configurations in the system view take effect for all IPv4 over IPv6 tunnels configured on a node. The configurations in the tunnel interface view take effect only for the current tunnel interface and override the configurations in the system view.
2. Run [**tunnel ipv4-ipv6 encapsulation-limit**](cmdqueryname=tunnel+ipv4-ipv6+encapsulation-limit) *encapsulation-limit*
   
   
   
   The maximum number of IPv6 encapsulations that can be performed on embedded tunnel nodes is configured.
3. Run [**tunnel ipv4-ipv6 flow-label**](cmdqueryname=tunnel+ipv4-ipv6+flow-label) *label-value*
   
   
   
   A flow label value is set for the IPv4 over IPv6 tunnel so that the device can recognize and provide special handling of packets in a specified flow.
4. Run [**tunnel ipv4-ipv6 hop-limit**](cmdqueryname=tunnel+ipv4-ipv6+hop-limit) *hop-limit*
   
   
   
   The maximum number of hops along the IPv4 over IPv6 tunnel is configured so that packet transmission can be terminated when routing loops occur on the tunnel.
5. Run [**tunnel ipv4-ipv6 traffic-class**](cmdqueryname=tunnel+ipv4-ipv6+traffic-class) { **original** | *class-value* }
   
   
   
   A traffic class value of the IPv4 over IPv6 tunnel is set.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.