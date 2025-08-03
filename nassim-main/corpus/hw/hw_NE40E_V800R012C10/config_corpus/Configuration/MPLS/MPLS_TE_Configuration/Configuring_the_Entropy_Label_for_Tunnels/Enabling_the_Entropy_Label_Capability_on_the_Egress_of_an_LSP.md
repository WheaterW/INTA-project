Enabling the Entropy Label Capability on the Egress of an LSP
=============================================================

The entropy label capability can be configured on the egress of an LSP to load-balance traffic.

#### Context

The growth of user networks worsens the load imbalance on transit nodes. To address this problem, the entropy label capability can be configured. When the entropy label capability is configured, it must be enabled also on the egress.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**entropy-label-capability
   enable**](cmdqueryname=entropy-label-capability+enable)
   
   
   
   The entropy label capability is configured on the egress of an LSP
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.