Adding an Interface to an MSTP Process - Access Links
=====================================================

The links connecting Multiple Spanning Tree Protocol (MSTP) devices and access rings are called access links. After being added to MSTP processes, interfaces on the access links can participate in MSTP calculation.

#### Context

Do as follows on the devices connected to access rings:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   The interface specified in this command must be an interface that connects a device to an accessing ring.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp binding process**](cmdqueryname=stp+binding+process) *process-id*
   
   
   
   The current interface is added to the MSTP process.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.