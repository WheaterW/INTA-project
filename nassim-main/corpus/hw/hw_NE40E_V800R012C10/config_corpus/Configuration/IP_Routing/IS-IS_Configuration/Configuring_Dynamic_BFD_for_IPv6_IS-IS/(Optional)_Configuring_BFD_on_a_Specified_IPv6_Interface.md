(Optional) Configuring BFD on a Specified IPv6 Interface
========================================================

You can configure dynamic BFD session parameters for a specified IPv6 interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) To configure BFD session check for an IS-IS process, perform the following steps:
   1. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
      
      
      
      The IS-IS view is displayed.
   2. Run [**bfd session-up check**](cmdqueryname=bfd+session-up+check)
      
      
      
      BFD session check is configured for the IS-IS process.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the Layer 2 network is normal, IS-IS neighbor relationships can be established and routes can be delivered. However, if the Layer 3 network is unreachable, upper-layer traffic loss occurs. To resolve this problem, configure BFD session check for an IS-IS process by running the [**bfd session-up check**](cmdqueryname=bfd+session-up+check) command. This ensures that an IS-IS neighbor relationship is established only when the BFD session is up on corresponding interfaces. After this function is configured, it applies only to the neighbor relationships to be established (it does not apply to existing neighbor relationships).
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**isis ipv6 bfd enable**](cmdqueryname=isis+ipv6+bfd+enable)
   
   
   
   BFD is enabled for the IPv6 interface to establish BFD sessions.
   
   
   
   BFD must be enabled globally before you perform this step. If BFD is enabled globally, this step is performed, and the IPv6 status of neighbors is up (or the DIS is up in the case of a broadcast network), default BFD parameters are used by this interface to establish BFD sessions.
5. (Optional) Run [**isis ipv6 bfd**](cmdqueryname=isis+ipv6+bfd) { **min-rx-interval** *receive*-*interval* | **min-tx-interval** *transmit*-*interval* | **detect-multiplier** *multiplier-value* | **frr-binding** } \*
   
   
   
   BFD parameters are configured to establish BFD sessions.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If BFD session parameters are configured for both a process and an interface, those configured for the interface take precedence and are used by this interface to establish BFD sessions.
6. (Optional) Run [**isis ipv6 bfd incr-cost**](cmdqueryname=isis+ipv6+bfd+incr-cost) { *cost-value* | **max-reachable** } [ **wtr** *wtr-value* ]
   
   
   
   The interface is enabled to adjust the cost based on the status of an associated BFD session.
   
   
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
   
   The cost restoration delay configured for BFD association on an interface takes precedence over that configured for BFD association in a process.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.