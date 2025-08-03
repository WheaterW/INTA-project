Configuring VLAN-based BPDU Tunneling
=====================================

You can configure VLAN-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs (VLAN is short for virtual local area network). After VLAN-based BPDU tunneling is configured, the PEs do not send BPDUs to their CPUs for processing. Instead, they transparently transmit the BPDUs through BPDU tunnels over the Layer 2 network of the carrier network to user networks.

#### Context

You can configure VLAN-based BPDU tunneling based on [the different roles of PEs and CEs](#EN-US_TASK_0172363711__step_dc_vrp_bpdu-tunnel_cfg_001301) or on [the same role of PEs and CEs](#EN-US_TASK_0172363711__step_dc_vrp_bpdu-tunnel_cfg_001302).

Different roles of PEs and CEs: CEs are customers, and PEs are providers.

Same role of PEs and CEs: CEs and PEs are both customers.


#### Procedure

* Different roles of PEs and CEs
  1. On a PE and P, run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp bridge role provider**](cmdqueryname=bpdu-tunnel+stp+bridge+role+provider)
     
     
     
     The PE and P are configured as a provider.
     
     
     
     This command is supported only by the admin VS but takes effect on all VSs.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. (Optional) Run [**port link-type**](cmdqueryname=port+link-type) { **hybrid** | **trunk** }
     
     
     
     The interface type is configured.
  5. Run [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass) **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }
     
     
     
     The VLAN IDs that the PE allows to pass are configured.
  6. (Optional) Run [**stp disable**](cmdqueryname=stp+disable)
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If PEs and CEs are configured with different roles, the PEs can transparently transmit BPDUs sent by the CEs. In this case, you do not need to enable BPDU tunneling on the interfaces of the PEs.
* Same role of PEs and CEs
  1. On a PE, run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp group-mac**](cmdqueryname=bpdu-tunnel+stp+group-mac) *group-mac*
     
     
     
     The well-known destination Media Access Control (MAC) address of BPDUs is changed to a specified MAC address.
     
     
     
     This command is supported only by the admin VS but takes effect on all VSs.
     
     The well-known MAC address of BPDUs can be changed only to a multicast MAC address, which cannot be a reserved multicast MAC address in the range of 0180-C200-0000 to 0180-C200-002F.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. Run [**bpdu-tunnel stp vlan**](cmdqueryname=bpdu-tunnel+stp+vlan) *vlan-id1* [ **to** *vlan-id2* ]
     
     
     
     BPDU tunneling is enabled on the PE interface to transparently transmit BPDUs with specified VLAN IDs.
  5. Run [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass) **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** }
     
     
     
     The VLAN IDs that the PE allows to pass are configured.
  6. Run [**stp disable**](cmdqueryname=stp+disable)
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If PEs and CEs have the same role, the PEs cannot transparently transmit BPDUs sent by the CEs. In this case, you need to enable BPDU tunneling on the PE interfaces.