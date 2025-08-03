Configuring Alarm Thresholds for Board Performance
==================================================

This section describes how to configure alarm thresholds for the forwarding performance resource usage, packet reassembly resource usage, traffic bandwidth usage, and value-added service bandwidth usage of a board.

#### Context

Configuring alarm thresholds for the forwarding performance resource usage, packet reassembly resource usage, traffic bandwidth usage, and value-added service bandwidth usage helps you learn the board performance in time. If a performance threshold-crossing alarm is generated, take immediate measures to prevent it from affecting services.

In VS mode, this configuration process is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**forward-alarm slot**](cmdqueryname=forward-alarm+slot) *slot-id* [**performance usage-rate alarm on**](cmdqueryname=performance+usage-rate+alarm+on) *onrate* [**off**](cmdqueryname=off) *offrate*
   
   
   
   An alarm threshold is configured for the forwarding performance resource usage.
3. Run [**forward-alarm slot**](cmdqueryname=forward-alarm+slot) *slot-id* [**packet reassembly resources usage-rate alarm on**](cmdqueryname=packet+reassembly+resources+usage-rate+alarm+on) *onrate* [**off**](cmdqueryname=off) *offrate*
   
   
   
   An alarm threshold is configured for the packet reassembly resource usage.
4. Run [**forward-alarm slot**](cmdqueryname=forward-alarm+slot) *slot-id* [**board flow output bandwidth usage-rate alarm on**](cmdqueryname=board+flow+output+bandwidth+usage-rate+alarm+on) *onrate* [**off**](cmdqueryname=off) *offrate*
   
   
   
   An alarm threshold is configured for the traffic bandwidth usage on a board.
5. Run [**forward-alarm slot**](cmdqueryname=forward-alarm+slot) *slot-id* [**service channel bandwidth usage-rate alarm on**](cmdqueryname=service+channel+bandwidth+usage-rate+alarm+on) *onrate* [**off**](cmdqueryname=off) *offrate*
   
   
   
   An alarm threshold is configured for the value-added service bandwidth usage on a board.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.