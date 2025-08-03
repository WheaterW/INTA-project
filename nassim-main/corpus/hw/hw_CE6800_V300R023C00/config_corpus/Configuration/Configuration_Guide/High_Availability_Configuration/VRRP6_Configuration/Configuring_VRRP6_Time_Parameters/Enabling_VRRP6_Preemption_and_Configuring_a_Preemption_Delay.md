Enabling VRRP6 Preemption and Configuring a Preemption Delay
============================================================

Enabling VRRP6 Preemption and Configuring a Preemption Delay

#### Context

If a network is unstable, configure either of the following preemption modes to improve master/backup state stability, and to prevent dual masters from coexisting and hosts from learning an incorrect MAC address of the master device due to frequent master/backup switchovers:

* Immediate preemption: The preemption delay is 0s, indicating that a backup device immediately preempts the master role after the master device fails. This mode minimizes service interruption duration.
* Delayed preemption: The master device preempts the master role after a specified preemption delay following recovery. Specifically, the master device waits for other services to recover (for example, route convergence is complete) before it preempts the master role to minimize packet loss.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP6 group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Change the working mode of the interface from Layer 2 to Layer 3. Determine whether to perform this step based on the device configuration.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure a preemption delay for the backup device in the VRRP6 group.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id preempt timer delay delay-time
   ```
   
   The default preemption delay is 5 seconds for a preemption caused by an interface up event or 0 seconds (indicating immediate preemption) for a preemption caused by any other reason.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When the IPv6 address owner recovers from a fault, it immediately becomes the master device despite the configured delay. The preemption delay is a period during which the original master device in the Backup state is waiting to preempt the master role, and it does not apply to the IPv6 address owner. Consequently, in a VRRP6 group that needs to be configured with a preemption delay, the master device cannot be configured as the IPv6 address owner.
5. (Optional) Configure the VRRP6 group to work in non-preemption mode.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id preempt disable
   ```
   
   When a VRRP6 group works in non-preemption mode, a backup device (regardless of priority) cannot preempt the master role as long as the master device is working properly.
6. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.