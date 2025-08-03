Configuring a VPN Instance
==========================

A VPN instance of the IPv6 address family can be configured to manage IPv6 VPN routes.

#### Context

In BGP/MPLS IPv6 VPN, a separate instance is created for each VPN to store VPN forwarding information. Such an instance is known as a VPN instance or VPN routing and forwarding (VRF) table. In related standards, it may also be referred to as a per-site forwarding table.

VPN instances are used to isolate VPN routes from public network routes. Routes of different VPN instances are isolated from one another. VPN instances need to be configured in all types of BGP/MPLS IPv6 VPN networking solutions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is created, and the VPN instance view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The name of a VPN instance is case sensitive. For example, **vpn1** and **VPN1** are considered different VPN instances.
3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
   
   
   
   A description about the VPN instance is configured.
   
   
   
   Similar to a host name or an interface description, the VPN instance description helps users memorize the VPN instance.
4. (Optional) Run [**service-id**](cmdqueryname=service-id) *id*
   
   
   
   A service ID is created for the VPN instance.
   
   
   
   A service ID is unique on a device. It distinguishes a VPN service from other VPN services on the network.
5. (Optional) Run [**vpn-id**](cmdqueryname=vpn-id) *vpn-id*
   
   
   
   A VPN ID is set.
   
   You can run this command to create a globally unique ID for a VPN instance. In a CU separation scenario, you can run this command to set the same VPN ID for the control plane and forwarding plane to prevent VPN ID inconsistency.
6. Run [**ipv6-family**](cmdqueryname=ipv6-family)
   
   
   
   A VPN instance IPv6 address family is configured, and its view is displayed.
   
   
   
   VPN instances support both the IPv4 and IPv6 address families. The VPN instance configuration is performed only after an address family is configured based on the types of routes to be advertised and data to be forwarded.
7. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is set for the VPN instance IPv6 address family.
   
   
   
   A VPN instance IPv6 address family takes effect only after being assigned an RD. The RDs of different VPN instances on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a large number of VPN instances need to be created and a large number of RDs need to be planned, run the [**route route-distinguisher auto**](cmdqueryname=route+route-distinguisher+auto) *rd-ip* command in the system view to enable automatic RD allocation and set the *rd-ip* parameter to an IPv4 address. Then the device can assign RDs in the format of *X.X.X.X:index* to all VPN instances that are not assigned RDs. The value of *index* is a 2-byte value automatically assigned in a range of 1 to 65535. Automatic RD allocation applies to VPN instances without manually configured RDs. If an RD has been configured for the IPv4 or IPv6 address family of a VPN instance using the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command, the device will not dynamically allocate a new RD to that address family of the VPN instance.
8. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
   
   
   
   One or more import VPN targets, one or more export VPN targets, or both of import and export VPN targets are configured for the VPN instance IPv6 address family.
   
   
   
   A VPN target is a BGP extended community attribute. It is used to control the advertisement or acceptance of VPN-IPv6 route information. A maximum of eight VPN targets can be configured using the [**vpn-target**](cmdqueryname=vpn-target) command. If you want to configure more VPN targets in the VPN instance IPv6 address family view, repeat running the [**vpn-target**](cmdqueryname=vpn-target) command.
9. (Optional) Run [**prefix limit**](cmdqueryname=prefix+limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }
   
   
   
   The maximum number of route prefixes supported by the VPN instance IPv6 address family is set.
   
   
   
   The configuration restricts the number of route prefixes imported from the CEs and other PEs into a VPN instance IPv6 address family on a PE, preventing the PE from receiving too many route prefixes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the number of route prefixes exceeds the maximum number, direct and static routes can still be added to the VPN routing table of the VPN instance IPv6 address family.
10. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
    
    
    
    An import route-policy is applied to the VPN instance IPv6 address family.
    
    
    
    In addition to using VPN targets to control the import and export of VPN routes, you can use an import route-policy to better control the import of VPN routes. It filters routes to be imported into the VPN instance IPv6 address family.
11. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
    
    
    
    An export route-policy is applied to the VPN instance IPv6 address family.
    
    
    
    In addition to using a VPN target to control the import and export of VPN routes, you can use an export route-policy to better control the export of VPN routes to other PEs. The export route-policy filters routes before they are advertised to other PEs.
    
    By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filter rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
12. (Optional) Run [**import route-filter**](cmdqueryname=import+route-filter) *route-filter-name*
    
    
    
    An import route-filter is configured for the VPN instance IPv6 address family.
    
    
    
    In addition to using VPN targets to control the import and export of VPN routes, you can use an import route-filter to better control the import of VPN routes. An import route-filter can filter routes to be imported into the VPN instance IPv6 address family.
13. (Optional) Run [**export route-filter**](cmdqueryname=export+route-filter) *route-filter-name* [ **add-ert-first** ]
    
    
    
    An export route-filter is configured for the VPN instance IPv6 address family.
    
    
    
    In addition to using VPN targets to control the import and export of VPN routes, you can use an export route-filter to better control the export of VPN routes to other PEs.
    
    By default, export VPN targets are added to VPN routes before these routes are matched against an export route-filter. If the export route-filter contains VPN target-related filtering rules, these rules cannot apply to these routes. If you want to apply the VPN target-related filter rules defined in an export route-filter to VPN routes, configure the **add-ert-first** parameter to configure the system to add export VPN targets to VPN routes before matching these routes against the export route-filter.
14. (Optional) Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
    
    
    
    A tunnel policy is applied to the VPN instance IPv6 address family.
    
    
    
    A tunnel can be specified for IPv6 VPN traffic forwarding when a tunnel policy is applied to the VPN instance IPv6 address family.
15. (Optional) Configure a label distribution mode for the VPN instance IPv6 address family.
    
    
    * Run the [**apply-label**](cmdqueryname=apply-label+pop-go) { **per-nexthop** | **per-route** } **pop-go** command to configure the VPN instance IPv6 address family to assign a label to each route or routes with the same next hop and outgoing label before the routes are sent to a peer PE. After receiving a data packet with the label, the peer PE removes the label, searches the ILM table for an outbound interface, and forwards the packet through the outbound interface.
    * Run the [**apply-label**](cmdqueryname=apply-label) { **per-instance** | **per-nexthop** | **per-route** } command to configure a label distribution mode for the VPN instance IPv6 address family.
    
    The [**apply-label**](cmdqueryname=apply-label) { **per-nexthop** | **per-route** } **pop-go** command is mutually exclusive with the [**apply-label**](cmdqueryname=apply-label) { **per-instance** | **per-nexthop** | **per-route** }. If you run both commands, the later configuration overrides the previous one.
16. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.