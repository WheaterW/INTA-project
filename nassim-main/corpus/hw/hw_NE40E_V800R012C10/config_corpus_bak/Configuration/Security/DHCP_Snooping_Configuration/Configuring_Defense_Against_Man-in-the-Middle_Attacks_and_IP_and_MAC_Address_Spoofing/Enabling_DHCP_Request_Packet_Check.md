Enabling DHCP Request Packet Check
==================================

To prevent man-in-the-middle attacks and IP/MAC address
spoofing, enable Dynamic Host Configuration Protocol (DHCP) request
packet check. After packet check is enabled on a device, the device
checks the received Address Resolution Protocol (ARP) or IP packets
to see whether the combination of source IP addresses and source MAC
addresses in the packets match entries in the DHCP snooping binding
table.

#### Context

For DHCP users, the DHCP snooping binding table is automatically
generated when DHCP snooping is enabled. For users using static IP
addresses, the DHCP snooping binding table needs to be manually configured.

Enable DHCP snooping in an interface, BD, or VLAN view.


#### Procedure

* Enable DHCP request packet check in a VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) { **arp** | **ip** } **enable** [ **interface** *interface-type* *interface-number* ]
     
     
     
     DHCP request packet check is enabled for the VLAN.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable DHCP request packet check in a BD
  view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) { **arp** | **ip** } **enable**
     
     
     
     DHCP request packet check is enabled in a BD.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable DHCP request packet check in an interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) { **arp** | **ip** } **enable**
     
     
     
     DHCP request packet check is enabled for the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.