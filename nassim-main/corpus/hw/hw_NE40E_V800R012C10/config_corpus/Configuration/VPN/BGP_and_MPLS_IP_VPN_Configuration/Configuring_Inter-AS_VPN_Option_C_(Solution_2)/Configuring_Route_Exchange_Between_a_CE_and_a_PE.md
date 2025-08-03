Configuring Route Exchange Between a CE and a PE
================================================

A PE and a CE can communicate using BGP, IGP, or a static route.

#### Procedure

* Configure the PE.
  
  
  
  Perform the following steps on the PE that connects to a CE
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name* command to enter the BGP VPN instance IPv4 address family view.
  4. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to configure the CE as a VPN peer.
  5. (Optional) Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ] command to configure the maximum number of hops allowed for an EBGP connection.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, you also need to run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for an EBGP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the device can establish an EBGP connection with only a directly connected peer.
  6. (Optional) Run the [**network**](cmdqueryname=network) *ip-address* *mask* command to advertise direct routes to the local CE.
     
     
     
     The PE automatically learns direct routes to the local CE. These learned routes take precedence over the direct routes advertised by the local CE through EBGP. If this step is not performed, the PE does not use MP-BGP to advertise direct routes destined for the local CE to the remote PE.
  7. (Optional) Run the [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ] command to permit routing loops.
  8. (Optional) Run the [**peer**](cmdqueryname=peer) *ip-address* **substitute-as** command to enable BGP AS number substitution.
     
     
     
     In a scenario where VPN sites in the same AS or those that have different private AS numbers communicate through the BGP/MPLS IP VPN backbone network, if a CE and its connected PE in a VPN site establish an EBGP connection, VPN routes from other VPN sites may carry the AS number of this VPN site. As a result, the CE discards the VPN routes, causing a failure in VPN site communication. To prevent this situation from occurring, run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the PE to enable AS number substitution.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the CE.
  
  
  
  Perform the following steps on the CE.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Run the [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number* command to specify a PE as a peer.
  4. (Optional) Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ] command to configure the maximum number of hops allowed for an EBGP connection.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, you also need to run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for an EBGP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the device can establish an EBGP connection with only a directly connected peer.
  5. Run the [**import-route**](cmdqueryname=import-route) { **rip** | **isis** | **ospf** } *process-id* [ **med** *med* | [ [**route-policy**](cmdqueryname=route-policy) *route-policy-name* | **route-filter** *route-filter-name* ] ] \* [ **non-relay-tunnel** ] command to import the routes of the local site.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.