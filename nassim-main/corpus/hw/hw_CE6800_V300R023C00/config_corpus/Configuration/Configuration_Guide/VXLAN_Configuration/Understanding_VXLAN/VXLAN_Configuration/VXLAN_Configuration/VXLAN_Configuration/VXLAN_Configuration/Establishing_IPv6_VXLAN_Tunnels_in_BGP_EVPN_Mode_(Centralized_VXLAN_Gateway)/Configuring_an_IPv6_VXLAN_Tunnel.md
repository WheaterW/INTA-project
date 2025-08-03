Configuring an IPv6 VXLAN Tunnel
================================

Configuring an IPv6 VXLAN Tunnel

#### Prerequisites

Before configuring an IPv6 VXLAN tunnel, you have completed the following task:

* Configure IPv6 routes to enable Layer 3 communication between nodes on the current network.
* If the simplified mode is used for configuration, complete [Configuring a BD Profile in Simplified Mode](../vrp/dc_vrp_vxlan_cfg_bdprofile01.html).


#### Context

In centralized VXLAN gateway scenarios, perform the following steps on the Layer 2 and Layer 3 gateways to establish IPv6 VXLAN tunnels using EVPN:

1. Enable EVPN to function as the VXLAN control plane. EVPN must be enabled before other EVPN configurations can be performed.
2. Configure a BGP EVPN peer relationship. Configure gateways to establish BGP EVPN peer relationships so that they can exchange EVPN routes. If an RR has been deployed, each gateway must establish a BGP EVPN peer relationship with the RR only.
3. (Optional) Configure an RR. In this case, each gateway must establish a BGP EVPN peer relationship with the RR only. This reduces the number of BGP EVPN peer relationships as well as the overall configuration workload. An existing device can be configured to function as an RR, or a standalone RR can be deployed. Layer 3 gateways are generally used as RRs, and Layer 2 gateways as RR clients.
4. Configure EVPN instances. EVPN instances can be used to manage EVPN routes received from and advertised to BGP EVPN peers.
5. Configure ingress replication. After ingress replication is configured for a VNI, the system uses BGP EVPN to construct a list of remote VTEPs. After a gateway receives a BUM packet, it sends a copy to every gateway in the list.
6. Configure subscription to the status of the exact route to an IPv6 VXLAN tunnel destination. After this function is configured, an IPv6 VXLAN tunnel is considered up only if its source IPv6 address and destination IPv6 address are reachable.


#### Procedure

1. Enable EVPN to function as the VXLAN control plane. 
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enable EVPN to function as the VXLAN control plane. 
      
      
      ```
      [evpn-overlay enable](cmdqueryname=evpn-overlay+enable)
      ```
      
      By default, EVPN is not enabled to function as the VXLAN control plane.
