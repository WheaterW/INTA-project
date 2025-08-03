Configuring Micro-Isolation CAR for MLD
=======================================

Configuring Micro-Isolation CAR for MLD

#### Context

By default, micro-isolation CAR is enabled for MLD. Micro-isolation can be performed on MLD messages based on interfaces or sub-interfaces to protect session establishment. When MLD messages suffer a traffic burst, bandwidth may be preempted among interfaces or sub-interfaces. As a result, the bandwidth of the MLD messages on the interfaces or sub-interfaces cannot be guaranteed. Therefore, you are advised not to disable this function in most cases.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run **[**micro-isolation protocol-car mld**](cmdqueryname=micro-isolation+protocol-car+mld)** { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value*} \*
   
   
   
   Parameters of micro-isolation CAR for MLD are configured.
   
   
   
   In normal cases, you are advised to use the default values. The value of **PIR** must be greater than or equal to that of **CIR**, and the value of **PBS** must be greater than or equal to that of **CBS**.
3. (Optional) Run [**micro-isolation protocol-car mld disable**](cmdqueryname=micro-isolation+protocol-car+mld+disable)
   
   
   
   Micro-isolation CAR is disabled for MLD.
   
   
   
   After the [**micro-isolation protocol-car mld disable**](cmdqueryname=micro-isolation+protocol-car+mld+disable) command is run, interface-based or sub-interface-based micro-isolation is no longer implemented for MLD messages. In normal cases, you are advised to keep micro-isolation CAR enabled for MLD.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.