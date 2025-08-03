(Optional) Configuring Flow Label-based Load Balancing
======================================================

After flow label-based load balancing is configured for an L2VPN, L2VPN services can be classified by flow label and forwarding paths can be selected based on these flow labels, improving forwarding efficiency.

#### Context

If multiple links are available for a PW between Ps, configure flow label-based load balancing to improve L2VPN traffic forwarding efficiency. After flow label-based load balancing is enabled on a PE, the PE adds a different label to each L2VPN data flow to distinguish them. After a P receives data packets carrying flow labels, it performs the hash operation and selects forwarding paths based on flow labels in the data packets, implementing load balancing. To enable flow label-based load balancing for PWs, run the [**flow-label**](cmdqueryname=flow-label) command.

You can configure flow label-based load balancing for VPLS by either VSI or PW. To enable flow label-based load balancing for all PWs in a VSI, see [Enable flow label-based load balancing for all PWs in a VSI](#EN-US_TASK_0172370097__step_1). To enable flow label-based load balancing for a specified PW in a VSI, see [Enable flow label-based load balancing for a specified PW in a VSI](#EN-US_TASK_0172370097__step_2).


#### Procedure

* Perform the following operations on both endpoint PEs to enable flow label-based load balancing for all PWs in a VSI:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**flow-label hash-fields**](cmdqueryname=flow-label+hash-fields) { **l2** | **l3** | **l4** } command to configure a hash element for flow label-based load balancing.
     
     
     
     This command takes effect only after L2VPN flow label-based load balancing is enabled for a VSI in the VSI-LDP view.
     
     This command is supported only by the admin VS.
  3. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view.
  4. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to enter the VSI-LDP view.
  5. Run the [**flow-label**](cmdqueryname=flow-label) { **both** | **send** | **receive** } [ **static** ] command to enable L2VPN flow label-based load balancing for the VSI. 
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Flow label-based load balancing can be enabled only when any of the following conditions is met:
       - The **receive** parameter is configured on the local PE, and the **send** parameter is configured on the remote PE.
       - The **send** parameter is configured on the local PE, and the **receive** parameter is configured on the remote PE.
       - Both the **send** and **receive** parameters are configured on the local and remote PEs.
     + If **static** is configured, the flow label-based load balancing capability is statically configured.
       
       If the static flow label-based load balancing configuration does not match on both ends, the device discards packets carrying a flow label, causing packet loss.
  6. Run the **commit** command to commit the configuration.
* Perform the following operations on both endpoint PEs to enable flow label-based load balancing for a specified PW in a VSI:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**flow-label hash-fields**](cmdqueryname=flow-label+hash-fields) { **l2** | **l3** | **l4** } command to configure a hash element for flow label-based load balancing.
     
     
     
     This command takes effect only after L2VPN flow label-based load balancing is enabled for the VSI in the VSI-LDP-PW view.
  3. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to enter the VSI view.
  4. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to enter the VSI-LDP view.
  5. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name* command to enter the VSI-LDP-PW view.
  6. (Optional) Run the [**flow-label disable**](cmdqueryname=flow-label+disable) command to disable flow label-based load balancing for the PW.
     
     
     
     If the [**flow-label**](cmdqueryname=flow-label) command has been run for the VSI to enable flow label-based load balancing for all PWs in the VSI but a PW does not need flow label-based load balancing, you can run this command to disable flow label-based load balancing for the PW.
  7. Run the [**flow-label**](cmdqueryname=flow-label) { **both** | **send** | **receive** } [ **static** ] command to enable L2VPN flow label-based load balancing for the PW.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Flow label-based load balancing can be enabled only when any of the following conditions is met:
       - The **receive** parameter is configured on the local PE, and the **send** parameter is configured on the remote PE.
       - The **send** parameter is configured on the local PE, and the **receive** parameter is configured on the remote PE.
       - Both the **send** and **receive** parameters are configured on the local and remote PEs.
     + If **static** is configured, the flow label-based load balancing capability is statically configured.
       
       If the static flow label-based load balancing configuration does not match on both ends, the device discards packets carrying a flow label, causing packet loss.
       
       In VPLS scenarios where services run properly, after you run the [**flow-label**](cmdqueryname=flow-label) command in the VSI view, PWs in the VSI will be re-established and temporary packet loss will occur.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.