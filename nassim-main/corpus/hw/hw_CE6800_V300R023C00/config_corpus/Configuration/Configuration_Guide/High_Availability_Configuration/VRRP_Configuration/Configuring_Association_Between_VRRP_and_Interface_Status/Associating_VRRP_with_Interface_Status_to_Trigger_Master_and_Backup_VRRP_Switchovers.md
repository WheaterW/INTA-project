Associating VRRP with Interface Status to Trigger Master/Backup VRRP Switchovers
================================================================================

Associating VRRP with Interface Status to Trigger Master/Backup VRRP Switchovers

#### Prerequisites

Before associating VRRP with interface status, you have completed the following tasks:

* Configure a VRRP group.
* Configure the master and backup devices in the VRRP group to work in preemption mode.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the VRRP group to track the interface.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track interface interface-type interface-number [ increase value-increased | reduce value-decreased ]
   ```
   * By default, a VRRP device reduces its priority by 10 if the tracked interface goes down.
   * **increase** *value-increased* specifies the value by which a VRRP device increases its priority if the tracked interface goes down.
   * **reduce** *value-decreased* specifies the value by which a VRRP device reduces its priority if the tracked interface goes down.![](public_sys-resources/note_3.0-en-us.png) 
   * When setting a value for *value-decreased*, ensure that the priority of the backup is higher than that of the master after the specified value is deducted to trigger a master/backup VRRP switchover.
   * If a device is the IP address owner, its interfaces cannot be tracked.
   * After a VRRP group is configured on an Eth-Trunk interface, the VRRP group cannot be configured to track its member interfaces.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.