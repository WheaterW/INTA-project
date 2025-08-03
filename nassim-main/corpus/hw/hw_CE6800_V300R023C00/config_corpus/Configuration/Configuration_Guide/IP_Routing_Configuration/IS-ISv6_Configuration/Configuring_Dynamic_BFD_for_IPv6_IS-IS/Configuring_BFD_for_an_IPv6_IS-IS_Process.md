Configuring BFD for an IPv6 IS-IS Process
=========================================

Configuring BFD for an IPv6 IS-IS Process

#### Prerequisites

Before configuring BFD for an IPv6 IS-IS process, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

IS-IS detects neighbor state changes through IIH exchanges. By default, if no response is received to three consecutive IIHs within a specified period (30 seconds by default), a neighbor is considered down. For networks that require fast convergence and zero packet loss, IS-IS cannot meet link fault detection requirements. To address this problem, you can configure BFD for IS-IS.

Sessions of dynamic BFD for IS-IS are dynamically established by IS-IS, preventing manual misconfigurations. Dynamic BFD is easy to configure and applies to the scenarios where BFD needs to be configured on the entire network. Dynamic BFD helps detect link faults rapidly and implement fast route convergence.


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
5. Enable IPv6 BFD for the IS-IS process to establish IPv6 BFD sessions.
   
   
   ```
   [ipv6 bfd all-interfaces enable](cmdqueryname=ipv6+bfd+all-interfaces+enable)
   ```
6. (Optional) Configure parameters for IPv6 BFD session establishment.
   
   
   ```
   [ipv6 bfd all-interfaces](cmdqueryname=ipv6+bfd+all-interfaces) { min-rx-interval receive-interval | min-tx-interval transmit-interval | detect-multiplier multiplier-value | frr-binding } *
   ```
   
   
   
   The command execution results apply to IPv6 BFD session parameters on all interfaces in the IS-IS process.
7. (Optional) Enable the IS-IS process to adjust the cost based on the status of an associated BFD session.
   
   
   ```
   [ipv6 bfd all-interfaces incr-cost](cmdqueryname=ipv6+bfd+all-interfaces+incr-cost) { cost-value | max-reachable }
   ```
   
   If the function of adjusting the cost based on the status of an associated BFD session is configured both for a process and an interface, the configuration on the interface takes precedence.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```