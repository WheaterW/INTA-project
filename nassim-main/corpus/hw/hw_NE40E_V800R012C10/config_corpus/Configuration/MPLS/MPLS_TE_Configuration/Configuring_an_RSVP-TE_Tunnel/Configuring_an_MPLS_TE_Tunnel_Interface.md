Configuring an MPLS TE Tunnel Interface
=======================================

An MPLS TE tunnel is established and managed on a tunnel interface. Therefore, the tunnel interface must be configured on the ingress of an MPLS TE tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run either of the following commands to assign an IP address to the tunnel interface:
   
   
   * To assign an IP address to the tunnel interface, run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
     
     The primary IP address must be configured before the secondary IP address can be configured for the tunnel interface.
   * To configure the tunnel interface to borrow the IP address of another interface, run [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type* *interface-number*![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An MPLS TE tunnel is unidirectional; therefore, you do not need to consider the peer IP address when performing IP address configuration for the tunnel. Generally, you are advised to specify the ingress LSR ID as the IP address of the tunnel interface, instead of configuring a unique IP address for the interface.
4. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **mpls** **te**
   
   
   
   MPLS TE is configured as the tunneling protocol.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Changing, deleting, or initially configuring the tunnel mode of a tunnel interface will delete all tunnel-related configurations on the interface, such as the MTU. Exercise caution when performing this operation.
5. Run [**destination**](cmdqueryname=destination) *ip-address*
   
   
   
   The destination address of a tunnel is configured, which is usually the LSR ID of the egress.
   
   Various types of tunnels require specific destination addresses. If a tunneling protocol is changed to MPLS TE from another protocol, a configured destination address is deleted automatically and a new destination address needs to be configured.
6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
   
   
   
   The tunnel ID is configured.
7. (Optional) Run [**mpls te signalled tunnel-name**](cmdqueryname=mpls+te+signalled+tunnel-name) *signalled-tunnel-name*
   
   
   
   The tunnel name carried in RSVP signaling messages is configured.
   
   Perform this step to fulfill the following purposes:
   
   * Facilitate TE tunnel management.
   * Allow a Huawei device to be connected to a non-Huawei device that uses a tunnel name that differs from the tunnel interface name.
8. (Optional) Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth) **ct0** *ct0-bw-value*
   
   
   
   The bandwidth is set for an MPLS TE tunnel.
   
   The bandwidth used by the tunnel cannot be higher than the maximum reservable link bandwidth.
   
   The bandwidth used by a tunnel does not need to be set if only a path needs to be configured for an MPLS TE tunnel.
9. (Optional) Run [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name* [ **secondary** ]
   
   
   
   An explicit path is configured for an MPLS TE tunnel.
   
   An explicit path does not need to be configured if only the bandwidth needs to be set for an MPLS TE tunnel.
10. (Optional) Run [**mpls te resv-style**](cmdqueryname=mpls+te+resv-style) { **ff** | **se** }
    
    
    
    A resource reservation style is configured.
    
    The SE style is used in the make-before-break scenario, and the fixed filter (FF) style is used in a few scenarios.
11. (Optional) Run [**mpls te cspf disable**](cmdqueryname=mpls+te+cspf+disable)
    
    
    
    Constraint shortest path first (CSPF) calculation is disabled when a TE tunnel is being established.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The [**mpls te cspf disable**](cmdqueryname=mpls+te+cspf+disable) command is only applicable in the inter-AS VPN Option C scenario. In other scenarios, running this command is not recommended.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.