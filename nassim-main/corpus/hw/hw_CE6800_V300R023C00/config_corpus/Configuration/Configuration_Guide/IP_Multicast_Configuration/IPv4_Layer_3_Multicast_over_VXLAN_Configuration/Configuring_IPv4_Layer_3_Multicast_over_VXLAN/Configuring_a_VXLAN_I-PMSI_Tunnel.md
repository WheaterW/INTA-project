Configuring a VXLAN I-PMSI Tunnel
=================================

Configuring a VXLAN I-PMSI Tunnel

#### Context

An I-PMSI tunnel is a PMSI tunnel that connects all PEs on the same MVPN. This enables all PEs on the same MVPN to receive multicast data traffic from the I-PMSI tunnel. In a scenario where VXLAN gateways are deployed in distributed mode, VXLAN is used to establish I-PMSI tunnels as PEs functioning as VXLAN gateways have established VXLAN tunnels with each other. Perform the following steps on each of the PEs functioning as VXLAN gateways:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an MVPN ID.
   
   
   ```
   [multicast mvpn](cmdqueryname=multicast+mvpn) mvpn-id
   ```
   
   An MVPN ID is the IP address of the originator PE on an MVPN. The MVPN ID is used as the value of the Administrator field in the VRF Route Import extended community attribute. If no MVPN ID is configured, BGP EVPN routes and C-multicast routes sent by a PE cannot carry the VRF Route Import extended community attribute.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The MVPN ID configured on a distributed VXLAN gateway must be the same as the gateway's VTEP IP address. If VXLAN gateways are deployed in M-LAG active-active mode, the master and backup gateways must have the same VTEP IP address.
3. Enter the VPN instance view.
   
   
   ```
   [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
   ```
4. Enter the VPN instance IPv4 address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family)
   ```
5. Configure an RD for the VPN instance IPv4 address family.
   
   
   ```
   [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
   ```
   
   A VPN instance IPv4 address family takes effect only after being assigned an RD. The RDs of different VPN instance IPv4 address families on the same PE must be different.
6. Configure a VPN-Target extended community.
   
   
   ```
   [vpn-target](cmdqueryname=vpn-target) { vpn-target } &<1-8> [ vrfRtType ]
   ```
7. Enable multicast routing for the VPN instance IPv4 address family.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
   ```
   
   By default, multicast routing is not enabled for a VPN instance IPv4 address family.
8. Configure a local VPN instance ID for the sender PE on the MVPN.
   
   
   ```
   [multicast mvpn route-import local-admin-id](cmdqueryname=multicast+mvpn+route-import+local-admin-id) local-admin-id
   ```
   
   By default, no local VPN instance ID is configured for a sender PE on an MVPN.
   
   The VRF Route Import extended community is in the format of Administrator field: Local Administrator field, where the Local Administrator field represents the sender PE's local VPN instance ID.
   
   A local VPN instance cannot share the same *local-admin-id* with other VPN instances.
9. Enter the VPN instance IPv4 address family MVPN view.
   
   
   ```
   [mvpn](cmdqueryname=mvpn)
   ```
10. (Optional) Configure an MVPN target for the VPN instance MVPN address family.
    
    
    ```
    [vpn-target](cmdqueryname=vpn-target) { vrfRT } & <1-8> [ vrfRTType ]
    ```
    
    
    
    By default, no MVPN target is configured for the VPN instance MVPN address family. The VPN instance MVPN address family uses the VPN target configured in the VPN instance IPv4 address family view as the MVPN target.
    
    When the routes of a VPN instance MVPN address family need to be isolated from those of the IPv4 address family belonging to the same VPN instance, perform this step to configure an exclusive MVPN target for the VPN instance MVPN address family.
11. Configure BGP as the signaling protocol for transmitting C-multicast routes.
    
    
    ```
    [c-multicast signaling](cmdqueryname=c-multicast+signaling) bgp
    ```
    
    
    
    By default, no signaling protocol is configured for transmitting C-multicast routes. To configure a signaling protocol for a PE to transmit C-multicast routes, run the [**c-multicast signaling**](cmdqueryname=c-multicast+signaling) command.
12. (Optional) Configure inter-AS automatic discovery.
    
    
    ```
    [auto-discovery inter-as](cmdqueryname=auto-discovery+inter-as)
    ```
    
    
    
    By default, inter-AS automatic discovery is disabled.
    
    In a scenario where an NG MVPN crosses different ASs, to enable PEs in different ASs to exchange Intra-AD routes for automatic MVPN peer discovery, perform this step.
13. (Optional) Enable PIM-SM RPTs to be set up not across the public network.
    
    
    ```
    [spt-only mode](cmdqueryname=spt-only+mode)
    ```
    
    
    
    If receivers use the (S, G) join mode, skip this step. By default, no PIM-SM RPTs are established on a multicast network.
    
    If receivers use the (\*, G) join mode, perform this step to configure the PIM-SM RPT setup mode.
14. (Optional) Enable the function of advertising (S, G) entry information in MSDP SA messages to the remote PE through BGP Source Active A-D routes.
    
    
    ```
    [import msdp](cmdqueryname=import+msdp)
    ```
    
    
    
    By default, (S, G) entry information in MSDP SA messages is not transmitted to the remote PE through BGP Source Active A-D routes.
    
    If PIM-SM RPT setup is not across the public network, you can deploy VPN RPs on PEs or CEs. If an RP is deployed on a CE, the CE needs to establish an MSDP peer relationship with its connected PE and transmit (S, G) entry information to the PE through MSDP SA messages. To enable this PE to transmit the (S, G) entry information to the remote PE through BGP Source Active A-D routes, perform this step.
15. (Optional) Enable the function to advertise (S, G) entry information in BGP Source Active A-D routes to the RP through MSDP SA messages.
    
    
    ```
    [export msdp](cmdqueryname=export+msdp)
    ```
    
    
    
    By default, (S, G) entry information in BGP Source Active A-D routes is not transmitted to the RP through MSDP SA messages.
    
    If PIM-SM RPT setup is not across the public network, you can deploy VPN RPs on PEs or CEs. If an RP is deployed on a CE, the CE needs to establish an MSDP peer relationship with its connected PE. To enable this PE to transmit (S, G) entry information in BGP Source Active A-D routes to the remote CE, perform this step.
16. (Optional) Configure a pruning delay during the RPT-to-SPT switchover in a scenario where PIM-SM RPT setup is across the public network.
    
    
    ```
    [rpt-prune-delay](cmdqueryname=rpt-prune-delay) delay-time
    ```
    
    By default, the pruning delay during the RPT-to-SPT switchover is 60 seconds.
17. Enter the MVPN I-PMSI view.
    
    
    ```
    [ipmsi-tunnel](cmdqueryname=ipmsi-tunnel)
    ```
18. Configure the device to use VXLAN to establish I-PMSI tunnels.
    
    
    ```
    [vxlan static](cmdqueryname=vxlan+static)
    ```
    
    
    
    By default, no I-PMSI tunnel establishment mode is configured.
19. Exit the VPN instance IPv4 address family MVPN view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
20. Exit the VPN instance IPv4 address family view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
21. Bind a VNI to the VPN instance.
    
    
    ```
    [vxlan vni](cmdqueryname=vxlan+vni) vni-id
    ```
22. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```