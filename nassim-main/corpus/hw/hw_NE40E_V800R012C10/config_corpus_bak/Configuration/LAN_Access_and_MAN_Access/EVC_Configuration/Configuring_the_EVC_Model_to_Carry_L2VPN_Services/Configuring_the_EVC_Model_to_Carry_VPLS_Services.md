Configuring the EVC Model to Carry VPLS Services
================================================

This section describes how to use the EVC model to carry virtual private LAN service (VPLS) services to reduce enterprise costs.

#### Context

In the traditional service model supported by the NE40E, common sub-interfaces (VLAN type), dot1q VLAN tag termination sub-interfaces, or QinQ VLAN tag termination sub-interfaces are created on the user-side interfaces of PEs. These sub-interfaces are bound to different Virtual Switching Instances (VSIs) on the carrier network to isolate services in different departments of an enterprise. If the enterprise sets up another department, the enterprise must lease another VSI from the carrier to isolate the departments, which increases costs.

To allow the enterprise to dynamically adjust its departments and reduce costs, deploy the Ethernet Virtual Connection (EVC) model on the PEs to allow multiple Bridge Domains (BDs) to access the same VSI and also to be isolated from each other.

A BD can access a VPLS network in either of the following modes:

* VSI pipe service mode
  
  A VSI functions as a network-side pipe, and BDs function as service instances at the access layer. A VSI can carry service traffic from multiple BDs. The pseudowires (PWs) must work in tagged mode. The BDs must use VLAN IDs as service delimiters.
  
  When a packet enters a PW from a BD, the ingress PE adds the BD ID to the packet as the outer tag (PW tag). When the packet leaves the PW, the egress PE searches for a VSI based on the VC label and searches for a BD based on the outer tag.
* VSI-exclusive service mode
  
  Each VSI provides access services for only one BD, and the BD exclusively consumes the VSI resources. The services in the VSI can be planned as needed. The PWs can work in either raw mode (with the VSI encapsulation type being Ethernet) or tagged mode (with the VSI encapsulation type being VLAN). The ingress PE adds a PW tag to packets that enter a PW only after the PW tag has been configured and the PW works in tagged mode. The egress PE does not verify the PW tag of packets that leave the PW. If the PW works in raw mode, the egress PE directly forwards the packets to the corresponding BD. If the PW works in tagged mode, the egress PE removes the outer tag before forwarding the packets to the corresponding BD.
#### Precautions

