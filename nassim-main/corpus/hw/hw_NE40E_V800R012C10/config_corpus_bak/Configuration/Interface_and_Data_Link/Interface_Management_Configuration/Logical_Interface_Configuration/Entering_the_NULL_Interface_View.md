Entering the NULL Interface View
================================

The system automatically creates a NULL0 interface. The NULL interface is used for preventing routing loops and filtering traffic.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface null**](cmdqueryname=interface+null) **0**
   
   
   
   The NULL interface view is displayed.
   
   
   
   The NULL interface is always in the Up state but does not forward any data packets. In addition, IP addresses cannot be configured on the NULL interface, and data link layer protocol cannot be encapsulated on the NULL interface.

#### Follow-up Procedure

The NULL interface is used to prevent routing loops and filtering traffic. If the [**ip route-static**](cmdqueryname=ip+route-static) **192.168.0.0 255.255.0.0 NULL 0** command is run, the device will discard all packets destined for the network segments 192.168.0.1 to 192.168.255.255.