(Optional) Configuring the Alarm Function forDiscarded DHCP Packets for Extending the IP Address Lease
======================================================================================================

By configuring the function described in this chapter, you can have an alarm generated when a specified number of Dynamic Host Configuration Protocol (DHCP) packets for extending the IP address lease are discarded.

#### Context

After DHCP request packet check is enabled, the device checks whether the source IP address, source MAC address, virtual local area network (VLAN) ID, and interface information carried in a received DHCP request packet match an entry in the DHCP snooping binding table. If no matching entry exists, the device considers the packet an attack packet and discards it. The device generates an alarm when the number of discarded DHCP packets for extending the IP address lease exceeds the threshold.

Configure the alarm function for discarded DHCP packets for extending the IP address lease in a VLAN, BD, or interface view.


#### Procedure

* Configure the alarm function for discarded DHCP packets for extending the IP address lease in a VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping alarm dhcp-request enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+enable) [ **interface** *interface-type interface-number* ]
  4. Run [**dhcp snooping alarm dhcp-request threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+threshold) *threshold* [ **interface** *interface-type* *interface-number* ]
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP packets for extending the IP address lease in a BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping alarm dhcp-request enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+enable)
  4. Run [**dhcp snooping alarm dhcp-request threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+threshold) *threshold-value*
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP packets for extending the IP address lease in an interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping alarm dhcp-request enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+enable)
  4. Run [**dhcp snooping alarm dhcp-request threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-request+threshold) *threshold-value*
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.