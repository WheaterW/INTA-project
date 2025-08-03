Configuring BGP Between an MCE and a PE
=======================================

Configuring BGP Between an MCE and a PE

#### Prerequisites

Before configuring MCE, you have completed the following tasks:

* Configure a VPN instance for each service on the MCE and its connected PE. For details, see [Configuring an IPv4 VPN Instance on a PE](vrp_L3VPNv4_cfg_0007.html).
* Configure link and network layer protocols for LAN interfaces, and connect the LAN interface for each type of service to the MCE.
* Bind each MCE interface and the PE interface connecting to the MCE to the VPN instance, and configure IP addresses for the interfaces. For detailed configurations, see [Binding an Interface to an IPv4 VPN Instance](vrp_L3VPNv4_cfg_0008.html).

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
  3. Enter the BGP VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
  4. Configure the MCE as a VPN BGP peer for the PE.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address as-number as-number
     ```
  5. (Optional) Configure the maximum number of hops allowed for an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     This step is mandatory if the PE is not directly connected to the MCE but an EBGP peer relationship needs to be established between them.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for a TCP connection.
     
     The default value of *hop-count* is 255. If the maximum number of hops is set to 1, the MCE can establish an EBGP connection with only a directly connected peer.
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
  3. Enter the BGP VPN instance IPv4 address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family) vpn-instance vpn-instance-name
     ```
  4. Configure the MCE as a VPN BGP peer for the PE.
     
     
     ```
     [peer](cmdqueryname=peer) ipv4-address as-number as-number
     ```
  5. (Optional) Configure the maximum number of hops allowed for an EBGP connection.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name } [ebgp-max-hop](cmdqueryname=ebgp-max-hop) [ hop-count ]
     ```
     
     This step is mandatory if the PE is not directly connected to the MCE but an EBGP peer relationship needs to be established between them.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for a TCP connection.
     
     The default value of *hop-count* is 255. If the maximum number of hops is set to 1, the MCE can establish an EBGP connection with only a directly connected peer.
  6. (Optional) Configure the MCE to import the direct routes in the site where it resides into its IPv4 VPN instance routing table.
     
     
     + Use the **import-route** command to import routes.
       ```
       [import-route](cmdqueryname=import-route) direct [ med med-value | route-policy route-policy-name ] *
       ```
     + Use the **network** command to import routes.
       ```
       [network](cmdqueryname=network) ipv4-address [ mask | mask-length ] [ route-policy route-policy-name ]
       ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```