Creating an mVRRP Group
=======================

You can create an mVRRP group. Other common VRRP groups can be bound to the mVRRP group and become service VRRP groups. The mVRRP group determines the master/backup status of the service VRRP groups.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**admin-vrrp vrid**](cmdqueryname=admin-vrrp+vrid) *virtual-router-id* [ **ignore-if-down** ]
   
   
   
   An mVRRP group is specified.
   
   
   
   Among multiple VRRP groups configured on two devices, the master device in a backup group has to broadcast VRRP Advertisement packets to the backup device through a user-side device. If the user-side device does not support broadcast, it cannot transparently forward VRRP Advertisement packets from the master device to the backup device. mVRRP can be enabled on interfaces directly connecting the master device to the backup device, implementing VRRP status negotiation.
   
   However, if either of the directly connected VRRP-enabled interfaces fails, the VRRP status on the other VRRP-enabled interface becomes Initialize, leading to service interruptions. To prevent service interruptions, configure the **ignore-if-down** parameter in the **admin-vrrp vrid** command. This setting helps the other VRRP-enabled device to ignore the interface Down event and ensures proper service transmission.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Adding the directly connected interfaces to an inter-board trunk for an mVRRP group is recommended, ensuring the link reliability. Do not run the [**shutdown**](cmdqueryname=shutdown) command on either of the directly connected VRRP-enabled interfaces, preventing two master devices from coexisting or adversely affecting service forwarding.
4. (Optional) Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **initialize state-hold-time** *timer-value*
   
   
   
   An Initialize state hold time is configured for the mVRRP group.
   
   After the mVRRP group is configured to ignore an interface Down event, you can run the command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.