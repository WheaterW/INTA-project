Configuring Route Recursion to SRv6 BE Paths
============================================

This section describes how to configure EVPN routes on PEs to carry SIDs and recurse to SRv6 BE paths based on SIDs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id* **static-mode**
   
   
   
   The static EVPL instance view is displayed.
3. Run [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name*
   
   
   
   The device is enabled to add the SID attribute to EVPN routes to be sent.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Static SRv6 EVPN VPWS supports only static SIDs. Configure a static SID for the locator specified by *locator-name*.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the static EVPL instance view.
5. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
   
   
   
   The VPWS EVPN instance view is displayed.
6. Run [**segment-routing ipv6 best-effort**](cmdqueryname=segment-routing+ipv6+best-effort)
   
   
   
   The device is enabled to recurse routes to SRv6 BE paths based on the SID attributes carried in these routes.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.