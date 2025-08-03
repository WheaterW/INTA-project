Understanding NFVI Distributed Gateways (Symmetric Mode)
========================================================

Huawei's network functions virtualization infrastructure (NFVI) telco cloud solution incorporates Data Center Interconnect (DCI) and data center network (DCN) solutions. A large volume of UE traffic enters the DCN and accesses its vUGW and vMSE. After being processed by the vUGW and vMSE, UE traffic (IPv4 or IPv6) is forwarded over the Internet through the DCN to the destination devices. Response traffic sent over the Internet from the destination devices to the UE also undergoes this process. To ensure that the UE traffic is load-balanced within the DCN in this process, you need to deploy the NFVI distributed gateway function on DCN devices.

![](../public_sys-resources/note_3.0-en-us.png) 

The vUGW is a unified packet gateway developed based on Huawei's CloudEdge solution. It can be used for 3rd Generation Partnership Project (3GPP) access in general packet radio service (GPRS), Universal Mobile Telecommunications System (UMTS), and Long Term Evolution (LTE) modes. The vUGW can function as a gateway GPRS support node (GGSN), serving gateway (S-GW), or packet data network gateway (P-GW) to meet carriers' various networking requirements in different phases and operational scenarios.

The vMSE is developed based on Huawei's multi-service engine (MSE). A carrier's network has many entities that provide different functions, including firewall, video acceleration, header enrichment, and URL filtering. All functions are added through patch installation. Over time, the network becomes increasingly slow, complicating service rollout and maintenance. To solve this problem, the vMSE integrates these different functions and manages them in a unified manner, providing value-added services for the data services initiated by users.


#### Networking Description

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001501), DC gateways are the DCN's border gateways, which exchange Internet routes with the external network through PEs. L2GW/L3GW1 and L2GW/L3GW2 connect to virtualized network functions (VNFs). VNF1 and VNF2, as virtualized NEs, can be deployed to respectively provide vUGW and vMSE functions and connect to L2GW/L3GW1 and L2GW/L3GW2 through interface processing units (IPUs).

This networking combines the distributed gateway function and the VXLAN active-active gateway function:

* The VXLAN active-active gateway function is deployed on DC gateways. Specifically, a bypass VXLAN tunnel is established between DC gateways. Both DC gateways use the same virtual anycast VTEP address to establish VXLAN tunnels with L2GW/L3GW1 and L2GW/L3GW2.
* The distributed gateway function is deployed on L2GW/L3GW1 and L2GW/L3GW2, and a VXLAN tunnel is established between L2GW/L3GW1 and L2GW/L3GW2.

![](../public_sys-resources/note_3.0-en-us.png) 

In the NFVI distributed gateway (symmetric mode) scenario, CloudEngine switches can function as only L2GWs/L3GWs. On the network shown in [Figure 1](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001501), each L2GW/L3GW represents two devices on the live network. Multichassis link aggregation (M-LAG) active-active is configured on the devices so that they function as one, thereby improving network reliability.


**Figure 1** NFVI distributed gateway networking (with active-active DC gateways)  
![](figure/en-us_image_0000001196094107.png)

#### Function Deployment

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001501), the number of bridge domains (BDs) must be planned according to the number of subnets to which the IPUs belong. For example, if five IP addresses planned for five IPUs are allocated to four subnets, you need to plan four different BDs. You need to configure all BDs and VBDIF interfaces only on L2GWs/L3GWs and bind all VBDIF interfaces to the same L3VPN instance. In addition, deploy the following functions on the network:

* Establish VPN BGP peer relationships between VNFs and DC gateways, so that VNFs can advertise UE routes to DC gateways.
* Configure VPN static routes on L2GW/L3GW1 and L2GW/L3GW2, or configure L2GWs/L3GWs to establish VPN IGP neighbor relationships with VNFs to obtain VNF routes with next hop addresses being IPU addresses.
* Establish BGP EVPN peer relationships between any two of the DC gateways and L2GWs/L3GWs. L2GWs/L3GWs can then advertise VNF routes to DC gateways and other L2GWs/L3GWs through BGP EVPN peer relationships. DC gateways can advertise the local loopback route and default route as well as obtained UE routes to L2GWs/L3GWs through BGP EVPN peer relationships.
* Traffic forwarded between the UE and Internet through VNFs is called north-south traffic, and traffic forwarded between VNF1 and VNF2 is called east-west traffic. To balance both types of traffic, you need to configure load balancing on DC gateways and L2GWs/L3GWs.


#### Generation of Forwarding Entries

After entering the DCN, traffic is forwarded from DC gateways to the VNF at Layer 3. The traffic from the VNF to DC gateways and then sent out of the DCN is also forwarded at Layer 3. On the network shown in [Figure 2](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001502), IPUs connect to multiple L2GWs/L3GWs. Layer 3 forwarding is used between DC gateways and VNFs. Some traffic forwarded by an L2GW/L3GW to the VNF is forwarded over a VXLAN tunnel to another L2GW/L3GW due to load balancing. After receiving VXLAN traffic, an L2GW/L3GW searches for matching routes. If these routes work in hybrid load-balancing mode, the L2GW/L3GW preferentially selects the access-side outbound interface to forward the traffic, thereby preventing loops.

