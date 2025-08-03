Disabling Gratuitous ARP Packet Sending
=======================================

You can disable an interface from sending gratuitous ARP packets to prevent CPU overload.

#### Context

If a device has a large number of interfaces and all interfaces are Up and are allocated IP addresses, the device may keep sending gratuitous ARP packets, consuming excessive CPU resources. As a result, services are affected. To prevent CPU overload, you can disable an interface from sending gratuitous ARP packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**arp gratuitous-arp send disable**](cmdqueryname=arp+gratuitous-arp+send+disable)
   
   
   
   The interface is disabled from sending gratuitous ARP packets.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Using the [**arp gratuitous-arp send disable**](cmdqueryname=arp+gratuitous-arp+send+disable) command will prevent sending gratuitous arp packet, and may cause IP collision detection failure and services to be interrupted. Exercise caution when running this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.