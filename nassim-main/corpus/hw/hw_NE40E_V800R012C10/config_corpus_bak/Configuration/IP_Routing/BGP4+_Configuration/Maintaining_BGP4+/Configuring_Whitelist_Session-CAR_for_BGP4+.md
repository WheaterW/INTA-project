Configuring Whitelist Session-CAR for BGP4+
===========================================

You can configure whitelist session-CAR for BGP4+ to isolate bandwidth resources by session for BGP4+ messages. This configuration prevents bandwidth preemption among BGP4+ sessions in the case of a traffic burst.

#### Context

The function of whitelist session-CAR for BGP4+ sets an independent CAR channel for each BGP4+ session to ensure that the bandwidth of each BGP4+ session is not preempted by other traffic (including traffic from other sessions of the same protocol and traffic from other protocols). When BGP4+ messages suffer a traffic burst, you can configure this task to adjust the message channel bandwidth of each BGP4+ session in the BGP4+ whitelist session CAR to ensure that BGP4+ messages are sent to the CPU normally.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the function becomes abnormal or affects other services, you can run the [**whitelist session-car bgp disable**](cmdqueryname=whitelist+session-car+bgp+disable) command to disable whitelist session-CAR for BGP4+. In normal cases, you are advised to keep whitelist session-CAR for BGP4+ enabled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car bgp**](cmdqueryname=whitelist+session-car+bgp+cir+cbs+pir+pbs) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for BGP4+ are configured.
   
   
   
   In normal cases, you are advised to use the default values of these parameters.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following command to check the previous configuration:

* Run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car+bgpv6+statistics) **bgpv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for BGP4+ on a specified interface board.
  
  To check the statistics within a specific period of time, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car+bgpv6+statistics+slot) **bgpv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for BGP4+ on the specified interface board; after a certain period of time, run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car+bgpv6+statistics) **bgpv6** **statistics** **slot** *slot-id* command.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The statistics about whitelist session-CAR for BGP4+ on a specified interface board cannot be restored after being cleared. Therefore, exercise caution when clearing the statistics.