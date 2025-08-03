Enabling ECMP Load Balancing Consistency
========================================

Enabling ECMP Load Balancing Consistency

#### Context

Equal-Cost Multi-Path routing (ECMP) implements load balancing and link backup. ECMP applies to the network where multiple links to the same destination are available. In the traditional routing technology, packets are forwarded to the destination through one link only; the other links are in backup or inactive state; switching between these links requires a certain period when dynamic routes are used. Different from the traditional routing technology, ECMP can use multiple links to increase transmission bandwidth and transmit data on a faulty link without any delay or packet loss.

When one link of equal-cost multiple paths fails, all traffic needs to be load balanced again based on hash calculation. ECMP load balancing consistency ensures that hash calculation is performed only for traffic on this faulty link, without affecting traffic on other normal links. This function ensures normal operation of services, in which sessions need to be maintained, on normal links.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**load-balance ecmp stateful enable**](cmdqueryname=load-balance+ecmp+stateful+enable) [ **min-number** *min-number-value* **max-number** *max-number-value* **accuracy** *accuracy-value* ]
   
   
   
   The ECMP load balancing consistency function is enabled and the ECMP load balancing consistency parameters are set.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring this function, pay attention to the following points:
   
   * To use this function, ensure that different destination addresses are reachable through the same or completely different equal-cost multiple paths.
   * After enabling this function, do not change the configured load balancing hash algorithm, hash algorithm offset, and load balancing mode. Otherwise, this function may be unable to take effect.
   * This function may be unable to take effect when outbound ports of equal-cost links are intermittently disconnected.
   * The ECMP load balancing consistency function takes effect only for common IPv4 traffic, but not for tunneled IPv4 traffic.
   * The ECMP load balancing consistency function does not take effect for IPv6 traffic.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.