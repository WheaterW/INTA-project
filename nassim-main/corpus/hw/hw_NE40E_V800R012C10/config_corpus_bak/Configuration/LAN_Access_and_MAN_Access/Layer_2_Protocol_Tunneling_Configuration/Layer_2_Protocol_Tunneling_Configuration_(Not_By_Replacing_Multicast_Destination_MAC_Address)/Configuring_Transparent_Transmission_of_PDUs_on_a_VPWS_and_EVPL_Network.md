Configuring Transparent Transmission of PDUs on a VPWS/EVPL Network
===================================================================

This section describes how to transparently transmit Layer 2 protocol data units (PDUs), such as LACP, LLDP, BPDU, CDP, and UDLD packets, on a VPWS/EVPL network to implement Layer 2 negotiation with remote users.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The sub-interface view is displayed.
3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   The sub-interface is associated with a VLAN, and a VLAN encapsulation mode is configured for the sub-interface.
4. Complete the VLL/CCC VPWS or EVPL configuration as needed.
   
   
   * For details about how to configure a VLL VPWS, see [Configuring LDP VPWS](../vrp/dc_vrp_vpws_cfg_3004.html), [Configuring BGP VPWS](../vrp/dc_vrp_vpws_cfg_6054.html), or [Configuring SVC VPWS](../vrp/dc_vrp_vpws_cfg_6000.html).
   * For details about how to configure a CCC VPWS, see [Configuring CCC VPWS PWs](../vrp/dc_vrp_vpws_cfg_6022.html).
   * For details about how to configure an EVPL, see [Configuring EVPN VPWS over MPLS](../vrp/dc_vrp_evpn_cfg_0020.html).
5. Run the corresponding command according to the type and protocol status of the Layer 2 protocol packets to be transparently transmitted.
   
   
   * For LLDPDUs, perform one of following operations depending on whether LLDP is enabled:
     
     + If LLDP is disabled globally or on the main interface, run the [**link-protocol transport**](cmdqueryname=link-protocol+transport) **lldp** command to configure the sub-interface to transparently transmit untagged LLDPDUs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If LLDP is disabled, tagged LLDPDUs can be transparently transmitted regardless of whether this command is run.
     + If LLDP is enabled both globally and on the main interface, run the [**link-protocol transport tagged**](cmdqueryname=link-protocol+transport+tagged) **lldp** command to configure the sub-interface to transparently transmit tagged LLDPDUs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If LLDP is enabled, untagged LLDPDUs cannot be transparently transmitted regardless of whether this command is run.
   * For LACPDUs, run the [**mode**](cmdqueryname=mode) **lacp-static** command to configure the involved Eth-Trunk interface to work in static LACP mode. Then, depending on whether the LACPDUs carry VLAN tags, run one of the following commands to configure the Eth-Trunk sub-interface to transparently transmit LACPDUs:
     
     + If the LACPDUs do not carry VLAN tags, run the [**link-protocol transport**](cmdqueryname=link-protocol+transport) **lacp** command.
     + If the LACPDUs carry VLAN tags, run the [**link-protocol transport tagged**](cmdqueryname=link-protocol+transport+tagged) **lacp** command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Only Eth-Trunk sub-interfaces can transparently transmit LACPDUs.
   * For BPDUs, perform the following operations:
     
     1. Run the [**bpdu-tunnel enable**](cmdqueryname=bpdu-tunnel+enable) command to enable BPDU tunneling on the main interface.
     2. Run the [**stp disable**](cmdqueryname=stp+disable) command to disable STP/RSTP/MSTP in the system view or interface view.
     3. Run the [**link-protocol transport**](cmdqueryname=link-protocol+transport) **bpdu** command to enable the sub-interface to transparently transmit untagged BPDUs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Only untagged BPDUs can be transparently transmitted.
   * If UDLD PDUs do not carry VLAN tags, run the [**link-protocol transport**](cmdqueryname=link-protocol+transport) **udld** command.
   * If CDPDUs do not carry VLAN tags, run the [**link-protocol transport**](cmdqueryname=link-protocol+transport) **cdp** command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.