Configuring a VPN Instance on an ASBR
=====================================

If an ASBR also functions as a PE, you need to configure a VPN instance enabled with the IPv4 address family on the ASBR to manage VPN routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is created, and the VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The IPv4 address family is enabled for the VPN instance, and the VPN instance IPv4 address family view is displayed.
4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the VPN instance IPv4 address family.
5. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> **import-extcommunity**
   
   
   
   A VPN target is configured for the VPN instance IPv4 address family.
6. (Optional) Run [**prefix limit**](cmdqueryname=prefix+limit) *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }
   
   
   
   The maximum number of route prefixes allowed by the VPN instance IPv4 address family is set.
   
   To prevent a large number of route prefixes from being imported to a VPN instance, configure the maximum number of route prefixes allowed by this VPN instance.
7. (Optional) Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
   
   
   
   A routing policy for importing VPN routes is configured.
   
   In addition to using VPN targets to control VPN route sending and receiving, an import routing policy can be used to filter routes imported to the VPN instance IPv4 address family or modify route attributes so that VPN route receiving can be better controlled.
8. (Optional) Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name* [ **add-ert-first** ]
   
   
   
   A routing policy for exporting VPN routes is configured.
   
   In addition to using VPN targets to control VPN route sending and receiving, an export routing policy can be used to filter routes to be advertised to other PEs or modify route attributes so that VPN route sending can be better controlled.
   
   By default, ERTs are added to VPN routes before these routes are matched against an export routing policy. If the export routing policy contains RT-related filtering rules, these rules cannot apply to these routes. If you want to apply the RT-related filtering rules defined in an export routing policy to VPN routes, run the **add-ert-first** command to configure the system to add ERTs to VPN routes before matching these routes against the export routing policy.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.