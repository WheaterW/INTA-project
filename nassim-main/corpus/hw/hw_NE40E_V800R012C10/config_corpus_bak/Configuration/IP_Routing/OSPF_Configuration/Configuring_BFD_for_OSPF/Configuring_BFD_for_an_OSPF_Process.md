Configuring BFD for an OSPF Process
===================================

Configuring BFD for an OSPF process helps the system rapidly detect link states and speeds up OSPF convergence in the case of a link state change.

#### Context

After BFD is configured for an OSPF process, when detecting a link failure, BFD rapidly notifies the failure to Routers on both ends of the link, triggering rapid OSPF convergence. When the OSPF neighbor relationship goes Down, the BFD session will be dynamically deleted.

Before configuring BFD for OSPF, enable BFD globally.

To configure BFD on all the interfaces in an OSPF process, perform the following operations on the Routers at both ends of the link where a BFD session is to be set up:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) **enable**
   
   
   
   BFD is enabled for the OSPF process to create BFD sessions.
4. (Optional) Run [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*
   
   
   
   BFD session parameters are modified.
   
   You can skip this step. The default interval at which BFD packets are transmitted and the default detection multiplier are recommended.
   
   The parameters are configured based on the network status and network reliability requirements. A short interval at which BFD packets are transmitted can be configured for a link that has a higher requirement for reliability. A long interval at which BFD packets are transmitted can be configured for a link that has a lower requirement for reliability.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Actual interval at which BFD packets are transmitted on the local Router = Max { configured interval *transmit-interval* at which BFD packets are transmitted on the local Router, configured interval *receive-interval* at which BFD packets are received on the peer Router }
   * Actual interval at which BFD packets are received on the local Router = Max { configured interval *transmit-interval* at which BFD packets are transmitted on the peer Router, configured interval *receive-interval* at which BFD packets are received on the local Router }
   * Actual time for detecting BFD packets = Actual interval at which BFD packets are received on the local Router x Configured detection multiplier *multiplier-value* on the peer Router
   
   For example:
   
   * On the local Router, the configured interval at which BFD packets are transmitted is 200 ms; the configured interval at which BFD packets are received is 300 ms; the detection multiplier is 4.
   * On the peer Router, the configured interval at which BFD packets are transmitted is 100 ms; the interval at which BFD packets are received is 600 ms; the detection multiplier is 5.
   
   Then:
   
   * On the local Router, the actual interval at which BFD packets are transmitted is 600 ms calculated by using the formula max {200 ms, 600 ms}; the interval at which BFD packets are received is 300 ms calculated by using the formula max {100 ms, 300 ms}; the detection period is 1500 ms calculated by multiplying 300 ms by 5.
   * On the peer Router, the actual interval at which BFD packets are transmitted is 300 ms calculated by using the formula max {100 ms, 300 ms}, the actual interval at which BFD packets are received is 600 ms calculated by using the formula max {200 ms, 600 ms}, and the detection period is 2400 ms calculated by multiplying 600 ms by 4.
5. (Optional) Prevent an interface from dynamically creating a BFD session.
   
   
   
   After BFD for OSPF is configured, all interfaces on which neighbor relationships are Full in the OSPF process will create BFD sessions. To prevent specific interfaces from being enabled with BFD, disable these interfaces from dynamically creating BFD sessions.
   
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**ospf bfd block**](cmdqueryname=ospf+bfd+block)
      
      
      
      An interface is prevented from dynamically creating a BFD session.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
      
      
      
      The OSPF view is displayed.
6. (Optional) Run [**bfd all-interfaces incr-cost**](cmdqueryname=bfd+all-interfaces+incr-cost) { *cost* | **max-reachable** } [ **wtr** *wtrIntvl* ] The OSPF process is configured to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The delay configured for an interface to restore the cost based on the BFD session status takes precedence over that configured for a process to restore the cost based on the BFD session status.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.