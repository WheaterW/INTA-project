Configuring a Best-Effort Path for a CR-LSP
===========================================

A best-effort path is configured to take over traffic if both the primary and hot-standby CR-LSPs fail.

#### Context

In best-effort path mode, perform the following steps on the ingress of the primary tunnel.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A best-effort path does not provide bandwidth guarantee for traffic. Configure the affinity attribute and hop limit as needed.

CR-LSP hot standby can work with a best-effort path to further enhance reliability. Ordinary CR-LSP backup cannot work with a best-effort path.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. Run [**mpls te backup**](cmdqueryname=mpls+te+backup) **ordinary best-effort**
   
   
   
   A best-effort path is configured for the CR-LSP.
4. (Optional) Run [**mpls te affinity property**](cmdqueryname=mpls+te+affinity+property) *properties* [ **mask** *mask-value* ] **best-effort**
   
   
   
   The affinity property of the best-effort path is configured.
5. (Optional) Run [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* **best-effort**
   
   
   
   The hop limit is set for the best-effort path.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.