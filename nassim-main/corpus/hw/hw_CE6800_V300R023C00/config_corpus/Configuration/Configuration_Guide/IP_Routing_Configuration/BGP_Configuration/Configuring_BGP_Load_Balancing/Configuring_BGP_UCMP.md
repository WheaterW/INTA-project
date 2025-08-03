Configuring BGP UCMP
====================

Configuring BGP UCMP

#### Prerequisites

Before configuring BGP UCMP, you have completed the following tasks:

* Load balancing has been implemented among BGP routes, and the BGP routes carry the Link Bandwidth extended community attribute and recurse to IP routes or tunnels.
* [Configure the Link Bandwidth extended community attribute](vrp_bgp_cfg_0084.html), or run the [**peer generate-link-bandwidth**](cmdqueryname=peer+generate-link-bandwidth) command to configure the device to obtain the link bandwidth of a specified directly connected EBGP peer and generate the extended community attribute.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Configure BGP UCMP to implement unequal-cost load balancing among BGP routes based on the Link Bandwidth extended community attribute.
   
   
   ```
   [load-balancing ucmp](cmdqueryname=load-balancing+ucmp)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* ] [ *mask* | *mask-length* ] command to check information about routes in the BGP routing table.