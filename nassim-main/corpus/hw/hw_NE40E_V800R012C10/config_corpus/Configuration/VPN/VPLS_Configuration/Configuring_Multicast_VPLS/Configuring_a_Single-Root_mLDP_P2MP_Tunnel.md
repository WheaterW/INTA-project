Configuring a Single-Root mLDP P2MP Tunnel
==========================================

This section describes how to configure a single-root mLDP
P2MP tunnel to minimize redundant traffic.

#### Procedure

* Perform the following steps on the root node:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  3. (Optional) Run [**ignore-ac-state**](cmdqueryname=ignore-ac-state)
     
     
     
     The VSI is configured
     to ignore AC status changes.
  4. Run [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel)
     
     
     
     The VSI-Inclusive view is created and displayed.
  5. Run [**root**](cmdqueryname=root)
     
     
     
     The current device is specified as the root node for
     multicast VPLS, and the VSI-Inclusive-Root view is displayed.
  6. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
     
     
     
     The tunnel type is
     specified as mLDP P2MP for the local VSI, and the VSI-Inclusive-Root-mLDP-P2MP
     view is displayed.
  7. Run [**root-ip**](cmdqueryname=root-ip) *ip-address*
     
     
     
     An IP address is specified for the mLDP P2MP tunnel's root node.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on each leaf node:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  3. Run [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel)
     
     
     
     The VSI-Inclusive view is created and displayed.
  4. Run [**leaf**](cmdqueryname=leaf)
     
     
     
     The current device is specified as a leaf node for multicast
     VPLS.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.