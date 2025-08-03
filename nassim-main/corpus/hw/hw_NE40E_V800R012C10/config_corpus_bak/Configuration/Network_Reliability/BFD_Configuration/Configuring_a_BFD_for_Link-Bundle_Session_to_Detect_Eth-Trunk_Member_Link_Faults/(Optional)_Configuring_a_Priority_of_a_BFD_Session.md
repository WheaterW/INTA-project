(Optional) Configuring a Priority of a BFD Session
==================================================

Setting the priority of a BFD session can ensure that packets with a higher priority are forwarded.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. Run [**tos-exp**](cmdqueryname=tos-exp) *tos-value* **dynamic**
   
   
   
   A priority is configured for the dynamic BFD session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.