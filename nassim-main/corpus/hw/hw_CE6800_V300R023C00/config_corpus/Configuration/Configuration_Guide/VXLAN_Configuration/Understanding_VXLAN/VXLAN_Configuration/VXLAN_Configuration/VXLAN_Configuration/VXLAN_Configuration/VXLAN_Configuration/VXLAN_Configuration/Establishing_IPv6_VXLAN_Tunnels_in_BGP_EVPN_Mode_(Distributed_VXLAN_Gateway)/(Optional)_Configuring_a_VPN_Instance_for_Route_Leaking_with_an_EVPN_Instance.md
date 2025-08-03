(Optional) Configuring a VPN Instance for Route Leaking with an EVPN Instance
=============================================================================

(Optional) Configuring a VPN Instance for Route Leaking with an EVPN Instance

#### Context

In a distributed IPv6 VXLAN gateway scenario, hosts on different network segments can communicate with one another only through Layer 3 forwarding. In this case, you must configure a VPN instance for route leaking with an EVPN instance. The VPN instance is used to store host routes or host network segment routes in order to distinguish tenants.

RDs are used to identify routes in EVPN and VPN instances. For multiple routes with the same prefix, the routes are considered the same if their RDs are the same or different if their RDs are different. When configuring RDs for an EVPN instance and a VPN instance, note the following points:

* If routes need to implement ECMP, different RDs must be configured. For example, when multiple border leaf nodes are deployed and send the same route to the DC, different RDs must be configured for the border leaf nodes.
* When routes do not need to implement ECMP, the same RD can be configured. For example, when distributed gateways with the same address are deployed in different locations, and the network segment routes of the gateways do not need to implement ECMP, the same RD can be configured for server leaf nodes connected to the gateways.

#### Procedure

* For an IPv4 overlay network, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a VPN instance and enter the VPN instance view.
     
     
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
  3. Create a VNI and associate the VNI with the VPN instance.
     
     
     ```
     [vxlan vni](cmdqueryname=vxlan+vni) vni-id
     ```
     
     By default, no VNI is associated with a VPN instance.
  4. Enable the IPv4 address family for the VPN instance, and enter the VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
  5. Configure an RD for the VPN instance IPv4 address family.
     
     
     ```
     [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
     ```
     
     By default, no RD is configured for the VPN instance IPv4 address family.
  6. (Optional) Configure a VPN target for the VPN instance IPv4 address family.
     
     
     ```
     [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ]
     ```
     
     
     
     By default, no VPN target is configured for a VPN instance IPv4 address family.
     
     If the current node needs to exchange L3VPN routes with other nodes in the same VPN instance, perform this step to configure VPN targets for the VPN instance.
  7. Configure the VPN target extended community attribute of EVPN routes in the VPN instance IPv4 address family.
     
     
     ```
     [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ] evpn
     ```
     
     
     
     When the local device advertises an EVPN IP prefix route to a peer, the route carries all the VPN targets in the export VPN target list configured for EVPN routes in this step. When the local device advertises an EVPN IRB route to a peer, the route carries all VPN targets in the export VPN target list of the EVPN instance in the BD.
     
     The IRB route or IP prefix route received by the local device can be added to the routing table of the local VPN instance IPv4 address family only when the VPN targets carried in the route overlap those in the import VPN target list configured for EVPN routes in this step.
  8. (Optional) Associate the VPN instance IPv4 address family with an import route-policy to filter EVPN routes imported to the VPN instance IPv4 address family.
     
     
     ```
     [import route-policy](cmdqueryname=import+route-policy) policy-name evpn
     ```
     
     To control the EVPN routes that enter the current VPN instance IPv4 address family more precisely, you can specify an import route-policy to filter EVPN routes and set route attributes for the routes that match the filter criteria.
  9. (Optional) Associate the VPN instance IPv4 address family with an export route-policy to filter EVPN routes to be advertised by the VPN instance IPv4 address family.
     
     
     ```
     [export route-policy](cmdqueryname=export+route-policy) policy-name evpn
     ```
     
     Perform this step to apply an export route-policy to the VPN instance IPv4 address family and set attributes for eligible EVPN routes. This enables the device to control EVPN routes to be advertised more precisely.
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* For an IPv6 overlay network, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a VPN instance and enter the VPN instance view.
     
     
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
  3. Create a VNI and associate the VNI with the VPN instance.
     
     
     ```
     [vxlan vni](cmdqueryname=vxlan+vni) vni-id
     ```
     
     By default, no VNI is associated with a VPN instance.
  4. Enable the IPv6 address family for the VPN instance, and enter the VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family)
     ```
  5. Configure an RD for the VPN instance IPv6 address family.
     
     
     ```
     [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
     ```
     
     By default, no RD is configured for the VPN instance IPv6 address family.
  6. (Optional) Configure a VPN target for the VPN instance IPv6 address family.
     
     
     ```
     [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ]
     ```
     
     
     
     By default, no VPN target is configured for a VPN instance IPv4 address family.
     
     If the current node needs to exchange L3VPN routes with other nodes in the same VPN instance, perform this step to configure VPN targets for the VPN instance.
  7. Configure the VPN target extended community attribute of EVPN routes in the VPN instance IPv6 address family.
     
     
     ```
     [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ] evpn
     ```
     
     
     
     When the local device advertises an EVPN IPv6 prefix route to a peer, the route carries all the VPN targets in the export VPN target list configured for EVPN routes in this step. When the local device advertises an EVPN IRBv6 route to a peer, the route carries all VPN targets in the export VPN target list of the EVPN instance in the BD.
     
     The IRBv6 route or IPv6 prefix route received by the local device can be added to the routing table of the local VPN instance IPv6 address family only when the VPN targets carried in the route overlap those in the import VPN target list configured for EVPN routes in this step.
  8. (Optional) Associate the VPN instance IPv6 address family with an import route-policy to filter EVPN routes imported to the VPN instance IPv6 address family.
     
     
     ```
     [import route-policy](cmdqueryname=import+route-policy) policy-name evpn
     ```
     
     To control the EVPN routes that enter the current VPN instance IPv6 address family more precisely, you can specify an import route-policy to filter EVPN routes and set route attributes for the routes that match the filter criteria.
  9. (Optional) Associate the VPN instance IPv6 address family with an export route-policy to filter EVPN routes to be advertised by the VPN instance IPv6 address family.
     
     
     ```
     [export route-policy](cmdqueryname=export+route-policy) policy-name evpn
     ```
     
     Perform this step to apply an export route-policy to the VPN instance IPv6 address family and set attributes for eligible EVPN routes. This enables the device to control EVPN routes to be advertised more precisely.
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```