Configuring mLDP P2MP Tunnels with Dual-Root Protection
=======================================================

This section describes how to configure mLDP P2MP tunnels with dual-root protection to ensure reliable transmission of multicast traffic.

#### Procedure

* Perform the following steps on the root node:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
  3. (Optional) Run the [**ignore-ac-state**](cmdqueryname=ignore-ac-state) command to configure the VSI to ignore AC status changes.
  4. Run the [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel) command to create and enter the VSI-Inclusive view.
  5. Run the [**root**](cmdqueryname=root) command to specify the current device as the root node for multicast VPLS and enter the VSI-Inclusive-Root view.
  6. Run the [**data-switch disable**](cmdqueryname=data-switch+disable) command to disable the current device from transmitting multicast traffic over P2P tunnels when the mLDP P2MP tunnel is down.
  7. (Optional) Run the [**bfd track interface**](cmdqueryname=bfd+track+interface) *interface-type* *interface-number* command to configure BFD to monitor the upstream AC interface.
  8. Run the [**mldp p2mp**](cmdqueryname=mldp+p2mp) command to specify the tunnel type as mLDP P2MP for the local VSI, and enter the VSI-Inclusive-Root-mLDP-P2MP view.
  9. Run the [**root-ip**](cmdqueryname=root-ip) *ip-address* command to specify an IP address for the mLDP P2MP tunnel's root node.
  10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on each leaf node:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enter the MPLS L2VPN view.
  3. Run the [**vpls p2mp group-select ldp enable**](cmdqueryname=vpls+p2mp+group-select+ldp+enable) command to configure the current device to receive traffic from only the primary mLDP P2MP tunnel.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
  6. Run the [**inclusive-provider-tunnel**](cmdqueryname=inclusive-provider-tunnel) command to create and enter the VSI-Inclusive view.
  7. Run the [**leaf**](cmdqueryname=leaf) command to specify the current device as a leaf node for multicast VPLS.
  8. Run the [**primary-root**](cmdqueryname=primary-root)*priRootIp* [ **trackbfd** ] **backup-root***bakRootIp* [ **trackbfd** ] [ **wtr***wtrValue* ] command to specify the primary and backup mLDP P2MP tunnels.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.