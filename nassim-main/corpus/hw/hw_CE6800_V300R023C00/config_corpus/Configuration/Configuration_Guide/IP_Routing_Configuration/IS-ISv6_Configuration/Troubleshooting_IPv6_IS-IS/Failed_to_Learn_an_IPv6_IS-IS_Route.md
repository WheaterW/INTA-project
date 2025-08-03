Failed to Learn an IPv6 IS-IS Route
===================================

Failed to Learn an IPv6 IS-IS Route

#### Fault Symptom

A device cannot learn an IPv6 IS-IS route from a neighbor when the link runs properly.


#### Possible Causes

1. An IS-IS neighbor relationship fails to be established.
2. IS-IS cost styles do not match.
3. The IS-IS route is not optimal.

#### Procedure

1. Check that an IS-IS neighbor relationship is established between the device and its neighbor.
   
   
   
   Run the [**display isis peer**](cmdqueryname=display+isis+peer) command on each device on the link to check whether an IS-IS neighbor relationship has been established.
   
   If an IS-IS neighbor relationship fails to be established, see [Failed to Establish an IPv6 IS-IS Neighbor Relationship](vrp_isis_ipv6_cfg_0084.html).
2. Check that the IS-IS cost styles of the two ends match.
   
   
   
   Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **isis** command on the device and its neighbor to check their IS-IS cost styles.
   
   The device can learn IS-IS routes from its neighbor only if their IS-IS cost styles match.
   
   IS-IS cost styles are classified as follows:
   * narrow: indicates that the device sends and accepts packets with cost style narrow.
   * narrow-compatible: indicates that the device accepts packets with cost style narrow or wide but sends packets only with cost style narrow.
   * compatible: indicates that the device sends and accepts packets with cost style narrow or wide.
   * wide-compatible: indicates that the device accepts packets with cost style narrow or wide but sends packets only with cost style wide.
   * wide: indicates that the device sends and accepts packets with cost style wide.
   
   If the IS-IS cost style of one end is narrow and the IS-IS cost style of the other end is wide or wide-compatible, the two ends cannot communicate with each other.
   
   If the IS-IS cost style of one end is narrow-compatible and the IS-IS cost style of the other end is wide, the two ends cannot communicate with each other.
   
   If the IS-IS cost styles of the two ends do not match, run the [**cost-style**](cmdqueryname=cost-style) command on either end so that the IS-IS cost styles match.
3. Check that the IS-IS route is the optimal route.
   
   Run the [**display isis route**](cmdqueryname=display+isis+route) command to check the IS-IS routing table. If the specified route exists in the IS-IS routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] **verbose** command to check whether another route with the same prefix exists in the IP routing table and its preference is higher than that of IS-IS.![](public_sys-resources/note_3.0-en-us.png) 
   
   If the **State** field of a route is **Active Adv**, the route is active. If routes that have the same prefix but are discovered by different routing protocols exist, the one with the highest preference is active.
   
   
   If another route with the same prefix exists in the IP routing table and its preference is higher than that of IS-IS, modify the configuration based on network planning.