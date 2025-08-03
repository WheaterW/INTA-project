Configuring Loop Prevention
===========================

Configuring Loop Prevention

#### Context

On a network running a spanning tree protocol, a device maintains the root port and blocked port states based on BPDUs received from upstream devices. However, if the ports cannot receive BPDUs from upstream devices because of link congestion or unidirectional link failures, the device re-selects a root port. In this case, the original root port will then become a designated port, and the original blocked ports will change to the Forwarding state. This may cause loops on the network; however, it can be avoided through loop prevention.

If the root port or alternate port does not receive BPDUs from the upstream device for a long time, the device enabled with loop prevention sends a notification to the NMS. In this case, the root port enters the Discarding state and becomes the designated port, while the alternate port remains blocked and becomes the designated port. This prevents loops. In this case, loops will not occur on the network. The root or alternate port is restored to the Forwarding state only when it receives BPDUs.

If the device has an alternate port, which is a backup for the root port, configure loop prevention on both the root and alternate ports.

Root protection and loop prevention cannot be configured on the same port.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view of the root port or alternate port.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable loop prevention.
   
   
   ```
   [stp loop-protection](cmdqueryname=stp+loop-protection)
   ```
   
   By default, loop prevention is disabled.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp vlan**](cmdqueryname=display+stp+vlan) [ *vlan-id* ] **information** [ **brief** ] command and check the Protection Type field to verify the loop prevention configuration.