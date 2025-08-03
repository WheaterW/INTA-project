Enabling DHCP Snooping
======================

Enabling DHCP Snooping

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001513040322__fig201551904532), DeviceA is a Layer 2 access device that forwards DHCP request messages from the clients to the DHCP server. When you enable DHCP snooping on DeviceA, note the following:

* Before enabling DHCP snooping, you must run the **dhcp enable** command to enable DHCP on the device.
* After DHCP snooping is enabled globally, you need to enable DHCP snooping on the interfaces (interface 1, interface 2, and interface 3 in the figure) connected to the clients or the VLAN (VLAN 10 in the figure) to which the interfaces belong.
  
  If multiple clients belong to the same VLAN, you can enable DHCP snooping in this VLAN to simplify configurations.

**Figure 1** Network diagram of configuring basic DHCP snooping functions  
![](../images/en-us_image_0000001564120455.png)
![](../public_sys-resources/note_3.0-en-us.png) 

* Before configuring basic DHCP snooping functions, enable DHCP and DHCP snooping globally.
* DHCP snooping does not support the BOOTP protocol. However, diskless workstations use this protocol. As such, diskless workstations cannot generate dynamic binding entries through DHCP snooping. IPSG and DAI are implemented based on binding entries. To use these functions on a diskless workstation, you need to run the **[**user-bind static**](cmdqueryname=user-bind+static)** command to configure static binding entries.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable DHCP.
   
   
   ```
   [dhcp enable](cmdqueryname=dhcp+enable)
   ```
   
   By default, DHCP is disabled on a device.
3. Enable DHCP snooping globally.
   
   
   ```
   [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
   ```
   
   By default, DHCP snooping is disabled on a device.
4. Enable DHCP snooping in the VLAN, BD, or interface view.
   
   
   * Enter the VLAN view and enable DHCP snooping in the VLAN.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
     [quit](cmdqueryname=quit)
     ```
     
     To enable DHCP snooping in multiple VLAN views in batches, run the [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable) [ [**vlan**](cmdqueryname=vlan) { *vlan-id1* [ [**to**](cmdqueryname=to) *vlan-id2* ] } &<1-10> ] command.
   * Enter the interface view and enable DHCP snooping on the interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
     [quit](cmdqueryname=quit)
     ```
   * Enter the BD view and enable DHCP snooping in the BD.
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     [dhcp snooping enable](cmdqueryname=dhcp+snooping+enable)
     [quit](cmdqueryname=quit)
     ```
   
   
   
   By default, DHCP snooping is disabled on a device.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```