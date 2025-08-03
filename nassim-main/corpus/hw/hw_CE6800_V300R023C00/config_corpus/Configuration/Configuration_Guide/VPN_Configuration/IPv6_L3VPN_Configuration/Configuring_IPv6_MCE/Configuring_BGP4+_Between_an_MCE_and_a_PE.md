Configuring BGP4+ Between an MCE and a PE
=========================================

Configuring BGP4+ Between an MCE and a PE

#### Prerequisites

Before configuring MCE, complete the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv6 VPN Instance on a PE](vrp_L3VPNv6_cfg_0006.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind the MCE's interfaces and the PE's interface connected to the MCE to VPN instances and configure IP addresses for these interfaces. For details, see [Binding an Interface to the IPv6 VPN Instance](vrp_L3VPNv6_cfg_0007.html).

#### Procedure

* Configure the PE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the BGP VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     ```
  4. Configure the MCE as a VPN peer for the PE.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address as-number as-number
     ```
  5. (Optional) Set the maximum number of hops allowed for an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     This step is mandatory if the PE is not directly connected to the MCE but an EBGP peer relationship needs to be established between them.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for the TCP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the PE can establish an EBGP connection with only a directly connected peer.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the MCE.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the BGP VPN instance IPv6 address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family) vpn-instance vpn-instance-name
     ```
  4. Configure the PE as a VPN peer for the MCE.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address as-number as-number
     ```
  5. (Optional) Set the maximum number of hops allowed for an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     This step is mandatory if the PE is not directly connected to the MCE but an EBGP peer relationship needs to be established between them.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for the TCP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the MCE can establish an EBGP connection with only a directly connected peer.
  6. (Optional) Configure the MCE to import the direct routes in the site where it resides into its IPv6 VPN instance routing table.
     
     
     ```
     [import-route](cmdqueryname=import-route) direct [ med med-value | route-policy route-policy-name ] *
     ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ **verbose** ] command on the MCE to check the IPv6 routing table of the VPN instance.