Enabling TE Detour FRR
======================

TE detour FRR must be enabled on the ingress of a primary tunnel before TE Auto FRR is configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The TE tunnel interface view is displayed.
3. Run [**mpls te detour**](cmdqueryname=mpls+te+detour)
   
   
   
   TE detour FRR is enabled.
   
   
   
   If you run the [**mpls te detour**](cmdqueryname=mpls+te+detour) and [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) commands on the same tunnel interface, the latest configuration overrides the previous one.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the preceding configuration is complete, check the configuration.

* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) command to check TE tunnel information.
* Run the [**display mpls te tunnel path**](cmdqueryname=display+mpls+te+tunnel+path) command to check TE tunnel path information on the local node.
* Run the [**display mpls rsvp-te psb-content**](cmdqueryname=display+mpls+rsvp-te+psb-content) command to check RSVP-TE path state block (PSB) information on the local node.