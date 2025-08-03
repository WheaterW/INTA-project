Configuring Association Between VRRP and BFD to Trigger Rapid Master/Backup VRRP Switchovers
============================================================================================

Configuring Association Between VRRP and BFD to Trigger Rapid Master/Backup VRRP Switchovers

#### Prerequisites

Before configuring association between VRRP and BFD, you have completed the following tasks:

* Configure a VRRP group.
* Ensure that VRRP devices support BFD.

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface where a VRRP group resides.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Perform any of the following operations as required:
   * Associate the VRRP group with a common BFD session.
     ```
     [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ increase value-increased | reduce value-reduced ]
     ```
     
     By default, the device that tracks a BFD session reduces its VRRP priority by 10 if the BFD session goes down.
   * Associate the VRRP group with link and peer BFD sessions.
     
     1. Associate the VRRP group with link and peer BFD sessions.
        ```
        [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track bfd { bfd-session-id | session-name bfd-configure-name } [ peer | link ]
        ```
     2. Configure a threshold for the number of VRRP-tracked link BFD sessions that go down.
        
        ```
        [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id track link-bfd down-number
        ```
        
        If the number of VRRP-tracked link BFD sessions that go down reaches or exceeds the threshold specified by *down-number*, the VRRP group performs a master/backup VRRP switchover.
   * Associate the VRRP group with a VRID-based dynamic BFD session.
     1. Create a VRID-based dynamic BFD session for the VRRP group, and configure the peer IP address bound to the dynamic BFD session.
        ```
        [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id bfd peer-ip peer-ip-address
        ```
     2. Configure parameters for the VRID-based dynamic BFD session.
        
        ```
        [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id bfd { min-rx-interval transmit-interval | min-tx-interval receive-interval | detect-multiplier multiplier-value } *
        ```
        
        The default minimum intervals for sending and receiving BFD Control packets are 10 ms, and the default local detection multiplier is 3.
5. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

![](public_sys-resources/note_3.0-en-us.png) 

* If you specify **session-name** *bfd-configure-name* when associating a VRRP group with a common BFD session or link and peer BFD sessions, the VRRP group can be bound to a static BFD session with either manually specified or automatically negotiated discriminators. If *bfd-session-id* is specified, the VRRP group can be associated only with a static BFD session with manually specified discriminators.
* If a VRRP group is bound to an mVRRP group, the VRRP group status is consistent with the mVRRP group status. As such, the VRRP group cannot track any BFD sessions for fast master/backup VRRP switchovers.
* After a VRRP group is associated with a link BFD session and a peer BFD session, the backup device switches to the Master state if it detects the peer BFD session down event before detecting the link BFD session down event. In addition, the backup device switches to the Initialize state after it detects the peer BFD session down event. To resolve this problem, run the [**min-tx-interval**](cmdqueryname=min-tx-interval) command in the BFD session view to set the interval for sending link BFD Control packets to a value less than the interval for sending peer BFD Control packets.


#### Verifying the Configuration

* Run the [**display vrrp**](cmdqueryname=display+vrrp) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ *virtual-router-id* ] [ **verbose** ] command to check the VRRP group status.
* Run the **[**display vrrp bfd session**](cmdqueryname=display+vrrp+bfd+session)** {****all**** | ****interface**** { **interface-name** | **interface-type** **interface-number** } ****vrid**** **virtual-router-id** } command to check the configuration and status of the VRID-based dynamic BFD session.