**Figure 2** Traffic loop  
![](figure/en-us_image_0000001150067484.png)
In symmetric mode, forwarding entries are created on each DC gateway and L2GW/L3GW as follows:

1. BDs are deployed on each L2GW/L3GW and bound to links connecting to the IPU interfaces on the associated network segments. Then, VBDIF interfaces are configured as the gateways of these IPU interfaces. The number of BDs is the same as the number of network segments to which the IPU interfaces belong. A VPN static route is configured on each L2GW/L3GW or a VPN IGP neighbor relationship is established between each L2GW/L3GW and the VNF. This allows the L2GW/L3GW to generate a route forwarding entry with the destination address being the VNF address, next hop being the IPU address, and outbound interface being the associated VBDIF interface.
   
   **Figure 3** Route forwarding entry for traffic from an L2GW/L3GW to the VNF  
   ![](figure/en-us_image_0000001150228184.png)
2. After VPN static or IGP routes are configured on the L2GW/L3GW, they are imported into the BGP EVPN routing table and then sent as IP prefix routes to the DC gateway through the BGP EVPN peer relationship.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   There are multiple links and routes between the L2GW/L3GW and VNF. To implement load balancing, you need to enable the Add-Path function when configuring routes to be imported into the BGP EVPN routing table.
3. The next hop address of an IP prefix route received by the DC gateway is the IP address of the L2GW/L3GW, and the route recurses to a VXLAN tunnel. In this case, incoming traffic is forwarded at Layer 3.
   
   **Figure 4** Forwarding entries on the DC gateway and L2GW/L3GW  
   ![](figure/en-us_image_0000001196067961.png)
4. To establish a VPN BGP peer relationship with the VNF, the DC gateway needs to advertise its loopback address to the L2GW/L3GW. In addition, because the DC gateway uses the anycast VTEP address for the L2GW/L3GW, the VNF1-to-DCGW1 loopback protocol packets may be sent to DCGW2. Therefore, the DC gateway needs to advertise its loopback address to the other DC gateway. Finally, each L2GW/L3GW has a forwarding entry for the VPN route to the loopback addresses of DC gateways, and each DC gateway has a forwarding entry for the VPN route to the loopback address of the other DC gateway. After the VNF and DC gateways establish BGP peer relationships, the VNF can send UE routes to the DC gateways. The next hops of these routes are the VNF address.
   
   **Figure 5** Forwarding entries on the DC gateway and L2GW/L3GW  
   ![](figure/en-us_image_0000001196108071.png)
5. In symmetric mode, the L2GW/L3GW needs to learn UE routes. Therefore, a route-policy needs to be configured on the DC gateway to enable the DC gateway to advertise UE routes to the L2GW/L3GW after setting the original next hops of these routes as the gateway IP address. Except UE routes, the DCN does not need to be aware of other external routes. Consequently, another route-policy needs to be configured on the DC gateway to ensure that the DC gateway advertises only loopback routes and default routes to the L2GW/L3GW.
   
   **Figure 6** Forwarding entries on the DC gateway and L2GW/L3GW  
   ![](figure/en-us_image_0000001196108073.png)
6. As the border gateway of the DCN, the DC gateway can exchange Internet routes with external PEs, such as routes to server addresses on the Internet.
   
   **Figure 7** Forwarding entries on the DC gateway and L2GW/L3GW  
   ![](figure/en-us_image_0000001150068362.png)
7. To implement load balancing during traffic transmission, load balancing and Add-Path can be configured on the DC gateway and L2GW/L3GW. This balances both north-south and east-west traffic.
   
   * North-south traffic balancing: Use DCGW1 in [Figure 1](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001501) as an example. DCGW1 can receive EVPN routes to VNF2 from L2GW/L3GW1 and L2GW/L3GW2. By default, after load balancing is configured, DCGW1 sends half of all traffic destined for VNF2 to L2GW/L3GW1 and sends the other half to L2GW/L3GW2. However, L2GW/L3GW1 has only one link to VNF2, whereas L2GW/L3GW2 has two links to VNF2. As a result, the traffic is not evenly balanced. To address this issue, the Add-Path function must be configured on the L2GW/L3GWs. After Add-Path is configured, L2GW/L3GW2 advertises two routes with the same destination address to DCGW1 to implement load balancing.
   * East-west traffic balancing: Use L2GW/L3GW1 in [Figure 1](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001501) as an example. Because Add-Path is configured on L2GW/L3GW2, L2GW/L3GW1 receives two EVPN routes from L2GW/L3GW2. In addition, L2GW/L3GW1 has a static or IGP route with the next hop being IPU3. The destination address of these three routes is the IP address of VNF2. To implement load balancing, hybrid load balancing among EVPN routes and routes of other routing protocols needs to be deployed.


#### Traffic Forwarding Process

