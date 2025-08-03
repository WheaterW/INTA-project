Configuring BFD for an IS-IS Process
====================================

By configuring BFD for an IS-IS process, you can set parameters for dynamic BFD sessions and enable dynamic BFD for IS-IS on all IS-IS interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) *process-id*
   
   
   
   The IS-IS view is displayed.
3. (Optional) Run [**bfd session-up check**](cmdqueryname=bfd+session-up+check)
   
   
   
   BFD session check is configured for the IS-IS process.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the Layer 2 network is running normally, IS-IS neighbor relationships can be established and routes can be delivered. However, if the Layer 3 network is unreachable, upper-layer traffic loss occurs. To resolve this problem, configure BFD session check for an IS-IS process using the [**bfd session-up check**](cmdqueryname=bfd+session-up+check) command. This ensures that an IS-IS neighbor relationship is established only when the BFD session is up on corresponding interfaces. After this function is configured, it applies only to the neighbor relationships to be established, not to existing neighbor relationships.
4. Run [**bfd all-interfaces enable**](cmdqueryname=bfd+all-interfaces+enable)
   
   
   
   BFD is enabled for the IS-IS process to establish BFD sessions.
   
   
   
   BFD must be enabled globally before you perform this step. If BFD is enabled globally, this step is performed, and the status of neighbors is up (or the DIS is up in the case of a broadcast network), default BFD parameters are used by all interfaces in the IS-IS process to establish BFD sessions.
5. (Optional) If you need to set BFD parameters for establishing a BFD session, run the [**bfd all-interfaces**](cmdqueryname=bfd+all-interfaces) { **min-rx-interval** *receive-interval* | **min-tx-interval** *transmit-interval* | **detect-multiplier** *multiplier-value* | **frr-binding** | **tos-exp** *tosexp-value* } \* command.
   
   BFD detection intervals are calculated as follows:
   * Effective interval at which BFD packets are sent by the local end = MAX { Configured minimum interval at which BFD packets are sent by the local end, Configured minimum interval at which BFD packets are received by the remote end }
   * Effective interval at which BFD packets are received by the local end = MAX { Configured minimum interval at which BFD packets are sent by the remote end, Configured minimum interval at which BFD packets are received by the local end }
   * Effective detection interval on the local end = Effective interval at which BFD packets are received by the local end x Detection multiplier configured on the remote end
   
   If **tos-exp** *tosexp-value* is specified, a priority is configured for all IS-IS BFD packets in the current process.
6. (Optional) Disable a specified interface from creating a BFD session.
   
   
   
   After BFD is configured for an IS-IS process, all interfaces on which neighbor relationships are up in the IS-IS process create BFD sessions. If BFD is not required on specific interfaces, disable these interfaces from creating BFD sessions.
   
   
   
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**isis bfd block**](cmdqueryname=isis+bfd+block)
      
      
      
      The interface is disabled from creating a BFD session.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**isis**](cmdqueryname=isis) *process-id*
      
      
      
      The IS-IS view is displayed.
7. (Optional) Run [**bfd all-interfaces incr-cost**](cmdqueryname=bfd+all-interfaces+incr-cost) { *cost-value* | **max-reachable** } [ **wtr** *wtr-value* ]
   
   
   
   The IS-IS process is enabled to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The delay configured for an interface to restore the cost based on the BFD session status takes precedence over that configured for a process to restore the cost based on the BFD session status.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.