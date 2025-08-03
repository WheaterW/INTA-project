Importing the IPv4 VPN Instance's Routes to the Routing Tables of a Public Network Instance
===========================================================================================

Importing the IPv4 VPN Instance's Routes to the Routing Tables of a Public Network Instance

#### Prerequisites

Before importing an IPv4 VPN instance's routes to the routing tables of a public network instance, you have completed the following tasks:

* [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html)
* [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Import different types of routes from a VPN instance into the public network instance's corresponding routing tables.
   * Import direct routes from the VPN instance into the public network instance's routing table for direct routes.
     ```
     [ip import-rib vpn-instance](cmdqueryname=ip+import-rib+vpn-instance) vpn-instance-name protocol direct [ route-policy route-policy-name ]
     ```
   * Import static routes from the VPN instance into the public network instance's routing table for static routes.
     ```
     [ip import-rib vpn-instance](cmdqueryname=ip+import-rib+vpn-instance) vpn-instance-name protocol static [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import OSPF routes from the VPN instance into the public network instance's routing table for OSPF routes.
     ```
     [ip import-rib vpn-instance](cmdqueryname=ip+import-rib+vpn-instance) vpn-instance-name protocol ospf process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import IS-IS routes from the VPN instance into the public network instance's routing table for IS-IS routes.
     ```
     [ip import-rib vpn-instance](cmdqueryname=ip+import-rib+vpn-instance) vpn-instance-name protocol isis process-id [ valid-route ] [ route-policy route-policy-name ]
     ```
   * Import BGP routes from the VPN instance into the public network instance's routing table for BGP routes.
     ```
     [bgp](cmdqueryname=bgp) as-number
     [ipv4-family](cmdqueryname=ipv4-family) unicast
     [import-rib vpn-instance](cmdqueryname=import-rib+vpn-instance) vpn-instance-name [ valid-route ] [ route-policy route-policy-name ]
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the **display ip routing-table vpn-instance** *vpn-instance-name* command to check IPv4 routes imported into a specified VPN instance.
* Run the **display ip routing-table** command to check IPv4 routes on the public network.