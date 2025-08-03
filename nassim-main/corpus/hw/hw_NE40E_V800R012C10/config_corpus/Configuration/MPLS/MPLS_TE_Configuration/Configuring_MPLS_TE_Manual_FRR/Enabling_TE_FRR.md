Enabling TE FRR
===============

TE FRR must be enabled on the ingress of a primary LSP before TE FRR is manually configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the primary tunnel interface is displayed.
3. Run [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) [ **bandwidth** ]
   
   
   
   TE FRR is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After TE FRR is enabled using the [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) command, run the [**mpls te bypass-attributes**](cmdqueryname=mpls+te+bypass-attributes) command to set bypass LSP attributes.
4. (Optional) Run [**mpls te frr-switch degrade**](cmdqueryname=mpls+te+frr-switch+degrade)
   
   
   
   The MPLS TE tunnel is enabled to mask the FRR function.
   
   
   
   After TE FRR takes effect, traffic is switched to the bypass LSP when the primary LSP fails. If the bypass LSP is not the optimal path, traffic congestion easily occurs. To prevent traffic congestion, you can configure LDP to protect TE tunnels. To have the LDP protection function take effect, you need to run the [**mpls te frr-switch degrade**](cmdqueryname=mpls+te+frr-switch+degrade) command to enable the MPLS TE tunnel to mask the FRR function. After the command is run:
   
   1. If the primary LSP is in the FRR-in-use state (that is, traffic has been switched to the bypass LSP), traffic cannot be switched to the primary LSP.
   2. If HSB is configured for the tunnel and an HSB LSP is available, traffic is switched to the HSB LSP.
   3. If no HSB LSP is available for the tunnel, the tunnel is unavailable, and traffic is switched to another tunnel like an LDP tunnel.
   4. If no tunnels are available, traffic is interrupted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.