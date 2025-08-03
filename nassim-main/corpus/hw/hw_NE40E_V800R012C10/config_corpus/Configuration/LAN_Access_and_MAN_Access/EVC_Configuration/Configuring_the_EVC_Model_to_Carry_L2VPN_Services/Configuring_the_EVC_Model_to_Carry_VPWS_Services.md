Configuring the EVC Model to Carry VPWS Services
================================================

This section describes how to use the EVC model to carry VPWS services. This implementation can facilitate network planning and management, thereby cutting down enterprise costs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number* **mode l2**
   
   
   
   The EVC Layer 2 sub-interface view is displayed.
3. Run [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* }\* *vc-id* [ **access-port** | [ **control-word** | **no-control-word** ] | **ignore-standby-state** | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking** ] | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **secondary** | **bypass** ] ]\*
   
   
   
   A VPWS connection is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The IDs of VCs using the same encapsulation type must be unique.
   * The **raw**, **tagged**, and **access-port** parameters are available in this command only for Ethernet links. In addition, the **access-port** parameter can be configured only on Ethernet main interfaces.
   * The default tunnel policy uses LDP tunnels for VPWS connections. To use a different type of tunnel, set the **tunnel-policy** *policy-name* parameter for the connection to reference the corresponding tunnel policy.
4. (Optional) Run [**encapsulation vlan pass**](cmdqueryname=encapsulation+vlan+pass)
   
   
   
   The EVC VPWS tagged mode is enabled.
   
   
   
   In EVC scenarios, if the EVC model is configured to carry VPWS services, PWs work in raw mode (with the VPWS encapsulation type being VLAN). In this case, packets leaving PWs are directly forwarded without having the outer tag removed. To solve this problem, run the [**encapsulation vlan pass**](cmdqueryname=encapsulation+vlan+pass) command to configure the PWs to work in tagged mode, so that the outer tag is removed when the packets leave the PWs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.