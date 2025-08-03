Configuring Micro-Isolation CAR for IGMP
========================================

Configuring_Micro-Isolation_CAR_for_IGMP

#### Context

By default, micro-isolation CAR is enabled for IGMP. Micro-isolation can be performed on IGMP messages based on interfaces or sub-interfaces to protect session establishment. When IGMP messages suffer a traffic burst, bandwidth may be preempted among interfaces or sub-interfaces. As a result, the bandwidth of the IGMP messages on the interfaces or sub-interfaces cannot be guaranteed. Therefore, you are advised not to disable this function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**micro-isolation protocol-car igmp**](cmdqueryname=micro-isolation+protocol-car+igmp)** { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value*} \*
   
   
   
   Parameters of micro-isolation CAR for IGMP are configured.
   
   
   
   In normal cases, you are advised to use the default values. The value of **PIR** must be greater than or equal to that of **CIR**, and the value of **PBS** must be greater than or equal to that of **CBS**.
3. (Optional) Run [**micro-isolation protocol-car igmp disable**](cmdqueryname=micro-isolation+protocol-car+igmp+disable)
   
   
   
   Micro-isolation CAR is disabled for IGMP.
   
   
   
   After the [**micro-isolation protocol-car igmp disable**](cmdqueryname=micro-isolation+protocol-car+igmp+disable) command is run, interface-based or sub-interface-based micro-isolation is no longer implemented for IGMP messages. In normal cases, you are advised to keep micro-isolation CAR enabled for IGMP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.