Configuring TCP Timers
======================

You can control the TCP connection time by setting the SYN-Wait timer and FIN-Wait timer.

#### Context

Two TCP timers are available:

* SYN-Wait timer: TCP starts the SYN-Wait timer when sending SYN packets. If no replies in response to SYN packets are received before the SYN-Wait timer expires, the TCP connection is terminated. The SYN-Wait timer ranges from 2 to 600 seconds, and the default value is 75 seconds.
* FIN-Wait timer: When the TCP connection status turns from FIN\_WAIT\_1 to FIN\_WAIT\_2, the FIN-Wait timer starts. If no FIN packets are received before the FIN-Wait timer expires, the TCP connection is terminated. The FIN-Wait timer ranges from 76 to 3600 seconds, and the default value is 675 seconds.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tcp timer syn-timeout**](cmdqueryname=tcp+timer+syn-timeout) *interval*
   
   
   
   The SYN-Wait timer for setting up TCP connections is configured.
3. Run [**tcp timer fin-timeout**](cmdqueryname=tcp+timer+fin-timeout) *interval*
   
   
   
   The FIN\_WAIT\_2 timer for setting up TCP connections is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.