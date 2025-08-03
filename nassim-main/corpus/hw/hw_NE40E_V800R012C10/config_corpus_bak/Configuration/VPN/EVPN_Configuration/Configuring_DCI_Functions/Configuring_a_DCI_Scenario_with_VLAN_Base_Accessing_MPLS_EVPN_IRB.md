Configuring a DCI Scenario with VLAN Base Accessing MPLS EVPN IRB
=================================================================

In a DCI scenario, to enable a DCI network to carry Layer 2 or Layer 3 services, you can associate Ethernet sub-interfaces with VLANs for gateway or DCN access and configure EVPN IRB.

#### Context

VXLAN tunnels are established in each DC for intra-DC VM communication. To implement Layer 2 or Layer 3 service communication between VMs in different DCs, associate Ethernet sub-interfaces with VLANs, create L3VPN or EVPN instances, and configure EVPN IRB on PEs on the DCI backbone network. This type of networking can be deployed in either of the following modes:

* Integrated deployment: As shown in [Figure 1](#EN-US_TASK_0172370570__fig_dc_vrp_dci_cfg_002901), the DC gateway and DCI-PE are the same device (DCI-PE-GW). That is, the PE also functions as the DC gateway for DCN access.
  
  **Figure 1** Configuring a DCI scenario with VLAN base accessing MPLS EVPN IRB (PEs also functioning as gateways)  
  ![](images/fig_dc_vrp_dci_cfg_002901.png)
* Separate deployment: As shown in [Figure 2](#EN-US_TASK_0172370570__fig_dc_vrp_dci_cfg_002801), the DC gateway and PE (DCI-PE) are separately deployed. The DCI-PEs consider DC gateways as CEs, receive Layer 2 and Layer 3 service traffic through Ethernet sub-interfaces and VBDIF interfaces associated with VLANs, and forward the traffic to other DCs through the DCI backbone network.
  
  **Figure 2** Configuring a DCI scenario with VLAN base accessing MPLS EVPN IRB (separate deployment of PEs and gateways)  
  ![](images/fig_dc_vrp_dci_cfg_000401.png)


#### Pre-configuration Tasks

Before configuring a DCI scenario with VLAN base accessing MPLS EVPN IRB, complete the following task:

Configure Layer 3 route reachability on the IPv4 network.


#### Procedure

1. Configure BGP EVPN peers.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a BGP RR needs to be configured on the network, establish BGP EVPN peer relationships between all the PEs and the RR.
   
   
   
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enable BGP and enter its view.
   2. Run the [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* } command to configure the remote PE as a peer.
   3. (Optional) Run the [**peer**](cmdqueryname=peer+connect-interface) *ipv4-address* **connect-interface** *interface-type* *interface-number* [ *ipv4-source-address* ] command to specify a source interface and a source address for the setup of a TCP connection with the BGP peer. 
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If loopback interfaces are used to establish a BGP connection, it is recommended that the [**peer connect-interface**](cmdqueryname=peer+connect-interface) command be run on both ends to ensure correct connection. If this command is run on only one end, the BGP connection may fail to be established.
   4. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name* command to enter the BGP-VPN instance IPv4 or IPv6 address family view.
   5. Run the [**import-route**](cmdqueryname=import-route) { **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** | **ospfv3** *process-id* | **ripng** *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \* command to import other protocol routes into the BGP-VPN instance IPv4/IPv6 address family. If host IP route advertisement is required, configure **direct** in the command. To advertise the subnet route of the host, use a dynamic routing protocol (such as OSPF) to advertise the route and then perform this step to import the routes of the dynamic routing protocol. To advertise host IP routes, you only need to configure import of direct routes. To advertise the subnet route of the host, use a dynamic routing protocol (such as OSPF) to advertise the route and then perform this step to import the routes of the dynamic routing protocol.
   6. Run the [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn) command to configure IP prefix route advertisement. This type of route can be used to advertise host IP routes as well as the routes on the subnet where the device resides. This type of route can be used to advertise host IP routes as well as the routes on the subnet where the device resides.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   8. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view.
   9. Run the [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable** command to enable the function to exchange EVPN routes with a specified peer or peer group.
   10. Run the [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** { **irb** | **irbv6** } command to enable the function to advertise IRB/IRBv6 routes.
   11. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   12. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
2. (Optional) Configure an L3VPN instance to store and manage received VM routes. Perform this step if you want the network to carry Layer 3 services.
   
   
   
   For IPv4 services, configure an IPv4 L3VPN instance.
   
   1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   2. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to create the VPN instance IPv4 address family and enter its view.
   3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance IPv4 address family.
   4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn** command to set one or multiple VPN targets of the VPN instance IPv4 address family.
   5. Run the [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) command to enable the device to generate and advertise EVPN IP prefix routes and IRB routes.
   6. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn** command to apply a specified tunnel policy to the VPN instance IPv4 address family to associate the tunnel policy with the EVPN routes leaked to the VPN instance IPv4 address family.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv4 address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
   
   For IPv6 services, configure an IPv6 L3VPN instance.
   
   1. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   2. Run the [**ipv6-family**](cmdqueryname=ipv6-family) command to create the VPN instance IPv6 address family and enter its view.
   3. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to set an RD for the VPN instance IPv6 address family.
   4. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn** command to set one or multiple VPN targets for the VPN instance IPv6 address family.
   5. Run the [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) command to enable the device to generate and advertise EVPN IP prefix routes and IRB routes.
   6. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn** command to apply a specified tunnel policy to the VPN instance IPv6 address family to associate the tunnel policy with the EVPN routes leaked to the VPN instance IPv6 address family.
   7. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance IPv6 address family view.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the VPN instance view.
3. Configure access-side interfaces.
   
   
   * If you want the network to carry both Layer 2 and Layer 3 services, perform the following configurations:
     
     1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the view of the BD to be bound to an EVPN instance.
     2. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name* [ **bd-tag** *bd-tag* ] command to bind the BD to the EVPN instance. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command to create a Layer 2 sub-interface and enter its view.
     5. Run the [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] } command to specify the encapsulation type of packets allowed to pass through the interface.
     6. Run the [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** } command to enable the function to remove VLAN tags from received packets.
     7. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the Layer 2 sub-interface to a BD, so that the sub-interface can transmit data packets through this BD.
     8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     9. Run the [**interface**](cmdqueryname=interface) **vbdif** *bd-id* command to create a VBDIF interface and enter its view.
     10. Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the VBDIF interface to a VPN instance.
     11. (Optional) Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the interface.
     12. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ] or [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } command to configure an IPv4/IPv6 address for the VBDIF interface to implement Layer 3 communication.
     13. (Optional) Run the [**mac-address**](cmdqueryname=mac-address) *mac-address* command to configure a MAC address for the VBDIF interface.
     14. Run the [**vxlan anycast-gateway enable**](cmdqueryname=vxlan+anycast-gateway+enable) command to enable the distributed gateway function.
         
         After the distributed gateway function is enabled, the device discards ARP packets received from the network side and learns only ARP packets received from the user side and generates host routes accordingly.
     15. Run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) or [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command to enable the function to collect host information.
     16. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * If you want the network to carry only Layer 2 services, perform the following configurations:
     
     1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the view of the BD to be bound to an EVPN instance.
     2. Run the [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *evpn-name* [ **bd-tag** *bd-tag* ] command to bind the BD to the EVPN instance. By specifying different *bd-tag* values, you can bind multiple BDs to the same EVPN instance. In this way, VLAN services of different BDs can access the same EVPN instance while being isolated.
     3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     4. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command to create a Layer 2 sub-interface and enter its view.
     5. Run the [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] } command to specify the encapsulation type of packets allowed to pass through the interface.
     6. Run the [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** } command to enable the function to remove VLAN tags from received packets.
     7. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to add the Layer 2 sub-interface to a BD, so that the sub-interface can transmit data packets through this BD.
     8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   * If you want the network to carry only Layer 3 services, see [Binding Interfaces to a VPN Instance](dc_vrp_mpls-l3vpn-v4_cfg_0156.html) or [Binding Interfaces to a VPN Instance](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).
4. Configure an EVPN instance in BD mode.
   1. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to create a BD EVPN instance and enter the EVPN instance view.
   2. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the EVPN instance.
   3. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the EVPN instance. The export VPN target of the local end must be the same as the import VPN target of the remote end, and the import VPN target of the local end must be the same as the export VPN target of the remote end.
   4. (Optional) Run the [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* command to associate the current EVPN instance with an import route-policy.
      
      
      
      To more precisely control the import of routes into the EVPN instance, perform this step to specify an import route-policy and set attributes for eligible routes.
   5. (Optional) Run the [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* command to associate the current EVPN instance with an export route-policy.
      
      
      
      To more precisely control the advertisement of EVPN routes, perform this step to specify an export route-policy and set attributes for eligible routes.
   6. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to associate the EVPN instance with a tunnel policy.
      
      
      
      This configuration enables PEs to use TE tunnels to transmit data packets.
   7. (Optional) Run the [**mac limit**](cmdqueryname=mac+limit) *number* { **simply-alert** | **mac-unchanged** } command to specify the maximum number of MAC addresses allowed in the EVPN instance.
      
      
      
      A device consumes more system resources as it learns more MAC addresses, and may fail to operate when busy with service processing. To limit the maximum number of MAC addresses allowed in an EVPN instance and thereby improving device security and reliability, run the [**mac limit**](cmdqueryname=mac+limit) command. After this configuration, if the number of MAC addresses exceeds the preset value, an alarm is reported to prompt you to check the validity of existing MAC addresses.
   8. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. (Optional) Configure an RR. To minimize the number of BGP EVPN peers on the network, deploy an RR.
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enable BGP and enter its view.
   2. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view.
   3. Run the [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client) command to configure the device as an RR, and its peer as an RR client.
      
      
      
      The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and the specified peer or peer group functions as its client or clients.
   4. (Optional) Run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between clients through the RR.
      
      
      
      If the clients of an RR have established full-mesh connections with each other, run the [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command to disable route reflection between clients through the RR to reduce cost. The [**undo reflect between-clients**](cmdqueryname=undo+reflect+between-clients) command applies only to RRs.
   5. (Optional) Run the [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) { *cluster-id-value* | *cluster-id-ipv4* } command to configure a cluster ID for the RR.
      
      
      
      If a cluster has multiple RRs, you can use this command to set the same cluster ID for these RRs to prevent routing loops.
      
      The [**reflector cluster-id**](cmdqueryname=reflector+cluster-id) command applies only to RRs.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.