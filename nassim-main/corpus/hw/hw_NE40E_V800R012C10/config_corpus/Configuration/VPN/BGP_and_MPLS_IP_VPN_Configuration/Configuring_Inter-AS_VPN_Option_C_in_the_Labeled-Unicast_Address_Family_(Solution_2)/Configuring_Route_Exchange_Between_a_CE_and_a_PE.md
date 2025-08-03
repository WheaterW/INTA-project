Configuring Route Exchange Between a CE and a PE
================================================

A PE and a CE can communicate using BGP, IGP, or a static route.

#### Procedure

* Configure the PE.
  
  
  
  Perform the following steps on the PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP VPN instance IPv4 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The CE is configured as a VPN peer.
  5. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops allowed for the EBGP connection is specified.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for a TCP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the device can establish an EBGP connection with only a directly connected peer.
  6. (Optional) Run [**network**](cmdqueryname=network) *ip-address* *mask*
     
     
     
     The direct routes are advertised to the local CE.
     
     
     
     The PE automatically learns direct routes to the local CE. These learned routes take precedence over the direct routes advertised by the local CE through EBGP. If this step is not performed, the PE does not use MP-BGP to advertise direct routes destined for the local CE to the remote PE.
  7. (Optional) Run [**peer**](cmdqueryname=peer) *ip-address* **allow-as-loop** [ *number* ]
     
     
     
     Routing loops are permitted.
  8. (Optional) Run [**peer**](cmdqueryname=peer) *ip-address* **substitute-as**
     
     
     
     The function to substitute BGP AS numbers is enabled.
     
     
     
     In a scenario where VPN sites in the same site or those that have different private AS numbers communicate through the BGP/MPLS IP VPN backbone network, if a CE and its connected PE in a VPN site establish an EBGP connection, VPN routes from other VPN sites may carry the AS number of this VPN site. As a result, the CE discards the VPN routes, causing a failure in VPN site communication. To prevent this situation from occurring, run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the PE to enable AS number substitution.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the CE.
  
  
  
  Perform the following steps on the CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number**
     
     
     
     The PE is configured as a VPN peer.
  4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
     
     
     
     The maximum number of hops allowed for the EBGP connection is specified.
     
     
     
     In most cases, a directly connected physical link must be available between EBGP peers. If you want to establish an EBGP peer relationship between indirectly connected peers, run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to set the maximum number of hops allowed for a TCP connection.
     
     The default *hop-count* value is 255. If the maximum number of hops is set to 1, the device can establish an EBGP connection with only a directly connected peer.
  5. Run [**import-route**](cmdqueryname=import-route) { **rip** | **isis** | **ospf** } *process-id* [ [ **med** *med* ] | [ [ [**route-policy**](cmdqueryname=route-policy) *route-policy-name* ] | [ **route-filter** *route-filter-name* ] ] ] \* [ **non-relay-tunnel** ]
     
     
     
     Routes of the local site are imported.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.