Enabling LDP Multi-Instance
===========================

This section describes how to configure LDP multi-instance. Before you configure LDP multi-instance, enable LDP for the specified VPN instance on each node.

#### Context

To configure the transport address for an LDP instance, you must use the IP address of the interfaces that are bound to the same VPN instance.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In LDP multi-instance scenarios, you can use the interface address to establish a session.

Perform the following steps on each LSR in an MPLS domain:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp+vpn-instance) **vpn-instance** *vpn-instance-name*
   
   
   
   LDP is enabled for the specified VPN instance, and the MPLS-LDP-VPN instance view is displayed.
   
   
   
   For LDP-enabled interfaces, note the following:
   
   * Configurations in the MPLS-LDP-VPN instance view only take effect on LDP-enabled interfaces that are bound to the same VPN instance.
   * Configurations in the MPLS LDP view do not take effect on LDP-enabled interfaces that are bound to the VPN instance.
3. (Optional) Run [**lsr-id**](cmdqueryname=lsr-id) *lsr-id*
   
   
   
   An LSR ID is configured for the LDP VPN instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In most applications, use the default LDP LSR ID. When VPN instances are used, such as a BGP/MPLS VPN, if the VPN address space and public network address space overlap, set LSR IDs for LDP instances so that TCP connections for LDP sessions can be properly established.