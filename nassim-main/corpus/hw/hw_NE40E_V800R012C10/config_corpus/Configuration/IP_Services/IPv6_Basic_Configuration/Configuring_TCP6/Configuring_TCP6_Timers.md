Configuring TCP6 Timers
=======================

Set two TCP6 timers to control the TCP6 connection time.

#### Context

Two TCP6 timers are available:

* SYN-Wait timer: When SYN packets are sent, the SYN-Wait timer starts. If response packets are not received before the SYN-Wait timer expires, the TCP6 connection is terminated. The SYN-Wait timeout period ranges from 2 to 600, in seconds, and the default value is 75 seconds.
* FIN-Wait timer: When the TCP connection status changes from FIN\_WAIT\_1 to FIN\_WAIT\_2, the FIN-Wait timer starts. If FIN packets are not received before the FIN-Wait timer expires, the TCP6 connection is terminated. The FIN-Wait timeout period ranges from 76 to 3600, in seconds, and the default value is 675 seconds.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp ipv6 timer syn-timeout**](cmdqueryname=tcp+ipv6+timer+syn-timeout) *interval*
   
   
   
   The SYN-Wait timeout period is configured for TCP6 connections.
3. Run [**tcp ipv6 timer fin-timeout**](cmdqueryname=tcp+ipv6+timer+fin-timeout) *interval*
   
   
   
   The FIN\_WAIT\_2 timeout period is configured for TCP6 connections.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.