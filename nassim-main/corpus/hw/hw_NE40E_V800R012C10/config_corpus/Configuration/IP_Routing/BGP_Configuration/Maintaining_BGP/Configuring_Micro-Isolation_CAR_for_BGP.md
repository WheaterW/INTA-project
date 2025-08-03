Configuring Micro-Isolation CAR for BGP
=======================================

You can configure micro-isolation CAR for BGP to isolate bandwidth resources by interface or sub-interface for BGP messages used to establish peer relationships.

#### Context

When BGP messages suffer a traffic burst, bandwidth may be preempted among interfaces and sub-interfaces. As a result, the BGP messages may fail to be sent properly. To resolve this problem, you can configure micro-isolation CAR for BGP to isolate bandwidth resources by interface or sub-interface for the BGP messages. If the default parameters of micro-isolation CAR for BGP do not meet service requirements, you can adjust them as required to ensure that the BGP messages can be sent properly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car bgp**](cmdqueryname=micro-isolation+protocol-car+bgp+cir+cbs+pir+pbs) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of micro-isolation CAR for BGP are configured.
   
   
   
   In normal cases, you are advised to use the default values of these parameters.
3. (Optional) Run [**micro-isolation protocol-car bgp disable**](cmdqueryname=micro-isolation+protocol-car+bgp+disable)
   
   
   
   Micro-isolation CAR for BGP is disabled.
   
   
   
   In normal cases, you are advised to keep this function enabled. Disable it if it becomes abnormal or adversely affects other services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.