Configuring the BGP Large-Community Attribute
=============================================

Configuring the BGP Large-Community Attribute

#### Prerequisites

Before configuring the BGP large-community attribute, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy+deny+permit+node) route-policy-name { deny | permit } node node
   ```
3. (Optional) Configure an if-match clause for the route-policy. The large-community attribute of routes can be added or modified only if the routes match the if-match clause.
   
   
   
   For details about the configuration, see [(Optional) Configuring an if-match Clause](vrp_route-policy_cfg_0014.html).
4. Configure the Large-Community attribute for BGP routes.
   
   
   ```
   [apply large-community](cmdqueryname=apply+large-community+additive+overwrite+delete) { aa:bb:cc } &<1-16> { additive | overwrite | delete }
   ```
   
   or
   
   ```
   [apply large-community-list](cmdqueryname=apply+large-community-list+additive+overwrite+delete) large-community-list-name { additive | overwrite | delete }
   ```
5. Exit the route-policy view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
7. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
8. Configure an export route-policy.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [route-policy](cmdqueryname=route-policy+export) route-policy-name export
   ```
9. Enable the device to advertise Large-Community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [advertise-large-community](cmdqueryname=advertise-large-community)
   ```
   
   
   
   By default, the device does not advertise Large-Community attributes to its peers or peer groups.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *network* [ *mask* | *mask-length* ] command to check detailed information about a specified BGP route.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+large-community+whole-match) **large-community** [ *aa:bb:cc*] &<1-33> [ **whole-match**] command to check information about routes with the specified BGP Large-Community attribute.