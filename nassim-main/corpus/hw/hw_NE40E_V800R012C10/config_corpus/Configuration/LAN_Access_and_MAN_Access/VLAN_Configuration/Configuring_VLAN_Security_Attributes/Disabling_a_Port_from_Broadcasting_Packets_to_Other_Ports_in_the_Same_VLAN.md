Disabling a Port from Broadcasting Packets to Other Ports in the Same VLAN
==========================================================================

Disabling a port from broadcasting packets to other ports in the same VLAN prevents malicious attacks and improves network security.

#### Context

If a port in a VLAN receives a broadcast or unknown unicast packet, it will broadcast the packet to other ports in the VLAN. If the broadcast or unknown unicast packet is malicious, system resources waste and device performance deteriorates or even the device malfunctions. Disabling the port from broadcasting packets to other ports in the VLAN prevents malicious attacks.

This security scheme is applicable to topology-stable networks or networks on which MAC addresses are configured and forwarding paths are specified.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
   
   
   
   The VLAN view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a device is configured with multiple VLANs, configuring VLAN names to facilitate management and maintenance is recommended:
   
   Run the [**name**](cmdqueryname=name) *vlan-name* command in the VLAN view. After a VLAN name is configured, you can run the [**vlan vlan-name**](cmdqueryname=vlan+vlan-name) *vlan-name* command in the system view to enter the corresponding VLAN view.
3. Run [**broadcast discard**](cmdqueryname=broadcast+discard)
   
   
   
   The port is disabled from broadcasting packets to other ports in the same VLAN.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.