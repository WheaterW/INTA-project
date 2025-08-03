Configuring a VPN Instance
==========================

A VPN instance can be configured on a PE to manage VPN routes.

#### Context

An instance is created to comprise the VPN forwarding information for each VPN in a BGP/MPLS IP VPN. This instance is called a VPN instance or a VPN routing and forwarding (VRF) table. In related standards, a VPN instance is called a per-site forwarding table.

VPN instances are used to isolate VPN routes from public network routes. Routes of different VPN instances are isolated from one another. VPN instances need to be configured in all types of BGP/MPLS IP VPN networking solutions.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name* command to create a VPN instance and enter its view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The name of a VPN instance is case sensitive. For example, **vpn1** and **VPN1** are considered different VPN instances.
   
   PEs do not have default VPN instances. Multiple VPN instances can be created on a PE.
3. (Optional) Run the [**description**](cmdqueryname=description) *description-information* command to configure a description for the VPN instance.
   
   
   
   Similar to a host name or an interface description, the VPN instance description helps users memorize the VPN instance.
4. (Optional) Run the [**service-id**](cmdqueryname=service-id) *id* command to create a service ID for the VPN instance. 
   
   
   
   A service ID is unique on a device. It distinguishes a VPN service from other VPN services on the network.
5. (Optional) Run the [**vpn-id**](cmdqueryname=vpn-id) *vpn-id* command to configure a VPN ID. You can run the [**vpn-id**](cmdqueryname=vpn-id) command to create a globally unique ID for a VPN instance based on the plan. In a CU separation scenario, you can run the [**vpn-id**](cmdqueryname=vpn-id) command to set the same VPN ID for the control plane and forwarding plane, preventing VPN ID inconsistency.
6. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enable the VPN instance IPv4 address family and enter its view.
   
   
   
   The VPN instance configuration can be performed only after an address family is configured based on the types of routes to be advertised and data to be forwarded.
7. Run the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command to configure an RD for the VPN instance IPv4 address family.
   
   
   
   A VPN instance IPv4 address family takes effect only after being assigned an RD. The RDs of different VPN instance IPv4 address families on a PE must be different.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If you set an RD for the VPN instance IPv4 address family directly after you create a VPN instance and enter its view, the VPN instance IPv4 address family is automatically enabled and its view is displayed.
   * If a large number of VPN instances need to be created and a large number of RDs need to be planned, run the [**route route-distinguisher auto**](cmdqueryname=route+route-distinguisher+auto) *rd-ip* command in the system view to enable automatic RD allocation and set the *rd-ip* parameter to an IPv4 address. Then the device can assign RDs in the format of *X.X.X.X:index* to all VPN instances that are not assigned RDs. The value of *index* is a 2-byte value automatically assigned in a range of 1 to 65535. Automatic RD allocation applies to VPN instances without manually configured RDs. If an RD has been configured for the IPv4 or IPv6 address family of a VPN instance using the [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher* command, the device will not dynamically allocate a new RD to that address family of the VPN instance.
8. Run the [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] command to configure VPN targets for the VPN instance IPv4 address family. 
   
   
   
   VPN targets are a type of BGP extended community attribute used to control the import and export of VPN routes. A maximum of eight VPN targets can be configured using the [**vpn-target**](cmdqueryname=vpn-target) command. If you want to configure more VPN targets in the VPN instance IPv4 address family view, repeatedly run the [**vpn-target**](cmdqueryname=vpn-target) command.
9. (Optional) Run the [**prefix limit**](cmdqueryname=prefix+limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** } command to configure the maximum number of route prefixes supported by the VPN instance IPv4 address family.
   
   The configuration restricts the number of route prefixes imported from the CEs and peer PEs into a VPN instance IPv4 address family on a local PE, preventing the local PE from receiving too many route prefixes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the scenario where the number of route prefixes exceeds a specified maximum number, after the [**prefix limit**](cmdqueryname=prefix+limit) command is run to increase the allowed maximum number of route prefixes in a VPN instance IPv4 address family or the [**undo prefix limit**](cmdqueryname=undo+prefix+limit) command is run to delete the maximum number, the device adds excess route prefixes of various protocols to the VPN IP routing table.
   
   After the number of route prefixes exceeds the maximum number, direct and static routes can still be added to the routing table of the VPN instance IPv4 address family.
10. (Optional) Run the [**import route-policy**](cmdqueryname=import+route-policy) *policy-name* command to apply an import route-policy to the VPN instance IPv4 address family.
    
    
    
    In addition to using VPN targets to control VPN route import and export, an import route-policy can be configured to better control VPN route import. The import route-policy filters the routes to be imported to the VPN instance IPv4 address family or modify route attributes.
11. (Optional) Run the [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ] command to apply an export route-policy to the VPN instance IPv4 address family.
    
    
    
    In addition to using VPN targets to control VPN route import and export, an export route-policy can be configured to better control VPN route export. The export route-policy filters routes to be advertised to other PEs or modify route attributes.
    
    By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filtering rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
12. (Optional) Run the [**import route-filter**](cmdqueryname=import+route-filter) *route-filter-name* command to apply an import route-filter to the VPN instance IPv4 address family.
    
    
    
    In addition to using VPN targets to control VPN route import and export, an import route-filter can be configured to better control VPN route import. The import route-filter filters the routes to be imported to the VPN instance IPv4 address family or modifies route attributes.
13. (Optional) Run the [**export route-filter**](cmdqueryname=export+route-filter) *route-filter-name* [ **add-ert-first** ] command to apply an export route-filter to the VPN instance IPv4 address family.
    
    
    
    In addition to using VPN targets to control VPN route import and export, an export route-filter can be configured to better control VPN route export. The export route-filter filters routes to be advertised to other PEs or modifies route attributes.
    
    By default, export VPN targets are added to VPN routes after these routes match an export route-filter. If the export route-filter contains VPN target-related filtering rules, the route-filter cannot apply to these routes. To prevent such rule-induced failures, configure **add-ert-first** to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-filter.
14. (Optional) Run the [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* command to apply a tunnel policy to the VPN instance IPv4 address family.
    
    
    
    A tunnel can be specified for IPv4 VPN data forwarding using a tunnel policy that is applied to a VPN instance IPv4 address family.
15. (Optional) Run the [**apply-label per-instance static**](cmdqueryname=apply-label+per-instance+static) *static-label-value* command to configure all routes to be advertised to the peer PEs in the current VPN instance IPv4 address family to use the same static label. 
    
    
    
    In a VPN scenario where a CE is multi-homed to PEs for load balancing, this command allows VPNv4 routes sent by a downstream device to carry the same static label so that traffic can be load-balanced for the downstream device.
16. (Optional) Configure a label distribution mode for the VPN instance IPv4 address family.
    
    
    * Run the [**apply-label**](cmdqueryname=apply-label+pop-go) { **per-nexthop** | **per-route** } **pop-go** command to configure the VPN instance IPv4 address family to assign a label to each route or routes with the same next hop before the routes are sent to a peer PE. After receiving a data packet with the label, the peer PE removes the label, searches the ILM table for an outbound interface, and forwards the packet through the outbound interface.
    * Run the [**apply-label**](cmdqueryname=apply-label) { **per-instance** | **per-nexthop** | **per-route** } command to configure a label distribution mode for the VPN instance IPv4 address family.
    
    The [**apply-label**](cmdqueryname=apply-label) { **per-nexthop** | **per-route** } **pop-go** command is mutually exclusive with the [**apply-label**](cmdqueryname=apply-label) { **per-instance** | **per-nexthop** | **per-route** } command. If you run both commands, the later configuration overrides the previous one.
17. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.