2. Configure BGP EVPN peer relationships.
   1. Enable BGP and enter the BGP or BGP multi-instance view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
      ```
      
      By default, BGP is disabled. If an RR has been deployed, each gateway must establish a BGP EVPN peer relationship with the RR only.
   2. (Optional) Configure a BGP router ID.
      
      
      ```
      [router-id](cmdqueryname=router-id) ipv4-address
      ```
      
      By default, no BGP router ID is configured.
   3. Configure a peer device.
      
      
      ```
      [peer](cmdqueryname=peer+as-number) ipv6-address as-number as-number
      ```
      
      By default, no BGP peer is created.
   4. (Optional) Specify the source interface and source address used to establish a TCP connection with the BGP peer.
      
      
      ```
      [peer](cmdqueryname=peer+connect-interface) ipv6-address connect-interface interface-type interface-number [ ipv6-source-address ]
      ```
      
      By default, the outbound interface of a BGP message serves as the source interface.
      
      ![](../public_sys-resources/note_3.0-en-us.png) 
      
      When loopback interfaces are used to establish a BGP connection, running the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command on both ends is recommended to ensure connectivity. If this command is run on one end only, the BGP connection may fail to be established.
   5. (Optional) Set the maximum number of hops allowed by an EBGP EVPN connection.
      
      
      ```
      [peer](cmdqueryname=peer+ebgp-max-hop) ipv6-address [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
      ```
      
      The default value of *hop-count* is 255. In most cases, a directly connected physical link must be available between EBGP EVPN peers. If you want to establish EBGP EVPN peer relationships between indirectly connected peers, you must run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to configure the maximum number of hops for a TCP connection.
      
      ![](../public_sys-resources/note_3.0-en-us.png) 
      
      When a loopback interface is used to establish an EBGP EVPN peer relationship, you must run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) (where the value of *hop-count* is not less than 2) command. Otherwise, the peer relationship fails to be established.
   6. Enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
      
      
      ```
      [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
      ```
      
      By default, the BGP-EVPN address family view or BGP multi-instance EVPN address family view is disabled.
   7. Enable the ability to exchange EVPN routes with a specified peer or peer group.
      
      
      ```
      [peer](cmdqueryname=peer+enable) { group-name | ipv6-address } enable
      ```
      
      By default, the ability to exchange EVPN routes with a peer or peer group is automatically enabled only in the BGP-IPv6 unicast address family.
   8. (Optional) Specify a route-policy for routes received from or to be advertised to a BGP EVPN peer or peer group.
      
      
      ```
      [peer](cmdqueryname=peer+route-policy) { group-name | ipv6-address } route-policy route-policy-name { import | export }
      ```
      
      The route-policy helps the device to import or advertise desired routes only. This not only facilitates route management, but also reduces the routing table size and system resource consumption.
   9. (Optional) Set the maximum number of MAC advertisement routes that can be received from a peer.
      
      
      ```
      [peer](cmdqueryname=peer+mac-limit) { group-name | ipv6-address } [mac-limit](cmdqueryname=mac-limit) number [ percentage ] [ alert-only | idle-forever | idle-timeout times ]
      ```
      
      If a large proportion of MAC advertisement routes imported from a peer or peer group to an EVPN instance are inapplicable, you are advised to run this command to limit the maximum number of such routes that can be imported. If the number of imported MAC advertisement routes exceed the specified maximum, the device displays an alarm, prompting you to check the validity of such routes imported to the EVPN instance.
   10. (Optional) Enable next hop recursion of EVPN routes to default routes.
       
       
       ```
       [nexthop recursive-lookup default-route](cmdqueryname=nexthop+recursive-lookup+default-route)
       ```
       
       If a configuration error or fault occurs, the next hop of the EVPN route from the local VTEP to the remote VTEP may be unreachable, preventing the IPv6 VXLAN tunnel from being established. To prevent this situation, perform this step and configure the remote VTEP to send a default route to the local VTEP. When the next hop of the EVPN route from the local VTEP to the remote VTEP is unreachable, the EVPN route can recurse its next hop to the default route, allowing the IPv6 VXLAN tunnel to be successfully established.
   11. (Optional) Configure BGP to ignore the IGP metric when selecting the optimal route.
       
       
       ```
       [bestroute igp-metric-ignore](cmdqueryname=bestroute+igp-metric-ignore)
       ```
       
       By default, BGP uses the IGP metric as one of the conditions for selecting the optimal route. To exclude the IGP metric of next-hop routes as a condition for selecting the optimal BGP EVPN route on a VTEP, perform this step.
   12. (Optional) Enable BGP to advertise locally suppressed specific routes to a specified BGP EVPN peer or peer group.
       
       
       ```
       [peer](cmdqueryname=peer+advertise+suppressed-detail-route) { peerIpv6Addr | group-name } advertise suppressed-detail-route
       ```
       
       By default, BGP does not advertise locally suppressed specific routes to a BGP EVPN peer or peer group. Route summarization is usually configured for BGP to control the size of a BGP routing table, but this prevents locally suppressed specific routes from being sent to BGP EVPN peers by default. To advertise all specific routes to a specified BGP EVPN peer, perform this step.
   13. (Optional) Set a specified peer as an independent update peer-group.
       
       
       * To set a specified peer as an independent update peer-group, run the [**peer**](cmdqueryname=peer+update-group-independen) *peerIpv6Addr* **update-group-independent enable** command.
       * To set each peer in a peer group as an independent update peer-group, run the [**peer**](cmdqueryname=peer+update-group-independen) *peerGroupName* **update-group-independent** command.
       
       By default, no peer is set as an independent update peer-group. The configuration of a peer takes precedence over that of the peer group to which the peer belongs.
3. (Optional) Configure a Layer 3 gateway as an RR. In this case, each gateway needs to establish a BGP EVPN peer relationship with the RR only, reducing the number of BGP EVPN peer relationships to be established and simplifying configuration.
   1. Specify an RR and its clients.
      
      
      ```
      [peer](cmdqueryname=peer+reflect-client) { ipv6-address | group-name } [reflect-client](cmdqueryname=reflect-client)
      ```
      
      By default, the RR and its clients are not configured.
   2. (Optional) Configure the RR not to change the next hops of routes to be advertised to an EBGP EVPN peer.
      
      
      ```
      [peer](cmdqueryname=peer+next-hop-invariable) { group-name | ipv6-address } next-hop-invariable
      ```
      
      By default, a BGP EVPN speaker changes the next hops of routes to the interface that it uses to establish EBGP EVPN peer relationships before advertising these routes to EBGP EVPN peers.
   3. Disable the function to filter received EVPN routes based on VPN targets. If you do not perform this step, the RR will fail to receive and reflect the routes sent by clients.
      
      
      ```
      [undo policy vpn-target](cmdqueryname=undo+policy+vpn-target)
      ```
      
      By default, VPN-Target filtering is enabled.
   4. (Optional) Configure a reflection policy for the RR.
      
      
      ```
      [rr-filter](cmdqueryname=rr-filter) extended-list-number
      ```
      
      By default, no reflection policy is configured for an RR. Perform this step if you want the RR to reflect only the IBGP routes whose extended community attributes match those in the reflection policy.
   5. Exit the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Exit the BGP view or BGP multi-instance view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
4. (Optional) Configure EVPN instances in batches.
   
   
   
   If the simplified mode is used for configuration, perform this step to configure EVPN instances in batches by binding a BD range to a BD profile. After this step is performed, you do not need to perform Step 5.
   
   
   
   1. Enter the BD range view.
      
      
      ```
      [bridge-domain range](cmdqueryname=bridge-domain+range) { bdIdBgn [ to bdIdEnd ] } &<1-10>
      ```
   2. Bind the BD range to a BD profile.
      
      
      ```
      [binding bridge-domain profile](cmdqueryname=binding+bridge-domain+profile) profileId
      ```
   3. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
5. Configure an EVPN instance (one at a time).
   1. Enter the BD view.
      
      
      ```
      [bridge-domain](cmdqueryname=bridge-domain) bd-id
      ```
   2. (Optional) Bind the BD to a BD profile.
      
      
      ```
      [binding bridge-domain profile](cmdqueryname=binding+bridge-domain+profile) profileId
      ```
      
      When the simplified mode is used for configuration, perform this step. Steps c to f are then not required.
   3. Create a VNI and associate the VNI with the BD.
      
      
      ```
      [vxlan vni](cmdqueryname=vxlan+vni) vni-id
      ```
      
      By default, no VNI is created.
   4. Create an EVPN instance in a BD.
      
      
      ```
      [evpn](cmdqueryname=evpn)
      ```
      
      By default, no EVPN instance is created for VXLANs.
   5. Configure an RD for the EVPN instance.
      
      
      ```
      [route-distinguisher](cmdqueryname=route-distinguisher) { route-distinguisher | auto }
      ```
      
      By default, no RD is configured for BD EVPN instances.
   6. Configure VPN targets for the EVPN instance.
      
      
      ```
      [vpn-target](cmdqueryname=vpn-target) { vpn-target &<1-8> | auto } [ both | export-extcommunity | import-extcommunity ]
      ```
      
      By default, no VPN target is configured for BD EVPN instances. The import and export VPN targets of the local end must be the same as the export and import VPN targets of the remote end, respectively.
   7. (Optional) Associate the EVPN instance with an import route-policy.
      
      
      ```
      [import route-policy](cmdqueryname=import+route-policy) policy-name
      ```
      
      By default, an EVPN instance matches the export VPN targets of received routes against its import VPN targets to determine whether to import these routes. Perform this step to associate the EVPN instance with an import route-policy and set attributes for eligible routes. This enables you to control the routes to be imported into the EVPN instance more precisely.
   8. (Optional) Associate the EVPN instance with an export route-policy.
      
      
      ```
      [export route-policy](cmdqueryname=export+route-policy) policy-name
      ```
      
      By default, an EVPN instance adds all VPN targets in the export VPN target list to EVPN routes to be advertised to its peers. Perform this step to associate the EVPN instance with an export route-policy and set attributes for eligible routes. This enables you to control the routes to be advertised more precisely.
   9. (Optional) Disable the device from sending local MAC routes with the current VNI to the EVPN peer.
      
      
      ```
      [mac-route no-advertise](cmdqueryname=mac-route+no-advertise)
      ```
      
      Local MAC routes can be advertised by default. In Layer 3 gateway scenarios where Layer 2 traffic forwarding is not involved, perform this step to disable local MAC routes carrying the current VNI from being advertised to the EVPN peer gateway. This configuration prevents an EVPN peer gateway from receiving unnecessary MAC routes, thereby conserving device resources.
   10. (Optional) Disable the device from delivering a MAC address entry for the MAC route carrying the current VNI received from the EVPN peer.
       
       
       ```
       [mac rib-only](cmdqueryname=mac+rib-only)
       ```
       
       By default, a device delivers MAC entries for remote MAC routes.
       
       If Layer 3 gateways do not exchange Layer 2 traffic, perform this step to conserve forwarding entry resources.
   11. (Optional) Disable the device from generating an EVPN MAC route when the local MAC address exists in both a MAC address entry and an ARP/ND entry.
       
       
       ```
       [local mac-only-route no-generate](cmdqueryname=local+mac-only-route+no-generate)
       ```
       
       If a MAC address entry and an ARP/ND entry on the local gateway both contain the local MAC address, the gateway generates both an EVPN MAC/IP route and an EVPN MAC route by default. To optimize memory utilization, perform this step so that the gateway generates only an EVPN MAC/IP route. To ensure normal Layer 2 traffic forwarding, run the **mac-ip route generate-mac** command on the peer gateway to enable the function to generate MAC address entries based on MAC/IP routes.
   12. (Optional) Enable the function to generate MAC address entries based on MAC/IP routes.
       
       
       ```
       [mac-ip route generate-mac](cmdqueryname=mac-ip+route+generate-mac)
       ```
       
       
       
       By default, the function is not enabled.
       
       If the peer gateway is configured not to advertise MAC routes (using the **mac-route no-advertise** command) or not to generate MAC routes (using the **local mac-only-route no-generate** command), the local gateway cannot generate MAC entries by default. To ensure normal Layer 2 traffic forwarding, perform this step on the local gateway to enable the function to generate MAC entries based on MAC/IP routes.
   13. Exit the EVPN instance view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   14. Exit the BD view and return to the system view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
6. Configure ingress replication.
   1. Create an NVE interface and enter its view.
      
      
      ```
      [interface](cmdqueryname=interface) nve nve-number
      ```
   2. Configure an IPv6 address for the source VTEP.
      
      
      ```
      [source](cmdqueryname=source) ipv6-address
      ```
      
      By default, no IPv6 address is configured for a VTEP.
   3. Configure ingress replication.
      
      
      ```
      [vni](cmdqueryname=vni) vni-id head-end peer-list protocol bgp
      ```
      
      By default, no ingress replication is configured for a VNI.
      
      With this function, the ingress of an IPv6 VXLAN tunnel replicates and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IPv6 addresses to which the ingress of an IPv6 VXLAN tunnel should send replicated BUM packets.
7. (Optional) Enable subscription to the status of the exact route to the IPv6 VXLAN tunnel destination. The VXLAN tunnel can go up only when the exact route to its destination IPv6 address is reachable.
   
   
   ```
   [quit](cmdqueryname=quit)
   [vxlan tunnel-status track exact-route](cmdqueryname=vxlan+tunnel-status+track+exact-route)
   ```
   
   By default, subscription to the status of the exact route to an IPv6 VXLAN tunnel destination is disabled. An IPv6 VXLAN tunnel is considered up if the exact route of its source IPv6 address and the route of the network segment where its destination IPv6 address resides are reachable.
8. (Optional) Enable the device to use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   
   ```
   [assign forward nvo3 udp src-port extend enable](cmdqueryname=assign+forward+nvo3+udp+src-port+extend+enable)
   ```
   
   By default, the device does not use the extension mode when encapsulating the outer UDP source port number into VXLAN packets.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Only the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this command.
9. (Optional) Enable the device to add its router ID (a private extended community attribute) to locally generated EVPN routes.
   
   
   ```
   [evpn](cmdqueryname=evpn+%28system+view%29)
   [router-id-extend private enable](cmdqueryname=router-id-extend+private+enable)
   ```
   
   If both IPv4 and IPv6 VXLAN tunnels need to be established between two devices, one device's IP address is repeatedly added to the other device's ingress replication list while the IPv4 and IPv6 VXLAN tunnels are being established. As a result, each device forwards two copies of BUM traffic to its peer, leading to duplicate traffic. To address this problem, run the [**router-id-extend private enable**](cmdqueryname=router-id-extend+private+enable) command on each device so that they each add their router IDs to EVPN routes. After receiving the EVPN routes, the peer device checks whether they carry the same router ID. If they do, the EVPN routes are from the same device. In this case, the peer device adds only the IP address of the device whose EVPN routes carry the IPv4 VXLAN tunnel identifier to the ingress replication list, thereby preventing duplicate traffic.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```