Configuring Root Protection on a Port
=====================================

The root protection function on a device protects a root bridge by preserving the role of a designated port.

#### Context

Due to incorrect configurations or malicious attacks on the network, a root bridge may receive Bridge Protocol Data Units (BPDUs) with a higher priority. Consequently, the legitimate root bridge is no longer able to serve as the root bridge, and the network topology is incorrectly changed, triggering spanning tree recalculation. This also may cause the traffic that should be transmitted over high-speed links to be transmitted over low-speed links, leading to network congestion. The root protection function on a device is used to protect the root bridge by preserving the role of the designated port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Root protection is configured on a designated port. Root protection takes effect only on designated ports. If root protection is configured on other types of ports, root protection does not take effect.

Do as follows on the root bridge.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet interface participating in STP calculation is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run [**stp root-protection**](cmdqueryname=stp+root-protection)
   
   
   
   Root protection is configured on the device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.