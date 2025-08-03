Configuring the Path for ICMP Reply Messages
============================================

The path along which ICMP reply messages travel must be specified on both the ingress and egress.

#### Context

Perform the following steps on the ingress and egress:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Perform either of the following operations:
   
   
   * To enable a node to transmit ICMP reply messages over IP routes, run the **ttl expiration pop** command.
   * To enable a node to transmit ICMP reply messages along an LSP, run the **undo ttl expiration pop** command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.