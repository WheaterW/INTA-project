Configuring PIM
===============

Configuring PIM on a VPN allows a VPN multicast routing table to be established to guide multicast traffic forwarding.

#### Context

On an mLDP in-band MVPN network, PIM is used as the multicast routing protocol on VPNs. A PIM neighbor relationship can be established between devices only after PIM-SM is enabled on interfaces of the devices, enabling a VPN multicast routing table to be established to guide multicast traffic forwarding.

Perform the following steps on PEs' interfaces bound to VPN instances and on the CEs' interfaces connected to the PEs:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**multicast routing-enable**](cmdqueryname=multicast+routing-enable) command to enable multicast routing. This command needs to be run only on CEs.
3. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
4. Run the [**pim sm**](cmdqueryname=pim+sm) command to enable PIM-SM.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the current version, mLDP signaling can transmit only PIM-SM/PIM-SSM (S, G) Join messages.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.