Configuring CHADDR Field Check
==============================

If you want your device to check the client hardware address (CHADDR) field validity, configure CHADDR field check.

#### Context

The CHADDR field check function allows the device to check whether the media access control (MAC) address in the CHADDR field of a received Dynamic Host Configuration Protocol (DHCP) request packet matches that in the header of the packet. If they match, the device considers the packet valid and forwards it. If they do not match, the device considers the packet an attack packet and discards it.

Configure CHADDR field check in a VLAN, BD, or interface view.


#### Procedure

* Enable CHADDR field check in the VLAN view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  3. Run [**dhcp check**](cmdqueryname=dhcp+check) **chaddr** **enable** [ **interface** *interface-type* *interface-number* ]
     
     CHADDR field check is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable CHADDR field check in the BD view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**dhcp check chaddr enable**](cmdqueryname=dhcp+check+chaddr+enable)
     
     CHADDR field check is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable CHADDR field check in the interface view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
     
     This interface is a user-side interface.
  3. Run [**dhcp check**](cmdqueryname=dhcp+check) **chaddr** **enable**
     
     CHADDR field check is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.