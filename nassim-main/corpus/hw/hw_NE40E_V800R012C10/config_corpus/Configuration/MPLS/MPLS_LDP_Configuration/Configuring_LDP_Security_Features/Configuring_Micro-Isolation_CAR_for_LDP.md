Configuring Micro-Isolation CAR for LDP
=======================================

Configuring Micro-Isolation CAR for LDP

#### Context

The micro-isolation CAR function is enabled for LDP by default to isolate CPCAR channels between LDP peers and implement micro-isolation protection for LDP connection establishment packets. When traffic bursts occur in the LDP service, the packets of LDP peers may preempt the bandwidth. To prevent this issue, you are advised to keep this function enabled.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car**](cmdqueryname=micro-isolation+protocol-car+ldp-tcp+ldp-udp-local+cir+cbs+pir) { **ldp-tcp** | **ldp-udp-local** } { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of micro-isolation CAR for LDP are configured.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. (Optional) Run [**micro-isolation protocol-car ldp disable**](cmdqueryname=micro-isolation+protocol-car+ldp+disable)
   
   
   
   Micro-isolation CAR is disabled for LDP.
   
   
   
   In normal cases, you are advised to keep micro-isolation CAR enabled for LDP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.