Configuring an L2VPN Monitoring Group
=====================================

During fault rectification in a link protection scenario, if service VSI PWs go up prior to protocol VSI PWs, service VSI loops occur. To prevent this issue, you can configure an L2VPN monitoring group to monitor the VSI recovery status and delay the unblocking of service VSI PWs.

#### Usage Scenario

In a link protection scenario such as RRPP, if a device restarts, a board resets, or both the primary and secondary PWs fail, the service and protocol VSI PWs also fail. (The protocol VSI is a VSI that transmits link protection protocol packets.) When the fault recovers, the service VSI PWs may go up prior to the protocol VSI PWs. This will result in a service VSI loop, adversely affecting service traffic.

To solve this problem, create an L2VPN monitoring group, bind the protocol VSI PWs to the monitoring group, and specify the monitoring group to be tracked in the service VSI. If the service VSI PWs go up prior to the protocol VSI PWs bound to the monitoring group, the device blocks the service VSI PWs. When all the protocol VSI PWs bound to the monitoring group go up, the hold-off timer is started. After the timer expires, the service PWs are unblocked. This ensures that no service VSI loop occurs in such a scenario.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The protocol VSI is a VSI that transmits link protection protocol packets.

#### Pre-configuration Tasks

Before configuring an L2VPN monitoring group, complete the following tasks:

* Create the protocol VSI and related PWs.
* Create the service VSI and related PWs.
* Configure link protection.


#### Procedure

* Configure an L2VPN monitoring group and set a hold-off time for unblocking service VSI PWs.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls**](cmdqueryname=mpls) command to enable MPLS.
  3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  4. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enter the MPLS L2VPN view.
  5. Run the [**monitor-group**](cmdqueryname=monitor-group) *monitor-group-name* command to configure an L2VPN monitoring group.
  6. Run the [**monitor enable**](cmdqueryname=monitor+enable) command to enable the monitoring function for the L2VPN monitoring group.
  7. (Optional) Run the [**trigger unblock-delay**](cmdqueryname=trigger+unblock-delay) *max-delay-time* command to configure the maximum hold-off time for the L2VPN monitoring group to perform unblocking.
  8. Run the [**binding pw**](cmdqueryname=binding+pw) **ldp** **vsi** *vsi-name* **peer** *peer-ip* **pw-id** *pw-id* **encapsulation** { **vlan** | **ethernet** } command to bind the protocol VSI PWs to the L2VPN monitoring group.
  9. (Optional) Run the [**binding-pw-up trigger unblock-delay**](cmdqueryname=binding-pw-up+trigger+unblock-delay) *delay-time* command to configure the hold-off time for unblocking the service VSI PWs after the protocol VSI PWs bound to the L2VPN monitoring group go up.
  10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure service VSI PWs in LDP mode to track the L2VPN monitoring group.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the service VSI view.
  3. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to configure LDP as the PW signaling protocol and enter the VSI-LDP view.
  4. Run the [**peer**](cmdqueryname=peer) *peer-address* [ **negotiation-vc-id** *vc-id* ] **pw** *pw-name* command to configure a VSI peer.
  5. Run the [**track monitor-group**](cmdqueryname=track+monitor-group) *group-name* command to configure service VSI PWs to track the L2VPN monitoring group. This step must be performed on both SPEs.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure service VSI PWs in BGP AD mode to track the L2VPN monitoring group.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the service VSI view.
  3. Run the [**bgp-ad**](cmdqueryname=bgp-ad) command to set the PW establishment mode of the VSI to BGP AD and enter the VSI-BGP AD view.
  4. Run the [**peer**](cmdqueryname=peer) *peer-address* **pw** *pw-name* command to create a PW and enter its view.
  5. Run the [**track monitor-group**](cmdqueryname=track+monitor-group) *group-name* command to configure service VSI PWs to track the L2VPN monitoring group. This step must be performed on both SPEs.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.