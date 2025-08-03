Configuring the NFVI Distributed Gateway Function (Segmented SR Tunnels)
========================================================================

In the NFVI telco cloud solution, the NFVI distributed gateway function allows UE traffic to be processed by vUGWs and vMSEs and transmitted over a DCN through segmented SR tunnels as well as being transmitted within a DCN in load-balancing mode.

#### Usage Scenario

The NFVI telco cloud solution uses the DCI + DCN networking. A large amount of UE traffic is sent to vUGWs and vMSEs on the DCN. After being processed by the vUGWs and vMSEs, the UE traffic is forwarded over the DCN to destination devices on the Internet. The destination devices send traffic to UEs in similar ways. To achieve these functions and ensure traffic load balancing on the DCN, you need to deploy the NFVI distributed gateway function.

[Figure 1](#EN-US_TASK_0172370574__fig_dc_vrp_evpn_cfg_012101) shows the networking of an NFVI distributed gateway (segmented SR tunnels). DC GWs, which are the border gateways of the DCN, exchange Internet routes with external devices over PEs. L2GW/L3GW1 and L2GW/L3GW2 are connected to VNFs. VNF1 and VNF2 that function as virtualized NEs are deployed to implement the vUGW functions and vMSE functions, respectively. VNF1 and VNF2 are connected to L2GW/L3GW1 and L2GW/L3GW2 through IPUs.

In NFVI distributed gateway networking (segmented SR tunnels), the number of bridge domains (BDs) needs to be planned based on the number of network segments corresponding to each IPU. An example assumes that the five IP addresses planned for five IPUs belong to four network segments. In this case, four BDs need to be planned. You need to configure the BDs and the corresponding VBDIF interfaces on all DC GWs and L2GWs/L3GWs and bind all the VBDIF interfaces to the same L3VPN instance. In addition, the following functions need to be deployed on the network:

* Establish BGP VPN peer relationships between VNFs and DC GWs so that the VNFs can advertise UE routes (UE IP addresses) to DC GWs.
* On L2GW/L3GW1 and L2GW/L3GW2, configure static VPN routes with the IP addresses of VNFs as the destination addresses and the IP addresses of IPUs as next-hop addresses.
* Establish BGP EVPN peer relationships between any DC GW and L2GW/L3GW. L2GWs/L3GWs can then flood the static routes destined for VNFs to other devices based on the BGP EVPN peer relationships. DC GWs can then advertise local loopback routes and default routes to L2GWs/L3GWs through BGP EVPN peer relationships.
* Establish BGP VPNv4/v6 peer relationships between DC GWs and PEs. DC GWs can then advertise UE routes to PEs and receive the Internet routes sent by external devices based on the BGP VPNv4/v6 peer relationships.
* Deploy SR tunnels between PEs and DC GWs and between DC GWs and L2GWs/L3GWs to carry service traffic.
* The traffic transmitted between UEs and the Internet over VNFs is north-south traffic. The traffic transmitted between VNF1 and VNF2 is east-west traffic. To achieve load balancing of east-west traffic and north-south traffic, deploy the load balancing function on DC GWs and L2GWs/L3GWs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NFVI distributed gateway function supports both IPv4 and IPv6 services. If a step does not differentiate IPv4 and IPv6 services, this step applies to both IPv4 and IPv6 services.


**Figure 1** Networking of an NFVI distributed gateway (segmented SR tunnels)  
![](images/fig_dc_vrp_evpn_feature_002001.png)
#### Pre-configuration Tasks

Before configuring the NFVI distributed gateway function, complete the following tasks:

* Allow the routes between PEs and DC GWs and between DC GWs and L2GWs/L3GWs to be reachable.
* Deploy SR tunnels between PEs and DC GWs and between DC GWs and L2GWs/L3GWs.
* Configure BD EVPN on DC GWs and L2GWs/L3GWs. The configuration includes creating EVPN instances and L3VPN instances, establishing BGP EVPN peer relationships, and configuring VBDIF interfaces.
* Deploy the EBGP VPNv4 or EBGP VPNv6 function between PEs and DC GWs.
* Configure the static routes destined for VNF1 and VNF2 on L2GWs/L3GWs by referring to [Static VPN IPv4 Routes](dc_vrp_static-route_disjoin_cfg_0004.html) or [Static VPN IPv6 Routes](dc_vrp_static-route_disjoin_cfg_0009.html).


[Configuring Route Recursion to SR Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0122.html)

To use SR tunnels to transmit service traffic, configure route recursion to SR tunnels.

[Configuring Route Advertisement on DC GWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0123.html)

Route advertisement can be configured on DC GWs for them to construct their own forwarding entries based on received EVPN or BGP routes.

[Configuring Route Advertisement on L2GW/L3GWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0124.html)

Route advertisement allows L2GW/L3GWs to construct their own forwarding entries based on received EVPN or BGP routes.

[(Optional) Configuring Load Balancing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0125.html)

Load balancing needs to be deployed to achieve balanced network traffic distribution.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_evpn_cfg_0126.html)

After configuring the NFVI distributed gateway function, verify the configuration. On DC GWs, you can view the VPN peer relationships between DC GWs and VNFs and information about the UE routes received from VNFs.