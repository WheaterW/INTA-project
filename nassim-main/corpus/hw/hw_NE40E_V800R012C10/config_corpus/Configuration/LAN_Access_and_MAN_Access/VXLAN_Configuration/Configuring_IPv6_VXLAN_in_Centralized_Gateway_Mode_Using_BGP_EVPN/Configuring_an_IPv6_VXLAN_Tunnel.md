Configuring an IPv6 VXLAN Tunnel
================================

Using BGP EVPN to establish an IPv6 VXLAN tunnel between VTEPs involves a series of operations. These include establishing a BGP EVPN peer relationship, configuring an EVPN instance, and configuring ingress replication.

#### Context

To enable BGP EVPN to establish IPv6 VXLAN tunnels in centralized gateway scenarios, complete the following tasks on the involved gateways:

1. Configure a BGP EVPN peer relationship. After the gateways on an IPv6 VXLAN establish such a relationship, they can exchange EVPN routes. If an RR is deployed on the network, each gateway only needs to establish a BGP EVPN peer relationship with the RR.
2. (Optional) Configure an RR. The deployment of RRs simplifies configurations because fewer BGP EVPN peer relationships need to be established. An existing device can be configured to also function as an RR, or a new device can be deployed for this specific purpose. Layer 3 gateways on an IPv6 VXLAN are generally used as RRs, and Layer 2 gateways used as RR clients.
3. Configure an EVPN instance. EVPN instances can be used to manage EVPN routes received from and advertised to BGP EVPN peers.
4. Configure ingress replication. After ingress replication is configured on an IPv6 VXLAN gateway, the gateway uses BGP EVPN to construct a list of remote VTEP peers that share the same VNI with itself. After the gateway receives BUM packets, its sends a copy of the BUM packets to each gateway in the list.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, BUM packets can be forwarded only through ingress replication. This means that non-Huawei devices must have ingress replication configured to establish IPv6 VXLAN tunnels with Huawei devices. If ingress replication is not configured, the tunnels fail to be established.



#### Procedure

