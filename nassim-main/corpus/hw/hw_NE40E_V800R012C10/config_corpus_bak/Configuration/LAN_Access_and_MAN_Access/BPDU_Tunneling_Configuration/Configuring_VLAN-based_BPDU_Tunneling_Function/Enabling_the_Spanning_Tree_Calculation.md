Enabling the Spanning Tree Calculation
======================================

Bridge protocol data units (BPDUs) from user networks are transparently transmitted through different BPDU tunnels over the Layer 2 network of a carrier network to perform the spanning tree calculation.

#### Context

Perform the following steps on provider edges (PEs) and customer edges (CEs).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**stp enable**](cmdqueryname=stp+enable)
   
   
   
   The spanning tree calculation is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.