Configuring VPLS Service Isolation
==================================

Configuring VPLS Service Isolation

#### Context

Users of different services can be isolated using different VSIs. Users in the same VSI may also need to be isolated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**isolate spoken**](cmdqueryname=isolate+spoken) [ [**include-multicast**](cmdqueryname=include-multicast) ]
   
   
   
   Forwarding isolation is enabled between AC interfaces, between UPE PWs, and between AC interfaces and UPE PWs in a VSI.
   
   
   
   If the users using the same service are bound in the same VSI, run the [**isolate spoken**](cmdqueryname=isolate+spoken) command to forbid the users from accessing each other.
   * On a non-hierarchical VPLS network, VSI service isolation prohibits traffic forwarding between AC interfaces.
   * On an HVPLS network, service isolation prohibits traffic forwarding between AC interfaces, between UPE PWs, and between AC interfaces and UPE PWs.
4. Run [**isolate hub-ac hub-pw**](cmdqueryname=isolate+hub-ac+hub-pw)
   
   
   
   Forwarding isolation is enabled between hub AC interfaces and PWs in a VSI.
5. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The AC interface view is displayed.
7. (Optional) Run [**hub-mode enable**](cmdqueryname=hub-mode+enable)
   
   
   
   The VSI attribute on the AC interface is changed from spoke to hub.
   
   
   
   After you run the [**isolate spoken**](cmdqueryname=isolate+spoken) command, traffic forwarding is prohibited between AC interfaces in a VSI. If a sub-interface in the VSI needs to communicate with other sub-interfaces in the VSI, you must run the [**hub-mode enable**](cmdqueryname=hub-mode+enable) command on the sub-interface to change the VSI attribute from spoke to hub.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.