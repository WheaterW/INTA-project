(Optional) Configuring Soft Preemption for RSVP-TE Tunnels
==========================================================

The setup and holding priorities and the preemption function are configured to allow TE tunnels to be established preferentially to transmit important services, preventing random resource competition during tunnel establishment.

#### Context

If there is no path meeting the bandwidth requirement of a desired tunnel, a device can tear down an established tunnel and use bandwidth resources assigned to that tunnel to establish a desired tunnel. This is called preemption. The following preemption modes are supported:

* Hard preemption: A tunnel with a higher setup priority can preempt resources assigned to a tunnel with a lower holding priority. Consequently, some traffic is dropped on the tunnel with a lower holding priority during the hard preemption process.
* Soft preemption: After a tunnel with a higher setup priority preempts the bandwidth of a tunnel with a lower holding priority, the soft preemption function retains the tunnel with a lower holding priority for a specified period of time. If the ingress finds a better path for this tunnel after the time elapses, the ingress uses the make-before-break (MBB) mechanism to reestablish the tunnel over the new path. If the ingress fails to find a better path after the time elapses, the tunnel goes Down.


#### Procedure

* Configure software preemption in the RSVP-TE tunnel interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
     
     
     
     MPLS TE is configured as a tunnel protocol.
  4. (Optional) Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **rsvp-te**
     
     
     
     A signaling protocol is configured for the tunnel.
     
     By default, the signaling protocol of a tunnel is RSVP-TE.
  5. Run [**mpls te soft-preemption**](cmdqueryname=mpls+te+soft-preemption)
     
     
     
     Software preemption is configured in the RSVP-TE tunnel interface view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure software preemption in the MPLS view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te**](cmdqueryname=mpls+te)
     
     
     
     MPLS TE is globally enabled.
  4. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
     
     
     
     RSVP-TE is enabled.
  5. Run [**mpls te soft-preemption**](cmdqueryname=mpls+te+soft-preemption)
     
     
     
     Software preemption is configured in the global MPLS view.
     
     
     
     After the preceding configuration, the device performs soft preemption for tunnels that meet the following conditions:
     
     + P2P tunnels that use RSVP-TE as the signaling protocol, including manual tunnels, manual bypass tunnels, auto tunnels, auto bypass tunnels, IP-prefix tunnels, and auto tunnels delivered by a PCE controller.
     + Manual tunnels whose tunnel interfaces have no [**mpls te soft-preemption block**](cmdqueryname=mpls+te+soft-preemption+block) or [**mpls te resv-style**](cmdqueryname=mpls+te+resv-style) **ff** command configured.
     
     If the [**mpls te soft-preemption**](cmdqueryname=mpls+te+soft-preemption) command has been run in the view of a manual tunnel interface, this configuration takes precedence over that in the global MPLS view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.