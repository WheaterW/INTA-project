Importing the Public Network Instance's Routes to the Routing Tables of an IPv4 VPN Instance
============================================================================================

Importing the Public Network Instance's Routes to the Routing Tables of an IPv4 VPN Instance

#### Prerequisites

Before configuring a device to import routes from a public network instance into the routing tables of an IPv4 VPN instance, you have completed the following tasks:

* [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html)
* [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Import different types of routes from the public network instance into the VPN instance's routing tables.
   * Import direct routes from the public network instance into the VPN instance's routing table for direct routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) public protocol direct [ route-policy route-policy-name ]
     ```
   * Import static routes from the public network instance into the VPN instance's routing table for static routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) public protocol static [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import OSPF routes from the public network instance into the VPN instance's routing table for OSPF routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) public protocol ospf process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import IS-IS routes from the public network instance into the VPN instance's routing table for IS-IS routes.
     ```
     [ip vpn-instance](cmdqueryname=ip+vpn-instance) vpn-instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family)
     ```
     ```
     [import-rib](cmdqueryname=import-rib) public protocol isis process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from the public network instance into the VPN instance's routing table for BGP routes.
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
     ```
     [import-rib public](cmdqueryname=import-rib+public) [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from the public network instance into the VPN instance's BGP multi-instance routing table.
     ```
     [bgp](cmdqueryname=bgp) as-number instance instance-name
     ```
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
     ```
     [import-rib](cmdqueryname=import-rib) base-instance public [ include-label-route ]  [ valid-route ] [ route-policy route-policy-name ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **display ip routing-table vpn-instance** *vpn-instance-name* command to check IPv4 routes imported into a specified VPN instance.
* Run the **display ip routing-table** command to check IPv4 routes on the public network.