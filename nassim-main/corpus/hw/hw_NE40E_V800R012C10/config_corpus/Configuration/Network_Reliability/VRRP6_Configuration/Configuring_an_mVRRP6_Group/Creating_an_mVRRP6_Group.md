Creating an mVRRP6 Group
========================

You can create an mVRRP6 group and bind common VRRP6 groups to the mVRRP6 group. The mVRRP6 group determines the master/backup status of the common VRRP6 groups.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where the VRRP6 group resides is displayed.
3. Run [**admin-vrrp6 vrid**](cmdqueryname=admin-vrrp6+vrid) *virtual-router-id* [ **ignore-if-down** ]
   
   
   
   An mVRRP6 group is created.
   
   When multiple VRRP6 groups are configured on two devices, the master device in a VRRP6 group has to broadcast VRRP6 Advertisement packets to the backup device through a user-side device. If the user-side device does not support broadcast, it cannot transparently forward VRRP6 Advertisement packets from the master device to the backup device. An mVRRP6 group can be created on interfaces directly connecting the master device to the backup device, implementing VRRP6 status negotiation. If either of the directly connected VRRP6-enabled interfaces fails, the VRRP6 status on the other VRRP6-enabled interface becomes Initialize, causing service interruptions. To prevent this issue, configure the **ignore-if-down** parameter in this command. After a device detects an interface down event from the other device, this device does not respond to the event and properly forwards service traffic.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure intermediate link reliability when an mVRRP6 group is configured on a directly connected interface, deploy an inter-board trunk. To prevent both directly connected devices from switching to the Master state, do not run the [**shutdown**](cmdqueryname=shutdown) command on the directly connected interfaces unless an interface down event is caused by a master device failure.
4. (Optional) Run [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **initialize state-hold-time** *timer-value*
   
   
   
   An Initialize state hold time is configured for the mVRRP6 group.
   
   
   
   After the mVRRP6 group is configured to ignore an interface down event, you can run the command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.