(Optional) Configuring the DHCP Snooping Binding Table
======================================================

Dynamic entries in the DHCP snooping binding table are automatically generated when DHCP snooping is enabled. Static entries in the DHCP snooping binding table must be manually configured.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The static IP address and the IP address allocated to a user in static mode are the IP addresses that are manually configured on the client. Static users are those who use static IP addresses.

If the IP addresses allocated to users are static IP addresses, static binding entries can be configured for these IP addresses, ensuring static IP address anti-embezzlement. If there are a large number of static users, static binding entries must be configured for each static IP address; otherwise, unauthorized users who attempt to embezzle static IP addresses cannot be isolated.

Dynamic entries in the DHCP snooping binding table do not need to be configured. They are automatically generated when DHCP snooping is enabled. However, static entries in the DHCP snooping binding table must be configured by running commands.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* For the IP addresses dynamically allocated to users, devices automatically learn the MAC addresses of users and create a binding relationship table. The table does not need to be configured manually.
* For the IP addresses statically allocated to users, devices cannot create a binding relationship table. The table must be created manually.

If the binding relationship table for static users is not created manually, the following situations occur:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If the device is configured to forward packets that do not match any entry in the binding relationship table, the packets of all static users are forwarded. All static users can access the DHCP server normally. This is the default condition of the devices.
* If the device is configured for discard packets that do not match any entry in the binding relationship table, the packets of all static users are discarded. All static users cannot access the DHCP server.

If the created binding table must contain interface information, the Option82 function must be enabled. If the Option82 function is not enabled and DHCP snooping is enabled on the VLANIF interface, entries in the created DHCP snooping binding table do not contain interface information. For details, see the description of how to ["configure the Option82 function"](dc_vrp_dhcp-snooping_cfg_0016_1.html).

When an interface receives an Address Resolution Protocol (ARP) or IP packet, the interface matches the source IP address and source MAC address of the ARP or IP packet with entries in the DHCP snooping binding table. The interface checks the MAC address, IP address, interface, and virtual local area network (VLAN) information. Based on this check, the interface performs the following actions:

* The ARP or IP packet is discarded if its source IP address and source MAC address do not match any entry in the DHCP snooping binding table.
* The ARP or IP packet is forwarded if its source IP address and source MAC address match an entry in the DHCP snooping binding table.

When an interface receives an ARP or IP packet, the interface matches the source IP address and source MAC address of the ARP or IP packet with entries in the DHCP snooping binding table. The ARP or IP packet is forwarded if its source IP address and source MAC address match an entry in the DHCP snooping binding table, or is discarded if its source IP address and source MAC address do not match any entry in the DHCP snooping binding table.


#### Procedure

* Configure DHCP snooping static entries for a VLAN.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping bind-table static**](cmdqueryname=dhcp+snooping+bind-table+static) **ip-address** *ip-address* [ **mac-address** *mac-address* ] [ **interface** *interface-type* *interface-number* [ **ce-vlan** *ce-vlan-id* ] ]
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure static DHCP snooping binding entries.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping bind-table static**](cmdqueryname=dhcp+snooping+bind-table+static) **ip-address** *ip-address* [ **mac-address** *mac-address* ] [ **vlan** *vlan-id* [ **ce-vlan** *ce-vlan-id* ] ]
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure static DHCP snooping binding entries.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping bind-table static**](cmdqueryname=dhcp+snooping+bind-table+static) **ip-address** *ip-address* [ **mac-address** *mac-address* ] [ **vlan** *vlan-id* [ **ce-vlan** *ce-vlan-id* ] ]
     
     
     
     The static DHCP snooping entry is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure backup for the DHCP snooping binding table.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp snooping bind-table**](cmdqueryname=dhcp+snooping+bind-table) **autosave** *filename*
     
     
     
     Automatic backup is configured for the DHCP snooping binding table.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the file integrity check mode of the DHCP snooping binding table.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp snooping database authentication-mode**](cmdqueryname=dhcp+snooping+database+authentication-mode) { **check** | **no-check** | **force-check** }
     
     
     
     The file integrity check mode of the DHCP snooping binding table is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.