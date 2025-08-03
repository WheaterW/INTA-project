Configuring a DS-TE Bandwidth Constraints Model
===============================================

If CT bandwidth preemption is allowed, the Russian dolls model (RDM) is recommended to efficiently use bandwidth resources. If CT bandwidth preemption is not allowed, the MAM is recommended.

#### Context

Perform the following steps on each LSR in a DS-TE domain:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te ds-te bcm**](cmdqueryname=mpls+te+ds-te+bcm) { **mam** | **rdm** }
   
   
   
   A DS-TE bandwidth constraint model is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.