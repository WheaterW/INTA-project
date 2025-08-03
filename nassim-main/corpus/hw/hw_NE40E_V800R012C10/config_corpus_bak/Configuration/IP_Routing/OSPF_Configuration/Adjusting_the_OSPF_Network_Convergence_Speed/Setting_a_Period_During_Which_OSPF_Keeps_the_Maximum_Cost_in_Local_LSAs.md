Setting a Period During Which OSPF Keeps the Maximum Cost in Local LSAs
=======================================================================

If a period during which OSPF keeps the maximum cost in local LSAs is configured and an OSPF interface changes from Down to Up, traffic is switched back only when the period elapses.

#### Context

When an OSPF interface changes from down to up, the OSPF neighbor relationship is re-established. After IGP route convergence is completed, traffic is switched back. In most cases, IGP routes converge quickly. However, many services that depend on IGP routes may require a delayed switchback. In this case, you can run the [**ospf peer hold-max-cost**](cmdqueryname=ospf+peer+hold-max-cost) command to specify a period during which OSPF keeps the maximum cost in local LSAs. After the OSPF neighbor relationship reaches the Full state, the traffic forwarding path remains unchanged during the specified period. After this period expires, the normal cost is restored, and traffic is switched back normally.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPF interface view is displayed.
3. Run [**ospf peer hold-max-cost**](cmdqueryname=ospf+peer+hold-max-cost) **timer** *timer*
   
   
   
   A period during which OSPF keeps the maximum cost in local LSAs is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.