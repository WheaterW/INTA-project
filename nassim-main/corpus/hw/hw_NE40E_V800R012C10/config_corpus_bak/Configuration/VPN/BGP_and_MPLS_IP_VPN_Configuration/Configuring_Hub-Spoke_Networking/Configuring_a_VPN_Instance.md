Configuring a VPN Instance
==========================

A VPN instance can be configured on a PE to manage VPN routes.

#### Context

In the hub-spoke networking, a PE connected to a central site (hub site) is called a hub PE and a PE connected to a non-central site (spoke site) is called a spoke PE. The spoke and hub PEs must have VPN instances configured. If the hub CE is connected to the hub PE through two links, the hub PE must have two VPN instances configured, for example, **vpn\_in** and **vpn\_out**. If the hub CE is connected to the hub PE through a single link, the hub PE needs only one VPN instance configured, for example, **vpnhub**.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Steps 1 to 8 are performed to configure one VPN instance. Configurations of different VPN instances are similar. If different VPN instances are configured on the same device, each VPN instance must have a particular name, RD, and description.



#### Procedure

* Configure each spoke PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The view of a VPN instance is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     The description of the VPN instance is configured.
     
     
     
     The description is used to record the purpose of creating the VPN instance and the CEs connected to the VPN instance.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is set for the VPN instance IPv4 address family.
     
     
     
     A VPN instance IPv4 address family takes effect only after being assigned an RD. Before setting an RD, you can configure only the description of the VPN instance, and no other parameters can be configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target2* &<1-8> **import-extcommunity**
     
     
     
     One or more import VPN targets are configured for the VPN instance so that the VPN instance can accept VPNv4 routes advertised by the hub PE.
     
     
     
     *vpn-target2* must be within the export VPN target list configured on the hub PE.
  7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> **export-extcommunity**
     
     
     
     One or more export VPN targets are configured so that the routes of the sites that the spoke PE accesses carry the VPN target.
     
     
     
     *vpn-target1* must be within the import VPN target list configured on the hub PE.
  8. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
     
     
     
     An import route-policy is applied to the VPN instance IPv4 address family.
     
     
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an import route-policy to better control the acceptance of VPN routes. The import route-policy can be used to filter the routes to be imported to the VPN instance IPv4 address family or modify route attributes.
  9. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
     
     
     
     An export route-policy is applied to the VPN instance IPv4 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an export route-policy to better control the advertisement of VPN routes. The export route-policy filters routes to be advertised to other PEs or modify route attributes.
     
     By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filtering rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
  10. (Optional) Run [**apply-label per-instance**](cmdqueryname=apply-label+per-instance)
      
      
      
      MPLS label allocation based on the VPN instance IPv4 address family (known as one label per instance) is configured. Then, all routes of the VPN instance IPv4 address family are assigned the same label.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the hub PE (to which a hub CE is connected through two links).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name1*
     
     
     
     The view of a VPN instance (named **vpn\_in**) is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     The description of the VPN instance is configured.
     
     The description is used to record the purpose of creating the VPN instance and the CEs connected to the VPN instance.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is set for the VPN instance IPv4 address family.
     
     A VPN instance IPv4 address family takes effect only after being assigned an RD. Before setting an RD, you can configure only the description of the VPN instance, and no other parameters can be configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> **import-extcommunity**
     
     
     
     Import VPN targets are configured for the VPN instance IPv4 address family so that the VPN instance can accept VPNv4 routes advertised by all spoke PEs.
     
     
     
     The *vpn-target1* list here must contain the export VPN targets configured on all spoke PEs.
  7. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
     
     
     
     An import route-policy is applied to the VPN instance IPv4 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an import route-policy to better control the acceptance of VPN routes. The import route-policy filters the routes to be imported to the VPN instance IPv4 address family or modify route attributes.
  8. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
     
     
     
     An export route-policy is applied to the VPN instance IPv4 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an export route-policy to better control the advertisement of VPN routes. The export route-policy filters routes to be advertised to other PEs or modify route attributes.
     
     By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filtering rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  11. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name2*
      
      
      
      The view of a VPN instance (named **vpn\_out**) is displayed.
  12. (Optional) Run [**description**](cmdqueryname=description) *description-information*
      
      
      
      The description of the VPN instance is configured.
      
      The description is used to record the purpose of creating the VPN instance and the CEs connected to the VPN instance.
  13. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family view is displayed.
  14. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is set for the VPN instance IPv4 address family.
      
      A VPN instance IPv4 address family takes effect only after being assigned an RD. Before setting an RD, you can configure only the description of the VPN instance, and no other parameters can be configured.
  15. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target2* &<1-8> **export-extcommunity**
      
      
      
      Export VPN targets are configured to advertise the routes of the hub site and all spoke sites.
      
      
      
      The *vpn-target2* list here must contain the import VPN targets configured on all spoke PEs.
  16. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
      
      
      
      An import route-policy is applied to the VPN instance IPv4 address family.
      
      In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an import route-policy to better control the acceptance of VPN routes. The import route-policy filters the routes to be imported to the VPN instance IPv4 address family or modify route attributes.
  17. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
      
      
      
      An export route-policy is applied to the VPN instance IPv4 address family.
      
      In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an export route-policy to better control the advertisement of VPN routes. The export route-policy filters routes to be advertised to other PEs or modify route attributes.
      
      By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filtering rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
  18. (Optional) Run [**apply-label per-instance**](cmdqueryname=apply-label+per-instance)
      
      
      
      MPLS label distribution based on the VPN instance IPv4 address family (known as one label per instance) is configured. One label is assigned to all the routes of the VPN instance IPv4 address family.
  19. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the hub PE (to which a hub CE is connected through a single link).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name1*
     
     
     
     The view of a VPN instance (named **vpnhub**) is displayed.
  3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
     
     
     
     The description of the VPN instance is configured.
     
     The description is used to record the purpose of creating the VPN instance and the CEs connected to the VPN instance.
  4. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The VPN instance IPv4 address family view is displayed.
  5. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is set for the VPN instance IPv4 address family.
     
     A VPN instance IPv4 address family takes effect only after being assigned an RD. Before setting an RD, you can configure only the description of the VPN instance, and no other parameters can be configured.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> **import-extcommunity**
     
     
     
     Import VPN targets are configured so that the VPN instance can accept the VPNv4 routes advertised by all spoke PEs.
     
     
     
     The *vpn-target1* list here must contain the export VPN targets configured on all spoke PEs.
  7. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target2* &<1-8> **export-extcommunity**
     
     
     
     Export VPN targets are configured so that the routes advertised to all spoke sites carry this attribute.
     
     The *vpn-target2* list here must contain the import VPN targets configured on all spoke PEs.
  8. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
     
     
     
     An import route-policy is applied to the VPN instance IPv4 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, you can use an import route-policy to better control the acceptance of VPN routes. The import route-policy filters the routes to be imported to the VPN instance IPv4 address family or modify route attributes.
  9. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
     
     
     
     An export route-policy is applied to the VPN instance IPv4 address family.
     
     Before performing this step, you must create a route-policy that permits only default routes based on [Creating a Route-Policy](dc_vrp_route-policy_cfg_0001.html). Then perform this step to enable the hub PE to advertise only default routes to spoke PEs.
     
     By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filtering rules, the route-policy cannot apply to these routes. To prevent such rule-induced failures, configure the **add-ert-first** parameter to instruct the device to add export VPN targets to VPN routes before these routes are matched against the export route-policy.
  10. (Optional) Run [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go)
      
      
      
      The device is configured to assign a label to each VPNv4 route to be sent to its BGP VPNv4 peer. Then, after the device receives a labeled data packet from its BGP VPNv4 peer, the device directly searches the ILM table for an outbound interface based on the label carried in the packet, removes the label, and forwards the packet through the found outbound interface.
      
      After the [**apply-label per-route pop-go**](cmdqueryname=apply-label+per-route+pop-go) command is run, the hub PE records in the ILM table the mapping between the label assigned to each VPNv4 route and the outbound interface name in the route before sending a route to a spoke PE. After the hub PE receives a labeled data packet from a spoke PE, the hub PE directly searches the ILM table for an outbound interface based on the label carried in the packet, but no longer searches the IP forwarding table based on the longest-match rule. The hub PE then removes the label, and forwards the packet through the found outbound interface, therefore preventing the data packet from being forwarded to another spoke PE without passing through the hub CE.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.