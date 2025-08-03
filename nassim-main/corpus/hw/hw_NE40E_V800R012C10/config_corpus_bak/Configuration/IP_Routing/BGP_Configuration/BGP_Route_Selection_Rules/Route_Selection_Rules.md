Route Selection Rules
=====================

When multiple received routes are available to the same destination, BGP selects one optimal route based on BGP route selection rules and adds it to the IP routing table for traffic forwarding.

On the NE40E, when multiple routes to the same destination are available, BGP selects routes based on rules. For details about the rules, see [BGP Route Processing](feature_0005549734.html).

[Figure 1](#EN-US_CONCEPT_0172366300__fig118023455314) shows the BGP route selection process.

**Figure 1** BGP route selection process  
![](figure/en-us_image_0000001264951885.png)

BGP selects routes by comparing route attributes in a fixed order. When a route attribute is a sufficient condition for determining the optimal route, BGP does not compare the other attributes. If BGP fails to select the optimal route after comparing all route attributes, the route that was first received is selected as the optimal route. [Table 1](#EN-US_CONCEPT_0172366300__table_fig_dc_vrp_bgp_path_selection_000201) lists the abbreviated alias, route selection rules, and remarks of each matching item. [Table 1](#EN-US_CONCEPT_0172366300__table_fig_dc_vrp_bgp_path_selection_000201) shows that the route priority is directly proportional to the PrefVal or Local\_Pref value and inversely proportional to the rest of the attribute values or lengths. In addition, the first column can be summarized as a character string (OPPAAA OMTCC RA), which helps memorize the matching sequence.

**Table 1** BGP route selection process
| Abbreviated Alias | Matching Item | Route Selection Rules | Remarks |
| --- | --- | --- | --- |
| O | Origin AS | Valid > NotFound > Invalid | BGP origin AS validation states are applied to route selection in a scenario where the device is connected to an RPKI server. |
| P | PrefVal | The route with the largest PrefVal value is preferred.  The default value is 0. | It is valid only locally. |
| P | Local\_Pref | The route with the largest Local\_Pref value is preferred.  The default value is 100. | To modify the default Local\_Pref value of BGP routes, run the [**default local-preference**](cmdqueryname=default+local-preference) command. |
| A  NOTE:  A is the initial of the character string (ASNIL). | Route generation mode | A > S > N > I > L, where:  * A: indicates the summary routes manually generated using the [**aggregate**](cmdqueryname=aggregate) command. * S: indicates the summary routes automatically generated using the [**summary automatic**](cmdqueryname=summary+automatic) command. * N: indicates the routes imported using the [**network**](cmdqueryname=network) command. * I: indicates the routes imported using the [**import-route**](cmdqueryname=import-route) command. * L: indicates the routes learned from peers. | - |
| A | Accumulated Interior Gateway Protocol (AIGP) | The route with the smallest AIGP value is preferred.  The route with AIGP to the route without AIGP is preferred. | - |
| A | AS\_Path | The route with the shortest AS\_Path length is preferred. | If the **bestroute as-path-ignore** command is run, BGP no longer compares the AS\_Path lengths during route selection. |
| O | Origin | IGP > EGP > Incomplete | - |
| M | Multi Exit Discriminator (MED) | The route with the smallest MED value is preferred.  The default value is 0. | If the [**bestroute med-none-as-maximum**](cmdqueryname=bestroute+med-none-as-maximum) command is configured, BGP considers the largest MED value (4294967295) as the MED of a route that does not carry MED.  For details about MED usage, see [MED](dc_vrp_bgp_path_selection_0011.html). |
| T | Peer type | EBGP > IBGP | - |
| C | IGP metric | The route with the smallest IGP metric is preferred. | If the **bestroute igp-metric-ignore** command is run, BGP does not compare the IGP metrics of candidate routes. |
| C | Cluster\_List | The route with the shortest Cluster\_List length is preferred. | By default, BGP compares Cluster\_Lists prior to Originator\_IDs during route selection. To enable BGP to compare Originator\_IDs prior to Cluster\_Lists during route selection, run the [**bestroute routerid-prior-clusterlist**](cmdqueryname=bestroute+routerid-prior-clusterlist) command. |
| R | Router ID | The route with the smallest router ID is preferred. | If routes carry the Originator\_ID, the originator ID is substituted for the router ID during route selection. The route with the smallest Originator\_ID is preferred. |
| A | Peer IP address | The route learned from the peer with the smallest IP address is preferred. | - |



#### Selection of the Routes for Load Balancing

After BGP load balancing is configured, the BGP routes that meet the following conditions are used as equal-cost routes for load balancing:

* Original next-hop addresses are different.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  For labeled VPN unicast routes, the original next hops or labels are different.
* The routes have the same PrefVal value.
* The routes have the same Local\_Pref value.
* All the routes are summarized or non-summarized routes.
* The routes have the same AIGP value.
* The routes have the same AS\_Path length.
* The routes have the same origin type (IGP, EGP, or incomplete).
* The routes have the same MED value.
* All the routes are EBGP or IBGP routes. If the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp) command is run, load balancing can be implemented among EBGP and IBGP routes.
* The metric values of the IGP routes to which BGP routes within an AS recurse are the same. After the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command is run, the device does not compare IGP metric values when selecting routes for load balancing.
* All routes are blackhole routes, or none of them are blackhole routes.

Load balancing can be implemented between non-leaked routes or between leaked routes, but not between labeled BGP routes and non-labeled BGP routes even if the preceding conditions are met. If the [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross) command is run in a VPN, load balancing can be implemented between unlabeled unicast VPN routes and labeled routes. Load balancing cannot be implemented between blackhole routes and non-blackhole routes.


#### VPN Route Selection Rules

On the NE40E, the rules for selecting VPN BGP routes are the same as those for selecting public network BGP routes. The only difference is that VPN BGP routes need to be leaked based on VPN targets. For details about route leaking, see "BGP VPN Route Leaking" in NE40E *Feature Description > IP Routing > BGP*.