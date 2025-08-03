(Optional) Configuring a Policy for Triggering SR-MPLS BE LSP Establishment
===========================================================================

A policy can be configured to allow the ingress node to establish SR-MPLS BE LSPs based on eligible routes.

#### Context

After SR is enabled, a large number of SR-MPLS BE LSPs will be established if policy control is not configured. As a result, resources are wasted. To prevent resource wastes, a policy for establishing SR-MPLS BE LSPs can be configured. The policy allows the ingress to use only allowed routes to establish SR-MPLS BE LSPs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**segment-routing lsp-trigger**](cmdqueryname=segment-routing+lsp-trigger) { **none** | **host** | **ip-prefix** *ip-prefix-name* }
   
   
   
   A policy is configured for the ingress to establish SR-MPLS BE LSPs.
   
   
   
   * **host**: Host IP routes with 32-bit masks are used as the policy for the ingress to establish SR-MPLS BE LSPs.
   * **ip-prefix**: FECs that match an IP prefix list are used as the policy for the ingress to establish SR-MPLS BE LSPs.
   * **none**: The ingress is not allowed to establish SR-MPLS BE LSPs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.