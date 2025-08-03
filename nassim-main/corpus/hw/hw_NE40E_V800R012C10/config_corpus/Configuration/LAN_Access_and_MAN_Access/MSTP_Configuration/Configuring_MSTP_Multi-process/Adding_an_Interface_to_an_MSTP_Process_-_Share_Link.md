Adding an Interface to an MSTP Process - Share Link
===================================================

The link shared by multiple access rings is called a share link. The interfaces on the share link need to participate in Multiple Spanning Tree Protocol (MSTP) calculation in multiple access rings in different MSTP processes. After being added to MSTP processes, interfaces on the access links can participate in MSTP calculation.

#### Context

Do as follows on the devices connected to access rings:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   The interface specified in this command must be an interface on the share link between the devices configured with MSTP multi-process, not an interface that connects a device to an access ring.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp binding process**](cmdqueryname=stp+binding+process) *process-id1* [ **to** *process-id2* ] **link-share**
   
   
   
   The interface is added to multiple MSTP processes to complete MSTP calculation.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For a process with share links, you must run the [**stp enable**](cmdqueryname=stp+enable) command globally. For an interface that is added to the process in link-share mode, you must run the [**stp enable**](cmdqueryname=stp+enable) command in the interface view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.