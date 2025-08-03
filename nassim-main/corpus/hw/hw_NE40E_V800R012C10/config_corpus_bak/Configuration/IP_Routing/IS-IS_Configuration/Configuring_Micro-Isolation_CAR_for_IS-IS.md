Configuring Micro-Isolation CAR for IS-IS
=========================================

Configuring_Micro-Isolation_CAR_for_IS-IS

#### Context

By default, micro-isolation CAR is enabled for IS-IS, implementing micro-isolation protection for IS-IS packets based on interfaces and destination MAC addresses to protect session establishment. When IS-IS packets encounter a traffic burst, a large number of IS-IS packets may preempt interface bandwidth resources. In the case of an attack, a large number of invalid packets sent to other MAC addresses may preempt the bandwidth. Therefore, you are advised not to disable this function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car isis**](cmdqueryname=micro-isolation+protocol-car+isis) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Micro-isolation CAR parameters are configured for IS-IS.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. (Optional) Run [**micro-isolation protocol-car isis disable**](cmdqueryname=micro-isolation+protocol-car+isis+disable)
   
   
   
   Micro-isolation CAR is disabled for IS-IS.
   
   
   
   By default, micro-isolation CAR is enabled for IS-IS. To disable this function, run the [**micro-isolation protocol-car isis disable**](cmdqueryname=micro-isolation+protocol-car+isis+disable) command. If this function is disabled, micro-isolation protection is no longer implemented for IS-IS packets based on interfaces and destination MAC addresses. In normal cases, you are advised to keep micro-isolation CAR enabled for IS-IS.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.