(Optional) Configuring the Alarm Function for Discarded Man-in-the-Middle Attack and IP/MAC Address Spoofing Packets
====================================================================================================================

By configuring the function described in this chapter, you can have an alarm generated when a specified number of man-in-the-middle attack and IP/MAC address spoofing packets are discarded.

#### Context

After packet check is enabled, if a received Address Resolution Protocol (ARP) or IP packet of a man-in-the-middle attack or IP/MAC address spoofing does not match any entry in the Dynamic Host Configuration Protocol (DHCP) snooping binding table, the device discards the ARP or IP packet. With the function described in this section configured, when the number of discarded packets reaches a specified threshold, an alarm is generated.

Configure the alarm function for discarded man-in-the-middle attack and IP/MAC address spoofing packets in a VLAN, BD, or interface view.


#### Procedure

* Configure the alarm function for discarded man-in-the-middle attack and IP/MAC address spoofing packets in a VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**enable**](cmdqueryname=enable) [ **interface** *interface-type interface-number* ]
     
     
     
     The alarm function is enabled for man-in-the-middle attacks and IP/MAC address spoofing in the VLAN view, so that an alarm is generated when the number of discarded IP and ARP packets reaches a specified threshold.
  4. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**threshold**](cmdqueryname=threshold) *threshold* [ **interface** *interface-type* *interface-number* ]
     
     
     
     An alarm threshold is configured for the number of discarded IP and ARP packets caused by man-in-the-middle attacks and IP/MAC address spoofing.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded man-in-the-middle attack and IP/MAC address spoofing packets in a BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**enable**](cmdqueryname=enable)
     
     
     
     The alarm function is enabled for man-in-the-middle attacks and IP/MAC address spoofing in the BD view, so that an alarm is generated when the number of discarded IP and ARP packets reaches a specified threshold.
  4. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**threshold**](cmdqueryname=threshold) *threshold-value*
     
     
     
     An alarm threshold is configured for the number of discarded IP and ARP packets caused by man-in-the-middle attacks and IP/MAC address spoofing.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded man-in-the-middle attack and IP/MAC address spoofing packets in an interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**enable**](cmdqueryname=enable)
     
     
     
     The alarm function is enabled for man-in-the-middle attacks and IP/MAC address spoofing in the interface view, so that an alarm is generated when the number of discarded IP and ARP packets reaches a specified threshold.
  4. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) { **arp** | **ip** } [**threshold**](cmdqueryname=threshold) *threshold-value*
     
     
     
     An alarm threshold is configured for the number of discarded IP and ARP packets caused by man-in-the-middle attacks and IP/MAC address spoofing.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.