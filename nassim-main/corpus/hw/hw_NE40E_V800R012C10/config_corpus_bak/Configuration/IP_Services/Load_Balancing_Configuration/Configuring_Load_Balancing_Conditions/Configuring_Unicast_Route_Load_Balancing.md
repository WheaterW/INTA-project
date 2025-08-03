Configuring Unicast Route Load Balancing
========================================

Before configuring unicast route load balancing, please attention to the maximum number of routes of the unicast routing table. The route load balancing increases the number of routes.

#### Configuring Load Balancing Among IGP Routes

Configuration Procedure:

1. Deploy multiple links of the same cost/metric to achieve load balancing.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Modification of IGP cost impacts on BGP route selection.
2. (Optional) Set the maximum number of routes among which load balancing is performed. For different products and different protocols, the maximum number of equal-cost routes is different, as shown in [Table 1](#EN-US_CONCEPT_0172365019__tab_04401).

**Table 1** Configuration Guide for Maximum Number of IGP Load-balancing
| Route Type | Command Format | View |
| --- | --- | --- |
| OSPF | [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* | OSPF view |
| OSPFv3 | [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* | OSPFv3 view |
| IS-IS | [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* | IS-IS view  IS-IS topology view  IS-IS IPv6 topology view |
| IS-IS IPv6 | [**ipv6 maximum load-balancing**](cmdqueryname=ipv6+maximum+load-balancing) *number*  NOTE:  This command is valid only for an IPv6 base topology, and invalid for IPv6 routes in multi-topology.  The [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* command in the IS-IS IPv6 topology view is used to configure load balancing among IPv6 routes in multi-topology. | IS-IS view |
| RIP | [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* | RIP view |
| RIPng | [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) *number* | RIPng view |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

For different products and different protocols, the maximum number of equal-cost routes is different. The maximum value can be adjusted by purchasing license files.



#### Configuring Load Balancing Among BGP Routes

There are three solutions for Load Balancing Among BGP Routes

* **Solution 1**: Static routes or equal-cost IGP routes for BGP route recursion. Configuration Procedure:
  
  1. Establish the BGP peers relationship using Loopback interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The default TTL value of an EBGP packet is 1. You must run the [**peer ebgp-max-hop**](cmdqueryname=peer+ebgp-max-hop) command to change the TTL value on both communication parties.
  2. Deploy multiple links between the BGP peers.
  3. Configure multiple static routes or equal-cost IGP routes to the loopback interface address of the remote BGP peer.
  4. Set the maximum number of equal-cost routes to implement BGP route load balancing. For details on how to set the maximum number of equal-cost routes, see [Table 2](#EN-US_CONCEPT_0172365019__tab_04402).![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     By default, the maximum number of equal-cost BGP routes is 1, that is, the load balancing among BGP routes is not enabled by default.
     
     If the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) command is configured, when the routes advertised from the EBGP peer are advertised to IBGP peers, the next hop address of the routes is set as the local IP address by which the IBGP peer is established. If the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) command is not configured, the next hop address of the routes is not changed when the routes are advertised to the IBGP peer, unless the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is configured.
  
  **Table 2** Configuration Guide for Maximum Number of BGP Load-balancing
  | Route Type | Command Format | Views | Default value |
  | --- | --- | --- | --- |
  | BGP | 1. Run the [**maximum load-balancing**](cmdqueryname=maximum+load-balancing) [ **ebgp** | **ibgp** ] *number* command to set the maximum number of equal-cost routes. 2. (Optional) Run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command to configure a router to ignore comparing the AS\_Path attributes of the routes among which load balancing is performed. 3. Run the [**commit**](cmdqueryname=commit). | BGP view  BGP IPv4 unicast address family view  BGP IPv6 unicast address family view  BGP-VPN instance IPv4 address family view  BGP-VPN instance IPv6 address family view | 1 |
  | EBGP and IBGP | 1. Run the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp) *number* command to set the maximum number of equal-cost routes. 2. (Optional) Run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command to configure a router to ignore comparing the AS\_Path attributes of the routes among which load balancing is performed. 3. Run the [**commit**](cmdqueryname=commit). | BGP-VPN instance IPv4 address family view  BGP-VPN instance IPv6 address family view | 1 |
  
  For application case of **Solution 1**, see [BGP Route Load Balancing in an RR Scenario](load-balance_feature_055.html).
* **Solution 2**: Modify BGP route attributes according to the rule of BGP route selection. Configuration Procedure:
  
  1. Deploy multiple links between the BGP peers.
  2. Modify BGP route attributes according to the rule of BGP route selection. For detailed information about the rule of BGP route selection, see [Load Balancing Among BGP Routes](load-balance_feature_013.html).
  3. Set the maximum number of routes among which load balancing is performed, see the above table.
* **Solution 3**: Divide the destination addresses into multiple groups and deploy multiple links between the BGP peers, one link for each group. Suitable scenarios: there are multiple EBGP peers in the same AS to the same destination. Configuration Procedure:
  
  1. Configure a static route to the virtual address of the remote EBGP peer on each EBGP router. Load balancing among EBGP routes is implemented through route recursion.
  2. Configure ACL, IP-prefix, AS-Path filter, community-filter, extcommunity-filter, or Route Distinguisher (RD) filter to divide the destination addresses into multiple groups.
  3. Configure route policies to set the next hop address as the Loopback address of the EBGP peer so that one link is used for each group.
  4. Apply the route policies to the routes advertisement from the EBGP routers to RR or IBGP peer.
  
  For application case of **Solution 3**, see [Solution to the Low Equal-Cost Route Specification on the Remote Device Without Interrupting Services](load-balance_feature_056.html).


#### Follow-up Procedure

Run the **save** command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.