(Optional) Configuring the Alarm Function forDiscarded DHCP Packets with Incorrect CHADDR Fields
================================================================================================

By configuring the function described in this chapter, you can have an alarm generated when a specified number of Dynamic Host Configuration Protocol (DHCP) packets with incorrect client hardware address (CHADDR) fields are discarded.

#### Context

After CHADDR field check is enabled, the device checks whether the media access control (MAC) address in the CHADDR field of a received DHCP packet matches that in the frame header of the packet. If they match, the device considers the packet valid and forwards it. If they do not match, the device considers the packet an attack packet and discards it. The device generates an alarm when the number of discarded DHCP packets with incorrect CHADDR fields reaches the predetermined threshold.

Configure the alarm function for discarded DHCP packets with incorrect CHADDR fields in a VLAN, BD, or interface view.


#### Procedure

* Configure the alarm function for discarded DHCP packets with incorrect CHADDR fields in a VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) **dhcp-chaddr** **enable** [ **interface** *interface-type interface-number* ]
     
     
     
     CHADDR field check is enabled for the VLAN.
  4. Run [**dhcp snooping alarm dhcp-chaddr threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-chaddr+threshold) *threshold* [ **interface** *interface-type* *interface-number* ]
     
     
     
     The alarm threshold for discarded DHCP packets with incorrect CHADDR fields is configured for the VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP packets with incorrect CHADDR fields in a BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) **dhcp-chaddr enable**
     
     
     
     CHADDR field check is enabled in the BD.
  4. Run [**dhcp snooping alarm dhcp-chaddr threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-chaddr+threshold) *threshold*
     
     
     
     The alarm threshold for discarded DHCP packets with incorrect CHADDR fields is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP packets with incorrect CHADDR fields in an interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping alarm**](cmdqueryname=dhcp+snooping+alarm) **dhcp-chaddr** **enable**
     
     
     
     CHADDR field check is enabled for the interface.
  4. Run [**dhcp snooping alarm dhcp-chaddr threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-chaddr+threshold) *threshold-value*
     
     
     
     The alarm threshold for discarded DHCP packets with incorrect CHADDR fields is configured for the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.