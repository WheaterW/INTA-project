Configuring a Source Interface for an IPv4 over IPv6 Tunnel
===========================================================

You can only specify a loopback interface as the source interface for an IPv4 over IPv6 tunnel interface and use it to communicate with other devices because a loopback interface stays in the Up state after being created.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number*
   
   
   
   A loopback interface is created.
3. (Optional) Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* A VPN instance is bound to the loopback interface.
   
   
   
   In VPN scenarios, the loopback interface must be bound to the VPN instance to which the device belongs.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
5. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* }
   
   
   
   An IPv6 address is configured for the loopback interface.
6. Run [**binding tunnel ipv4-ipv6**](cmdqueryname=binding+tunnel+ipv4-ipv6)
   
   
   
   IPv4 over IPv6 is enabled on the loopback interface.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.