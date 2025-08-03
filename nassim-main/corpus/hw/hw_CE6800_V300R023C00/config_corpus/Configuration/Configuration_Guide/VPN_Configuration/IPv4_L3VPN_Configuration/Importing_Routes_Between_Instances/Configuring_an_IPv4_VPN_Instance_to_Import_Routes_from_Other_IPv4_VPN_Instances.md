Configuring an IPv4 VPN Instance to Import Routes from Other IPv4 VPN Instances
===============================================================================

Configuring an IPv4 VPN Instance to Import Routes from Other IPv4 VPN Instances

#### Prerequisites

Before configuring an IPv4 VPN instance to import routes from other IPv4 VPN instances, you have completed the following tasks:

* [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html)
* [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Import different types of routes from another VPN instance into the VPN instance's routing tables.
   * Import direct routes from another VPN instance into the VPN instance's routing table for direct routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol direct [ route-policy route-policy-name ]
     ```
   * Import static routes from another VPN instance into the VPN instance's routing table for static routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol static [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import OSPF routes from another VPN instance into the VPN instance's routing table for OSPF routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol ospf process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import IS-IS routes from another VPN instance into the VPN instance's routing table for IS-IS routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) vpn-instance vpn-instance-name protocol isis process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from another VPN instance into the BGP routing table in the BGP VPN instance IPv4 address family.
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
     ```
     [import-rib](cmdqueryname=import-rib) [ instance instance-name ] vpn-instance vpn-instance-name [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from another VPN instance into the BGP routing table in the BGP VPN instance IPv4 address family.
     ```
     [bgp](cmdqueryname=bgp) as-number instance instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
     ```
     [import-rib](cmdqueryname=import-rib) base-instance vpn-instance vpn-instance-name [ include-label-route ] [ valid-route ] [ route-policy route-policy-name ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **display ip routing-table vpn-instance** *vpn-instance-name* command to check IPv4 routes imported into a specified VPN instance.
* Run the **display ip routing-table** command to check IPv4 routes on the public network.