Configuring an MTI
==================

Configuring_an_MTI

#### Context

MTIs are virtual interfaces. MTIs allow interaction between the public network instance and VPN instances on PEs. By exchanging PIM packets between MTIs, PEs can set up PIM neighbor relationships with each other in the public network instance.

An MTI can be configured in either of the following modes:

* Automatic configuration mode
  
  If a PE is bound to multiple VPN instances, each instance needs to be configured with an MTI address. In this situation, you can use automatic configuration to configure IP addresses for all MTIs globally.
* Manual configuration mode
  
  When the number of VPN instances bound to a PE is small, you can configure an IP address and a Maximum Transmission Unit (MTU) for each MTI manually.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If both of the modes are configured, the manual configuration mode takes precedence over the automatic configuration mode.



#### Procedure

* Configure the automatic configuration mode globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**multicast-domain source-interface**](cmdqueryname=multicast-domain+source-interface) *interface-type* *interface-number*
     
     
     
     An interface from which an MTI references an IP address is specified for all VPN instances.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, use the loopback interface address as the MTI address.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the automatic configuration mode for a specified VPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
  4. Run [**multicast-domain source-interface**](cmdqueryname=multicast-domain+source-interface) *interface-type* *interface-number*
     
     
     
     An interface from which an MTI references an IP address is specified for the VPN instance.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To avoid frequent protocol changes caused by interface flapping, use the loopback interface address as the MTI address.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the manual configuration mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **mtunnel** *number*
     
     
     
     The MTI interface view is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before running the [**interface**](cmdqueryname=interface) **mtunnel** *number* command, ensure that a Share-Group has been configured, and the specified MTI has been bound to it.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The IP address of the MTI is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The MTI address must be the same as the IP address that is used to set up the Internal Border Gateway Protocol (IBGP) peer relationship on the PE on the public network. Otherwise, C-multicast packets received on the MTI cannot pass the Reverse Path Forwarding (RPF) check.
  4. (Optional) Run [**mtu**](cmdqueryname=mtu) *mti-mtu*
     
     
     
     The MTU value of the MTI is configured. By default, the MTU value of the MTI is 1472 bytes.
     
     
     
     When being transmitted between a VPN instance and the public network instance, multicast packets need to be encapsulated into or decapsulated from tunnels. If the length of multicast packets of private networks equals or approaches the maximum transmission unit (MTU) of the outbound interface of the public network instance, the length of packets into which multicast packets are encapsulated will exceed the MTU of the outbound interface of the public network instance. The encapsulated packets then need to be fragmented before being sent out through the outbound interface of the public network instance and reassembled after arriving at the receive end. Therefore, setting a small MTU on the MTI is recommended to allow large multicast packets of private networks to be fragmented before being encapsulated into packets. Packets then do not need to be reassembled on the receive end, and this improves efficiency.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.