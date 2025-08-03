Configuring QinQ-based BPDU Tunneling
=====================================

You can configure QinQ-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs (QinQ is short for 802.1Q in 802.1Q). After QinQ-based BPDU tunneling is configured, the PEs do not send BPDUs to their CPUs for processing. Instead, they transparently transmit the BPDUs through BPDU tunnels over the Layer 2 network of the carrier network to user networks. This configuration also saves virtual local area network (VLAN) ID resources for the carrier network.

#### Context

You can configure QinQ-based BPDU tunneling based on [the different roles of PEs and CEs](#EN-US_TASK_0172363719__step_dc_vrp_bpdu-tunnel_cfg_001901) or on [the same role of PEs and CEs](#EN-US_TASK_0172363719__step_dc_vrp_bpdu-tunnel_cfg_001902).

Different roles of PEs and CEs: CEs are customers, and PEs are providers.

Same role of PEs and CEs: CEs and PEs are both customers.


#### Procedure

* Different roles of PEs and CEs
  
  
  
  Perform the following steps on each PE and P:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp bridge role provider**](cmdqueryname=bpdu-tunnel+stp+bridge+role+provider)
     
     
     
     The PE and P are configured as a provider.
     
     This command is supported only by the Admin-VS but takes effect on all VSs.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. (Optional) Run [**port link-type**](cmdqueryname=port+link-type) { **hybrid** | **trunk** }
     
     
     
     The interface type is configured.
  5. Run [**port vlan-stacking**](cmdqueryname=port+vlan-stacking) **vlan** *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3*
     
     
     
     The interface is configured to add an outer VLAN tag to BPDUs that the interface receives.
  6. (Optional) Run [**stp disable**](cmdqueryname=stp+disable)
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Same role of PEs and CEs
  
  
  
  Perform the following steps on each PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp group-mac**](cmdqueryname=bpdu-tunnel+stp+group-mac) *group-mac*
     
     
     
     The well-known destination Media Access Control (MAC) address of BPDUs is changed to a specified MAC address.
     
     
     
     This command is supported only on the Admin-VS but takes effect on all VSs.
     
     The well-known MAC address of BPDUs can be changed only to a multicast MAC address, which cannot be a reserved multicast MAC address in the range of 0180-C200-0000 to 0180-C200-002F.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. Run [**port vlan-stacking**](cmdqueryname=port+vlan-stacking) **vlan** *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3*
     
     
     
     The interface is configured to add an outer VLAN tag to BPDUs that the interface receives.
  5. Run [**bpdu-tunnel stp vlan**](cmdqueryname=bpdu-tunnel+stp+vlan) *vlan-id1* [ **to** *vlan-id2* ]
     
     
     
     BPDU tunneling is enabled on the interface to transparently transmit BPDUs with specified VLAN IDs.
     
     
     
     The VLAN ID range specified in this step must include the inner VLAN IDs specified in Step 4.
  6. Run [**stp disable**](cmdqueryname=stp+disable)
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In this scenario, no special configuration is required on Ps.