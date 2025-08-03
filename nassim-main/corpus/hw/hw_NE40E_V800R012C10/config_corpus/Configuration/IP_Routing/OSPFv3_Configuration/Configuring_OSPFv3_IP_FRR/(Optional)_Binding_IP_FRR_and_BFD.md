(Optional) Binding IP FRR and BFD
=================================

Binding IP FRR and BFD enables the lower layer to fast respond to a link change so that traffic can be rapidly switched to the backup link if the primary link fails.

#### Context

Binding the BFD session status to the link status of an interface ensures that link failures are detected rapidly and that traffic is rapidly switched to the backup link.

* If IP FRR of an OSPFv3 process is bound to BFD, IP FRR on all interfaces in the OSPFv3 process is bound to BFD.
* If only a small number of interfaces need to have IP FRR bound to BFD, bind IP FRR on each interface to BFD one by one.

Perform the following steps on the Router where IP FRR and BFD need to be associated:


#### Procedure

* Bind IP FRR and BFD in an OSPFv3 process.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3)
     
     
     
     An OSPFv3 process is enabled, and the OSPFv3 view is displayed.
  3. Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **frr-binding**
     
     
     
     IP FRR and BFD are bound in the OSPFv3 process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind IP FRR and BFD on a specified OSPFv3 interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     An interface view is displayed.
  3. Run [**ospfv3 bfd**](cmdqueryname=ospfv3+bfd) **frr-binding**
     
     
     
     IP FRR and BFD are bound on the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

The BFD configuration on an interface takes precedence over that in an OSPFv3 process. If BFD is enabled on an interface, a BFD session is established based on the BFD parameters set on the interface.