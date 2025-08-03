Enabling IGMP
=============

To enable an interface to process user join requests, enable IGMP on the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo pim sm**](cmdqueryname=undo+pim+sm) command will delete PIM neighbor relationships on the interface and interrupt the multicast service running on the interface.
4. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.