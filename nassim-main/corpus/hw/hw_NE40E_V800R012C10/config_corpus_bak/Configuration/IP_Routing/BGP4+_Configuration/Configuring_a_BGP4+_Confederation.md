Configuring a BGP4+ Confederation
=================================

On a large BGP4+ network, configuring a BGP4+ confederation reduces the number of IBGP connections and simplifies routing policy management, which increases the route advertisement efficiency.

#### Usage Scenario

A confederation is a solution to the increasing number of IBGP connections in an AS. The confederation divides an AS into multiple sub-ASs. In each sub-AS, IBGP peer relationships are set up or an RR is configured on one of the IBGP peers. EBGP connections are set up between sub-ASs.


#### Pre-configuration Tasks

Before configuring a BGP4+ confederation, complete the following tasks:

* Configure link layer protocol parameters and assigning IP addresses to the interfaces to ensure that the status of the link layer protocol of the interface is Up.
* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

* Configure a BGP4+ confederation.
  
  
  
  Perform the following steps on the BGP4+ router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**confederation id**](cmdqueryname=confederation+id) *as-number*
     
     
     
     The confederation ID is set.
  4. Run [**confederation peer-as**](cmdqueryname=confederation+peer-as) { *as-number* } &<1-32>
     
     
     
     A sub-AS number is set for other EBGP peers connected to the local AS.
     
     The *as-number* parameter set for a sub-AS is valid only in the confederation.
     
     The [**confederation id**](cmdqueryname=confederation+id) and [**confederation peer-as**](cmdqueryname=confederation+peer-as) commands must be run for all the EBGP peers in a confederation, and the EBGP peers must have the same confederation ID.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The old speaker supporting 2-byte AS numbers and the new speaker supporting 4-byte AS numbers cannot exist in the same confederation. Otherwise, routing loops may occur because AS4\_Path does not support confederations.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the compatibility of the confederation.
  
  
  
  If the confederation implementation of some Routers do not comply with the standard protocol, you can perform the following steps on BGP4+ routers for compatibility:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**confederation nonstandard**](cmdqueryname=confederation+nonstandard)
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the following command to check the previous configuration.

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer+verbose) [ *ipv6-address* ] **verbose** command to check detailed information about the specified peer.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) [ *ipv6-address* *prefix-length* ] command to check information about routes in the BGP4+ routing table.