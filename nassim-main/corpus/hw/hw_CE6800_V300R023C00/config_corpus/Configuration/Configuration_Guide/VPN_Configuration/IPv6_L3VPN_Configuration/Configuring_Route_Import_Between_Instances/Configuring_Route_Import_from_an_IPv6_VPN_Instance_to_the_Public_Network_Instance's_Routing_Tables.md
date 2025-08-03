Configuring Route Import from an IPv6 VPN Instance to the Public Network Instance's Routing Tables
==================================================================================================

Configuring Route Import from an IPv6 VPN Instance to the Public Network Instance's Routing Tables

#### Prerequisites

Before configuring route import from an IPv6 VPN instance into the public network instance's routing tables, you have completed the following task:

* [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html)
* [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Import different types of IPv6 routes from a VPN instance into the public network instance's corresponding routing tables.
   * Import direct routes from the VPN instance into the public network instance's routing table for direct routes.
     ```
     [ipv6 import-rib vpn-instance](cmdqueryname=ipv6+import-rib+vpn-instance) vpn-instance-name protocol direct [ route-policy route-policy-name ]
     ```
   * Import static routes from the VPN instance into the public network instance's routing table for static routes.
     ```
     [ipv6 import-rib vpn-instance](cmdqueryname=ipv6+import-rib+vpn-instance) vpn-instance-name protocol static [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import OSPFv3 routes from the VPN instance into the public network instance's routing table for OSPFv3 routes.
     ```
     [ipv6 import-rib vpn-instance](cmdqueryname=ipv6+import-rib+vpn-instance) vpn-instance-name protocol ospfv3 process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import IS-ISv6 routes from the VPN instance into the public network instance's routing table for IS-ISv6 routes.
     ```
     [ipv6 import-rib vpn-instance](cmdqueryname=ipv6+import-rib+vpn-instance) vpn-instance-name protocol isis process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from the VPN instance into the public network instance's routing table for BGP routes.
     ```
     [bgp](cmdqueryname=bgp) as-number
     [ipv6-family](cmdqueryname=ipv6-family) unicast
     [import-rib vpn-instance](cmdqueryname=import-rib+vpn-instance) vpn-instance-name [ valid-route ] [ route-policy route-policy-name ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about IPv6 routes imported into a specified VPN instance.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check public network IPv6 routes.