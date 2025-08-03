(Optional) Configuring IGMP
===========================

Enable the Internet Group Management Protocol (IGMP) on a multicast device's interface that is connected to users, implementing multicast group member management on the local network.

#### Context

IGMP, a protocol in the TCP/IP protocol suite, manages IPv4 multicast group members. IGMP sets up and maintains multicast group member relationships between IP hosts and neighboring multicast routers directly connected to the hosts.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   *interface-type* *interface-number* specifies an interface connected to user hosts.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM is enabled.
4. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Configure an IGMP version, create a static multicast group, or specify the multicast groups to which interfaces are allowed to be added. For details, see IGMP Configuration.