Setting the AS\_Path Attribute
==============================

The AS\_Path attribute is used to prevent routing loops and control route selection.

#### Procedure

* Set the AS\_Path attribute in the IPv6 address family view.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run the following commands to configure the AS\_Path attribute as required:
     
     
     + To enable the device to accept the routes that contain the local AS number if the number of repetitions in the route is within the configured limit, run the [**peer**](cmdqueryname=peer+allow-as-loop) { *ipv6-address* | *group-name* } **allow-as-loop** [ *number* ] command.
     + To prevent the AS\_Path attribute from being used for route selection, run the [**bestroute as-path-ignore**](cmdqueryname=bestroute+as-path-ignore) command.
     + To configure the AS\_Path attribute to carry only public network AS numbers, run the [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**public-as-only**](cmdqueryname=public-as-only+force+replace+include-peer-as+limited+replace) [ **force** [ **replace** ] [ **include-peer-as** ] | **limited** [ **replace** ] [ **include-peer-as** ] ] or [**peer**](cmdqueryname=peer+public-as-only+import+force) { *ipv6-address* | *group-name* } **public-as-only** **import** [ **force** ] command.
     
     The commands in Step 4 are optional and can be used in random order.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a fake AS number.
  
  
  
  Perform the following steps on a BGP4+ device:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+dual-as+prepend-global-as+prepend-local-as+prepend-fake-as) { *ipv6-address* | *group-name* } **fake-as** *fake-as-value* [ **dual-as** ] [ **prepend-global-as** ] [ **prepend-fake-as** ]
     
     
     
     A fake AS number is configured.
     
     
     
     This command hides the actual AS number. In this case, EBGP peers in other ASs can learn only this fake AS number of the local end and consider the fake AS number as the AS number of the local peer.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This command is applicable only to EBGP peers.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Substitute the AS numbers in the AS\_Path attribute.
  
  
  
  In a BGP/MPLS IP VPN scenario, if the ASs to which two VPN sites belong use private AS numbers, the AS numbers of the two VPN sites may be the same. If a CE in a VPN site sends a VPN route to the connected PE (EBGP peer) and this route is advertised to the remote PE and then to the remote CE, the remote CE will discard the route due to AS number repetition. As a result, different sites of the same VPN cannot communicate with each other. In this case, you need to run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the PE to enable AS number substitution. That is, the PE replaces the AS number of the VPN site where the CE resides in the received VPN route with the local AS number. This prevents the remote CE from discarding routes due to duplicate AS numbers.
  
  In a BGP public network scenario, when two devices with the same AS number learn a BGP route from each other through the same EBGP peer, the route may be discarded because the AS\_Path attribute contains duplicate AS numbers. To prevent this problem, run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the EBGP peer shared by the two devices to enable AS number substitution.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  Exercise caution when running the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command because improper use of the command may cause routing loops.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **substitute-as**
     
     
     
     The device is configured to replace the AS number in the AS\_Path attribute.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable BGP to check, or disable BGP from checking, the first AS number in the AS\_Path attribute of each Update message received from a specified EBGP peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv6 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } **check-first-as** { **enable** | **disable** }
     
     
     
     The device is enabled to check or disabled from checking the first AS number in the AS\_Path attribute contained in the update messages received from a specified EBGP peer or peer group.
     
     
     
     If the **peer check-first-as enable** command is run, the device checks whether the first AS number in the AS\_Path attribute contained in the update messages received from the specified EBGP peer or peer group is the number of the AS where the EBGP peer or peer group resides. If the two AS numbers are different, the local device discards the update messages. If the **peer check-first-as disable** command is run, the device accepts all update messages received from the specified EBGP peer or peer group, regardless whether the two AS numbers are the same. If the **undo peer check-first-as disable** command is run, the default configuration takes effect.
     
     The check function can be configured for a specified EBGP peer, peer group, or for BGP as a whole. If the function is not configured for a specified EBGP peer, the device checks whether the function is configured for the related peer group; if the function is not configured for the peer group, the device checks whether the function is configured in the BGP view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     After the configuration is complete, if you want to check the received routes again, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.