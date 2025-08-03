Configuring a Service Interface
===============================

On the NE40E, a logical GMPLS UNI is bound to a GMPLS UNI tunnel so that the logical GMPLS UNI can transmit upper layer services, such as MPLS, IGP, and VPN services, along the GMPLS UNI tunnel.

#### Context

Using logical GMPLS UNIs as service interfaces facilitates redundancy protection for interfaces connecting the IP and optical layer devices. If a GMPLS UNI tunnel bound to a logical GMPLS UNI fails, the logical GMPLS UNI automatically searches for another available GMPLS UNI tunnel and switches traffic to the new tunnel, which implements redundancy protection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface gmpls-uni**](cmdqueryname=interface+gmpls-uni) *interface-number*
   
   
   
   A service interface is created, and the logical GMPLS UNI view is displayed.
3. Run [**ip address**](cmdqueryname=ip+address+mask) *ip-address* { **mask** | *mask-length* }
   
   
   
   An IP address is assigned to the interface.
4. (Optional) Configure upper layer service applications, such as a static route, an IGP, or MPLS.
   
   
   
   The configuration procedure is similar to that on a physical interface. The configuration details are not provided.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.