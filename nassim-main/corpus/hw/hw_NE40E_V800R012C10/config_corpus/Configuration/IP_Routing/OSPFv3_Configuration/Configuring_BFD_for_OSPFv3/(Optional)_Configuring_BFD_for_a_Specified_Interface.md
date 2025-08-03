(Optional) Configuring BFD for a Specified Interface
====================================================

To configure BFD only on a specified interface, or enable an interface to detect link failures faster after BFD for OSPFv3 is enabled globally, configure BFD on the specified interface.

#### Context

To configure BFD only on a specified interface, or enable an interface to detect link failures faster after BFD for OSPFv3 is enabled globally, perform the following steps on the interface:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 bfd**](cmdqueryname=ospfv3+bfd) **enable** [ **instance** *instance-id* ]
   
   
   
   BFD is enabled on the interface to create BFD sessions.
   
   
   
   When BFD is configured globally and the neighbor state is Full, BFD sessions are established using default BFD parameters.
   
   To set parameters for BFD sessions as required, run the [**ospfv3 bfd**](cmdqueryname=ospfv3+bfd) { **min-transmit-interval** *min-transmit-value* | **min-receive-interval** *min-receive-value* | **detect-multiplier** *detect-multiplier-value* | **frr-binding** } \* [ **instance** *instance-id* ] command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The configuration of BFD on an interface takes precedence over that in a process. That is, if BFD session parameters are configured for both a process and an interface, the parameters on the interface will be used to establish BFD sessions on the interface.
   * If the parameters of BFD sessions are set but the [**ospfv3 bfd**](cmdqueryname=ospfv3+bfd) **enable** command is not run, BFD is not enabled on the interface.
   
   The default interval at which BFD packets are transmitted and the default detection multiplier are recommended. As such, this step can be skipped.
   
   The parameters need to be configured based on network conditions and requirements on network reliability. A short transmission interval for BFD packets can be set for a link that requires higher reliability, and a long transmission interval can be used for a link that has low reliability requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local device = Max { *min-transmit-value* (interval at which BFD packets are transmitted) set on the local device, *min-receive-value* (interval at which BFD packets are received) set on the peer device }
   * Actual interval at which BFD packets are received on the local device = Max { *min-transmit-value* (interval at which BFD packets are transmitted) set on the peer device, *min-receive-value* (interval at which BFD packets are received) set on the local device }
   * Actual period for BFD detection on the local device = Actual interval at which BFD packets are received on the local device x Detection multiplier specified by *detect-multiplier-value* on the peer device
   
   For example:
   
   * On the local device, the interval at which BFD packets are transmitted is set to 200 ms, the interval at which BFD packets are received is set to 300 ms, and the detection multiplier is set to 4.
   * On the peer device, the interval at which BFD packets are transmitted is set to 100 ms, the interval at which BFD packets are received is set to 600 ms, and the detection multiplier is set to 5.
   
   Then:
   
   * On the local device, the actual interval at which BFD packets are transmitted is 600 ms (calculated through Max { 200 ms, 600 ms }); the actual interval at which BFD packets are received is 300 ms (calculated through Max { 100 ms, 300 ms }); the actual detection period is 1500 ms (calculated through 300 ms x 5).
   * On the peer device, the actual interval at which BFD packets are transmitted is 300 ms (calculated through Max { 100 ms, 300 ms }); the actual interval at which BFD packets are received is 600 ms (calculated through Max { 200 ms, 600 ms }); the actual detection period is 2400 ms (calculated through 600 ms x 4).
4. (Optional) Run [**ospfv3 bfd incr-cost**](cmdqueryname=ospfv3+bfd+incr-cost) { *cost* | **max-reachable** } [ **wtr** *wtrIntvl* ]
   
   
   
   The OSPFv3 interface is configured to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The delay configured for an interface to restore the cost based on the BFD session status takes precedence over that configured for a process to restore the cost based on the BFD session status.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.