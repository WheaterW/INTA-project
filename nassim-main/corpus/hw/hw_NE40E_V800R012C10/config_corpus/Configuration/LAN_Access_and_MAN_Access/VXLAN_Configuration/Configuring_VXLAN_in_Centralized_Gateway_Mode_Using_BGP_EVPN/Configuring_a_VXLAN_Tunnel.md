Configuring a VXLAN Tunnel
==========================

To allow VXLAN tunnel establishment between VTEPs using EVPN, establish a BGP EVPN peer relationship, configure an EVPN instance, and configure ingress replication.

#### Context

In centralized VXLAN gateway scenarios, perform the following steps on the Layer 2 and Layer 3 VXLAN gateways to use EVPN for establishing VXLAN tunnels:

1. Configure a BGP EVPN peer relationship. Configure VXLAN gateways to establish BGP EVPN peer relationships so that they can exchange EVPN routes. If an RR has been deployed, each VXLAN gateway only needs to establish a BGP EVPN peer relationship with the RR.
2. (Optional) Configure an RR. After an RR is configured, each VXLAN gateway only needs to establish a BGP EVPN peer relationship with the RR. RR deployment reduces the number of BGP EVPN peer relationships to be established, simplifying configurations. A live-network device can be used as an RR, or a standalone RR can be deployed. Layer 3 VXLAN gateways are generally used as RRs, and Layer 2 VXLAN gateways as RR clients.
3. Configure an EVPN instance. EVPN instances can be used to manage EVPN routes received from and advertised to BGP EVPN peers.
4. Configure ingress replication. After ingress replication is configured for a VNI, the system uses BGP EVPN to construct a list of remote VTEPs. After a VXLAN gateway receives BUM packets, its sends a copy of the BUM packets to every VXLAN gateway in the list.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

BUM packet forwarding is implemented only using ingress replication. To establish a VXLAN tunnel between a Huawei device and a non-Huawei device, ensure that the non-Huawei device also has ingress replication configured. Otherwise, communication fails.



#### Procedure

1. Configure a BGP EVPN peer relationship.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      BGP is enabled, and the BGP view is displayed.
   2. (Optional) Run [**router-id**](cmdqueryname=router-id) *router-id-value*
      
      
      
      A BGP router ID is set.
   3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The peer device is configured as a BGP peer.
   4. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ]
      
      
      
      A source interface and a source address are specified to set up a TCP connection with the BGP peer.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When loopback interfaces are used to establish a BGP connection, running the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command on both ends is recommended to ensure the connectivity. If this command is run on only one end, the BGP connection may fail to be established.
   5. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
      
      
      
      The maximum number of hops is set for an EBGP EVPN connection.
      
      
      
      In most cases, a directly connected physical link must be available between EBGP EVPN peers. If you want to establish EBGP EVPN peer relationships between indirectly connected devices, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command. The command also can configure the maximum number of hops for an EBGP EVPN TCP connection.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When a loopback interface is used to establish an EBGP EVPN peer relationship, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command (of which the value of *hop-count* is not less than 2). Otherwise, the peer relationship fails to be established.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a specified peer or peer group.
   8. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **advertise encap-type vxlan**
      
      
      
      The device is enabled to advertise EVPN routes that carry the VXLAN encapsulation attribute to the peer or peer group.
   9. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **route-policy** *route-policy-name* { **import** | **export** }
      
      
      
      A routing policy is specified for routes received from or to be advertised to a BGP EVPN peer or peer group.
      
      
      
      After the routing policy is applied, the routes received from or to be advertised to a specified BGP EVPN peer or peer group will be filtered, ensuring that only desired routes are imported or advertised. This configuration helps manage routes and reduce required routing entries and system resources.
   10. (Optional) Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
       
       
       
       The maximum number of MAC advertisement routes that can be received from each peer is configured.
       
       If an EVPN instance may import many invalid MAC advertisement routes from peers and these routes occupy a large proportion of the total MAC advertisement routes. If the received MAC advertisement routes exceed the specified maximum number, the system displays an alarm, instructing users to check the validity of the MAC advertisement routes received in the EVPN instance.
   11. (Optional) Perform the following operations to enable the function to advertise the routes carrying the large-community attribute to BGP EVPN peers:
       
       
       
       The large-community attribute includes a 2-byte or 4-byte AS number and two 4-byte **LocalData** fields, allowing the administrator to flexibly use route-policies. Before enabling the function to advertise the routes carrying the large-community attribute to BGP EVPN peers, [configure the route-policy related to the large-community attribute](dc_vrp_bgp_cfg_4059.html) and use the route-policy to set the large-community attribute.
       
       
       
       1. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **route-policy** *route-policy-name* **export**
          
          The outbound route-policy of the BGP EVPN peer is configured.
       2. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise-large-community**
          
          The device is enabled to advertise the routes carrying the large-community attribute to BGP EVPN peers or peer groups.
          
          If the routes carrying the large-community attribute does not need to be advertised to one BGP EVPN peer in the peer group, run the [**peer**](cmdqueryname=peer) *ipv4-address* **advertise-large-community** **disable** command.
   12. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* **graceful-restart static-timer** *restart-time*
       
       
       
       The maximum duration from the time the local device finds that the peer device is restarted to the time a BGP EVPN session is re-established is set.
       
       
       
       BGP GR prevents traffic interruptions caused by re-establishment of a BGP peer relationship. You can run either the **graceful-restart timer restart** *time* or **peer graceful-restart static-timer** command to set this maximum wait time.
       
       * To set the maximum wait time for re-establishing all BGP peer relationships, run the **graceful-restart timer restart** command in the BGP view. The maximum wait time can be set to 3600s at most.
       * To set the maximum wait time for re-establishing a specified BGP-EVPN peer relationship, run the **peer graceful-restart static-timer** command in the BGP EVPN view. The maximum wait time can be set to a value greater than 3600s.
       
       If both the **graceful-restart timer restart** *time* and **peer graceful-restart static-timer** commands are run, the latter configuration takes effect.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This step can be performed only after GR has been enabled using the **graceful-restart** command in the BGP view.
   13. (Optional) Run the [**peer**](cmdqueryname=peer+path-attribute-treat+%28BGP-EVPN+address+family+view%29) *peerIpv4Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** } command to configure a special mode for processing BGP EVPN path attributes. Alternatively, run the [**peer**](cmdqueryname=peer) *peerIpv4Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value** command to configure a mode for processing incorrect BGP EVPN path attributes.
       
       
       
       A BGP EVPN Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP EVPN sessions may flap. To enhance reliability, you can perform this step to configure a processing mode for specified BGP EVPN path attributes or incorrect path attributes.
       
       The **path-attribute-treat** parameter specifies a path attribute processing mode, which can be any of the following ones:
       * Discarding specified attributes
       * Withdrawing the routes with specified attributes
       * Processing specified attributes as unknown attributes
       
       The **treat-with-error** parameter specifies a processing mode for incorrect path attributes. The mode can be as follows:
       
       * Accepting the path attributes with a value of 0.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP-EVPN address family view.
   15. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BGP view.
