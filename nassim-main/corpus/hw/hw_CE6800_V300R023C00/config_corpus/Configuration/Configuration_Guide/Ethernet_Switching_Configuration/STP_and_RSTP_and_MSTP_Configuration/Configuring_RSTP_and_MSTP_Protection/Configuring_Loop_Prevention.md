Configuring Loop Prevention
===========================

Configuring Loop Prevention

#### Context

On an RSTP or MSTP network, a device maintains root and blocked port states based on BPDUs received from an upstream device. If the device cannot receive BPDUs from the upstream device because of link congestion or unidirectional link failures, the device will select a new root port. In this case, the original root port will then become a designated port, and the original blocked ports will change to the Forwarding state. This will cause loops on the network; however, it can be avoided through loop prevention.

If the root or alternate ports do not receive BPDUs from the upstream device for a long time, the device enabled with loop prevention sends a notification to the NMS. If the root port is used, then it enters the Discarding state. The blocked ports remain blocked and do not forward packets. In this case, loops will not occur on the network, and after receiving BPDUs, the root or alternate port is restored to the Forwarding state.

If the device has an alternate port, which is a backup for the root port, configure loop prevention on both the root and the alternate ports.

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
4. (Optional) Add the interface to a specified MSTP process with a non-zero ID.
   
   
   
   Skip this step if the interface belongs to MSTP process 0.
   
   ```
   [stp binding process](cmdqueryname=stp+binding+process) process-id
   ```
5. Enable loop prevention.
   
   
   ```
   [stp loop-protection](cmdqueryname=stp+loop-protection)
   ```
   
   By default, loop prevention is disabled.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the following commands and check the Protection Type field to verify the loop prevention configuration.

* [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ]
* [**display stp active**](cmdqueryname=display+stp+active)