On the network shown in [Figure 1](#EN-US_TASK_0172363386__fig_dc_vrp_evc_cfg_003101), different user networks connect to PE1 through the same CE, and a BD is bound to a VSI for VPLS access. However, due to VPLS split horizon, the user-side interface on PE1 will not forward packets it receives, and therefore users in the same VSI cannot communicate. To allow users to communicate, run the [**local-switch enable**](cmdqueryname=local-switch+enable) command on the user-side Layer 2 sub-interface on PE1. This enables local switching for the EVC Layer 2 sub-interface.

**Figure 1** Local switching for an EVC Layer 2 sub-interface  
![](images/fig_dc_vrp_evc_cfg_003101.png)
#### Pre-configuration Tasks

Before configuring the EVC model to carry VPLS services, create VSIs. VSI IDs are used to differentiate VSIs during PW signaling negotiation.

The VSIs for BDs must be configured using the [**vsi bd-mode**](cmdqueryname=vsi+bd-mode) command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Ensure that MPLS L2VPN has been enabled on the device before you create VSIs.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* [ **pw-tag** *pw-tag-value* ]
   
   
   
   The BD is bound to a VSI.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the VSI pipe service mode is used, multiple BDs can access the same VSI. In this case, you must specify a PW tag so that the peer BD can receive packets from the BD with the same PW tag.
4. (Optional) Run [**reserve-interface fast-switch enable**](cmdqueryname=reserve-interface+fast-switch+enable)
   
   
   
   The reserve-interface fast switching function is enabled.
   
   In a VPLS over EVC scenario where the public-network-and-private-network decoupling function is configured, to allow broadcast traffic to be rapidly switched to the slave interface board when the master interface board fails, perform this step.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

In a VPLS over EVC scenario, each BD functions as an access-side service instance and EVC Layer 2 sub-interfaces join each BD as AC interfaces. The status of a BD is determined by the status of all EVC Layer 2 sub-interfaces in the BD and the VSI. A BD goes down only when all its EVC Layer 2 sub-interfaces and the VSI are both down. The EVC Layer 2 sub-interface status is independent of the VSI status. In a VPWS accessing VPLS scenario where a VSI VC is configured on the local end and a VPWS VC is configured on the remote end, if all EVC Layer 2 sub-interfaces in the BD are down, the remote VPWS VC cannot quickly detect the fault. As a result, traffic is interrupted. To solve this problem, run the [**response-ac-state**](cmdqueryname=response-ac-state) command, so that the VSI can learn the AC interface down event immediately after all EVC Layer 2 sub-interfaces in a BD go down. Then, the VSI will set the PW status to down.

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   The VSI view is displayed.
3. Run [**response-ac-state**](cmdqueryname=response-ac-state)
   
   The VSI is enabled to learn the AC interface down event when all EVC Layer 2 sub-interfaces in a BD are down.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

A BD goes down after all EVC Layer 2 sub-interfaces leave the BD. By default, a PE sends MAC Withdraw messages with the 0x404 TLV type to all peers when a BD goes down. After the [**interface-status-change mac-withdraw enable**](cmdqueryname=interface-status-change+mac-withdraw+enable) command is run, a PE sends MAC Withdraw messages with the 0x406 TLV type to all its peers each time an EVC Layer 2 sub-interface leaves the BD. As a result, when a BD goes down, the PE will send MAC Withdraw messages twice. To solve this problem, perform the following steps:

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   The VSI view is displayed.
3. Run [**mac-withdraw bd-status down disable**](cmdqueryname=mac-withdraw+bd-status+down+disable)
   
   The PE is configured not to send MAC Withdraw messages with the 0x404 TLV type to all its peers when a BD goes down.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

When the status of an EVC Layer 2 sub-interface changes, a PE sends MAC Withdraw messages that do not carry the PW tag to all its peers. When a peer receives this message, it clears MAC addresses in the VSI based on the message, causing the MAC addresses of other BDs to be deleted incorrectly. To solve this problem, perform the following steps:

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   The EVC Layer 2 sub-interface view is displayed.
3. Run [**interface-status-change [ up | down ] mac-withdraw enable**](cmdqueryname=interface-status-change+%5B+up+%7C+down+%5D+mac-withdraw+enable)
   
   The PE is enabled to send a MAC Withdraw message to all its peers when the EVC Layer 2 sub-interface status changes.
4. Run [**quit**](cmdqueryname=quit)
   
   Return to the system view.
5. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **bd-mode**
   
   The BD VSI view is displayed.
6. Run [**mac-withdraw enable**](cmdqueryname=mac-withdraw+enable)
   
   MAC Withdraw is enabled.
7. Run [**mac-withdraw bd pw-tag enable**](cmdqueryname=mac-withdraw+bd+pw-tag+enable)
   
   The PE is configured to send MAC Withdraw messages that carry the PW tag to its peers when its AC interface status changes or the BD goes down.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

In EVC scenarios, when a BD accesses a VPLS network in VSI-exclusive service mode, PWs work in raw mode (with the VSI encapsulation type being VLAN). In this case, packets leaving PWs are directly forwarded without having the outer tag removed. To solve this problem, perform the following steps to configure the PWs to work in tagged mode, so that the outer tag is removed when the packets leave the PWs:

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* **bd-mode**
   
   The BD VSI view is displayed.
3. Run [**pwsignal ldp**](cmdqueryname=pwsignal+ldp)
   
   The VSI-LDP view is displayed.
4. Run [**vsi-id**](cmdqueryname=vsi-id) *vsi-id*
   
   A VSI ID is configured.
5. Run [**peer**](cmdqueryname=peer) *peer-address*
   
   A peer is specified for the current VSI.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name*
   
   A PW is created for the VSI.
7. Run [**encapsulation vlan pass**](cmdqueryname=encapsulation+vlan+pass)
   
   The BD VPLS tagged mode is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.