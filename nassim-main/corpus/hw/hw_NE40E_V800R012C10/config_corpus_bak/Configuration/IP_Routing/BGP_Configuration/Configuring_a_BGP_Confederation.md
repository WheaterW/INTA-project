Configuring a BGP Confederation
===============================

On a large BGP network, configuring a BGP confederation reduces the number of IBGP connections and simplifies routing policy management, which increases the route advertisement efficiency.

#### Usage Scenario

A confederation is a solution to the increasing number of IBGP connections in an AS. The confederation divides an AS into multiple sub-ASs. In each sub-AS, IBGP peer relationships are set up or an RR is configured on one of the IBGP peers. EBGP connections are set up between sub-ASs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Compared with RRs, confederations facilitate IGP extensions.



#### Pre-configuration Tasks

Before configuring a BGP confederation, complete the following tasks:

* Configure link layer protocol parameters and assigning IP addresses to the interfaces to ensure that the status of the link layer protocol of the interface is Up.
* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

* Configure a BGP Confederation.
  
  
  
  Perform the following steps on the BGP device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**confederation id**](cmdqueryname=confederation+id) *as-number*
     
     
     
     A confederation ID is set.
  4. Run [**confederation peer-as**](cmdqueryname=confederation+peer-as) { *as-number* } &<1-32>
     
     
     
     The number of the sub-AS where other EBGP peers connected to the local AS reside is specified.
     
     
     
     The *as-number* used to specify a sub-AS in a confederation is valid in the confederation.
     
     The [**confederation id**](cmdqueryname=confederation+id) and [**confederation peer-as**](cmdqueryname=confederation+peer-as) commands must be run for all EBGP peers in a confederation, and the EBGP peers must have the same confederation ID.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The old speaker supporting 2-byte AS numbers and the new speaker supporting 4-byte AS numbers cannot exist in the same confederation. Otherwise, routing loops may occur because AS4\_Path does not support confederations.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure confederation compatibility.
  
  
  
  If some Routers in a confederation do not comply with the standard protocols, you can perform the following steps so that the local device is compatible with them:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**confederation nonstandard**](cmdqueryname=confederation+nonstandard)
     
     
     
     Confederation compatibility is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) [ *ipv4-address* ] **verbose** command to check detailed peer information.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about routes in the BGP routing table.