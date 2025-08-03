Configuring an IPv6 VPN Instance on a PE
========================================

Configuring an IPv6 VPN Instance on a PE

#### Prerequisites

Before configuring an IPv6 VPN instance, you have completed the following task:

* Configure link layer protocol parameters for interfaces to ensure that these interfaces work properly.

#### Context

A VPN instance is also called a VRF or a per-site forwarding table.

VPN instances are used to isolate VPN routes from public network routes. Routes of different VPN instances are isolated from one another.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a VPN instance and enter the VPN instance view.
   
   
   ```
   [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The name of a VPN instance is case-sensitive. For example, **vpn1** and **VPN1** are considered different VPN instances.
3. (Optional) Configure a description for the VPN instance.
   
   
   ```
   [description](cmdqueryname=description) description-information
   ```
4. Enable the VPN instance IPv6 address family, and enter the VPN instance IPv6 address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family)
   ```
   
   Configurations in a VPN instance can be performed only after an address family is enabled for the VPN instance based on the advertised route and type of forwarded data.
5. Configure an RD for the VPN instance IPv6 address family.
   
   
   ```
   [route-distinguisher](cmdqueryname=route-distinguisher) route-distinguisher
   ```
   
   A VPN instance IPv6 address family takes effect only after having an RD configured. The RDs of different VPN instance IPv6 address families on a PE must be different.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you perform this step in the view of a newly created VPN instance, the VPN instance IPv6 address family is automatically enabled and the VPN instance IPv6 address family view is automatically displayed.
6. Configure VPN targets for the VPN instance IPv6 address family.
   
   
   ```
   [vpn-target](cmdqueryname=vpn-target) vpn-target &<1-8> [ both | export-extcommunity | import-extcommunity ]
   ```
   
   VPN targets are a type of BGP extended community attribute used to control the import and export of VPN routes. You can configure a maximum of eight import VPN targets and eight export VPN targets each time the [**vpn-target**](cmdqueryname=vpn-target) command is run. Run this command multiple times if you want to configure more VPN targets in the VPN instance IPv6 address family.
7. Set the maximum number of route prefixes allowed for the VPN instance IPv6 address family.
   
   
   ```
   [prefix limit](cmdqueryname=prefix+limit) number { alert-percent [ route-unchanged ] | simply-alert }
   ```
   
   
   This configuration prevents a VPN instance IPv6 address family on a PE from receiving too many route prefixes.![](public_sys-resources/note_3.0-en-us.png) 
   
   After the [**prefix limit**](cmdqueryname=prefix+limit) command is run to increase the maximum number of route prefixes allowed for a VPN instance IPv6 address family or the [**undo prefix limit**](cmdqueryname=undo+prefix+limit) command is run to cancel the limit, the device adds newly received route prefixes of various protocols to the VRF table for the VPN instance IPv6 address family.
   
   When the number of route prefixes exceeds the limit, direct routes and static routes can still be added to the VRF table for the VPN instance IPv6 address family.
8. (Optional) Configure an import route-policy for the VPN instance IPv6 address family.
   
   
   ```
   [import route-policy](cmdqueryname=import+route-policy) policy-name
   ```
   
   In addition to using VPN targets to control VPN route import and export, an import route-policy can be configured to better control VPN route import. An import route-policy can be used to filter routes to be imported into the VPN instance IPv6 address family or modify route attributes.
9. (Optional) Configure an export route-policy for the VPN instance IPv6 address family.
   
   
   ```
   [export route-policy](cmdqueryname=export+route-policy) policy-name [ add-ert-first ]
   ```
   
   
   
   In addition to using VPN targets to control VPN route import and export, an export route-policy can be configured to better control VPN route export. An export route-policy can be used to filter routes to be advertised to other PEs or modify route attributes.
   
   By default, export VPN targets are added to VPN routes after these routes are matched against an export route-policy. If the export route-policy contains VPN target-related filtering rules, it cannot apply to VPN routes. To address this issue, configure the **add-ert-first** parameter. This instructs the device to add export VPN targets to VPN routes before matching these routes against the export route-policy.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```