2. (Optional) Configure a Layer 3 VXLAN gateway as an RR. If an RR is configured, each VXLAN gateway only needs to [establish a BGP EVPN peer relationship](#EN-US_TASK_0172363801__bgp_evpn_peer) with the RR, reducing the number of BGP EVPN peer relationships to be established and simplifying configuration.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   2. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a specified peer or peer group.
   4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **next-hop-invariable**
      
      
      
      The device is prevented from changing the next hop address of a route when advertising the route to an EBGP peer.
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      The device is configured as an RR and an RR client is specified.
   6. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
      
      
      
      The function to filter received EVPN routes based on VPN targets is disabled. If you do not perform this step, the RR will fail to receive and reflect the routes sent by clients.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
3. Configure an EVPN instance.
   1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
      
      
      
      A BD EVPN instance is created, and the EVPN instance view is displayed.
   2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the EVPN instance.
   3. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the EVPN instance. The export VPN target of the local end must be the same as the import VPN target of the remote end, and the import VPN target of the local end must be the same as the export VPN target of the remote end.
   4. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
      
      
      
      The current EVPN instance is associated with an import routing policy.
      
      To control route import more precisely, perform this step to associate the EVPN instance with an import routing policy and set attributes for eligible routes.
   5. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
      
      
      
      The current EVPN instance is associated with an export routing policy.
      
      To control route export more precisely, perform this step to associate the EVPN instance with an export routing policy and set attributes for eligible routes.
   6. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      
      
      The EVPN instance is associated with a tunnel policy.
      
      This configuration allows data packets between PEs to be forwarded through a TE tunnel.
   7. (Optional) Run [**mac limit**](cmdqueryname=mac+limit) *number* { **simply-alert** | **mac-unchanged** }
      
      
      
      The maximum number of MAC addresses allowed by an EVPN instance is configured.
      
      After a device learns a large number of MAC addresses, system performance may deteriorate when the device is busy processing services. This is because MAC addresses consume system resources. To improve system security and reliability, run the [**mac limit**](cmdqueryname=mac+limit) command to configure the maximum number of MAC addresses allowed by an EVPN instance. If the number of MAC addresses learned by an EVPN instance exceeds the maximum number, the system displays an alarm message, instructing you to check the validity of MAC addresses in the EVPN instance.
   8. (Optional) Run [**mac-route no-advertise**](cmdqueryname=mac-route+no-advertise)
      
      
      
      The device is disabled from sending local MAC routes with the current VNI to the EVPN peer.
      
      
      
      In Layer 3 VXLAN gateway scenarios where Layer 2 traffic forwarding is not involved, perform this step to disable local MAC routes from being advertised to the EVPN peer. This configuration prevents the EVPN peer from receiving MAC routes, thereby conserving device resources.
   9. (Optional) Run [**local mac-only-route no-generate**](cmdqueryname=local+mac-only-route+no-generate)
      
      
      
      The device is disabled from generating an EVPN MAC route when the local MAC address exists in both a MAC address entry and an ARP/ND entry.
   10. (Optional) Run [**mac-ip route generate-mac**](cmdqueryname=mac-ip+route+generate-mac)
       
       
       
       The function to generate MAC address entries based on MAC/IP routes is enabled.
   11. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the EVPN instance view.
   12. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
       
       
       
       The BD view is displayed.
   13. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode**
       
       
       
       A VNI is created and associated with the BD, and split horizon is applied to the BD.
   14. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ]
       
       
       
       A specified EVPN instance is bound to the BD. By specifying different *bd-tag* values, you can bind multiple BDs with different VLANs to the same EVPN instance and isolate services in the BDs.
   15. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the BD view to return to the system view.
4. Configure ingress replication.
   1. Run [**interface**](cmdqueryname=interface) **nve** *nve-number*
      
      
      
      An NVE interface is created, and the NVE interface view is displayed.
   2. Run [**source**](cmdqueryname=source) *ip-address*
      
      
      
      An IP address is configured for the source VTEP.
   3. Run [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list protocol bgp**
      
      
      
      An ingress replication list is configured.
      
      
      
      After the ingress of a VXLAN tunnel receives broadcast, unknown unicast, and multicast (BUM) packets, it replicates these packets and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IP addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.