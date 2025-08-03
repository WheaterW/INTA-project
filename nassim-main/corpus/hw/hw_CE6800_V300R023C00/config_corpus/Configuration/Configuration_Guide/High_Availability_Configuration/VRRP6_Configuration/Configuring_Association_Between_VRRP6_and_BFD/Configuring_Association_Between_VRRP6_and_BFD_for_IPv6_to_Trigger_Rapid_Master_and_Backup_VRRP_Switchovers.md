Configuring Association Between VRRP6 and BFD for IPv6 to Trigger Rapid Master/Backup VRRP Switchovers
======================================================================================================

Configuring Association Between VRRP6 and BFD for IPv6 to Trigger Rapid Master/Backup VRRP Switchovers

#### Prerequisites

Before configuring association between VRRP6 and BFD for IPv6, you have completed the following tasks:

* Configure a VRRP6 group.
* Ensure that VRRP6 devices support BFD for IPv6.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP6 group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Perform any of the following operations as required:
   * Associate the VRRP6 group with a common BFD for IPv6 session.
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ increase value-increased | reduce value-reduced ]
     ```
   * Associate the VRRP6 group with a link or peer BFD for IPv6 session.
     
     ```
     [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ peer | link ]
     ```
   
   When associating a VRRP6 group with a BFD for IPv6 session, note the following:
   
   * If you specify **session-name** *bfd-configure-name* when associating a VRRP6 group with a BFD for IPv6 session, the VRRP6 group can be bound to a static BFD for IPv6 session with either manually specified or automatically negotiated discriminators.
   * If *bfd-session-id* is specified, the VRRP6 group can be associated only with a static BFD for IPv6 session with manually specified discriminators.![](public_sys-resources/note_3.0-en-us.png) 
   * If a VRRP6 group is bound to an mVRRP6 group, the VRRP6 group status is consistent with the mVRRP6 group status. As such, the VRRP6 group cannot track any BFD sessions for IPv6 to trigger fast master/backup VRRP switchovers.
   * After a VRRP6 group is associated with link and peer BFD sessions for IPv6, the backup device switches to the Master state if it detects the peer BFD for IPv6 session down event before detecting the link BFD for IPv6 session down event. In addition, the backup device switches to the Initialize state after it detects the peer BFD for IPv6 session down event. To resolve the problem, run the [**min-tx-interval**](cmdqueryname=min-tx-interval) command in the BFD session view to set the interval for sending link BFD for IPv6 Control packets to a value less than the interval for sending peer BFD for IPv6 Control packets.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check VRRP6 group information.