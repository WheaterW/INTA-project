Configuring Route Import from One IPv6 VPN Instance into Another IPv6 VPN Instance
==================================================================================

Configuring Route Import from One IPv6 VPN Instance into Another IPv6 VPN Instance

#### Prerequisites

Before configuring route import from one IPv6 VPN instance into another IPv6 VPN instance, complete the following task:

* [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html)
* [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Import different types of routes from another VPN instance into the VPN instance's routing tables.
   * Import direct routes from another VPN instance into the VPN instance's routing table for direct routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     [ipv6-family](cmdqueryname=ipv6-family)
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol direct [ route-policy route-policy-name ]
     ```
   * Import static routes from another VPN instance into the VPN instance's routing table for static routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     [ipv6-family](cmdqueryname=ipv6-family)
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol static [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import OSPFv3 routes from another VPN instance into the VPN instance's routing table for OSPFv3 routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     [ipv6-family](cmdqueryname=ipv6-family)
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol ospfv3 process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import IS-ISv6 routes from another VPN instance into the VPN instance's routing table for IS-ISv6 routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     [ipv6-family](cmdqueryname=ipv6-family)
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol isis process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from another VPN instance into the BGP routing table in the BGP VPN instance IPv6 address family.
     ```
     [bgp](cmdqueryname=bgp) as-number
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     [import-rib vpn-instance](cmdqueryname=import-rib+vpn-instance) vpn-instance-name [ valid-route ] [ route-policy route-policy-name ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about IPv6 routes imported into a specified VPN instance.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check public network IPv6 routes.