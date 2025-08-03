Configuring a Single-Root P2MP TE Tunnel
========================================

This section describes how to configure a single-root P2MP TE tunnel to minimize traffic redundancy.

#### Procedure

* Perform the following steps on the root node:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
  3. (Optional) Run the [**ignore-ac-state**](cmdqueryname=ignore-ac-state) command to configure the VSI to ignore AC status changes.
  4. Run the [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel) command to create and enter the VSI-Inclusive view.
  5. Run the [**root**](cmdqueryname=root) command to specify the current device as the root node for multicast VPLS and enter the VSI-Inclusive-Root view.
  6. Run the [**mpls-te**](cmdqueryname=mpls-te) command to specify the tunnel type as P2MP TE for the local VSI and enter the VSI-Inclusive-Root-MPLS-TE view.
  7. Run the [**p2mp**](cmdqueryname=p2mp) { **dynamic** | **te-template** *template-name* } command to create a P2MP TE tunnel.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on each leaf node:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
  3. Run the [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel) command to create and enter the VSI-Inclusive view.
  4. Run the [**leaf**](cmdqueryname=leaf) command to specify the current device as a leaf node for multicast VPLS.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.