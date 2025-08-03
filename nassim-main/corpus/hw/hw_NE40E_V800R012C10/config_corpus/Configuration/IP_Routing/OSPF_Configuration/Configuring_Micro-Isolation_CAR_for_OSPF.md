Configuring Micro-Isolation CAR for OSPF
========================================

By default, micro-isolation CAR is enabled for OSPF, implementing micro-isolation protection for OSPF packets based on interfaces and destination IP addresses to protect session establishment.

#### Context

By default, micro-isolation CAR is enabled for OSPF, implementing micro-isolation protection for OSPF packets based on interfaces and destination IP addresses to protect session establishment. When OSPF packets encounter a traffic burst, a large number of OSPF packets may preempt interface bandwidth resources. In the case of an attack, a large number of invalid packets sent to other IP addresses may preempt the bandwidth. Therefore, you are advised not to disable this function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car ospf**](cmdqueryname=micro-isolation+protocol-car+ospf) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Micro-isolation CAR parameters are configured for OSPF.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. (Optional) Run [**micro-isolation protocol-car ospf disable**](cmdqueryname=micro-isolation+protocol-car+ospf+disable)
   
   
   
   Micro-isolation CAR is disabled for OSPF.
   
   
   
   By default, micro-isolation CAR for OSPF is enabled. To disable this function, run the [**micro-isolation protocol-car ospf disable**](cmdqueryname=micro-isolation+protocol-car+ospf+disable) command. If this function is disabled, micro-isolation protection is no longer implemented for OSPF packets based on interfaces and destination IP addresses. In normal cases, you are advised to keep micro-isolation CAR enabled for OSPF.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.