(Optional) Configuring the Protection Switching Function
========================================================

A protection switching function, such as link or node protection, can be configured to provide high availability for an inter-AS seamless MPLS network.

#### Context

On an inter-AS seamless MPLS network that has protection switching enabled, if a link or node fails, traffic switches to a backup path, which implements uninterrupted traffic transmission.

| Tunnel Type | Protected Object | Nodes to Be Configured | Detection Method | Protection Function |
| --- | --- | --- | --- | --- |
| MPLS TE tunnel (without Ps on links at the network layer) | Protects access rings, aggregation rings, and links at the core layer. | All nodes | [Configure BFD for interface.](#EN-US_TASK_0172368656__BFD_interface) | Configure either of the following TE FRR functions:   * [Configure TE manual FRR.](#EN-US_TASK_0172368656__TE_FRR1) * [Configure MPLS TE Auto FRR.](#EN-US_TASK_0172368656__TE_FRR2) |
| MPLS TE tunnel (with Ps on links at the network layer) | Protects access rings, aggregation rings, and links at the core layer. | All nodes | [Configure static BFD for CR-LSP](#EN-US_TASK_0172368656__BFD_CR-LSP1) or [dynamic BFD for CR-LSP.](#EN-US_TASK_0172368656__BFD_CR-LSP2) | [Configure CR-LSP hot standby.](#EN-US_TASK_0172368656__Hotstandby2) |
| MPLS TE tunnel | Protects AGGs, AGG ASBRs, and core ASBRs. | CSGs, AGGs, AGG ASBRs, and MASGs | [Configure BFD for TE.](#EN-US_TASK_0172368656__BFD_TE) | Configure BGP LSP FRR. |
| MPLS LDP LSP | Protects access rings and aggregation rings, as well as links, AGGs, AGG ASBRs, and core ASBRs at the core layer. | All nodes | [Configure static BFD to monitor an LDP LSP](#EN-US_TASK_0172368656__BFD_LDP1) or [dynamic BFD for LDP LSPs.](#EN-US_TASK_0172368656__BFD_LDP2) | Configure BGP LSP FRR. |
| MPLS TE tunnel or MPLS LDP LSP | Protect links between each pair of an AGG ASBR and a core ASBR. | AGG ASBRs and core ASBRs | [Configure BFD for interface.](#EN-US_TASK_0172368656__BFD_interface) | Configure BGP LSP FRR. |
| MPLS TE tunnel or MPLS LDP LSP | Protects a whole BGP LSP and MP-BGP peers on an L3VPN. | CSGs and MASGs | [Configure BFD for BGP tunnel.](#EN-US_TASK_0172368656__BFD_BGPLSP) | Configure either of the following VPN FRR functions:   * [Enable VPN FRR in the VPN instance IPv4 address family view.](#EN-US_TASK_0172368656__VPN1) * [Enable VPN FRR in the BGP-VPN instance IPv4 address family view.](#EN-US_TASK_0172368656__VPN2) |




#### Procedure

* Configure BFD for interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd+bind+peer-ip+vpn-instance+interface+source-ip) *session-name* **bind** **peer-ip** *peer-ip* [ **vpn-instance** *vpn-name* ] **interface** *interface-type* *interface-number* [ **source-ip** *source-ip* ]
     
     
     
     A BFD session for IPv4 is bound to an interface.
  3. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
     
     
     
     The local discriminator of the BFD session is created.
  4. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
     
     
     
     The remote discriminator of the BFD session is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The local and remote discriminators on the two ends of a BFD session must be correctly associated. That is, the local discriminator of the local device must be the same as the remote discriminator of the remote device, and the remote discriminator of the local device must be the same as the local discriminator of the remote device. If the association is incorrect, a BFD session cannot be set up.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure TE manual FRR.
  
  
  
  Perform the following steps on the ingress of the primary tunnel:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The tunnel interface view of the primary tunnel is displayed.
  3. Run [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute+bandwidth) [ **bandwidth** ]
     
     
     
     The TE FRR function is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Configure an FRR bypass tunnel.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The tunnel interface view of a bypass tunnel is displayed.
  3. Run [**tunnel-protocol mpls te**](cmdqueryname=tunnel-protocol+mpls+te)
     
     
     
     MPLS TE is configured as a tunnel protocol.
  4. Run [**destination**](cmdqueryname=destination) *ip-address*
     
     
     
     The LSR ID of an MP is configured as the destination address of the bypass tunnel.
  5. Run [**mpls te tunnel-id**](cmdqueryname=mpls+te+tunnel-id) *tunnel-id*
     
     
     
     A tunnel ID of the bypass tunnel is set.
  6. (Optional) Run [**mpls te path explicit-path**](cmdqueryname=mpls+te+path+explicit-path) *path-name*
     
     
     
     An explicit path is specified for the bypass tunnel.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Physical links of a bypass tunnel cannot overlap protected physical links of the primary tunnel.
  7. (Optional) Run [**mpls te bandwidth**](cmdqueryname=mpls+te+bandwidth+ct0) **ct0** *bandwidth*
     
     
     
     The bandwidth is set for the bypass tunnel.
  8. Run [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel)
     
     
     
     The bypass tunnel function is enabled.
     
     After a bypass tunnel is configured, the device automatically records routes related to the bypass tunnel.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Note the following settings to prevent a protection failure:
     
     + A tunnel interface can only be used by either a bypass tunnel or a backup tunnel. That is, you can configure either the [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel) command or [**mpls te backup**](cmdqueryname=mpls+te+backup) command.
     + A tunnel interface can only be used by either a bypass tunnel or a primary tunnel. That is, you can configure either the [**mpls te bypass-tunnel**](cmdqueryname=mpls+te+bypass-tunnel) command or [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) command.
  9. Run [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) *interface-type* *interface-number*
     
     
     
     The interface on which traffic is protected by the bypass tunnel is specified.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + A tunnel interface can only be used by either a bypass tunnel or a backup tunnel. That is, you can configure either the [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) command or [**mpls te backup**](cmdqueryname=mpls+te+backup) command.
     + A tunnel interface can only be used by either a bypass tunnel or a backup tunnel. That is, you can configure either the [**mpls te protected-interface**](cmdqueryname=mpls+te+protected-interface) command or [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute) command.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure MPLS TE Auto FRR.
  
  
  
  Perform the following steps on the ingress or a transit node of a primary tunnel:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr)
     
     
     
     MPLS TE Auto FRR is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the outbound interface on the primary tunnel is displayed.
  6. (Optional) Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr+link+node+default) { **link** | **node** | **default** }
     
     
     
     TE Auto FRR is enabled on the interface.
     
     By default, all MPLS TE-enabled interfaces support TE Auto FRR after MPLS TE Auto FRR is enabled globally. To disable TE Auto FRR on interfaces, run the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr+block) **block** command on these interfaces. The [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr+block) **block** command disables TE Auto FRR on interfaces, even if TE Auto FRR is enabled or re-enabled globally.
     
     By default, TE Auto FRR is disabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr+default) **default** command is run, the interface Auto FRR capability status is the same as the global Auto FRR capability status.
  7. Run [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute+bandwidth) [ **bandwidth** ]
     
     
     
     The TE FRR function is enabled.
     
     The **bandwidth** parameter can be configured to enable FRR bandwidth protection for the primary tunnel.
  8. (Optional) Run [**mpls te bypass-attributes**](cmdqueryname=mpls+te+bypass-attributes+bandwidth+priority) **bandwidth** *bandwidth* [ **priority** *setup-priority* [ *hold-priority* ] ]
     
     
     
     Attributes for the Auto FRR bypass tunnel are set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + These attributes for the Auto FRR bypass tunnel can be set only after the [**mpls te fast-reroute**](cmdqueryname=mpls+te+fast-reroute+bandwidth) **bandwidth** command is run for the primary tunnel.
     + The Auto FRR bypass tunnel bandwidth cannot exceed the primary tunnel bandwidth.
     + If no attributes are configured for an Auto FRR bypass tunnel, the Auto FRR bypass tunnel by default uses the same bandwidth as that of the primary tunnel.
     + The setup priority of the bypass tunnel cannot be higher than the holding priority. Each priority of the bypass tunnel cannot be higher than that of the primary tunnel.
     + If the primary tunnel bandwidth is changed or FRR is disabled, the bypass tunnel attributes are automatically deleted.
     + On one TE tunnel interface, the bypass tunnel bandwidth and the multi-CT are mutually exclusive.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure static BFD for CR-LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally on the local node, and the BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**bfd**](cmdqueryname=bfd+bind+mpls-te+interface+tunnel+te-lsp+backup) *session-name* **bind** **mpls-te** **interface** **tunnel** *interface-number* **te-lsp** [ **backup** ]
     
     
     
     The BFD session is bound to the primary or backup CR-LSP of the specified tunnel.
     
     If the **backup** parameter is specified, the BFD session is bound to the backup CR-LSP.
  5. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
     
     
     
     The local discriminator of the BFD session is configured.
  6. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
     
     
     
     The remote discriminator of the BFD session is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The local discriminator of the local device and the remote discriminator of the remote device are the same, and the remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
  7. Run [**process-pst**](cmdqueryname=process-pst)
     
     
     
     BFD is enabled to modify the port status table or link status table.
     
     
     
     If the BFD session on a trunk or VLAN member interface allows BFD to modify the port status table or link status table, and the interface is configured with the BFD session, you must configure the WTR time for the BFD session for detecting the interface. This prevents the BFD session on the interface from flapping when the member interface joins or leave the interface.
  8. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
     
     
     
     The minimum interval at which BFD packets are sent is configured.
  9. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
     
     
     
     The local minimum interval at which BFD packets are received is configured.
  10. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      The local BFD detection multiplier is configured.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure dynamic BFD for CR-LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally on the local node, and the BFD view is displayed.
  3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view is displayed.
  4. Run [**mpls te bfd enable**](cmdqueryname=mpls+te+bfd+enable)
     
     
     
     The capability of dynamically creating BFD sessions is enabled on the TE tunnel.
     
     The command configured in the tunnel interface view takes effect only on the current tunnel interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure CR-LSP hot standby.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
     
     
     
     The MPLS TE tunnel interface view is displayed.
  3. Run [**mpls te backup**](cmdqueryname=mpls+te+backup+hot-standby+mode+revertive+wtr+non-revertive) **hot-standby** [ **mode** { **revertive** [ **wtr** *interval* ] | **non-revertive** } | **overlap-path** | **wtr** [ *interval* ] | **dynamic-bandwidth** ]
     
     
     
     CR-LSP hot standby is configured.
     
     
     
     Select the following parameters as needed to enable sub-functions:
     + **mode** **revertive** [ **wtr** *interval* ]: enables a device to switch traffic back to the primary CR-LSP.
     + **mode** **non-revertive**: disables a device from switching traffic back to the primary CR-LSP.
     + **overlap-path**: allows a hot-standby CR-LSP to overlap the primary CR-LSP if no available path is provided for the hot-standby CR-LSP.
     + **wtr** *interval*: sets the time before a traffic switchback is performed.
     + **dynamic-bandwidth**: enables a hot-standby CR-LSP to obtain bandwidth resources only after the hot-standby CR-LSP takes over traffic from a faulty primary CR-LSP. This function helps efficiently use network resources and reduce network costs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BFD for TE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally on the local node, and the BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**bfd**](cmdqueryname=bfd+bind+mpls-te+interface+tunnel) *session-name* **bind** **mpls-te** **interface** **tunnel** *interface-number*
     
     
     
     The TE tunnel to be detected by BFD sessions is specified.
     
     
     
     When the TE tunnel is in the Down state, a BFD session cannot be established.
  5. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
     
     
     
     The local discriminator of the BFD session is configured.
  6. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
     
     
     
     The remote discriminator of the BFD session is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The local discriminator of the local device and the remote discriminator of the remote device are the same, and the remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
  7. Run [**process-pst**](cmdqueryname=process-pst)
     
     
     
     BFD is enabled to modify the port status table or link status table.
     
     
     
     If the BFD session on a trunk or VLAN member interface allows BFD to modify the port status table or link status table, and the interface is configured with the BFD session, you must configure the WTR time for the BFD session for detecting the interface. This prevents the BFD session on the interface from flapping when the member interface joins or leave the interface.
  8. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
     
     
     
     The minimum interval at which BFD packets are sent is configured.
  9. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
     
     
     
     The local minimum interval at which BFD packets are received is configured.
  10. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      The local BFD detection multiplier is configured.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure static BFD to monitor an LDP LSP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally on the local node, and the BFD view is displayed.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**bfd**](cmdqueryname=bfd+bind+ldp-lsp+peer-ip+nexthop+interface) *session-name* **bind** **ldp-lsp** **peer-ip** *ip-address* **nexthop** *ip-address* [ **interface** *interface-type* *interface-number* ]
     
     
     
     A BFD session is bound to an LDP LSP.
  5. Run [**discriminator**](cmdqueryname=discriminator+local) **local** *discr-value*
     
     
     
     The local discriminator of the BFD session is configured.
  6. Run [**discriminator**](cmdqueryname=discriminator+remote) **remote** *discr-value*
     
     
     
     The remote discriminator of the BFD session is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The local discriminator of the local device and the remote discriminator of the remote device are the same, and the remote discriminator of the local device and the local discriminator of the remote device are the same. A discriminator inconsistency causes the BFD session to fail to be established.
  7. Run [**process-pst**](cmdqueryname=process-pst)
     
     
     
     BFD is enabled to modify the port status table or link status table.
     
     
     
     If the BFD session on a trunk or VLAN member interface allows BFD to modify the port status table or link status table, and the interface is configured with the BFD session, you must configure the WTR time for the BFD session for detecting the interface. This prevents the BFD session on the interface from flapping when the member interface joins or leave the interface.
  8. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
     
     
     
     The minimum interval at which BFD packets are sent is configured.
  9. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
     
     
     
     The local minimum interval at which BFD packets are received is configured.
  10. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      The local BFD detection multiplier is configured.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure dynamic BFD for LDP LSPs.
  
  
  
  Perform the following steps on the ingress:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  5. Run [**mpls bfd enable**](cmdqueryname=mpls+bfd+enable)
     
     
     
     The capability of dynamically establishing a BFD session is configured on the ingress.
  6. Run [**mpls bfd-trigger**](cmdqueryname=mpls+bfd-trigger+host+fec-list) { **host** | **fec-list** *list-name* }
     
     
     
     A policy for establishing an LDP BFD session is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Perform the following steps on the egress:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The capability of passively creating a BFD session is configured on the egress.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BGP LSP FRR.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In a seamless MPLS scenario, BGP LSP FRR must be configured on both the ingress and a transit node.
  
  
  
  Perform the following steps on the ingress:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**auto-frr**](cmdqueryname=auto-frr)
     
     
     
     BGP Auto FRR is enabled for unicast routes.
  5. Run [**bestroute nexthop-resolved**](cmdqueryname=bestroute+nexthop-resolved+tunnel) **tunnel** [ **inherit-ip-cost** ]
     
     
     
     Labeled BGP IPv4 unicast routes can participate in route selection only when their next hops recurse to tunnels.
  6. Run [**ingress-lsp protect-mode bgp-frr**](cmdqueryname=ingress-lsp+protect-mode+bgp-frr)
     
     
     
     BGP LSP FRR is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Perform this step on each CSG and MASG to enable the protection switching function for the whole BGP LSP.
  7. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Perform the following steps on the transit node:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**auto-frr**](cmdqueryname=auto-frr)
     
     
     
     BGP Auto FRR is enabled for unicast routes.
  5. Run [**bestroute nexthop-resolved**](cmdqueryname=bestroute+nexthop-resolved+tunnel) **tunnel** [ **inherit-ip-cost** ]
     
     
     
     Labeled BGP IPv4 unicast routes can participate in route selection only when their next hops recurse to tunnels.
  6. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BFD for BGP tunnel.
  
  
  
  Perform the following steps on the ingress of an E2E BGP tunnel:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  5. Run [**mpls bgp bfd enable**](cmdqueryname=mpls+bgp+bfd+enable)
     
     
     
     The capability of dynamically establishing BGP BFD sessions is enabled on the ingress.
  6. Run [**mpls bgp bfd-trigger-tunnel**](cmdqueryname=mpls+bgp+bfd-trigger-tunnel+host+ip-prefix) { **host** | **ip-prefix** *ip-prefix-name* }
     
     
     
     A policy for dynamically establishing a BGP BFD session is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  Perform the following steps on the egress of an E2E BGP tunnel:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The capability of passively creating a BFD session is configured on the egress.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable VPN FRR in the VPN instance IPv4 address family view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  4. Run [**vpn frr**](cmdqueryname=vpn+frr)
     
     
     
     VPN FRR is enabled.
  5. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the VPN instance view.
  6. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  7. (Optional) Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  8. (Optional) Run [**peer**](cmdqueryname=peer+mpls-local-ifnet+disable) { *group-name* | *ipv4-address* } **mpls-local-ifnet** **disable**
     
     
     
     The capability of establishing an MPLS local IFNET tunnel between a CSG and MASG is disabled.
     
     
     
     In the inter-AS seamless MPLS network transmitting L3VPN services, a CSG and MASG establish an MP-EBGP peer relationship. Therefore, an MPLS local IFNET tunnel between the CSG and MASG is automatically established over the MP-EBGP peer relationship. The MPLS local IFNET tunnel fails to transmit traffic because the CSG and MASG are indirectly connected.
     
     If a fault occurs on the tunnel between the CSG and MASG, traffic recurses to the MPLS local IFNET tunnel, not a backup tunnel or an FRR bypass tunnel. As the MPLS local IFNET tunnel cannot forward traffic, traffic is interrupted. To prevent the traffic interruption, run the [**peer mpls-local-ifnet disable**](cmdqueryname=peer+mpls-local-ifnet+disable) command to disable the establishment of an MPLS local IFNET tunnel between the CSG and MASG.
  9. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  10. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
      
      
      
      A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
      
      The *delay-value* is an integer ranging from 0 to 3600, in seconds. The default *delay-value* is 0, indicating that the device on which FRR is configured selects a route to the intermediate device on the primary path without a delay.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Enable VPN FRR in the BGP-VPN instance IPv4 address family view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**peer**](cmdqueryname=peer+mpls-local-ifnet+disable) { *group-name* | *ipv4-address* } **mpls-local-ifnet** **disable**
     
     
     
     The capability of establishing an MPLS local IFNET tunnel between a CSG and MASG is disabled.
     
     In the inter-AS seamless MPLS network transmitting L3VPN services, a CSG and MASG establish an MP-EBGP peer relationship. Therefore, an MPLS local IFNET tunnel between the CSG and MASG is automatically established over the MP-EBGP peer relationship. The MPLS local IFNET tunnel fails to transmit traffic because the CSG and MASG are indirectly connected.
     
     If a fault occurs on the tunnel between the CSG and MASG, traffic recurses to the MPLS local IFNET tunnel, not a backup tunnel or an FRR bypass tunnel. As the MPLS local IFNET tunnel cannot forward traffic, traffic is interrupted. To prevent the traffic interruption, run the [**peer mpls-local-ifnet disable**](cmdqueryname=peer+mpls-local-ifnet+disable) command to disable the establishment of an MPLS local IFNET tunnel between the CSG and MASG.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  5. Run [**auto-frr**](cmdqueryname=auto-frr)
     
     
     
     VPN Auto FRR is enabled.
  6. (Optional) Run [**route-select delay**](cmdqueryname=route-select+delay) *delay-value*
     
     
     
     A delay for selecting a route to the intermediate device on the primary path is configured. After the primary path recovers, an appropriate delay ensures that traffic switches back to the primary path after the intermediate device completes refreshing forwarding entries.
     
     The *delay-value* is an integer ranging from 0 to 3600, in seconds. The default *delay-value* is 0, indicating that the device on which FRR is configured selects a route to the intermediate device on the primary path without a delay.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.