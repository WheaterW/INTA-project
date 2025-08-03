Enabling DHCP Request Packet Check
==================================

To prevent unauthorized clients from sending Dynamic Host Configuration Protocol (DHCP) request packets to request IP addresses, the device checks whether information carried in a received DHCP request packet matches an entry in the DHCP snooping binding table. The checked information includes the source IP and MAC addresses. If a matching entry exists, the device considers the packet valid and forwards it. If no matching entry exists, the device considers the packet an attack packet and discards it.

#### Context

In dynamic address assignment mode, the device generates a DHCP snooping binding table to record DHCP client information. In static address assignment mode, configure a DHCP static binding table to record DHCP client information.

Enable DHCP request packet check in a VLAN, BD, or interface view.


#### Procedure

* Enable DHCP request packet check for a VLAN.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) **dhcp-request** **enable** [ **interface** *interface-type* *interface-number* ]
     
     
     
     DHCP request packet check is enabled for the VLAN.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable DHCP snooping in the BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     
     
     The BD view is displayed.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) **dhcp-request enable**
     
     
     
     DHCP request packet check is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable DHCP request packet check for an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
     
     The interface is the user-side interface.
  3. Run [**dhcp snooping check**](cmdqueryname=dhcp+snooping+check) **dhcp-request** **enable**
     
     
     
     DHCP request packet check is enabled for the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.