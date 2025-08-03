Configuring Fast Refreshing of Routes with Single Next Hops
===========================================================

Fast refreshing routes with single next hops speeds up route convergence and reduces packet loss.

#### Usage Scenario

If routes have only single next hops, a link switchover takes a long time due to slow route convergence. To solve this problem, configure fast refreshing of routes with single next hops to speed up route convergence and reduce packet loss.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.


![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Fast route refreshing causes a device's forwarding performance to deteriorate by about 15%. Determine whether to enable this function based on your network conditions.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**single-nexthop bgp fast-refresh enable**](cmdqueryname=single-nexthop+bgp+fast-refresh+enable)
   
   
   
   Fast refreshing of routes with single next hops is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.