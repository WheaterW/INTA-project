Configuring BFD for OSPFv3
==========================

After enabling BFD for OSPFv3, you need to configure BFD parameters in the OSPFv3 process.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **enable**
   
   
   
   BFD is enabled for the OSPFv3 process to create BFD sessions.
4. (Optional) Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) { **min-transmit-interval** *Tx-Value* | **min-receive-interval** *Rx-Value* | **detect-multiplier** *Mul-Value* } \*
   
   
   
   BFD parameters are configured for the OSPFv3 process.
   
   
   
   The default interval at which BFD packets are transmitted and the default detection multiplier are recommended. As such, this step can be skipped.
   
   The parameters need to be configured based on network conditions and requirements on network reliability. A short transmission interval for BFD packets can be set for a link that requires higher reliability, and a long transmission interval can be used for a link that has low reliability requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local device = Max { *Tx-Value* (interval at which BFD packets are transmitted) set on the local device, *Rx-Value* (interval at which BFD packets are received) set on the peer device }
   * Actual interval at which BFD packets are received on the local device = Max { *Tx-Value* (interval at which BFD packets are transmitted) set on the peer device, *Rx-Value* (interval at which BFD packets are received) set on the local device }
   * Actual period for BFD detection on the local device = Actual interval at which BFD packets are received on the local device x Detection multiplier specified by *Mul-Value* on the peer device
   
   For example:
   
   * On the local device, the interval at which packets are transmitted is set to 200 ms, the interval at which packets are received is set to 300 ms, and the detection multiplier is set to 4.
   * On the peer device, the interval at which packets are transmitted is set to 100 ms, the interval at which packets are received is set to 600 ms, and the detection multiplier is set to 5.
   
   Then:
   
   * On the local device, the actual interval at which BFD packets are transmitted is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual interval at which BFD packets are received is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual detection period is 1500 ms (calculated by 300 ms x 5).
   * On the peer device, the actual interval at which BFD packets are transmitted is 300 ms (calculated by Max { 100 ms, 300 ms }); the actual interval at which BFD packets are received is 600 ms (calculated by Max { 200 ms, 600 ms }); the actual detection period is 2400 ms (calculated by 600 ms x 4).
5. (Optional) Disable a specified interface from creating a BFD session.
   
   
   
   After BFD is configured for an OSPFv3 process, all interfaces on which neighbor relationships are in Full state in the OSPFv3 process create BFD sessions. If BFD is not required on specific interfaces, disable these interfaces from creating BFD sessions.
   
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ospfv3 bfd block**](cmdqueryname=ospfv3+bfd+block)
      
      
      
      The interface is disabled from creating a BFD session.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
      
      
      
      The OSPFv3 view is displayed.
6. (Optional) Run [**bfd all-interfaces incr-cost**](cmdqueryname=bfd+all-interfaces+incr-cost) { *cost* | **max-reachable**} [ **wtr** *wtrIntvl* ] The OSPFv3 process is configured to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The delay configured for an interface to restore the cost based on the BFD session status takes precedence over that configured for a process to restore the cost based on the BFD session status.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.