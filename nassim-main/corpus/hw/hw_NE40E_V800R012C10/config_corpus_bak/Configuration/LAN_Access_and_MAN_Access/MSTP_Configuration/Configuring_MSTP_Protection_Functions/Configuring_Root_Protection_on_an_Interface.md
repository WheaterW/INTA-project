Configuring Root Protection on an Interface
===========================================

The root protection function on a device protects a root bridge by preserving the role of a designated port.

#### Context

Due to incorrect configurations or malicious attacks on the network, a root bridge may receive Bridge Protocol Data Units (BPDUs) with a higher priority. Consequently, the legitimate root bridge is no longer able to serve as the root bridge, and the network topology is illegitimately changed, triggering spanning tree recalculation. This also may cause the traffic that should be transmitted over high-speed links to be transmitted over low-speed links, leading to network congestion. The root protection function on a device is used to protect the root bridge by preserving the role of the designated port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Root protection is configured on a designated port. It takes effect only when being configured on the port that functions as a designated port on all Multiple Spanning Tree Instances (MSTIs). If root protection is configured on other types of ports, it does not take effect.

Do as follows on a root bridge in a Multiple Spanning Tree (MST) region:


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
4. Run [**stp root-protection**](cmdqueryname=stp+root-protection)
   
   
   
   Root protection is configured on the device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.