Configuring High-Priority Scheduling on an Interface
====================================================

High-priority scheduling can be configured for low-priority
traffic on an interface.

#### Context

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
   
   High-priority scheduling
   is supported only on POS and GE interfaces.
3. Run [**qos convergent-precedence high**](cmdqueryname=qos+convergent-precedence+high)
   
   
   
   High-priority
   scheduling is configured for traffic on the interface.
   
   By default,
   low-priority scheduling applies to traffic on an interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.