[Figure 8](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001509) shows the process of forwarding north-south traffic (from a UE to the Internet).

1. Upon receipt of UE traffic, the base station encapsulates the packets and redirects them to a GPRS tunneling protocol (GTP) tunnel whose destination address is the VNF address. The encapsulated packets reach the DC gateway through IP forwarding.
2. After receiving these packets, the DC gateway searches the VRF table and finds that the next hop of the forwarding entry corresponding to the VNF address is an IPU address and the outbound interface is a VXLAN tunnel. The DC gateway then performs VXLAN encapsulation and forwards the packets to the L2GW/L3GW at Layer 3.
3. Upon receipt of these packets, the L2GW/L3GW finds the corresponding VPN instance based on the L3VNI, searches for a matching route in the VPN instance's routing table based on the VNF address, and forwards the packets to the VNF.
4. After receiving the packets, the VNF removes their GTP tunnel header, searches the routing table based on their destination addresses, and forwards them to the L2GW/L3GW through the VNF's default gateway.
5. After receiving the packets, the L2GW/L3GW searches their VRF table for a matching forwarding entry. According to the default route advertised by the DC gateway to the L2GW/L3GW, the packets are encapsulated with the L3VNI and then forwarded to the DC gateway through the VXLAN tunnel.
6. Upon receipt, the DC gateway searches the corresponding VRF table for a matching forwarding entry based on the L3VNI and forwards these packets to the Internet.

**Figure 8** Process of forwarding north-south traffic from a UE to the Internet  
![](figure/en-us_image_0000001150252018.png)

[Figure 9](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001510) shows the process of forwarding north-south traffic from the Internet to a UE through the VNF.

1. A device on the Internet sends response traffic to a UE. The destination address of the response traffic is the destination address of the UE route. The route is advertised by the VNF to the DC gateway through the VPN BGP peer relationship, and the DC gateway in turn advertises the route to the Internet. Therefore, the response traffic must first be forwarded to the VNF.
2. After the response traffic reaches the DC gateway, the DC gateway searches the routing table for forwarding entries corresponding to UE routes. These routes are learned by the DC gateway from the VNF over the VPN BGP peer relationship and eventually recurse to VXLAN tunnels. The response packets are encapsulated into VXLAN packets and forwarded to the L2GW/L3GW at Layer 3.
3. Upon receipt of these packets, the L2GW/L3GW finds the corresponding VPN instance based on the L3VNI, searches for a matching route in the VPN instance's routing table based on the UE IP address, and forwards these packets to the VNF.
4. Upon receipt, the VNF processes the packets and finds the base station corresponding to the destination address of the UE. The VNF then encapsulates tunnel information into these packets (with the base station as the destination) and forwards them to the L2GW/L3GW through the default gateway.
5. Upon receipt, the L2GW/L3GW searches its VRF table for the default route advertised by the DC gateway to the L2GW/L3GW. Then, the L2GW/L3GW encapsulates the packets with the L3VNI and forwards them to the DC gateway over a VXLAN tunnel.
6. Upon receipt, the DC gateway searches its VRF table for the default (or specific) route based on the L3VNI and forwards these packets to the destination base station. The base station then decapsulates these packets and sends them to the target UE.

**Figure 9** Process of forwarding north-south traffic from the Internet to a UE  
![](figure/en-us_image_0000001196131887.png)

During this process, the VNF may (based on the packet information) send the received packets to another VNF for value-added service processing. In this case, east-west traffic is generated. [Figure 10](#EN-US_CONCEPT_0000001195967335__fig_dc_vrp_evpn_feature_001511) shows the process of forwarding east-west traffic (from VNF1 to VNF2), which differs from the north-south traffic forwarding process in packet processing after packets reach VNF1:

1. VNF1 sends a received packet to VNF2 for processing. VNF2 re-encapsulates the packet by using its own address as the destination address of the packet and sends the packet to the L2GW/L3GW1 over the default route.
2. Upon receipt, the L2GW/L3GW1 searches its VRF table and finds that multiple load-balancing routes exist. Some routes use the IPU as the outbound interface, and some routes use L2GW/L3GW2 as the next hop.
3. If these routes work in hybrid load-balancing mode, L2GW/L3GW1 preferentially selects only the routes with the outbound interfaces being IPUs and steers packets to VNF2 to prevent loops. If these routes do not work in hybrid load-balancing mode, L2GW/L3GW1 forwards packets along load-balancing routes. Packets are encapsulated into VXLAN packets before being sent to L2GW/L3GW2 at Layer 2. After these packets reach L2GW/L3GW2, L2GW/L3GW2 finds the corresponding BD based on the L2VNI, then finds the destination MAC address, and finally forwards these packets to VNF2.
4. Upon receipt, VNF2 processes the packet and forwards it to the Internet server. The subsequent forwarding process is the same as the process for forwarding north-south traffic.

**Figure 10** Process of forwarding east-west traffic (from VNF1 to VNF2)  
![](figure/en-us_image_0000001150092198.png)