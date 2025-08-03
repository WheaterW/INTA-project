Configuring Static MAC Address Entries
======================================

After a static MAC address entry is configured, packets with the destination MAC address matching the entry are forwarded from the specified outbound interface. This configuration protects a device from attack packets with forged MAC addresses.

#### Usage Scenario

If a network has fixed users or a server connects to a switch on the network, static MAC address entries need to be configured on the switch to prevent hackers from attacking the switch or the server. On the network shown in [Figure 1](#EN-US_TASK_0172362720__fig_dc_vrp_mac_cfg_000301), you can configure a static MAC address entry on the switch containing the MAC address of the server so that the switch forwards packets destined for the server through only a specified interface. This configuration prevents hackers from attacking the server using forged MAC addresses and from stealing information from the server, as well as ensures the communication between users and the server.

**Figure 1** Networking for static MAC address entry configuration  
![](figure/en-us_image_0000001316577222.png)

#### Pre-configuration Tasks

Before configuring a static MAC address entry, connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run one or more of the following commands to add static MAC address entries:
   
   
   * Run the [**mac-address static**](cmdqueryname=mac-address+vlan%EF%BC%88%E7%B3%BB%E7%BB%9F%E8%A7%86%E5%9B%BE%EF%BC%89) *mac-address* *interface-type interface-number* **vlan** *vlan-id* command to add a VLAN-based static MAC address entry.
   * Run the [**mac-address static**](cmdqueryname=mac-address+vsi) *mac-address* *interface-type interface-number* **vsi** *vsi-name* [ **pe-vid** *pe-vid* [ **ce-vid** *ce-vid* ] ] command to add a VSI-based static MAC address entry.
   * Run the [**mac-address static**](cmdqueryname=mac-address%28%E7%B3%BB%E7%BB%9F%E8%A7%86%E5%9B%BE%29) *mac-address* *interface-type interface-number* { **vlanif-type** *vlanif-number* | **vlanif-name** } **vsi** *vsi-name* command to configure a MAC address entry for the VSI bound to a VLANIF interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Static MAC address entries take precedence over dynamic MAC address entries.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following commands to check the previous configurations.

* Run the [**display mac-address**](cmdqueryname=display+mac-address) *mac-address* { [ **vlan** *vlan-id* ] | [ **vsi** *vsi-name* [ **ce-vlan** ] ] | [ **ce-vlan** ] } [ **verbose** ] command to check MAC address entries.
* Run the **display mac-address static** { { [ **vlan** *vlan-id* ] | [ *interface-type* *interface-number* | *interface-name* ] } \* | [ **vsi** *vsi-name* ] } [ { **verbose** | { **effective** [ **slot** *slot-id* ] } } \* ] command to check static MAC address entries.