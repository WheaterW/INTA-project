Creating a Sub-interface
========================

To ensure communication between VLANs, create Ethernet sub-interfaces on a Layer 3 device.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   An Ethernet sub-interface is created. If an Ethernet sub-interface already exists, the Ethernet sub-interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Sub-interfaces cannot be created on an Eth-Trunk member interface.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the scenario where an interface has a large number of sub-interfaces, if you run the [**shutdown**](cmdqueryname=shutdown) command in the sub-interface view to shut down the sub-interfaces one after another, the work load is huge. In this case, you can shut down the sub-interfaces in batches by running the [**shutdown interface**](cmdqueryname=shutdown+interface) command in the system view.