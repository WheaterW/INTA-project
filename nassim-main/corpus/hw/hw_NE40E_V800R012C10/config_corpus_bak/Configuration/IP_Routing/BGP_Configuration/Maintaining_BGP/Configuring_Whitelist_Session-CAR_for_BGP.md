Configuring Whitelist Session-CAR for BGP
=========================================

You can configure whitelist session-CAR for BGP to isolate bandwidth resources by session for BGP messages. This configuration prevents bandwidth preemption among BGP sessions in the case of a traffic burst.

#### Context

The function of whitelist session-CAR for BGP sets an independent CAR channel for each BGP session to ensure that the bandwidth of each BGP session is not preempted by other traffic (including traffic from other sessions of the same protocol and traffic from other protocols). When BGP messages suffer a traffic burst, you can configure this task to adjust the message channel bandwidth of each BGP session in the BGP whitelist session CAR to ensure that BGP messages are sent to the CPU normally.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In normal cases, you are advised to enable whitelist session-CAR for BGP. If this function becomes abnormal or adversely affects other services, you can run the [**whitelist session-car bgp disable**](cmdqueryname=whitelist+session-car+bgp+disable) command to disable this function.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car bgp**](cmdqueryname=whitelist+session-car+bgp+cir+cbs+pir+pbs) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for BGP are configured.
   
   
   
   In normal cases, you are advised to use the default values of these parameters.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+bgp+statistics+slot+bgp) **bgp** **statistics** **slot** *slot-id* command to check statistics about BGP whitelist session CAR on a specified interface board.
  
  To check the statistics within a specific period of time, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car+bgp+statistics+slot) **bgp** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for BGP on the specified interface board; after a certain period of time, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+bgp+statistics+slot) **bgp** **statistics** **slot** *slot-id* command.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The statistics about whitelist session-CAR for BGP on a specified interface board cannot be restored after being cleared. Therefore, exercise caution before clearing them.