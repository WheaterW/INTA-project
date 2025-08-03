Configuring Association Between VRRP6 and Interface Status
==========================================================

This section describes how to associate a VRRP6 group with a VRRP6-disabled interface on the master device. If the master device detects that the status of the VRRP6-disabled interface changed, it rapidly performs a master/backup VRRP6 switchover.

#### Context

A VRRP6 group cannot detect changes in the status of a VRRP6-disabled interface. If a VRRP6-disabled interface connected to a network fails, the VRRP6 group cannot detect the fault and still forwards user packets through the failed interface, which results in service interruptions.

To resolve this issue, configure the VRRP6 group to track the VRRP6-disabled interface. If the interface goes down, the VRRP6 group detects the fault and reduces the master device's priority to trigger a rapid master/backup VRRP6 switchover.

Perform the following steps on each device in a VRRP6 group:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface where a VRRP6 group resides is displayed.
3. Run either of the following commands based on the protocol type of the tracked interface.
   
   
   * To track the IPv4 status of an interface, run the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** **interface** { *interface-name* | *interface-type* *interface-number* } [ **increased** *value-increased* | **reduced** *value-decreased* ] command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When you configure a VRRP6 group to track the IPv4 status of an interface, the network-layer protocol of the tracked interface must contain IPv4. Otherwise, the VRRP6 group tracks the link status of the interface.
   * To track the IPv6 status of an interface, run the [**vrrp6 vrid**](cmdqueryname=vrrp6+vrid) *virtual-router-id* **track** *ipv6* **interface** { *interface-name* | *interface-type* *interface-number* } [ **increased** *value-increased* | **reduced** *value-decreased* ] command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When you configure a VRRP6 group to track the IPv6 status of an interface, the network-layer protocol of the tracked interface must contain IPv6. Otherwise, the VRRP6 group tracks the link status of the interface.
   
   
   
   **increased** *value-increased* specifies the value by which the VRRP priority increases when the tracked interface goes down. The value ranges from 1 to 255. The value 255 is reserved for an IP address owner, and therefore the largest value can be set to 254.
   
   **reduced** *value-decreased* specifies the value by which the VRRP priority reduces if the tracked interface goes down. The value ranges from 1 to 255. The smallest value can be set to 1.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After you enable a VRRP6 group to track a VRRP6-disabled interface, an IP address owner's priority does not change because it is fixed at 255.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.