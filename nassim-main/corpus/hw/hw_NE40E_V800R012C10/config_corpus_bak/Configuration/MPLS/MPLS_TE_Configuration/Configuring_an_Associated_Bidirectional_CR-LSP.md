Configuring an Associated Bidirectional CR-LSP
==============================================

Associated bidirectional CR-LSPs provide bandwidth protection for bidirectional services. Bidirectional switching can be performed for associated bidirectional CR-LSPs if faults occur.

#### Usage Scenario

MPLS networks face the following challenges:

* MPLS TE tunnels that transmit services are unidirectional. The ingress forwards services to the egress along an MPLS TE tunnel. The egress forwards services to the ingress over IP routes. As a result, the services may be congested because IP links do not reserve bandwidth for these services.
* Two MPLS TE tunnels in opposite directions are established between the ingress and egress. If a fault occurs on an MPLS TE tunnel, a traffic switchover can only be performed for the faulty tunnel, but not for the reverse tunnel. As a result, traffic is interrupted.

A forward CR-LSP and a reverse CR-LSP between two nodes are established. Each CR-LSP is bound to the ingress of its reverse CR-LSP. The two CR-LSPs then form an associated bidirectional CR-LSP. The associated bidirectional CR-LSP is primarily used to prevent traffic congestion. If a fault occurs on one end, the other end is notified of the fault so that both ends trigger traffic switchovers, which ensures that traffic transmission is uninterrupted.

The configurations in this section must be performed on tunnel interfaces of both the forward and reverse CR-LSPs. Each CR-LSP is bound to the ingress of its reverse CR-LSP.


#### Pre-configuration Tasks

Before configuring an associated bidirectional CR-LSP, complete either of the following tasks:

* Create RSVP-TE tunnels in opposite directions for an associated bidirectional dynamic CR-LSP to be established.
* Create static CR-LSPs in opposite directions for an associated bidirectional static CR-LSP to be established.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run [**mpls te reverse-lsp**](cmdqueryname=mpls+te+reverse-lsp) **protocol** { **rsvp-te** **ingress-lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* | **static** **lsp-name** *lsp-name* }
   
   
   
   A reverse CR-LSP is configured on the tunnel interface.
   
   Either of the following associated bidirectional CR-LSPs can be established:
   
   * Associated bidirectional static CR-LSP: Two static unidirectional CR-LSPs in opposite directions are bound to each other to form an associated bidirectional static CR-LSP. For this type of CR-LSP, you need to specify **static** **lsp-name** *lsp-name*.
   * Associated bidirectional dynamic CR-LSP: Two RSVP-TE tunnels in opposite directions are bound to each other to form an associated bidirectional dynamic CR-LSP. For this type of CR-LSP, you need to specify **rsvp-te** **ingress-lsr-id** *ingress-lsr-id* **tunnel-id** *tunnel-id* .
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display mpls te reverse-lsp**](cmdqueryname=display+mpls+te+reverse-lsp) command to view brief information about reverse CR-LSPs.

Run the [**display mpls te reverse-lsp**](cmdqueryname=display+mpls+te+reverse-lsp) **verbose** command to view detailed information about reverse CR-LSPs.