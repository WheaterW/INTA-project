(Optional) Configuring the Function to Report Remote LDP Session Down Traps Generated Due to RLFA Route Deletion
================================================================================================================

In a remote LFA FRR scenario, enable the function to report remote LDP session down traps generated due to RLFA route deletion if the function is required.

#### Context

After an ingress uses the remote LFA algorithm to calculate a PQ node, the ingress establishes a remote LDP session with the PQ node. The remote LDP session goes down when the RLFA route is deleted. Such session down issues occur frequently during remote LFA FRR convergence and do not harm service deployment. Therefore, you can configure the device not to report a trap when a remote LDP session goes down.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**session-state-trap remote-lfa-disable**](cmdqueryname=session-state-trap+remote-lfa-disable)
   
   
   
   The function to report remote LDP session down traps generated due to RLFA route deletion is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.