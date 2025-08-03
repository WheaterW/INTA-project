Configuring MAC Duplication Suppression for EVPN
================================================

Configuring MAC Duplication Suppression for EVPN

#### Prerequisites

Before configuring MAC duplication suppression for EVPN, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

On the EVPN VXLAN shown in [Figure 1](#EN-US_TASK_0000001176664043__fig_dc_vrp_evpn_cfg_008901), the two PEs are interconnected through both network-side and access-side links. The network encounters both BUM traffic loops and MAC route flapping. To resolve these problems, a local PE uses the MAC duplication suppression function, which is enabled by default. With this function, the system checks the number of times a MAC entry flaps within a detection period. If the number exceeds the upper threshold, the PE considers the MAC route to have flapped. In this case, the PE suppresses the flapping MAC route, and no longer sends the route to the remote PE over the BGP EVPN peer relationship.

**Figure 1** MAC duplication suppression for EVPN  
![](figure/en-us_image_0000001176743985.png)

If the default parameter settings of the MAC duplication suppression function do not meet requirements, you can set the parameters as needed.

![](../public_sys-resources/note_3.0-en-us.png) 

If the parameters are set in both the EVPN MAC-duplication view and EVPN instance MAC-duplication view, the configuration in the EVPN instance MAC-duplication view takes priority.



#### Procedure

* Configure MAC duplication suppression for all EVPN instances.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the global EVPN configuration view.
     
     
     ```
     [evpn](cmdqueryname=evpn)
     ```
  3. Enter the EVPN MAC-duplication view.
     
     
     ```
     [mac-duplication](cmdqueryname=mac-duplication)
     ```
  4. Configure loop detection parameters for MAC duplication suppression, including the detection period and the threshold for the number of MAC entry flaps within a detection period.
     
     
     ```
     [detect loop-times](cmdqueryname=detect+loop-times) loop-times detect-cycle detect-cycle-time
     ```
     
     By default, the loop detection period for MAC duplication suppression is 180s, and the threshold for MAC entry flaps within a detection period is 5.
  5. Configure a hold-off time to unsuppress MAC routes.
     
     
     ```
     [retry-cycle](cmdqueryname=retry-cycle) retry-times
     ```
     
     By default, the hold-off time to unsuppress MAC duplication is 540s.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure MAC duplication suppression for a specified EVPN instance.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BD view.
     
     
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     ```
  3. Enter the BD-EVPN instance view.
     
     
     ```
     [evpn](cmdqueryname=evpn)
     ```
  4. Enter the BD-EVPN instance MAC-duplication view.
     
     
     ```
     [mac-duplication](cmdqueryname=mac-duplication)
     ```
  5. Configure loop detection parameters for MAC duplication suppression, including the detection period and the threshold for the number of MAC entry flaps within a detection period.
     
     
     ```
     [detect loop-times](cmdqueryname=detect+loop-times) loop-times detect-cycle detect-cycle-time
     ```
     
     By default, the loop detection period for MAC duplication suppression is 180s, and the threshold for MAC entry flaps within a detection period is 5.
  6. Configure a hold-off time to unsuppress MAC routes.
     
     
     ```
     [retry-cycle](cmdqueryname=retry-cycle) retry-times
     ```
     
     By default, the hold-off time to unsuppress MAC duplication is 540s.
  7. (Optional) Set flapping MAC routes to blackhole MAC routes.
     
     
     ```
     [black-hole-dup-mac](cmdqueryname=black-hole-dup-mac)
     ```
     
     By default, flapping MAC routes are not set to blackhole MAC routes. After this step, if the source or destination MAC address of the forwarded traffic is the same as the MAC address of a blackhole MAC route, the traffic is discarded.
  8. (Optional) Configure a whitelist to filter received MAC routes. MAC duplication suppression is not performed on MAC addresses that match a specified ACL rule.
     
     
     ```
     [filter-policy](cmdqueryname=filter-policy) { acl-number | acl-name acl-name-value }
     ```
     
     By default, the received MAC routes are not filtered against a whitelist. When MAC duplication suppression is configured, to prevent the specified MAC address from being affected, perform this step to add the specified MAC address to the whitelist using an ACL rule.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     Before performing this step, you need to configure the ACL rule.
     
     When the **rule** command is used to configure a filtering rule for a named ACL, only the source address range specified by **source** and time period specified by **time-range** take effect.
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) **name** *vpn-instance-name* **mac-duplication** [ **bridge-domain** *bd-id* ] [ **mac-address** *mac-address* ] command to check information about MAC duplication suppression, including the involved parameters related to MAC duplication suppression and information about the suppressed MAC routes.
* Run the [**display evpn mac-duplication**](cmdqueryname=display+evpn+mac-duplication) command to check information about MAC duplication suppression in all EVPN instances.
* Run the [**display evpn mac-duplication statistics**](cmdqueryname=display+evpn+mac-duplication+statistics) command to check statistics about MAC duplication suppression in all EVPN instances.
* Run the [**display evpn vpn-instance mac-duplication history**](cmdqueryname=display+evpn+vpn-instance+mac-duplication+history) command to check historical records of MAC duplication suppression.

#### Follow-up Procedure

If a MAC route or a BD's MAC route no longer flaps and you want to restore it immediately instead of waiting for the configured hold-off timer to expire, you can manually clear the suppression state of the MAC route.

```
[reset evpn vpn-instance mac-duplication](cmdqueryname=reset+evpn+vpn-instance+mac-duplication) [ bridge-domain bd-id ] [ mac-address mac-address ]
```
If MAC routes of all EVPN instances no longer flap and you want to restore them immediately instead of waiting for the configured hold-off timer to expire, you can manually clear the suppression state of the MAC routes.
```
[reset evpn mac-duplication](cmdqueryname=reset+evpn+mac-duplication)
```

A MAC route is automatically unsuppressed if a static MAC address is configured for the route, or if a MAC address carrying the static flag is received by the EVPN instance and the received MAC address is the same as that of the MAC route.