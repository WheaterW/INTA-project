(Optional) Configuring BFD for a Specified Interface
====================================================

Configuring BFD for OSPF on a specified interface helps speed up OSPF convergence in the case of an interface failure.

#### Context

After BFD for OSPF is configured on a specified interface and the interface becomes faulty, the Router rapidly detects the fault and instructs OSPF to recalculate routes. This speeds up OSPF convergence. When the OSPF neighbor relationship goes Down, the BFD session between OSPF neighbors is dynamically deleted.

Before configuring BFD for OSPF, enable BFD globally.

Perform the following steps on the Router where a BFD session is to be established on a specified interface:![](../../../../public_sys-resources/note_3.0-en-us.png) 

The interface can be a physical interface or a GRE tunnel interface. If BFD is enabled on a GRE tunnel interface, millisecond-level fault detection can be implemented for the GRE tunnel.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is globally configured.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
5. Run [**ospf bfd**](cmdqueryname=ospf+bfd) **enable**
   
   
   
   BFD for OSPF is configured, and the default parameter values are used to establish a BFD session.
   
   
   
   If BFD is enabled globally and the neighbor relationships on the interface are in the Full state, OSPF creates a BFD session with default parameter values for the interface.
   
   The [**ospf bfd**](cmdqueryname=ospf+bfd) **enable** command can be run only in the VLANIF interface view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of BFD for OSPF on an interface takes precedence over that in the OSPF process.
6. (Optional) Run [**ospf bfd**](cmdqueryname=ospf+bfd) { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*
   
   
   
   BFD session parameters are modified.
   
   
   
   The default interval at which BFD packets are transmitted and the default detection multiplier are recommended. As such, this step can be skipped.
   
   The parameters need to be configured based on network conditions and requirements on network reliability. A short transmission interval for BFD packets can be set for a link that requires higher reliability, and a long transmission interval can be configured for a link that requires lower reliability.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local device = Max { *transmit-interval* (interval at which BFD packets are transmitted) set on the local device, *receive-interval* (interval at which BFD packets are received) set on the peer device }
   * Actual interval at which BFD packets are received on the local device = Max { *transmit-interval* (interval at which BFD packets are transmitted) set on the peer device, *receive-interval* (interval at which BFD packets are received) set on the local device }
   * Actual period for BFD detection on the local device = Actual interval at which BFD packets are received on the local device x Detection multiplier specified by *multiplier-value* on the peer device
   
   For example:
   
   * On the local device, the interval at which BFD packets are transmitted is set to 200 ms, the interval at which BFD packets are received is set to 300 ms, and the detection multiplier is set to 4.
   * On the peer device, the interval at which BFD packets are transmitted is set to 100 ms, the interval at which BFD packets are received is set to 600 ms, and the detection multiplier is set to 5.
   
   Then:
   
   * On the local device, the actual interval at which BFD packets are transmitted is 600 ms (calculated through Max { 200 ms, 600 ms }); the actual interval at which BFD packets are received is 300 ms (calculated through Max { 100 ms, 300 ms }); the actual detection period is 1500 ms (calculated through 300 ms x 5).
   * On the peer device, the actual interval at which BFD packets are transmitted is 300 ms (calculated through Max { 100 ms, 300 ms }); the actual interval at which BFD packets are received is 600 ms (calculated through Max { 200 ms, 600 ms }); the actual detection period is 2400 ms (calculated through 600 ms x 4).
7. (Optional) Run [**ospf bfd incr-cost**](cmdqueryname=ospf+bfd+incr-cost) { *cost* | **max-reachable** } [ **wtr** *wtrIntvl* ]
   
   
   
   The OSPF interface is configured to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The delay configured for an interface to restore the cost based on the BFD session status takes precedence over that configured for a process to restore the cost based on the BFD session status.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.