Configuring Micro-Isolation CAR for OSPFv3
==========================================

By default, micro-isolation CAR is enabled for OSPFv3, implementing micro-isolation protection for OSPFv3 packets based on interfaces and destination IP addresses to protect session establishment.

#### Context

By default, micro-isolation CAR is enabled for OSPFv3, implementing micro-isolation protection for OSPFv3 packets based on interfaces and destination IP addresses to protect session establishment. When OSPFv3 packets encounter a traffic burst, a large number of OSPFv3 packets may preempt interface bandwidth resources. In the case of an attack, a large number of invalid packets sent to other IP addresses may preempt the bandwidth. Therefore, you are advised not to disable this function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car ospfv3**](cmdqueryname=micro-isolation+protocol-car+ospfv3) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Micro-isolation CAR parameters are configured for OSPFv3.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. (Optional) Run [**micro-isolation protocol-car ospfv3 disable**](cmdqueryname=micro-isolation+protocol-car+ospfv3+disable)
   
   
   
   Micro-isolation CAR is disabled for OSPFv3.
   
   
   
   By default, micro-isolation CAR for OSPFv3 is enabled. To disable this function, run the [**micro-isolation protocol-car ospfv3 disable**](cmdqueryname=micro-isolation+protocol-car+ospfv3+disable) command. If this function is disabled, micro-isolation protection is no longer implemented for OSPFv3 packets based on interfaces and destination IP addresses. In normal cases, you are advised to keep micro-isolation CAR enabled for OSPFv3.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.