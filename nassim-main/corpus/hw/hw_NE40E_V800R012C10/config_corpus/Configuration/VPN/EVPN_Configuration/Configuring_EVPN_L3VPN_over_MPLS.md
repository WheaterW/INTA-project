Configuring EVPN L3VPN over MPLS
================================

On DCI and IP RAN networks, you can configure EVPN L3VPN over MPLS to carry Layer 3 services.

#### Usage Scenario

On a traditional network, BGP/MPLS IP VPN is often used to carry Layer 3 services. To additionally carry Layer 2 services, users have to deploy an L2VPN over the existing network, driving up deployment and O&M costs. To address this problem, deploy EVPN L3VPN over MPLS to carry Layer 3 services. To additionally carry Layer 2 services, you only need to add some EVPN configurations, achieving unified transport of both Layer 2 and Layer 3 services.

EVPN L3VPN over MPLS can replace BGP/MPLS IP VPN in the following scenarios to carry Layer 3 services:

* Intra-AS mutual VPN communication
  
  On the network shown in [Figure 1](#EN-US_TASK_0172370478__fig1794292110710), the VPNs at Site1 and Site2 need to communicate through the public MPLS network. To implement this communication, perform the following configurations:
  1. Configure an L3VPN instance on each PE to manage VPN routes.
  2. Establish a BGP EVPN peer relationship between the PEs to transmit EVPN routes carrying VPN routes.
  3. Establish an IGP neighbor relationship or BGP peer relationship between each PE and CE at the access side to exchange VPN routes.
  **Figure 1** Intra-AS mutual VPN communication  
  ![](figure/en-us_image_0000001227794701.png)
* Inter-AS mutual VPN communication
  
  On the network shown in [Figure 2](#EN-US_TASK_0172370478__fig163891638173), the VPNs at Site1 and Site2 need to communicate through two public MPLS networks in different ASs. To implement this communication, perform the following configurations:
  1. Configure an L3VPN instance on each PE to manage VPN routes.
  2. Establish IBGP EVPN peer relationships between PEs and ASBRs and an EBGP EVPN peer relationship between the ASBRs to transmit EVPN routes carrying VPN routes between the PEs.
  3. Establish an IGP neighbor relationship or BGP peer relationship between each PE and CE at the access side to exchange VPN routes.
  **Figure 2** Inter-AS mutual VPN communication  
  ![](figure/en-us_image_0000001228194751.png)
* DCI network
  
  The EVPN function applies to traditional DCs that interconnect through a DCI network. On the network shown in [Figure 3](#EN-US_TASK_0172370478__fig340018541475), DC GWs and DCI-PEs are separately deployed. The DCI-PEs consider the connected DC GWs as CEs, receive VM IP routes from the DCs through a routing protocol, and save and maintain the received routes. Deploying an EVPN over the DCI backbone network allows VM IP routes to be transmitted between DCs, implementing inter-DC VM communication. To implement this communication, perform the following configurations:
  1. Configure an L3VPN instance on each PE to manage VM IP routes.
  2. Establish an IBGP EVPN peer relationship between the PEs to transmit EVPN routes carrying VM IP routes.
  3. Establish an IGP neighbor relationship or BGP peer relationship between each PE and DC GW to exchange VM IP routes.
  **Figure 3** DCI network  
  ![](figure/en-us_image_0000001182875002.png "Click to enlarge")
* L2VPN accessing L3VPN
  
  In L2VPN accessing L3VPN scenarios, EVPN can be used as a substitute for BGP VPNv4 to function as the control plane of an L3VPN. For details about the method of configuring the L2VPN and stitching devices, see [Configuring L2VPN Accessing L3VPN](dc_vrp_l2-l3_cfg_5000.html). For details about the method of configuring the L3VPN, see the corresponding information in this section.
#### Pre-configuration Tasks

Before configuring EVPN L3VPN over MPLS, complete the following tasks:

* Configure Layer 3 route reachability on the IPv4 network.


[Configuring an L3VPN Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0039.html)

You can configure an L3VPN instance to store and manage received VPN routes or VM routes.

[Configuring BGP EVPN Peer Relationships](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0074.html)

You can configure BGP EVPN peer relationships between PEs or between PEs and ASBRs as required to exchange EVPN routes between the PEs. Additionally, you can configure BGP RRs to minimize the number of peer relationships, saving network resources.

[Configuring Route Exchange Between PEs and Access-Side Devices](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0073.html)

PEs and access-side devices can communicate through BGP, static routes (including default routes), or IGP. Configure route exchange between PEs and access-side devices according to the network plan.

[(Optional) Re-Encapsulating IRB (v6) Routes into the desired Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0071.html)

If you want to convert the IRB routes carrying the network segment address of a tenant host that are received by a device into host IP prefix routes or ARP routes, or convert the IRBv6 routes carrying the IPv6 network segment address of a tenant host that are received by a device into host IPv6 prefix routes or ND routes, you must enable the device to re-encapsulate IRB or IRBv6 routes into the desired routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0072.html)

After configuring EVPN L3VPN over MPLS, verify the EVPN and VPN routes received by devices.