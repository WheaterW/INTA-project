Associating an EVPL Instance with VRRP
======================================

Associate EVPL instances with VRRP on PEs, so that EVPN VPWS can determine the primary/secondary status of PWs based on the VRRP or VRRP6 group status.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   The EVPL instance view is displayed.
3. Run [**vrrp-id**](cmdqueryname=vrrp-id) *vrid* **interface** { *interface-name* | *interface-type* *interface-number* } or [**vrrp6-id**](cmdqueryname=vrrp6-id) *vrid* **interface** { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The EVPL instance is bound to the specified VRRP or VRRP6 group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.