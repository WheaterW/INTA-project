Configuring Basic BGP Community Attributes
==========================================

Configuring Basic BGP Community Attributes

#### Prerequisites

Before configuring BGP community attributes, you have completed the following task:

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
3. (Optional) Configure an if-match clause for the route-policy. The community attribute of routes can be added or modified only if the routes match the if-match clause.
   
   
   
   For details about the configuration, see [(Optional) Configuring an if-match Clause](vrp_route-policy_cfg_0014.html).
4. Configure community attributes for BGP routes.
   
   
   ```
   [apply community](cmdqueryname=apply+community+internet+no-advertise+no-export) { { cmntyNum | aa:nn } &<1-32> | internet | no-advertise | no-export | no-export-subconfed } * [ additive ]
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
9. Enable the device to send standard community attributes to the specified peer or peer group.
   
   
   ```
   [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [advertise-community](cmdqueryname=advertise-community)
   ```
   
   By default, the device advertises no community attribute to its peer or peer group.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *ipv4-address* [ *mask* | *mask-length*] command to check detailed information about a specified BGP route.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+community+internet+no-advertise) **community** [ *community-number* | *aa:nn* ] &<1-29> [ **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] \* [ **whole-match** ] command to check information about routes with a specified BGP community attribute.