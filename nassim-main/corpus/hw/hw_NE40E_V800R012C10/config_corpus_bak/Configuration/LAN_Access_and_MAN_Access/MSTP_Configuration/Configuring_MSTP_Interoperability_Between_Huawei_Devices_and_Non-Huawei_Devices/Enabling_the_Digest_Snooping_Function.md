Enabling the Digest Snooping Function
=====================================

When a Huawei device is connected to a non-Huawei device, if the region names, revision numbers, and VLAN-to-instance mappings configured on the two devices are consistent but the Bridge Protocol Data Unit (BPDU) keys are different, the two devices cannot communicate. To address this problem, enable the digest snooping function on the Huawei device.

#### Context

Do as follows on a device in a Multiple Spanning Tree (MST) region:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in spanning tree protocol calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. (Optional) Run [**stp binding process**](cmdqueryname=stp+binding+process) *process-id*
   
   
   
   The interface is bound to an MSTP process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step is performed only when the interface needs to be bound to an MSTP process with a non-zero ID. If the interface belongs to process 0, skip this step.
4. Run [**stp config-digest-snoop**](cmdqueryname=stp+config-digest-snoop)
   
   
   
   The digest snooping function is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.