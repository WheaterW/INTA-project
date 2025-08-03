Configuring BFD for an IS-IS Process
====================================

Configuring BFD for an IS-IS Process

#### Context

IS-IS detects neighbor state changes through Hello packet exchanges. By default, if no response is received to three consecutive Hello packets within a specified period (30 seconds by default), a neighbor is considered down. For networks that require fast convergence and zero packet loss, IS-IS cannot meet link fault detection requirements. To address this problem, you can configure BFD for IS-IS.

Sessions of dynamic BFD for the protocol are dynamically established by the protocol, preventing manual misconfigurations. Dynamic BFD is easy to configure and applies to the scenarios where BFD needs to be configured on the entire network. Dynamic BFD helps IS-IS detect link faults rapidly and implement fast route convergence.


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
4. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) process-id
   ```
5. Enable BFD for the IS-IS process.
   
   
   ```
   [bfd all-interfaces enable](cmdqueryname=bfd+all-interfaces+enable)
   ```
6. (Optional) Configure parameters for BFD session establishment.
   
   
   ```
   [bfd all-interfaces](cmdqueryname=bfd+all-interfaces) { min-rx-interval receive-interval | min-tx-interval transmit-interval | detect-multiplier multiplier-value | frr-binding } *
   ```
   
   
   
   The command execution results apply to BFD session parameters on all interfaces in the IS-IS process.
7. (Optional) Enable the IS-IS process to adjust the cost based on the status of an associated BFD session.
   
   
   ```
   [bfd all-interfaces incr-cost](cmdqueryname=bfd+all-interfaces+incr-cost) { cost-value | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```