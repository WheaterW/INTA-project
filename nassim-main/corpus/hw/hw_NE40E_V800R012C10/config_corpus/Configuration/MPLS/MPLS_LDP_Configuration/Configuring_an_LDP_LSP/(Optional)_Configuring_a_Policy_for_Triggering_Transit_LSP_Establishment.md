(Optional) Configuring a Policy for Triggering Transit LSP Establishment
========================================================================

A policy for triggering the establishment of transit LSPs can be configured to enable LDP to use routes that meet the specified policy to establish transit LSPs.

#### Context

After MPLS LDP is enabled, LDP LSPs are automatically established, including a large number of unnecessary transit LSPs, which wastes resources. A policy for triggering transit LSP establishment can be configured, allowing LDP to establish transit LSPs only for eligible routes. The local node does not send Label Mapping messages upstream for the routes that are filtered out. This limits the number of LSPs to be established, thereby reducing network resource consumption.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The MPLS-LDP-IPv4 view is displayed.
4. Run [**propagate mapping**](cmdqueryname=propagate+mapping+for+ip-prefix) **for** **ip-prefix** *ip-prefix-name*
   
   
   
   A policy for triggering transit LSP establishment is configured.
   
   
   
   The command takes effect in both the MPLS-LDP and MPLS-LDP-IPv4 views. If the command is configured in both views, only the latter configuration takes effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.