Configuring Interface-based BPDU Tunneling
==========================================

You can configure interface-based bridge protocol data unit (BPDU) tunneling based on the different roles of provider edges (PEs) and customer edges (CEs) or on the same role of PEs and CEs. After the configuration is complete, when an interface of a PE receives a BPDU from a user network, the PE adds a VLAN tag to the BPDU based on the PVID of the interface, selects a BPDU tunnel based on the VLAN ID in the tag, and transmits the BPDU through the BPDU tunnel. In this manner, BPDUs from different user networks are isolated.

#### Context

You can configure interface-based BPDU tunneling based on [the different roles of PEs and CEs](#EN-US_TASK_0172363703__step_dc_vrp_bpdu-tunnel_cfg_000701) or on [the same role of PEs and CEs](#EN-US_TASK_0172363703__step_dc_vrp_bpdu-tunnel_cfg_000702).

Different roles of PEs and CEs: CEs are customers, and PEs are providers.

Same role of PEs and CEs: CEs and PEs are both customers.


#### Procedure

* Different roles of PEs and CEs
  1. On a PE, run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp bridge role provider**](cmdqueryname=bpdu-tunnel+stp+bridge+role+provider)
     
     
     
     The PE is configured as a provider.
     
     
     
     This command is supported only by the admin VS but takes effect for all VSs.
  3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. (Optional) Run [**stp**](cmdqueryname=stp) **disable**
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If PEs and CEs are configured with different roles, the PEs can transparently transmit BPDUs sent by the CEs. In this case, you do not need to enable BPDU tunneling on the interfaces of the PEs.
* Same role of PEs and CEs
  1. On a PE, run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bpdu-tunnel stp group-mac**](cmdqueryname=bpdu-tunnel+stp+group-mac) *group-mac*
     
     
     
     The well-known destination Media Access Control (MAC) address of BPDUs is changed to a specified MAC address.
     
     
     
     This command is supported only on the admin VS but takes effect on all VSs.
     
     The well-known MAC address of BPDUs can be changed only to a multicast MAC address, which cannot be a reserved multicast MAC address in the range of 0180-C200-0000 to 0180-C200-002F.
  3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the PE interface connected to a CE is displayed.
  4. Run [**bpdu-tunnel enable**](cmdqueryname=bpdu-tunnel+enable)
     
     
     
     BPDU tunneling is enabled on the PE interface to transparently transmit BPDUs from a user network.
  5. Run [**stp**](cmdqueryname=stp) **disable**
     
     
     
     STP is disabled on the interface, which does not participate in spanning tree calculation.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If PEs and CEs have the same role, the PEs cannot transparently transmit BPDUs sent by the CEs. In this case, you need to enable BPDU tunneling on the PE interfaces.