1. Configure a BGP EVPN peer relationship.
   1. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      BGP is enabled, and its view is displayed.
   2. (Optional) Run [**router-id**](cmdqueryname=router-id) *router-id-value*
      
      
      
      A BGP router ID is set.
   3. Run [**peer**](cmdqueryname=peer+as-number+%28BGP+view%29+%28IPv6%29) *ipv6-address* **as-number** *as-number*
      
      
      
      An IPv6 BGP peer is specified.
   4. (Optional) Run [**peer**](cmdqueryname=peer+connect-interface+%28BGP+view%29+%28IPv6%29) *ipv6-address* **connect-interface** *interface-type* *interface-number* [ *ipv6-source-address* ]
      
      
      
      A source interface and a source IPv6 address used to set up a TCP connection with the BGP peer are specified.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, you are advised to run the [**peer connect-interface**](cmdqueryname=peer+connect-interface+%28BGP+view%29+%28IPv6%29) command on both ends of the link to ensure connectivity. If this command is run on only one end, the BGP connection may fail to be established.
   5. (Optional) Run [**peer**](cmdqueryname=peer+ebgp-max-hop+%28BGP+view%29+%28IPv6%29) *ipv6-address* [**ebgp-max-hop**](cmdqueryname=ebgp-max-hop) [ *hop-count* ]
      
      
      
      The maximum number of hops allowed for establishing an EBGP EVPN peer relationship is configured.
      
      
      
      The default value of *hop-count* is 255. In most cases, a directly connected physical link must be available between EBGP EVPN peers. If you want to establish EBGP EVPN peer relationships between indirectly connected devices, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop+%28BGP+view%29+%28IPv6%29) command. This command allows the devices to establish a TCP connection across multiple hops.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      When loopback interfaces are used to establish an EBGP EVPN peer relationship, the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop+%28BGP+view%29+%28IPv6%29) command must be run, with *hop-count* being at least 2. Otherwise, the peer relationship fails to be established.
   6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+enable+%28BGP-EVPN+address+family+view%29+%28IPv6%29) { *group-name* | *ipv6-address* } **enable**
      
      
      
      The device is enabled to exchange EVPN routes with a specified peer or peer group.
   8. Run [**peer**](cmdqueryname=peer+advertise+encap-type) { *group-name* | *ipv6-address* } **advertise encap-type vxlan**
      
      
      
      The device is enabled to advertise EVPN routes that carry the VXLAN encapsulation attribute to the peer or peer group.
   9. (Optional) Run [**peer**](cmdqueryname=peer+route-policy+export+%28BGP-EVPN+address+family+view%29+%28IPv6%29) { *group-name* | *ipv6-address* } **route-policy** *route-policy-name* { **import** | **export** }
      
      
      
      A route-policy is specified for routes to be received from or advertised to the BGP EVPN peer or peer group.
      
      
      
      The route-policy helps the device import or advertise only desired routes. This reduces the routing table size and system resource consumption, facilitating route management.
   10. (Optional) Run [**peer**](cmdqueryname=peer+route-limit+%28BGP-EVPN+address+family+view%29) { *group-name* | *ipv6-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
       
       
       
       The maximum number of MAC advertisement routes that can be imported from the peer or peer group is configured.
       
       
       
       If an EVPN instance imports many inapplicable MAC advertisement routes from a peer or peer group and they account for a large proportion of the total number of MAC advertisement routes, you are advised to run the [**peer**](cmdqueryname=peer+route-limit+%28BGP-EVPN+address+family+view%29) { *group-name* | *ipv6-address* } [**mac-limit**](cmdqueryname=mac-limit) *number* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** *times* ] command. This command limits the maximum number of MAC advertisement routes that can be imported. If the imported MAC advertisement routes exceed the specified maximum number, the device displays an alarm, prompting you to check the validity of the MAC advertisement routes imported to the EVPN instance.
   11. (Optional) Perform the following operations to enable the device to advertise routes with the large-community attribute to BGP EVPN peers.
       
       
       
       The large-community attribute includes a 2-byte or 4-byte AS number and two 4-byte **LocalData** fields, allowing the administrator to flexibly use route-policies. Before enabling the function to advertise the routes carrying the large-community attribute to BGP EVPN peers, [configure the route-policy related to the large-community attribute](dc_vrp_bgp_cfg_4059.html) and use the route-policy to set the large-community attribute.
       
       
       
       1. Run the [**peer**](cmdqueryname=peer) { *peerIpv6Addr* | *group-name* } **route-policy** *route-policy-name* **export** command to apply an export route-policy to filter routes to be advertised to a specified BGP EVPN peer or peer group.
       2. Run the [**peer**](cmdqueryname=peer) { *peerIpv6Addr* | *group-name* } **advertise-large-community** command to enable the device to advertise routes with the large-community attribute to a specified BGP EVPN peer or peer group.
          
          If the routes with the large-community attribute do not need to be advertised to a BGP EVPN peer in the peer group, run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **advertise-large-community** **disable** command.
   12. (Optional) Run [**peer**](cmdqueryname=peer) *peerIpv6Addr* **graceful-restart** **static-timer** *restart-time*
       
       
       
       The maximum hold-off time for re-establishing BGP peer relationships, namely, the maximum duration from the time the local device finds that the peer device restarts to the time the local device re-establishes a BGP peer relationship with the peer device, is configured.
       
       
       
       Graceful restart (GR) prevents traffic interruption caused by the re-establishment of BGP peer relationships. To set the maximum hold-off time, run either of the following commands:
       * To set the maximum hold-off time for re-establishing all BGP peer relationships, run the [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) command in the BGP view. The hold-off time can be set to 3600s at the most.
       * To set the maximum hold-off time for re-establishing a BGP EVPN peer relationship, run the [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) command in the BGP view. Use this command if you want to set a hold-off time longer than 3600s.
       
       If both the [**graceful-restart timer restart**](cmdqueryname=graceful-restart+timer+restart) *time* and [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) commands are run, the [**peer graceful-restart static-timer**](cmdqueryname=peer+graceful-restart+static-timer) command configuration takes precedence.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       This step can be performed only after GR has been enabled using the [**graceful-restart**](cmdqueryname=graceful-restart) command in the BGP view.
   13. (Optional) Run the [**peer**](cmdqueryname=peer+path-attribute-treat+%28BGP-EVPN+address+family+view%29+%28IPv6%29) *peerIpv6Addr* **path-attribute-treat** **attribute-id** { *id* [ **to** *id2* ] } &<1-255> { **discard** | **withdraw** | **treat-as-unknown** } command to configure a special mode for processing BGP EVPN path attributes. Alternatively, run the [**peer**](cmdqueryname=peer) *peerIpv6Addr* **treat-with-error** **attribute-id** *id* **accept-zero-value** command to configure a mode for processing incorrect BGP EVPN path attributes.
       
       
       
       A BGP EVPN Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP EVPN sessions may flap. To enhance reliability, you can perform this step to configure a processing mode for specified BGP EVPN path attributes or incorrect path attributes.
       
       The **path-attribute-treat** parameter specifies a path attribute processing mode, which can be any of the following ones:
       * Discarding specified attributes
       * Withdrawing the routes with specified attributes
       * Processing specified attributes as unknown attributes
       
       The **treat-with-error** parameter specifies a processing mode for incorrect path attributes. The mode can be as follows:
       
       * Accepting the path attributes with a value of 0.
