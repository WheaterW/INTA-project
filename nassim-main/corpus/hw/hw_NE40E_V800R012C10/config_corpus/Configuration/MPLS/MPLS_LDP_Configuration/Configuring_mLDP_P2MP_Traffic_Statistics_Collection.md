Configuring mLDP P2MP Traffic Statistics Collection
===================================================

mLDP P2MP traffic statistics collection can be enabled on the ingress, transit nodes, or bud nodes on mLDP P2MP LSPs.

#### Usage Scenario

To obtain mLDP P2MP LSP traffic statistics, configure mLDP P2MP traffic statistics collection.

Only statistics about the traffic forwarded on mLDP P2MP LSPs are collected. Therefore, statistics collection can be configured only on the ingress, transit nodes, or bud nodes.


#### Pre-configuration Tasks

Before configuring mLDP P2MP traffic statistics collection, [configure an mLDP P2MP tunnel](dc_vrp_ldp-p2p_cfg_0060.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls traffic-statistics**](cmdqueryname=mpls+traffic-statistics)
   
   
   
   MPLS traffic statistics collection is enabled globally, and the traffic statistics collection view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP traffic statistics collection is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After completing the configuration, you can run the following command to verify the configuration.

* Run the [**display mpls mldp lsp p2mp traffic-statistics**](cmdqueryname=display+mpls+mldp+lsp+p2mp+traffic-statistics+root-ip+lsp-id) [ **root-ip** *root-ip* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } | **in-label** *in-label-value* ] [ **verbose** ] command to check statistics about traffic forwarded on a specified mLDP P2MP LSP.

#### Follow-up Procedure

Before collecting statistics, run the [**reset mpls traffic-statistics mldp p2mp**](cmdqueryname=reset+mpls+traffic-statistics+mldp+p2mp+root-ip+lsp-id) [ **root-ip** *root-ip* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } | **in-label** *in-label-value* ] command to delete existing statistics.