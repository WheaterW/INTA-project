Configuring Micro-isolation Interface-based CAR
===============================================

You can configure micro-isolation interface-based CAR to provide micro-isolation protection for protocol packets based on interfaces.

#### Context

By default, micro-isolation interface-based CAR is enabled. If a traffic burst occurs, a large number of packets may preempt interface bandwidth. In this case, micro-isolation interface-based CAR can be implemented to provide micro-isolation protection for protocol packets based on interfaces.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **slot** *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**micro-isolation port-car disable**](cmdqueryname=micro-isolation+port-car+disable)
   
   
   
   Micro-isolation interface-based CAR is disabled.
   
   
   
   Disable this function if it encounters an exception or adversely affects other services. Typically, you are advised to enable this function.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.