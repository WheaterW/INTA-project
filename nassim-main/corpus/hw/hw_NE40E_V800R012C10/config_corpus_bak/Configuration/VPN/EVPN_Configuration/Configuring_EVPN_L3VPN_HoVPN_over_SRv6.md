Configuring EVPN L3VPN HoVPN over SRv6
======================================

An EVPN L3VPN HoVPN over SRv6 is a hierarchical EVPN over SRv6 network. Multiple PEs play different roles and form a hierarchical structure to implement the functions of a single PE, reducing PE performance requirements.

#### Context

Currently, EVPN over SRv6 is used as a mainstream transport solution for 5G services. For an EVPN over SRv6 network, you can deploy EVPN HVPN over SRv6 to improve scalability and prevent an individual PE from becoming a bottleneck. In this mode, the functions of a PE are distributed to multiple PEs. These PEs play different roles and form a hierarchical architecture to provide the functions of the single PE. In [Figure 1](#EN-US_TASK_0289315207__fig16042462166), an HVPN mainly consists of UPEs, SPEs, and NPEs.

* UPE: a device that is directly connected to users. UPEs provide user access functions. For example, CSGs connected to base stations function as UPEs in the following figure.
* SPE: a device that connects to a UPE and resides inside a service transport network. SPEs manage and advertise VPN routes. For example, ASGs function as SPEs in the following figure.
* NPE: a device that connects to an SPE and to the backbone network. For example, RSGs function as NPEs in the following figure.

**Figure 1** EVPN L3VPN HVPN over SRv6 networking  
![](figure/en-us_image_0000001232690293.png)

HVPN can be deployed in either of the following modes:

* HoVPN: SPEs advertise only default or summary routes to UPEs. The UPEs do not have specific routes destined for NPEs and can only use default routes to send VPN service data to SPEs, implementing route isolation. The HoVPN supports devices, such as UPEs, with relatively low route management capabilities, reducing network deployment costs.
* H-VPN: SPEs can advertise specific routes to UPEs. The UPEs function as RR clients and receive the specific routes reflected by SPEs functioning as RRs, facilitating route management and traffic forwarding control.

Currently, the EVPN HVPN over SRv6 network carrying Layer 3 services is deployed in EVPN L3VPN HoVPN over SRv6 mode.


#### Pre-configuration Tasks

Before configuring EVPN L3VPN HoVPN over SRv6, complete the following tasks:

* Configure an IGP between UPEs and SPEs and between SPEs and NPEs to implement network-layer connectivity.
* Complete the task of [Configuring EVPN L3VPN over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0252.html), [Configuring EVPN L3VPNv4 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpn_over_srv6-te_policy.html), or [Configuring EVPN L3VPNv6 over SRv6 TE Policy](dc_vrp_cfg_evpn-l3vpnv6_over_srv6-te_policy.html) between the UPEs and SPEs, and between the SPEs and NPEs.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  According to related standards, the VPN instance status obtained through an NMS can be up only when at least one interface bound to the VPN instance is up. In an HoVPN scenario, an SPE does not require any interface to be bound to a VPN instance. Consequently, the VPN instance status obtained by an NMS is down according to the standards, which is opposite to the actual VPN instance status. In this case, you can run the **transit-vpn** command in the VPN instance view or VPN instance IPv4/IPv6 address family view on the SPE. Then, the VPN instance status obtained by the NMS remains up, regardless of the binding between the VPN instance and interface.

#### Procedure

1. Configure each SPE to advertise only the default or summary route to each UPE.
   
   
   * Configure the SPE to advertise a default route to each UPE.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-instance-name* **0.0.0.0** { **0.0.0.0** | **0** } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } or [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-instance-name* **0::0** **0** { *nexthop-ipv6-address* | *interface-type* *interface-number* [ *nexthop-ipv6-address* ] }
        
        A default VPN IPv4/IPv6 static route is configured.
     3. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
        
        The BGP-VPN instance IPv4/IPv6 address family view is displayed.
     5. Run [**network**](cmdqueryname=network) **0.0.0.0** [ **0.0.0.0** | **0** ] [ **route-policy** *route-policy-name* ] or [**network**](cmdqueryname=network) **0::0** **0** [ **route-policy** *route-policy-name* ]
        
        The default route is imported to the routing table of the IPv4/IPv6 VPN instance.
     6. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
        
        EVPN IP prefix route advertisement is enabled.
     7. Run [**quit**](cmdqueryname=quit)
        
        Return to the BGP view.
     8. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
        
        The BGP-EVPN address family view is displayed.
     9. Run [**peer**](cmdqueryname=peer+upe) { *peerIpv6Addr* | *peerGroupName* } **upe**
        
        A BGP EVPN peer is specified as a UPE, or a group of BGP EVPN peers are specified as UPEs.
     10. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In this case, you also need to configure a route-policy on each NPE to prevent the NPEs from receiving the default route.
   * Configure the SPE to advertise a summary route to each UPE.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* or [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
        
        The BGP-VPN instance IPv4/IPv6 address family view is displayed.
     4. Run [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \* or [**aggregate**](cmdqueryname=aggregate) *ipv6-address* *prefix-length* [ **as-set** | **attribute-policy** *route-policy-name1* | **detail-suppressed** | **origin-policy** *route-policy-name2* | **suppress-policy** *route-policy-name3* ] \*
        
        A summary route is configured.
     5. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
        
        EVPN IP prefix route advertisement is enabled.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the BGP view.
     7. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
        
        The BGP-EVPN address family view is displayed.
     8. Run [**peer**](cmdqueryname=peer+upe) { *peerIpv6Addr* | *peerGroupName* } **upe**
        
        A BGP EVPN peer is specified as a UPE, or a group of BGP EVPN peers are specified as UPEs.
     9. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
2. Configure the SPE to advertise regenerated routes to each NPE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
      
      
      
      The BGP-EVPN address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+import+reoriginate) { *peerIpv6Addr* | *peerGroupName* } **import** **reoriginate**
      
      
      
      The device is enabled to add a regeneration flag to EVPN routes received from a UPE peer or UPE peer group.
      
      The *peerIpv6Addr* parameter specifies the IP address of a UPE peer, and the *peerGroupName* parameter specifies the name of a UPE peer group.
   5. Run [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *peerIpv6Addr* | *peerGroupName* } **advertise** **route-reoriginated** **evpn** **ip** or [**peer**](cmdqueryname=peer+advertise+route-reoriginated) { *peerIpv6Addr* | *peerGroupName* } **advertise** **route-reoriginated** **evpn** **ipv6**
      
      
      
      The SPE is enabled to regenerate the EVPN routes received from the UPEs as local EVPN routes and advertise these routes to the NPEs if EVPN L3VPNv4 or L3VPNv6 services are transmitted.
      
      The *peerIpv6Addr* parameter specifies the IP address of an NPE peer, and the *peerGroupName* parameter specifies the name of an NPE peer group.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on a UPE or NPE to check the VPN routing table. The command output shows the default routes or specific routes sent by the remote ends.
* Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) **prefix-route** command on a UPE or NPE to check the EVPN IP prefix routing table. The command output shows the EVPN IP prefix routes sent by the remote ends.