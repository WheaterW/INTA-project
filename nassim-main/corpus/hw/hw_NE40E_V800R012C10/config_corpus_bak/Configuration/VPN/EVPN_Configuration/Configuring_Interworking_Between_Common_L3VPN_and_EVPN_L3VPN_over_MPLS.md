Configuring Interworking Between Common L3VPN and EVPN L3VPN over MPLS
======================================================================

During the reconstruction of a common L3VPN into an EVPN L3VPN over MPLS, coexistence of the EVPN L3VPN over MPLS and common L3VPN occurs. To prevent network reconstruction from compromising communication, configure interworking between common L3VPN and EVPN L3VPN over MPLS, so that the common L3VPN and EVPN L3VPN over MPLS can communicate.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172370492__fig2056513373518), an L3VPN is already deployed. During the reconstruction of a common L3VPN into an EVPN L3VPN over MPLS, coexistence of the common L3VPN and EVPN L3VPN over MPLS occurs. To ensure communication between the common L3VPN and EVPN L3VPN over MPLS, configure interworking between these two types of VPNs on NPE1.


#### Pre-configuration Tasks

**Figure 1** Interworking between common L3VPN and EVPN L3VPN over MPLS  
![](figure/en-us_image_0000001229989409.png)

Before configuring interworking between common L3VPN and EVPN L3VPN over MPLS, complete the following tasks:

* Configure basic MPLS functions on NPE1, NPE2, and the UPE.
* Configure IGP on the UPE, NPE1, and NPE2 to ensure route reachability.
* Configure [BGP EVPN peer relationships](dc_vrp_evpn_cfg_0006.html) between NPE1 and NPE2.
* Deploy [basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html) or [basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html) between NPE1 and the UPE.

#### Procedure

* Configure NPE1 and NPE2 to generate and advertise EVPN IP prefix routes.
  
  
  
  For IPv4 services, perform the following configurations.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     A VPN instance is created, and its view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     The VPN instance IPv4 address family is enabled, and its view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     An RD is configured for the VPN instance IPv4 address family.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
     
     VPN targets are configured for the VPN instance IPv4 address family to exchange routes with the local EVPN instance.
  6. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
     
     EVPN is enabled to generate and advertise IP prefix and IRB routes.
  7. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
     
     EVPN routes that can be imported into the VPN instance IPv4 address family are associated with a tunnel policy.
  8. Run [**quit**](cmdqueryname=quit)
     
     Exit the VPN instance IPv4 address family view.
  9. Run [**quit**](cmdqueryname=quit)
     
     Exit the VPN instance view.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
  
  For IPv6 services, perform the following configurations.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     A VPN instance is created, and its view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     The VPN instance IPv6 address family is enabled, and its view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     An RD is configured for the VPN instance IPv6 address family.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
     
     VPN targets are configured for the VPN instance IPv6 address family to exchange routes with the local EVPN instance.
  6. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
     
     EVPN is enabled to generate and advertise IP prefix and IRB routes.
  7. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
     
     EVPN routes that can be imported into the VPN instance IPv6 address family are associated with a tunnel policy.
  8. Run [**quit**](cmdqueryname=quit)
     
     Exit the VPN instance IPv6 address family view.
  9. Run [**quit**](cmdqueryname=quit)
     
     Exit the VPN instance view.
  10. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
* Configure NPE1 to advertise routes re-originated by the EVPN address family to the VPNv4/VPNv6 peer (UPE).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  4. Run [**peer**](cmdqueryname=+peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
     
     
     
     The device is configured to add a re-origination flag to routes received from the BGP EVPN peer.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPNv4/VPNv6 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } **reflect-client**
     
     
     
     The UPE is specified as a BGP VPNv4/VPNv6 RR client to reflect BGP VPNv4/VPNv6 routes re-originated from EVPN routes.
  8. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** }
     
     
     
     The device is configured to advertise routes re-originated by the EVPN address family to the BGP VPNv4/VPNv6 peer.
     
     
     
     After the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** **evpn** { **mac-ip** | **ip** | **mac-ipv6** | **ipv6** } command is run, NPE1 re-originates the EVPN routes received from NPE2 by using MPLS to encapsulate these routes into BGP VPNv4/VPNv6 routes and then sends them to the UPE.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure NPE1 to advertise routes re-originated by the VPNv4/VPNv6 address family to the BGP EVPN peer (NPE2).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** or [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
     
     
     
     The BGP-VPNv4/VPNv6 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *ipv4-address* | *group-name* } **import** **reoriginate**
     
     
     
     The device is configured to add a re-origination flag to routes received from the VPNv4/VPNv6 peer.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  6. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
     
     
     
     The BGP-EVPN address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer+reflect-client) { *ipv4-address* | *group-name* } **reflect-client**
     
     
     
     NPE2 is specified as a BGP EVPN RR client to reflect BGP EVPN routes re-originated from BGP VPNv4/VPNv6 routes.
  8. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** }
     
     
     
     NPE1 is configured to advertise routes re-originated by the VPNv4/VPNv6 address family to the BGP EVPN peer (NPE2).
     
     
     
     After the [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *ipv4-address* | *group-name* } **advertise** **route-reoriginated** { **vpnv4** | **vpnv6** } command is run, NPE1 re-encapsulates the MPLS-encapsulated VPNv4/VPNv6 routes received from the UPE into EVPN routes and then sends them to NPE2.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  10. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 or IPv6 address family view is displayed.
  11. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
      
      
      
      The device is enabled to advertise host IP routes in the VPN instance as EVPN IP prefix routes.
  12. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the BGP view.
  13. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the BGP view.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command on NPE2 to check information about EVPN routes received from the UPE.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on NPE2 or the UPE to check information about VPN routes received from the remote end.