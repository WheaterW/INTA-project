Enabling DHCP Snooping
======================

To configure Dynamic Host Configuration Protocol (DHCP) snooping functions, enable DHCP snooping first.

#### Context

Enable DHCP snooping in the following sequence:

* Enable DHCP globally.
* Enable DHCP snooping globally.
* Enable DHCP snooping in an interface, BD, or VLAN view.


#### Procedure

* To protect Layer 2 devices against bogus DHCP server attacks, enable DHCP snooping in the VLAN view.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
     
     DHCP is enabled globally.
  3. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
     
     DHCP snooping is enabled globally.
  4. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     The VLAN view is displayed.
  5. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable) [ **interface** *interface-type* *interface-number* ]
     
     DHCP snooping is enabled in the VLAN.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* To protect Layer 3 devices against bogus DHCP server attacks, enable DHCP snooping in the interface view.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
     
     DHCP is enabled globally.
  3. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
     
     DHCP snooping is enabled globally.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  5. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
     
     DHCP snooping is enabled on the interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable DHCP snooping in the BD view.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
     
     DHCP is enabled globally.
  3. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
     
     DHCP snooping is enabled globally.
  4. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  5. Run [**dhcp snooping enable**](cmdqueryname=dhcp+snooping+enable)
     
     DHCP snooping is enabled in the BD.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Currently, DHCP snooping cannot be configured in VXLAN scenarios.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.