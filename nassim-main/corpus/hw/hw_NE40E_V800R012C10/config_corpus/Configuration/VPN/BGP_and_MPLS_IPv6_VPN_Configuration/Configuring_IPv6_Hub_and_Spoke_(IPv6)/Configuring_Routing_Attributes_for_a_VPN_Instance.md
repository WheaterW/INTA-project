Configuring Routing Attributes for a VPN Instance
=================================================

In the networking of Hub and Spoke, you can configure VPN targets on the Hub-PE and Spoke PEs to control the advertisement of VPN routes. The import VPN target configured on the Hub-PE must contain the export VPN targets configured on all the Spoke-PEs. The export VPN target list configured on the Hub-PE must contain the import VPN targets configured on all the Spoke-PEs.

#### Context

Controlling the acceptance of routes to be imported by the VPN instance IPv6 address family by configuring VPN targets is also a key part of the hub-spoke solution.


#### Procedure

* Configure the Hub-PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name1*
     
     
     
     The VPN instance view of VPN-in is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the VPN instance IPv6 address family.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> **import-extcommunity**
     
     
     
     One or multiple import VPN targets are configured for the VPN instance IPv6 address family to receive the VPNv6 routes advertised by all the Spoke-PEs.
     
     The *vpn-target1* list must contain all export *vpn-target* values of the Spoke-PEs.
  6. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
     
     
     
     An import route-policy for importing VPN routes is configured for the VPN instance IPv6 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an import route-policy can be configured to better control the acceptance of VPN routes. An import route-policy can be used to filter the routes to be imported to the VPN instance IPv6 address family or modify route attributes.
  7. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
     
     
     
     An export route-policy for advertising VPN routes is configured for the VPN instance IPv6 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an export route-policy can be configured to better control the advertisement of VPN routes. An export route-policy can be used to filter the routes advertised by the VPN instance IPv6 address family or modify route attributes.
     
     By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filter rules, the route-policy cannot apply to these routes. If you want to apply the route target-related filter rules defined in an export route-policy to VPN routes, configure the **add-ert-first** parameter to configure the system to add export VPN targets to VPN routes before matching these routes against the export route-policy.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name2*
     
     
     
     The VPN instance view of VPN-out is displayed.
  10. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      
      
      The VPN instance IPv6 address family view is displayed.
  11. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target2* &<1-8> **export-extcommunity**
      
      
      
      One or multiple export VPN targets are configured for the VPN instance IPv6 address family to advertise the routes of all the Hub sites and Spoke sites.
      
      The *vpn-target2* list must contain all import *vpn-target* values of Hub-PEs.
  12. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
      
      
      
      An import route-policy for importing VPN routes is configured for the VPN instance IPv6 address family. In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an import route-policy can be configured to better control the advertisement of VPN routes. An import route-policy can be used to filter the routes to be imported to the VPN instance IPv6 address family or modify route attributes.
  13. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
      
      
      
      An export route-policy for advertising VPN routes is configured for the VPN instance IPv6 address family.
      
      In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an export route-policy can be configured to better control the advertisement of VPN routes.
      
      By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filter rules, the route-policy cannot apply to these routes. If you want to apply the route target-related filter rules defined in an export route-policy to VPN routes, configure the **add-ert-first** parameter to configure the system to add export VPN targets to VPN routes before matching these routes against the export route-policy.
  14. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the Spoke-PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     The VPN instance view of VPN-in is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
     
     
     
     The VPN instance IPv6 address family view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
     
     
     
     An RD is configured for the VPN instance IPv6 address family.
  5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target2* &<1-8> **import-extcommunity**
     
     
     
     One or multiple import VPN targets are configured for the VPN instance IPv6 address family to accept the VPNv6 routes advertised by the Hub-PE.
     
     *vpn-target2* must be contained in the export *vpn-target* list of the Hub-PE.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target1* &<1-8> **export-extcommunity**
     
     
     
     One or multiple export VPN targets are configured for the VPN instance IPv6 address family to send the VPNv6 routes of sites connected to the Spoke PE.
     
     *vpn-target1* must be contained in the import *vpn-target* list of the Hub-PE.
  7. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
     
     
     
     An import route-policy for importing VPN routes is configured for the VPN instance IPv6 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an import route-policy can be configured to better control the acceptance of VPN routes. An import route-policy can be used to filter the routes to be imported to the VPN instance IPv6 address family or modify route attributes.
  8. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
     
     
     
     An export route-policy for advertising VPN routes is configured for the VPN instance IPv6 address family.
     
     In addition to using a VPN target to control the advertisement or acceptance of VPN routes, an export route-policy can be configured to better control the advertisement of VPN routes. An export route-policy can be used to filter the routes advertised by the VPN instance IPv6 address family or modify route attributes.
     
     By default, export VPN targets are added to VPN routes after these routes match an export route-policy. If the export route-policy contains VPN target-related filter rules, the route-policy cannot apply to these routes. If you want to apply the route target-related filter rules defined in an export route-policy to VPN routes, configure the **add-ert-first** parameter to configure the system to add export VPN targets to VPN routes before matching these routes against the export route-policy.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.