2. (Optional) Configure the Layer 3 gateway as an RR on the IPv6 VXLAN. If an RR is configured, each VXLAN gateway only needs to [establish a BGP EVPN peer relationship](#EN-US_TASK_0229407588__bgp_evpn_peer) with the RR. This simplifies configurations because fewer BGP EVPN peer relationships need to be established.
   1. Run [**peer**](cmdqueryname=peer+reflect-client+%28BGP-EVPN+address+family+view%29+%28IPv6%29) { *ipv6-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
      
      
      
      The device is configured as an RR, and RR clients are specified.
   2. (Optional) Run [**peer**](cmdqueryname=peer+next-hop-invariable+%28BGP-EVPN+address+family+view%29+%28IPv6%29) { *group-name* | *ipv6-address* } **next-hop-invariable**
      
      
      
      The device is enabled to keep the next hop address of a route unchanged when advertising the route to an EBGP EVPN peer.
   3. Run [**undo policy vpn-target**](cmdqueryname=undo+policy+vpn-target)
      
      
      
      The device is disabled from filtering received EVPN routes based on VPN targets. If you do not perform this step, the RR will fail to receive and reflect the routes sent by clients.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP-EVPN address family view.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
3. Configure an EVPN instance.
   1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
      
      
      
      A BD EVPN instance is created, and its view is displayed.
   2. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the EVPN instance.
   3. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      VPN targets are configured for the EVPN instance. The import and export VPN targets of the local end must be the same as the export and import VPN targets of the remote end, respectively.
   4. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
      
      
      
      The EVPN instance is associated with an import route-policy.
      
      
      
      Perform this step to associate the EVPN instance with an import route-policy and set attributes for eligible routes. This enables you to control routes to be imported into the EVPN instance more precisely.
   5. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
      
      
      
      The EVPN instance is associated with an export route-policy.
      
      
      
      Perform this step to associate the EVPN instance with an export route-policy and set attributes for eligible routes. This enables you to control routes to be advertised more precisely.
   6. (Optional) Run [**mac limit**](cmdqueryname=mac+limit) *number* { **simply-alert** | **mac-unchanged** }
      
      
      
      The maximum number of MAC addresses allowed in the EVPN instance is set.
      
      
      
      A device consumes more system resources as it learns more MAC addresses, meaning that the device may fail to operate when busy processing services. To limit the maximum number of MAC addresses allowed in an EVPN instance and thereby improving device security and reliability, run the [**mac limit**](cmdqueryname=mac+limit) command. After this configuration, if the number of MAC addresses exceeds the preset value, an alarm is triggered to prompt you to check the validity of existing MAC addresses.
   7. (Optional) Run [**mac-route no-advertise**](cmdqueryname=mac-route+no-advertise)
      
      
      
      The device is disabled from sending local MAC routes with the current VNI to the EVPN peer.
      
      
      
      In Layer 3 VXLAN gateway scenarios where Layer 2 traffic forwarding is not involved, perform this step to disable local MAC routes from being advertised to the EVPN peer. This configuration prevents the EVPN peer from receiving MAC routes, thereby conserving device resources.
   8. (Optional) Run [**local mac-only-route no-generate**](cmdqueryname=local+mac-only-route+no-generate)
      
      
      
      The device is disabled from generating an EVPN MAC route when the local MAC address exists in both a MAC address entry and an ARP/ND entry.
   9. (Optional) Run [**mac-ip route generate-mac**](cmdqueryname=mac-ip+route+generate-mac)
      
      
      
      The function to generate MAC address entries based on MAC/IP routes is enabled.
   10. Run [**quit**](cmdqueryname=quit)
       
       
       
       Exit the EVPN instance view.
   11. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
       
       
       
       The BD view is displayed.
   12. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode**
       
       
       
       A VNI is created and associated with the BD, and split horizon is specified for packet forwarding.
   13. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ]
       
       
       
       A specified EVPN instance is bound to the BD. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
   14. Run [**quit**](cmdqueryname=quit)
       
       
       
       Return to the system view.
4. Configure ingress replication.
   1. Run [**interface**](cmdqueryname=interface) **nve** *nve-number*
      
      
      
      An NVE interface is created, and its view is displayed.
   2. Run [**source**](cmdqueryname=source+%28NVE+interface+view%29+%28IPv6%29) *ipv6-address*
      
      
      
      An IPv6 address is configured for the source VTEP.
   3. Run [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list protocol bgp**
      
      
      
      Ingress replication is configured.
      
      
      
      With this function, the ingress of an IPv6 VXLAN tunnel replicates and sends a copy of any received BUM packets to each VTEP in the ingress replication list (a collection of remote VTEP IPv6 addresses).
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. (Optional) Enable the device to add its router ID (a private extended community attribute) to locally generated EVPN routes.
   1. Run [**evpn**](cmdqueryname=evpn+%28system+view%29)
      
      
      
      The global EVPN configuration view is displayed.
   2. Run [**router-id-extend private enable**](cmdqueryname=router-id-extend+private+enable)
      
      
      
      The device is enabled to add its router ID to locally generated EVPN routes.
      
      
      
      If both IPv4 and IPv6 VXLAN tunnels need to be established between two devices, one device's IP address is repeatedly added to the ingress replication list of the other device while the IPv4 and IPv6 VXLAN tunnels are being established. As a result, each device forwards two copies of BUM traffic to its peer, leading to duplicate traffic. To address this problem, run the [**router-id-extend private enable**](cmdqueryname=router-id-extend+private+enable) command on each device. This enables the device to add its router ID to EVPN routes. After receiving the EVPN routes, the peer device checks whether they carry the same router ID. If they do, the EVPN routes are from the same device. In this case, the peer device adds only the IP address of the device whose EVPN routes carry the IPv4 VXLAN tunnel identifier to the ingress replication list, thereby preventing duplicate traffic.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.