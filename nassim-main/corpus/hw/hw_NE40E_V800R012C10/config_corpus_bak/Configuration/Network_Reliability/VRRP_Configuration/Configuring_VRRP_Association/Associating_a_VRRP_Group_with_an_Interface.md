Associating a VRRP Group with an Interface
==========================================

You can associate a VRRP group with a VRRP-disabled interface on the master device. If the master device detects that the status of the VRRP-disabled interface changes, it rapidly performs a master/backup VRRP switchover.

#### Context

The master device cannot detect changes in the status of interfaces that are not in a VRRP group. If a VRRP-disabled interface connected to a network fails, the master device cannot detect the fault and still forwards user packets through the failed interface, which results in service interruptions.

To prevent this issue, associate the VRRP group with the VRRP-disabled interface. If the interface goes Down, the VRRP group detects the fault, reduces the priority of the master device, and sends VRRP Advertisement packets to elect a new master device.

Perform the following steps on a device on which an interface needs to be associated with a VRRP group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which the VRRP group is configured is displayed.
3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **track** **interface** {  *interface-name*  | *interface-type* *interface-number* } [ **increased** *value-increased* | **reduced** *value-decreased* ] 
   
   
   
   The VRRP group is configured to track the interface.
   
   
   
   * **increased** *value-increased* specifies the value by which the VRRP priority increases when the tracked interface goes Down. The value is an integer ranging from 1 to 255. The value 255 is reserved for an IP address owner, and therefore the largest value can be set to 254.
   * **reduced** *value-decreased* specifies the value by which the VRRP priority decreases when the tracked interface goes Down. The value is an integer ranging from 1 to 255. The lowest priority can reach 1.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a device is the IP address owner, its interfaces cannot be tracked.
   * After a VRRP group is configured on an Eth-Trunk interface, the VRRP group cannot be configured to track its member interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.