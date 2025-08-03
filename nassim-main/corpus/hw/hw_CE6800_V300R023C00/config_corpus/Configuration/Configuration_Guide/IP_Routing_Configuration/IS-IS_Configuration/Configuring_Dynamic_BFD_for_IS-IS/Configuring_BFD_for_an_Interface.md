Configuring BFD for an Interface
================================

Configuring BFD for an Interface

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. (Optional) Configure BFD session check for the IS-IS process.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   [bfd session-up check](cmdqueryname=bfd+session-up+check)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When the Layer 2 network is normal, IS-IS neighbor relationships can be established and routes can be delivered. However, if the Layer 3 network is unreachable, upper-layer traffic loss occurs. To resolve this problem, configure BFD session check for an IS-IS process by running the [**bfd session-up check**](cmdqueryname=bfd+session-up+check) command. This ensures that an IS-IS neighbor relationship is established only when the BFD session is up on corresponding interfaces. After this function is configured, it applies only to the neighbor relationships to be established (it does not apply to existing neighbor relationships).
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Enable BFD on the interface.
   
   
   ```
   [isis bfd enable](cmdqueryname=isis+bfd+enable)
   ```
   
   
   
   If BFD is enabled globally, this step is performed, and neighbors' status is up (the DIS is up in the case of a broadcast network), default BFD parameters are used by this interface to establish BFD sessions.
8. (Optional) Configure parameters for BFD session establishment.
   
   
   ```
   [isis bfd](cmdqueryname=isis+bfd) { min-tx-interval transmit-interval | min-rx-interval receive-interval | detect-multiplier multiplier-value | frr-binding } *
   ```
   
   The BFD configurations on an interface take precedence over those of a process. That is, if BFD session parameters are configured for both a process and an interface, the parameters on the interface will be used to establish BFD sessions.
9. (Optional) Enable the interface to adjust the cost based on the status of an associated BFD session.
   
   
   ```
   [isis bfd incr-cost](cmdqueryname=isis+bfd+incr-cost) { cost-value | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```