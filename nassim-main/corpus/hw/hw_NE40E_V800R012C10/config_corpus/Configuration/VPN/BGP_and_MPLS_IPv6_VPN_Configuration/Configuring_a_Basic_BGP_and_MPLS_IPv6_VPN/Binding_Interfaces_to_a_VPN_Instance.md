Binding Interfaces to a VPN Instance
====================================

After an interface is bound to a VPN instance, the interface becomes a part of the VPN. Packets entering the interface will be forwarded based on the VRF table of the VPN.

#### Context

After a VPN instance is configured on a PE, an interface that belongs to the VPN must be bound to the VPN instance. Otherwise, the interface functions as a public network interface and cannot forward VPN data.

Perform the following steps on the PEs that are connected to CEs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The interface is bound to the VPN instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Using the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command will delete Layer 3 (including IPv4 and IPv6) configurations, such as the IP address and routing protocol, on the interface. Reconfigure them after using the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command if needed.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
5. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address*/*prefix-length* }
   
   
   
   An IPv6 address is configured for the interface. After this command is run, some Layer 3 features, such as route exchange between the PE and CE, can be configured only after an IPv6 address is configured for the VPN interface on the PE.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.