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
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Change the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
6. Enable IPv6 BFD on the interface to establish IPv6 BFD sessions.
   
   
   ```
   [isis ipv6 bfd enable](cmdqueryname=isis+ipv6+bfd+enable)
   ```
   
   
   
   If BFD is enabled globally, this step is performed, and neighbors' IPv6 status is up (the DIS is up in the case of a broadcast network), default BFD parameters are used by this interface to establish BFD sessions.
7. (Optional) Configure parameters for IPv6 BFD session establishment.
   
   
   ```
   [isis ipv6 bfd](cmdqueryname=isis+ipv6+bfd) { min-tx-interval transmit-interval | min-rx-interval receive-interval | detect-multiplier multiplier-value | frr-binding } * 
   ```
   
   If IPv6 BFD session parameters are configured for both a process and an interface, those configured for the interface take precedence and are used by this interface to establish BFD sessions.
8. (Optional) Enable the interface to adjust the cost based on the status of an associated BFD session.
   
   
   ```
   [isis ipv6 bfd incr-cost](cmdqueryname=isis+ipv6+bfd+incr-cost) { cost-value | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```