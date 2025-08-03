(Optional) Binding IP FRR and BFD
=================================

Binding IP FRR and BFD enables the lower layer to fast respond to a link change so that traffic can be rapidly switched to the backup link if the primary link fails.

#### Context

After the parameter **frr-binding** is set to bind the BFD status to the link status of an interface, link failures can be detected rapidly. This ensures that traffic is rapidly switched to the backup link if the primary link fails.

Perform the following steps on the Router where IP FRR and BFD need to be bound:


#### Procedure

* Bind IP FRR and BFD in an OSPF process.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospf**](cmdqueryname=ospf)
     
     
     
     An OSPF process is started, and the OSPF view is displayed.
  3. Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **frr-binding**
     
     
     
     IP FRR and BFD are bound in the OSPF process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Bind IP FRR and BFD on a specified OSPF interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospf bfd**](cmdqueryname=ospf+bfd) **frr-binding**
     
     
     
     IP FRR and BFD are bound on the interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The BFD configuration on an interface takes precedence over that in an OSPF process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.