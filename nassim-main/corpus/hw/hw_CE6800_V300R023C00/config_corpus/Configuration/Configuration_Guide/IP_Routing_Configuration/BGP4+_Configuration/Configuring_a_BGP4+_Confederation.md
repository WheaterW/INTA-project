Configuring a BGP4+ Confederation
=================================

Configuring a BGP4+ Confederation

#### Prerequisites

Before configuring a BGP4+ confederation, you have completed the following tasks:

* Configure parameters of the data link layer protocol and IPv6 addresses for interfaces to ensure that the data link layer protocol on the interfaces is up.
* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

A confederation is used to deal with the increasing number of IBGP connections in an AS. The confederation divides an AS into multiple sub-ASs. In each sub-AS, IBGP peer relationships are set up or an RR is configured on one of the IBGP peers. EBGP connections are set up between sub-ASs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Set a confederation ID.
   
   
   ```
   [confederation id](cmdqueryname=confederation+id) as-number
   ```
4. Set a sub-AS number for other EBGP peers connected to the local AS.
   
   
   ```
   [confederation peer-as](cmdqueryname=confederation+peer-as) as-number &<1-32>
   ```
   
   The *as-number* used to configure a sub-AS in a confederation is valid only in the confederation.
   
   The [**confederation id**](cmdqueryname=confederation+id) and [**confederation peer-as**](cmdqueryname=confederation+peer-as) commands must be run for all EBGP peers in a confederation, and the same confederation ID must be specified for the EBGP peers.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Old speakers (supporting only 2-byte AS numbers) and new speakers (supporting 4-byte AS numbers) cannot coexist in the same confederation. Otherwise, routing loops may occur because the AS4\_Path function is not supported in confederations.
5. (Optional) Configure the device that supports standard confederations to be compatible with another device that does not support standard confederations.
   
   
   ```
   [confederation nonstandard](cmdqueryname=confederation+nonstandard)
   ```
   
   By default, a device that supports standard AS confederations is incompatible with another device that does not support standard AS confederations.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify it:

* Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer) [ *ipv6-address* ] **verbose** command to check detailed BGP4+ peer information.
* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) [ *ipv6-address* *prefix-length* ] command to check information about routes in the BGP4+ routing table.