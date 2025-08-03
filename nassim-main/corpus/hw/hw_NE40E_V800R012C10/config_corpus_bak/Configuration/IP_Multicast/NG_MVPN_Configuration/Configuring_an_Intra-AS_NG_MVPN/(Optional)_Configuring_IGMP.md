(Optional) Configuring IGMP
===========================

Configuring IGMP on the interfaces connecting a multicast device to a user network segment allows the device to manage multicast group members on the network segment.

#### Context

In the TCP/IP protocol suite, Internet Group Management Protocol (IGMP) manages IPv4 multicast group members. It sets up and maintains multicast group member relationships between IP hosts and neighboring multicast routers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   *interface-type* *interface-number* specifies the interface connecting to a user host.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
4. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Configure an IGMP version, create a static multicast group, or specify the multicast groups to which interfaces are allowed to be added. For details, see IGMP Configuration.