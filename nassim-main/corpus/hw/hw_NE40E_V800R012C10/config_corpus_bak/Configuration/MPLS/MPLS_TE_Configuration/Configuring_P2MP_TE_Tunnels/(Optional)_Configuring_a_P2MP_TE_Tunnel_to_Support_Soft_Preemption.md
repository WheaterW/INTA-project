(Optional) Configuring a P2MP TE Tunnel to Support Soft Preemption
==================================================================

Priorities and preemption are used to allow TE tunnels to be established preferentially to transmit important services, preventing resource competition during tunnel establishment.

#### Context

If there is no path meeting the bandwidth requirement of a desired tunnel, a device can tear down an established tunnel and use bandwidth resources assigned to that tunnel to establish a desired tunnel. This is called preemption. The following preemption modes are supported:

* Hard preemption: A CR-LSP with a higher setup priority can directly preempt resources assigned to a CR-LSP with a lower holding priority. Some traffic is dropped on the CR-LSP with a lower holding priority during the hard preemption process.
* Soft preemption: After a CR-LSP with a higher setup priority preempts bandwidth of a CR-LSP with a lower holding priority, the soft preemption function retains the CR-LSP with a lower holding priority for a specified period of time. If the ingress finds a better path for this CR-LSP after the time elapses, the ingress uses the make-before-break mechanism to reestablish the CR-LSP over the new path. If the ingress fails to find a better path after the time elapses, the CR-LSP goes down.


#### Procedure

* Configure soft preemption in the P2MP TE tunnel template view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls te p2mp-template**](cmdqueryname=mpls+te+p2mp-template) *template-name*
     
     
     
     The P2MP TE tunnel template view is displayed.
  3. Run [**soft-preemption**](cmdqueryname=soft-preemption)
     
     
     
     Soft preemption is enabled for the P2MP TE tunnel.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure soft preemption in the P2MP TE tunnel view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The P2MP TE tunnel interface view is displayed.
  3. Run [**mpls te soft-preemption**](cmdqueryname=mpls+te+soft-preemption)
     
     
     
     Soft preemption is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.