Setting the Interval at Which LSAs Are Updated
==============================================

You can set the interval at which LSAs are updated based on network connections and router resources.

#### Context

OSPF sets the interval for updating LSAs to 5s. This prevents network connections or route flapping from consuming excessive network bandwidth or device resources. On a stable network that requires fast route convergence, you can set the interval for updating LSAs to 0 seconds. In this manner, when the topology or a route changes, the change can be immediately advertised to the network through LSAs. This speeds up route convergence on the network. On an unstable network, routes are calculated frequently, consuming excessive CPU resources. In addition, LSAs that describe the unstable topology are frequently generated and transmitted on the unstable network. Due to the frequent processing of such LSAs, the entire network cannot become stable quickly. You can configure an intelligent timer so that the device can dynamically adjust the interval based on the user configuration and frequency of triggering events (such as route calculation) to quickly stabilize the network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) { 0 | **intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **other-type** *interval* ] | **other-type** *interval* [ **intelligent-timer** *max-interval* *start-interval* *hold-interval* ] }
   
   
   
   The interval at which LSAs are updated is configured.
   
   
   
   * **intelligent-timer**: uses the intelligent timer to set the update interval for OSPF Type 1 LSAs (router LSAs) and Type 2 LSAs (network LSAs).
   * *max-interval*: specifies the maximum interval at which OSPF LSAs are updated, in milliseconds.
   * *start-interval*: specifies the initial interval at which OSPF LSAs are updated, in milliseconds.
   * *hold-interval*: specifies the hold interval at which OSPF LSAs are updated, in milliseconds.
   * **other-type**: sets the update interval for OSPF Type 3 LSAs (network-summary-LSAs), Type 4 LSAs (ASBR-summary-LSAs), and Type 10 LSAs (opaque LSAs).
4. (Optional) Run [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) *interval* [ **threshold** *threshold* ]
   
   
   
   The suppression period that takes effect when sent OSPF LSAs flap is configured.
   
   
   
   If no flapping occurs in sent OSPF LSAs, you can run the [**lsa-originate-interval**](cmdqueryname=lsa-originate-interval) command to prevent frequent LSA sending by setting a proper interval at which LSAs are sent. If sent OSPF LSAs flap, you can run the [**lsa-originate-interval suppress-flapping**](cmdqueryname=lsa-originate-interval+suppress-flapping) command to set a flapping suppression period. This minimizes the impact of frequent LSA flapping on services. If both of them are configured, the device uses the larger value as the flapping suppression time.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.