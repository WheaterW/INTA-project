Configuring EVPN MAC Redirection
================================

To solve the problem that traffic received on the network side takes a detour in special scenarios, configure EVPN MAC redirection.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0000001553074961__fig17853203404315), CE1, CE2, PE1, PE2, and PE3 form an EVPN VPLS dual-homing network. CE1 is dual-homed to PE1 and PE2.

Upon receipt of traffic sent from CE2 to CE1, PE3 load-balances the traffic between PE1 and PE2. Because PE2 does not have CE1's MAC1, it forwards the traffic destined for CE1 to PE1 first. If you want PE2 to directly forward traffic to CE1, configure MAC redirection on the PE.

**Figure 1** EVPN VPLS networking  
![](figure/en-us_image_0000001504992434.png)

#### Pre-configuration Tasks

Before configuring EVPN MAC redirection, complete one of the following tasks:

* [Configure EVPN VPLS over MPLS (BD EVPN instance)](dc_vrp_evpn_cfg_0065.html).
* [Configure EVPN VPLS over SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html).
* [Configure EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html).

#### Procedure

* Configure MAC redirection for a single EVPN instance:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the BD EVPN instance view.
  3. Run the [**mac-redirect-compatible**](cmdqueryname=mac-redirect-compatible) **enable** command to enable MAC redirection for the EVPN instance.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure MAC redirection globally:
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**evpn**](cmdqueryname=evpn) command to enter the global EVPN configuration view.
  3. Run the [**mac-redirect-compatible**](cmdqueryname=mac-redirect-compatible) **enable** command to enable MAC redirection globally.
  4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  By default, an EVPN instance inherits the MAC redirection configuration in the global EVPN configuration view. If MAC redirection has been configured in the view of the EVPN instance, this configuration takes precedence over that in the global EVPN configuration view.

#### Verifying the Configuration

After the configuration is complete, perform the following operations to verify it.

* Run the [**display bgp evpn all routing-table mac-route**](cmdqueryname=display+bgp+evpn+routing-table) *prefix* command on PEs to check whether the Redirect Out-Interface field of the received MAC route contains information about the redirected AC interface. *prefix* is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X]. For example, *prefix* can be 0:48:0001-0001-0001:0:0.0.0.0.