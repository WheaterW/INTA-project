Configuring NS Multicast Suppression on an EVPN MPLS Network
============================================================

When a user accesses an EVPN MPLS network through a BD, NS multicast suppression can be configured to reduce or suppress excess NS messages.

#### Usage Scenario

When a user is connected to an EVPN MPLS network through a BD, IPv6 host neighbors are discovered in NS multicast mode. When a device receives an NS message for IPv6 address resolution, the device forwards the NS message in multicast mode in its BD. If a large number of NS messages are received within a specified period, forwarding all these NS messages on the EVPN occupies excessive network resources, which affects service running.

On the network shown in [Figure 1](#EN-US_TASK_0172365175__fig_dc_vrp_evpn_cfg_000301), NS multicast suppression can be configured on a PE. When receiving an NS message, the PE checks whether it can obtain the destination user information in the NS message. If so, it performs proxy ND or multicast-to-unicast processing to reduce or suppress NS message flooding.

NS multicast suppression can also prevent ND spoofing attacks. An ND spoofing attack means that an attacker associates its MAC address with the IPv6 address of a host so that any traffic destined for the IPv6 address can be sent to the attacker. With NS multicast suppression enabled, if such an attack is launched, the proxy ND table conflict detection mechanism triggers an IPv6 address conflict alarm, reminding users of the potential ND spoofing attack.

**Figure 1** NS multicast suppression  
![](images/fig_dc_vrp_evpn_cfg_000304.png)  


#### Pre-configuration Tasks

Before configuring NS multicast suppression, complete the following tasks:

* [Configure BD-based EVPN functions.](dc_vrp_evpn_cfg_0065.html)

#### Procedure

1. Enable NS multicast suppression.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   3. Run the [**ipv6 nd multicast-suppress**](cmdqueryname=ipv6+nd+multicast-suppress) { **proxy-reply** [ **unknown-options-unicast** ] | **unicast-forward** } [ **mismatch-discard** ] **enable** command to enable NS multicast suppression.
   4. (Optional) Run the [**ipv6 nd multicast-suppress**](cmdqueryname=ipv6+nd+multicast-suppress) { **host** | **router** } command to configure the R flag for NA messages when proxy ND is performed.
   5. (Optional) Run the [**ipv6 nd multicast-suppress dynamic limit**](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+limit) *limit-value* command to configure the maximum number of dynamic proxy ND entries that can be learned in the BD.
   6. (Optional) Run the [**ipv6 nd multicast-suppress dynamic expire-time**](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+expire-time) *expire-time-value* command to configure an aging time for dynamic proxy ND entries.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   8. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
2. Enable the function to flood ND entries or proxy ND entries through EVPN routes.
   
   
   
   Perform the following operations on a Layer 2 device:
   
   1. Run the [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id* command to enter the BD view.
   2. Run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command to enable the device to flood proxy ND entries through EVPN routes.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   4. Run the [**quit**](cmdqueryname=quit) command to exit the BD view.
   
   Perform the following operations on a Layer 3 device:
   
   1. Run the [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id* command to create a VBDIF interface and enter its view.
   2. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the interface.
   3. Run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command to enable the device to flood ND entries through EVPN routes.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Run the [**quit**](cmdqueryname=quit) command to exit the VBDIF interface view.
3. Configure BGP EVPN to advertise routes.
   
   
   1. Run the [**bgp**](cmdqueryname=bgp) *as-number* [ **instance** *instance-name* ] command to enter the BGP view or BGP multi-instance view.
   2. Run the [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn) command to enter the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
   3. Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise** **nd** command to enable the device to advertise ND routes.
   4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   5. Run the [**quit**](cmdqueryname=quit) command to exit the BGP-EVPN address family view or BGP multi-instance EVPN address family view.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the BGP view or BGP multi-instance view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised not to use weak security algorithms in the BGP feature. If you need to use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function first.
4. (Optional) Configure performance limiting for ND message processing.
   
   
   1. Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { **rs** | **ra** | **ns** | **na** } **anti-attack** **rate-limit** *limit-number* command to configure a rate limit for sending ND messages to the CPU, that is, the number of ND messages that can be processed per second.
   2. Run the [**ipv6 nd miss anti-attack rate-limit**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) *limit-number* command to configure a rate limit for sending ND Miss messages to the CPU, that is, the number of ND Miss messages that can be processed per second.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

* Run the [**display ipv6 nd multicast-suppress bridge-domain**](cmdqueryname=display+ipv6+nd+multicast-suppress+bridge-domain) [ *bd-id* ] [ **verbose** ] command to check information about proxy ND tables in BDs. If the *bd-id* parameter is not specified, information about proxy ND tables in all BDs is displayed.
* Run the [**display ipv6 nd packet statistics bridge-domain**](cmdqueryname=display+ipv6+nd+packet+statistics+bridge-domain) [ *bd-id* ] command to check ND message statistics in BDs. If the *bd-id* parameter is not specified, statistics about ND messages in all BDs are displayed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In the user view, run the [**reset ipv6 nd multicast-suppress dynamic bridge-domain**](cmdqueryname=reset+ipv6+nd+multicast-suppress+dynamic+bridge-domain) [ *bd-id* ] command to clear dynamic proxy ND entries in BDs. If the *bd-id* parameter is not specified, dynamic proxy ND entries in all BDs are cleared.
  
  In the user view, run the [**reset ipv6 nd packet statistics bridge-domain**](cmdqueryname=reset+ipv6+nd+packet+statistics+bridge-domain) [ *bd-id* ] command to clear ND message statistics in BDs. If the *bd-id* parameter is not specified, ND message statistics in all BDs are cleared.