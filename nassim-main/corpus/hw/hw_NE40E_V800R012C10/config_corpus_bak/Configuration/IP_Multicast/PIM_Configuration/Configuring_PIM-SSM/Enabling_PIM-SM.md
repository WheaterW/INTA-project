Enabling PIM-SM
===============

To enable a Router interface to establish PIM neighbor relationships with other Routers, enable PIM-SM.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**pim sm**](cmdqueryname=pim+sm)
   
   
   
   PIM-SM is enabled.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Running the [**undo pim sm**](cmdqueryname=undo+pim+sm) command will delete PIM neighbor relationships on the interface and interrupt the multicast service running on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.