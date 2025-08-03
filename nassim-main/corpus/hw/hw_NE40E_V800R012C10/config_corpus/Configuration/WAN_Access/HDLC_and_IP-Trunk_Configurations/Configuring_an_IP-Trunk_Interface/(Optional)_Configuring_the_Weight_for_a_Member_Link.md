(Optional) Configuring the Weight for a Member Link
===================================================

An IP-Trunk interface performs load balancing on member
links based on link weights. On an IP-Trunk interface, the greater
the weight of a member link, the heavier the load over the member
link. Therefore, to enable a member link to transmit more traffic,
increase the weight for the link.

#### Procedure

1. On the Router that uses the IP-Trunk interface, run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The view of a member interface of an IP-Trunk interface is
   displayed.
3. Run [**distribute-weight**](cmdqueryname=distribute-weight) *weight-value*
   
   
   
   The weight of the member link is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.