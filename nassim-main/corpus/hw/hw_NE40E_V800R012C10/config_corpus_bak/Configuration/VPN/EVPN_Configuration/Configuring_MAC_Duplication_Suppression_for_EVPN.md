Configuring MAC Duplication Suppression for EVPN
================================================

If PEs communicate through both network-side and access-side links in an EVPN scenario, MAC routes may flap. To resolve this issue, configure MAC duplication suppression.

#### Usage Scenario

On the EVPN E-LAN shown in [Figure 1](#EN-US_TASK_0172370511__fig42411312194317), the two PEs may be interconnected through both network-side and access-side links. If this is the case, a BUM traffic loop and MAC route flapping both occur, preventing devices from working properly. By default, MAC duplication suppression is enabled on a device. Also by default, the system checks the number of times a MAC entry flaps within a detection period. If the number of MAC flaps exceeds the upper threshold, the system considers MAC route flapping to be occurring on the network and consequently suppresses the flapping MAC routes. The suppressed MAC routes cannot be sent to a remote PE through a BGP EVPN peer relationship.

**Figure 1** MAC duplication suppression for a VPN  
![](figure/en-us_image_0000001193700090.png)

By default, EVPN MAC duplication suppression is enabled. In the scenario shown in the [figure](#EN-US_TASK_0172370511__fig18835536205217), you need to disable EVPN MAC duplication suppression on SLeaf nodes.

**Figure 2** MAC duplication suppression for a VPN  
![](figure/en-us_image_0000001281726621.png)

If you want to modify parameter configurations related to MAC duplication suppression, perform the following procedure.


#### Pre-configuration Tasks

Before configuring MAC duplication suppression for EVPN, complete the following tasks:

* Deploy [EVPN VPLS over IS-IS SRv6 BE](dc_vrp_srv6_cfg_all_0023_copy.html), [BD EVPN functions](dc_vrp_evpn_cfg_0065.html), [basic EVPN functions](dc_vrp_evpn_cfg_0003.html), or [EVPN VPLS over SRv6 TE Policy](dc_vrp_cfg_evpn-vpls_over_srv6-te_policy_copy.html) on the network.

#### Procedure

* Configure MAC duplication suppression for all EVPN instances.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**evpn**](cmdqueryname=evpn)
     
     
     
     The EVPN global configuration view is displayed.
  3. Run [**mac-duplication**](cmdqueryname=mac-duplication)
     
     
     
     The EVPN-mac-dup view is displayed.
  4. Run [**detect loop-times**](cmdqueryname=detect+loop-times) *loop-times* **detect-cycle** *detect-cycle-time*
     
     
     
     Loop detection parameters for MAC duplication suppression are configured, including the detection period and the threshold for the number of MAC entry flaps within a detection period. The default detection period is 180s, and the default threshold is 5.
  5. Run [**retry-cycle**](cmdqueryname=retry-cycle) *retry-times*
     
     
     
     A timer for stopping MAC duplication suppression is configured.
  6. (Optional) Perform the following steps to disable MAC duplication suppression globally (as shown in [Figure2 MAC duplication ...](#EN-US_TASK_0172370511__fig18835536205217)):
     
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the EVPN global configuration view.
     2. Run [**undo mac-duplication**](cmdqueryname=undo+mac-duplication)
        
        MAC duplication suppression is disabled globally.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure MAC duplication suppression for a specified EVPN instance.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run either of the following commands to enter the EVPN instance view or BD EVPN instance view:
     
     
     + [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
     + [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
  3. Run [**mac-duplication**](cmdqueryname=mac-duplication)
     
     
     
     The EVPN-MAC-dup view is displayed.
  4. Run [**detect loop-times**](cmdqueryname=detect+loop-times) *loop-times* **detect-cycle** *detect-cycle-time*
     
     
     
     Loop detection parameters for MAC duplication suppression are configured, including the detection period and the threshold for the number of MAC entry flaps within a detection period.
  5. Run [**retry-cycle**](cmdqueryname=retry-cycle) *retry-times*
     
     
     
     A timer for stopping MAC duplication suppression is configured.
  6. Run [**black-hole-dup-mac**](cmdqueryname=black-hole-dup-mac) [ **block-source-interface** ]
     
     
     
     The flapping MAC routes are set to blackhole MAC routes. If the source or destination MAC address of the forwarded traffic is the same as the MAC address of the blackhole MAC route, the traffic is discarded.
     
     
     
     The **block-source-interface** parameter enables AC interface blocking. This means that, if the traffic comes from a local AC interface and the source MAC address of the traffic is the same as the MAC address of a blackhole MAC route, the AC interface is blocked. In this way, a loop can be removed quickly. Only BD EVPN instances support AC interface blocking.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Only BD EVPN instances support AC interface blocking.
     
     To enable AC interface blocking, first [enable MAC flapping loop detection](dc_vrp_mflp_cfg_0400.html) in the BD.
  7. (Optional) Run [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name-value* }
     
     
     
     The device is configured to filter received MAC routes. MAC duplication suppression is not performed on MAC addresses that match a specified ACL rule.
     
     
     
     If MAC duplication suppression is configured, to prevent the specified MAC address from being affected, perform this step to add the specified MAC address to the whitelist using an ACL rule.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before performing this step, configure the ACL rule first.
     
     If the **rule** command is used to configure a filtering rule for a named ACL, only the source address range specified by **source** and time period specified by **time-range** take effect.
  8. (Optional) To disable MAC duplication suppression for the current EVPN instance (as shown in [Figure 2](#EN-US_TASK_0172370511__fig18835536205217)), perform the following steps:
     
     
     1. Run the [**quit**](cmdqueryname=quit) command to return to the EVPN instance or BD EVPN instance view.
     2. Run the [**mac-duplication disable**](cmdqueryname=mac-duplication+disable) command to disable MAC duplication suppression for the current EVPN instance.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

When a MAC route to a specific MAC address or MAC routes in a specific BD have stopped flapping and you want to restore them before the configured hold-off timer expires, run the [**reset evpn vpn-instance**](cmdqueryname=reset+evpn+vpn-instance) *vpn-instance-name* **mac-duplication** [ **bridge-domain** *bd-id* ] [ **mac-address** *mac-address* ] command in the user view. This allows you to manually clear the suppression state of the MAC routes.

Under certain conditions, a MAC route is unsuppressed automatically. For this to take place, a static MAC address must be configured or an EVPN instance must receive a MAC address that carries the static flag. The MAC address must be the same as that of the suppressed MAC route.

#### Verifying the Configuration

* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) **name** *vpn-instance-name* **mac-duplication** [ **bridge-domain** *bd-id* ] [ **mac-address** *mac-address* ] command to check information about MAC duplication suppression, including the involved parameters and information about the suppressed MAC routes.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) **name** *vpn-instance-name* **mac-duplication** [**history**](cmdqueryname=history) command to check the historical records of MAC route duplication.