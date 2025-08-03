Enabling PIM-DM
===============

This section describes how to enable PIM-DM. On a PIM-DM network, PIM-DM must be enabled on interfaces for the Router to set up PIM neighbor relationships with neighboring devices to process data from them.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

PIM-DM and PIM-SM cannot be enabled on the same interface. The PIM modes of Router interfaces that belong to the same instance must be the same. When a Router is deployed in a PIM-DM domain, it is advised to enable PIM-DM on all non-boundary interfaces.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast routing-enable**](cmdqueryname=multicast+routing-enable)
   
   
   
   IP multicast routing is enabled for the public network instance.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**pim dm**](cmdqueryname=pim+dm)
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If you run the [**undo pim dm**](cmdqueryname=undo+pim+dm) command, PIM neighbor and protocol status information on the interface will be removed. This operation adversely affects the multicast service currently running on the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.