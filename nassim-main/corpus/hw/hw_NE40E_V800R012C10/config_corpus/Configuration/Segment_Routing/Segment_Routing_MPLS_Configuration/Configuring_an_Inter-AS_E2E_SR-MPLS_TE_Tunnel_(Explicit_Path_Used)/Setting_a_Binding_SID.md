Setting a Binding SID
=====================

Using binding SIDs reduces the number of labels in a label stack on an NE, which helps build a large-scale network.

#### Context

To reduce the number of label stack layers encapsulated by an NE, a binding SID needs to be used. A binding SID can represent the label stack of an intra-AS SR-MPLS TE tunnel. After binding SIDs and BGP peer SIDs are orchestrated properly, E2E SR-MPLS TE LSPs can be established.

An SR-MPLS TE tunnel is unidirectional. In the following operations, the binding SID is set for the unidirectional SR-MPLS TE tunnel only within an AS domain.

* To set a binding SID of a reverse SR-MPLS TE tunnel, perform the configuration on the ingress of the reverse tunnel.
* To set a binding SID of an SR-MPLS TE tunnel in another AS domain, perform the configuration on the ingress of the specific AS domain.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The intra-AS SR-MPLS TE tunnel interface view is displayed.
3. Run [**mpls te binding-sid**](cmdqueryname=mpls+te+binding-sid) **label** *label-value*
   
   
   
   A binding SID is specified for the intra-AS SR-MPLS TE tunnel.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.