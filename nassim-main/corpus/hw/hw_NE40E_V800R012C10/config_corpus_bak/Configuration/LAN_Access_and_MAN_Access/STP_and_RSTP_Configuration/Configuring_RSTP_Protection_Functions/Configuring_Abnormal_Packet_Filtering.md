Configuring Abnormal Packet Filtering
=====================================

You can configure the device to process or discard specified packets in order to filter unexpected packets.

#### Context

On a network running STP, RSTP, or MSTP, a device may receive unexpected STP, RSTP, or MSTP BPDUs due to incorrect configurations or malicious network attacks. If these unexpected packets are transparently transmitted on the network, spanning tree calculation may be affected, causing network flapping. To address this problem, enable the function to filter abnormal packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of an interface participating in spanning tree calculation, or run the [**pw**](cmdqueryname=pw) *pw-name* command to enter the VSI-LDP-PW view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configuration can be configured both on a Layer 2 interface and a Layer 3 interface.
3. Run either or both of the following commands to configure abnormal packet filtering:
   
   
   * Run the [**stp permit packet**](cmdqueryname=stp+permit+packet) **source-mac** *source-mac* *source-mac-mask* command to enable the interface to process STP, RSTP, and MSTP BPDUs carrying a specified source MAC address.
   * Run the [**stp deny packet**](cmdqueryname=stp+deny+packet) **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>} command to enable the interface to discard STP, RSTP, and MSTP BPDUs carrying a specified VLAN ID.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If this operation is incorrectly performed, a broadcast storm may occur.
   * If both of the preceding commands are configured in the same interface view or VSI-LDP-PW view, the device preferentially executes the [**stp deny packet**](cmdqueryname=stp+deny+packet) { **vlan** *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command.
   * A maximum of 16 source MAC addresses or VLAN IDs can be configured in the same interface view or VSI-LDP-PW view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.