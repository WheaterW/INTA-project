(Optional) Configuring the Maximum Number of Dynamic ND Entries
===============================================================

Configuring the maximum number of dynamic ND entries protects against RA flood attacks.

#### Procedure

* Configure the maximum number of dynamic ND entries on a Layer 3 interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled for the interface.
  4. Run [**ipv6 nd neighbor-limit**](cmdqueryname=ipv6+nd+neighbor-limit) *max-number*
     
     
     
     The maximum number of dynamic ND entries is configured on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the maximum number of dynamic ND entries on a Layer 2 interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**portswitch**](cmdqueryname=portswitch)
     
     
     
     The interface working mode is switched to Layer 2.
  4. Run [**ipv6 nd neighbor-limit vlan**](cmdqueryname=ipv6+nd+neighbor-limit+vlan) *vlanBegValue* [ **to** *vlanEndValue* ] **maximum** *limit-number*
     
     
     
     The maximum number of dynamic ND entries is configured on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.