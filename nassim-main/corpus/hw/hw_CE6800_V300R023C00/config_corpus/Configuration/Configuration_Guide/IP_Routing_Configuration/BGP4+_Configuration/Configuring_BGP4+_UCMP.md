Configuring BGP4+ UCMP
======================

Configuring BGP4+ UCMP

#### Prerequisites

Before configuring BGP4+ UCMP, you have completed the following task:

* Ensure that load balancing is implemented among BGP4+ routes and the BGP4+ routes carry the Link Bandwidth extended community attribute and are forwarded through IP or tunnels.
* [Configure the Link Bandwidth extended community attribute](vrp_bgp6_cfg_0067.html), or run the [**peer generate-link-bandwidth**](cmdqueryname=peer+generate-link-bandwidth) command to configure a device to obtain the link bandwidth of a specified directly connected EBGP peer and generate the extended community attribute.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Configure BGP4+ UCMP to implement unequal-cost load balancing among BGP4+ routes based on the Link Bandwidth extended community attribute.
   
   
   ```
   [load-balancing ucmp](cmdqueryname=load-balancing+ucmp)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* *prefix-length* command to check information about routes in the BGP4+ routing table.