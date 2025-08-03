(Optional) Configuring IGMP
===========================

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on the network segment.

#### Context

IGMP, a protocol in the TCP/IP protocol suite, manages IPv4 multicast group members. IGMP sets up and maintains multicast group member relationships between IP hosts and neighboring multicast routers directly connected to the hosts.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   The *interface-type* *interface-number* parameter specifies the interface connected to a user host.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.