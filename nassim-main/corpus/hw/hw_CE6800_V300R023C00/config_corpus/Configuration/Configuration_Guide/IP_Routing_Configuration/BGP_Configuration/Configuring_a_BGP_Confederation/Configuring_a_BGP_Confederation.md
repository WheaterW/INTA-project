Configuring a BGP Confederation
===============================

Configuring a BGP Confederation

#### Prerequisites

Before configuring a BGP confederation, you have completed the following tasks:

* Configure parameters of the data link layer protocol and IP addresses for interfaces to ensure that the data link layer protocol on the interfaces is up.
* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

A confederation is used to deal with the increasing number of IBGP connections in an AS. The confederation divides an AS into multiple sub-ASs. In each sub-AS, IBGP peer relationships are set up between all IBGP peers or an RR is configured on one of the IBGP peers. EBGP connections are set up between sub-ASs. On a large BGP network, configuring a BGP confederation helps reduce the number of IBGP connections to be established and simplifies route-policy management, which increases route advertisement efficiency.

![](public_sys-resources/note_3.0-en-us.png) 

Unlike RRs, confederations facilitate the implementation of IGP extensions.



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
5. (Optional) Configure the device that supports standard AS confederations to be compatible with another device that does not support standard AS confederations.
   
   
   ```
   [confederation nonstandard](cmdqueryname=confederation+nonstandard)
   ```
   
   By default, a device that supports standard AS confederations is incompatible with another device that does not support standard AS confederations.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* ] **verbose** command to check detailed information about peers.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *ipv4-address*] [ *mask* | *mask-length*] [ **longer-prefixes**] command to check information about routes in the BGP routing table.