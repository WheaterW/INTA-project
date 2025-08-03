Configuring an MPLS TE Associated Tunnel Group
==============================================

If the bandwidth of a service tunnel is insufficient, you can create an associated tunnel group and specify both an original tunnel and its split tunnels to carry services.

#### Prerequisites

Before configuring an MPLS TE associated tunnel group, complete the following task:

* [Configure RSVP-TE tunnels.](dc_vrp_te-p2p_cfg_0003.html)

#### Context

The bandwidth of an MPLS TE tunnel is limited, but the bandwidth of services carried by the tunnel cannot be limited. As a result, the tunnel bandwidth may become insufficient in some service scenarios, for example, when routes or VPN services recurse to the tunnel. To address this issue, you can create an associated tunnel group, specify the current tunnel as the original tunnel of the group, and specify split tunnels for the original tunnel. The split tunnels can carry services together with the original tunnel, relieving bandwidth pressure.


#### Procedure

1. Configure split tunnels.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
      
      
      
      A tunnel interface is created, and its view is displayed.
   3. Run either of the following commands to assign an IP address to the tunnel interface:
      
      
      * To configure an IP address, run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] command.
        
        The secondary IP address of a tunnel interface can be configured only after the primary IP address is configured.
      * To borrow an IP address from another interface, run the [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type interface-number* command.
      
      Although an MPLS TE tunnel can be established even if its tunnel interface has no IP address, the tunnel cannot forward traffic. Therefore, the tunnel interface must have an IP address to implement traffic forwarding. An MPLS TE tunnel is unidirectional; therefore, you do not need to consider the peer IP address when performing IP address configuration for the tunnel. You are advised to specify the ingress LSR ID as the IP address of the tunnel interface, instead of configuring a unique IP address for the interface.
   4. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
      
      
      
      MPLS TE is enabled.
   5. Run [**destination**](cmdqueryname=destination) *ip-address*
      
      
      
      A destination IP address is assigned to the tunnel. Generally, the egress LSR ID is used as the destination IP address.
   6. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
      
      
      
      A tunnel ID is set.
   7. Run [**mpls te signal-protocol**](cmdqueryname=mpls+te+signal-protocol) **rsvp-te**
      
      
      
      RSVP-TE is enabled.
   8. Run [**mpls te split-tunnel**](cmdqueryname=mpls+te+split-tunnel)
      
      
      
      The tunnel is configured as a split tunnel.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure an associated tunnel group.
   1. Run [**mpls te associate-tunnel-group**](cmdqueryname=mpls+te+associate-tunnel-group)*group-id*
      
      
      
      An associated tunnel group is created, and its view is displayed.
   2. Run [**mpls te original-tunnel**](cmdqueryname=mpls+te+original-tunnel)*tunnel-name*
      
      
      
      An original tunnel is specified for the associated tunnel group.
   3. Run [**mpls te split-tunnel**](cmdqueryname=mpls+te+split-tunnel)*tunnel-name*
      
      
      
      A split tunnel is specified for the associated tunnel group.
      
      
      
      Repeat this command if you want to add more split tunnels.
   4. (Optional) Run [**mpls te backup active-standby**](cmdqueryname=mpls+te+backup+active-standby)
      
      
      
      The active/standby mode is enabled for the associated tunnel group.
      
      
      
      After the [**mpls te backup active-standby**](cmdqueryname=mpls+te+backup+active-standby) command is run, the original tunnel and its split tunnels work in active/standby mode. Normally, only the original tunnel can carry service traffic. Split tunnels are sequenced based on a selection rule (for example, in ascending order of tunnel ID). They protect the original tunnel. If the original tunnel is faulty or in the "FRR in use" state, traffic is switched from the original tunnel to the first split tunnel; if the first split tunnel is faulty, traffic is switched to the second split tunnel, and so on, implementing traffic switching from the original tunnel to split tunnels.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After an MPLS TE associated tunnel group is configured, you can run the [**display mpls te associate-tunnel-group**](cmdqueryname=display+mpls+te+associate-tunnel-group) [ *group-id* ] command to check information about the group.