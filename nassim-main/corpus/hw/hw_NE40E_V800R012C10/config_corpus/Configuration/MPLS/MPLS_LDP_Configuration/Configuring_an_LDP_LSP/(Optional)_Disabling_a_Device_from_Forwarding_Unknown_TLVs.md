(Optional) Disabling a Device from Forwarding Unknown TLVs
==========================================================

A local device can be disabled from forwarding unknown TLVs to peers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is globally enabled.
3. Run [**propagate mapping unknown-tlv disable**](cmdqueryname=propagate+mapping+unknown-tlv+disable)
   
   
   
   The device is disabled from forwarding unknown TLVs.
   
   
   
   If an upstream device cannot process unknown TLVs, network problems may occur. In this case, you can run this command to disable the local device from forwarding unknown TLVs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.