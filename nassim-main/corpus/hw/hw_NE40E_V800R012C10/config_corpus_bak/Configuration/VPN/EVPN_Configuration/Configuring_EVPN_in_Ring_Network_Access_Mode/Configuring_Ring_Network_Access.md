Configuring Ring Network Access
===============================

If MSTP is deployed on a ring network, run the [**evpn stp-ring-id**](cmdqueryname=evpn+stp-ring-id) command on dual-homing PEs to configure the same ring ID for them. The dual-homing PEs are then identified by the same ring ID.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-name*
   
   
   
   The interface view is displayed.
3. Run [**stp tc-snooping enable**](cmdqueryname=stp+tc-snooping+enable)
   
   
   
   The main interface is enabled to snoop STP TC BPDUs.
4. Run **[**stp tc-snooping notify bridge-domain**](cmdqueryname=stp+tc-snooping+notify+bridge-domain)******process**** *processId*
   
   
   
   Topology change (TC) notification is enabled on the main interface.
5. Run [**esi**](cmdqueryname=esi) *esi*
   
   
   
   An ESI is configured on the interface.
6. Run [**evpn stp-ring-id**](cmdqueryname=evpn+stp-ring-id) *ring-id*
   
   
   
   A ring ID is configured on the interface.
   
   
   
   The same ring ID must be configured for each dual-homing PE.