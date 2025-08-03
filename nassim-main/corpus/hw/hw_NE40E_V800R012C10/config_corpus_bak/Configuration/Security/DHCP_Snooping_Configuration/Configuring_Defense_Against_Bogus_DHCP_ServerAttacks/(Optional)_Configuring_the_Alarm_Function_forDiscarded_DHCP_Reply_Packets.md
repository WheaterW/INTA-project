(Optional) Configuring the Alarm Function forDiscarded DHCP Reply Packets
=========================================================================

If an alarm needs to be generated when a specified number of Dynamic Host Configuration Protocol (DHCP) reply packets are discarded, you can configure the alarm function for discarded DHCP reply packets.

#### Context

After trusted and untrusted interfaces are configured, the device discards all DHCP reply packets received from untrusted interfaces. You can set a threshold for the number of discarded packets. When the number of discarded packets reaches the threshold, an alarm is generated.

For a Layer 2 device, configure the alarm function for discarded DHCP reply packets in a VLAN view. For a Layer 3 device, configure the alarm function for discarded DHCP reply packets in an interface view or in a BD view.


#### Procedure

* Configure the alarm function for discarded DHCP reply packets in a VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping alarm dhcp-reply enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-reply+enable) [ **interface** *interface-type interface-number* ]
     
     
     
     The alarm function for discarded DHCP reply packets is enabled for the VLAN.
  4. Run [**dhcp snooping alarm dhcp-reply threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-reply+threshold) *threshold* [ **interface** *interface-type* *interface-number* ]
     
     
     
     The alarm threshold for the number of discarded packets is configured for the VLAN.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP reply packets in a BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping alarm dhcp-reply enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-reply+enable)
     
     
     
     The alarm function for discarded DHCP reply packets is enabled in the BD.
  4. Run [**dhcp snooping alarm threshold**](cmdqueryname=dhcp+snooping+alarm+threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of discarded packets is configured in the BD.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the alarm function for discarded DHCP reply packets in an interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**dhcp snooping alarm dhcp-reply enable**](cmdqueryname=dhcp+snooping+alarm+dhcp-reply+enable)
     
     
     
     The alarm function for discarded DHCP reply packets is enabled for the interface.
  4. Run [**dhcp snooping alarm dhcp-reply threshold**](cmdqueryname=dhcp+snooping+alarm+dhcp-reply+threshold) *threshold-value*
     
     
     
     The alarm threshold for the number of discarded packets is configured for the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.