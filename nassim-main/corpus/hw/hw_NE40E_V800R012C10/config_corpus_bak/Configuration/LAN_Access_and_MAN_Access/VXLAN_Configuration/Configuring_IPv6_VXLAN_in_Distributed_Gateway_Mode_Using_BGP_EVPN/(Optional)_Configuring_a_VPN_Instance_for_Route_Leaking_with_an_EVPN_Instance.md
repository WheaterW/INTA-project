(Optional) Configuring a VPN Instance for Route Leaking with an EVPN Instance
=============================================================================

To enable communication between VMs on different subnets, configure a VPN instance for route leaking with an EVPN instance. This configuration enables Layer 3 connectivity. To isolate multiple tenants, you can use different VPN instances.

#### Procedure

* For an IPv4 overlay network, perform the following operations:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created, and the VPN instance view is displayed.
  3. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id*
     
     
     
     A VNI is created and associated with the VPN instance.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family is enabled, and its view is displayed.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the VPN instance IPv4 address family.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     VPN targets are configured for the VPN instance IPv4 address family.
     
     
     
     If the current node needs to exchange L3VPN routes with other nodes in the same VPN instance, perform this step to configure VPN targets for the VPN instance.
  7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
     
     
     
     The VPN target extended community attribute for EVPN routes is configured for the VPN instance IPv4 address family.
     
     
     
     When the local device advertises an EVPN IP prefix route to a peer, the route carries all the VPN targets in the export VPN target list configured for EVPN routes in this step. When the local device advertises an EVPN IRB route to a peer, the route carries all the VPN targets in the export VPN target list of the EVPN instance in BD mode.
     
     The IRB route or IP prefix route received by the local device can be added to the routing table of the local VPN instance IPv4 address family only when the VPN targets carried in the IRB route or IP prefix route overlap those in the import VPN target list configured for EVPN routes in this step.
  8. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy+evpn) *policy-name* **evpn**
     
     
     
     The VPN instance IPv4 address family is associated with an import route-policy that is used to filter EVPN routes imported to the VPN instance IPv4 address family.
     
     
     
     To control EVPN route import to the VPN instance IPv4 address family more precisely, perform this step to associate the VPN instance IPv4 address family with an import route-policy and set attributes for eligible routes.
  9. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
     
     
     
     The VPN instance IPv6 address family is associated with an export route-policy that is used to filter EVPN routes to be advertised by this address family. Perform this step to more precisely control EVPN routes to be advertised by this address family and set attributes for eligible EVPN routes.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv4 address family view.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* For an IPv6 overlay network, perform the following operations:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created, and the VPN instance view is displayed.
  3. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id*
     
     
     
     A VNI is created and associated with the VPN instance.
  4. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family is enabled, and its view is displayed.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the VPN instance IPv6 address family.
  6. (Optional) Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     VPN targets are configured for the VPN instance IPv6 address family.
     
     
     
     If the current node needs to exchange L3VPN routes with other nodes in the same VPN instance, perform this step to configure VPN targets for the VPN instance.
  7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
     
     
     
     The VPN target extended community attribute for EVPN routes is configured for the VPN instance IPv6 address family.
     
     
     
     When the local device advertises an EVPN IPv6 prefix route to a peer, the route carries all the VPN targets in the export VPN target list configured for EVPN routes in this step. When the local device advertises an EVPN IRBv6 route to a peer, the route carries all the VPN targets in the export VPN target list of the EVPN instance in BD mode.
     
     The IRBv6 route or IPv6 prefix route received by the local device can be added to the routing table of the local VPN instance IPv6 address family only when the VPN targets carried in the IRBv6 route or IPv6 prefix route overlap those in the import VPN target list configured for EVPN routes in this step.
  8. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* **evpn**
     
     
     
     The VPN instance IPv6 address family is associated with an import route-policy that is used to filter EVPN routes imported to the VPN instance IPv6 address family.
     
     
     
     To control import of EVPN routes to the VPN instance IPv6 address family more precisely, perform this step to associate the VPN instance IPv6 address family with an import route-policy and set attributes for eligible EVPN routes.
  9. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* **evpn**
     
     
     
     The VPN instance IPv6 address family is associated with an export route-policy that is used to filter EVPN routes to be advertised by this address family. Perform this step to more precisely control EVPN routes to be advertised by this address family and set attributes for eligible EVPN routes.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance IPv6 address family view.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the VPN instance view.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.