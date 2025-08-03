Configuring Micro-isolation CAR for PCEP
========================================

Configuring Micro-isolation CAR for PCEP

#### Context

Micro-isolation CAR is enabled by default for PCEP to implement micro-isolation protection for PCEP connection establishment packets. If a device is attacked, the messages of one PCEP session may preempt the bandwidth of other PCEP sessions. Therefore, you are advised to keep this function enabled.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car pcep-ipv4**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Micro-isolation CAR parameters are configured for PCEP.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Exception Handling

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**micro-isolation protocol-car pcep-ipv4 disable**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4+disable) command to disable micro-isolation CAR for PCEP.
   
   
   
   By default, micro-isolation CAR is enabled for PCEP. To disable this function for PCEP, run the [**micro-isolation protocol-car pcep-ipv4 disable**](cmdqueryname=micro-isolation+protocol-car+pcep-ipv4+disable) command. In normal cases, you are advised to keep micro-isolation CAR enabled for PCEP.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.