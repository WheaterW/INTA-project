Setting the AS\_Path Attribute
==============================

The AS\_Path attribute is used to prevent routing loops and control route selection.

#### Procedure

* Enable a BGP device to accept the routes that contain the local AS number if the number of repetitions in each route is within a configured limit.
  
  
  
  Generally, BGP uses AS numbers to detect routing loops. In the Hub and Spoke networking, if EBGP runs between a Hub-PE and a Hub-CE at a Hub site, a route sent from the Hub-PE to the Hub-CE carries the AS number of the Hub-PE. If the Hub-CE sends an Update message that contains the AS number of the Hub-PE to the Hub-PE, the Hub-PE will deny it.
  
  To ensure proper route transmission in the Hub and Spoke networking, configure all the BGP peers on the path, along which the Hub-CE advertises VPN routes to the Spoke-CE, to allow the routes with the local AS number repeated once in the AS\_Path attribute to pass through.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+allow-as-loop) { *ipv4-address* | *group-name* } [**allow-as-loop**](cmdqueryname=peer+allow-as-loop) [ *number* ]
     
     
     
     Repetitions of the local AS number are allowed.
     
     
     
     In most cases, a BGP device checks the AS\_Path attribute of a route received from a peer. If the AS\_Path carries the local AS number, the BGP device discards this route to avoid routing loops.
     
     In some special applications, you can use this command to allow the AS\_Path attribute of a route received from a peer to contain the local AS number and set the allowed repetition count of the local AS number.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable the device from comparing AS\_Path attributes during route selection.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**bestroute as-path-ignore**](cmdqueryname=bestroute+as-path-ignore)
     
     
     
     The local device is disabled from comparing AS\_Path attributes during route selection.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a fake AS number.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+fake-as) { *ipv4-address* | *group-name* } [**fake-as**](cmdqueryname=peer+fake-as) *fake-as-value* [ **dual-as** ] [ **prepend-global-as** ] [ **prepend-fake-as** ]
     
     
     
     A fake AS number is configured.
     
     
     
     This command hides the actual AS number. In this case, EBGP peers in other ASs can learn only this fake AS number of the local end and set the fake AS number as the AS number of the local peer when establishing peer relationships with the local end.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**peer fake-as**](cmdqueryname=peer+fake-as) command is applicable only to EBGP peers.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Substitute the AS numbers in the AS\_Path attribute.
  
  
  
  In a BGP/MPLS IP VPN scenario, if the ASs to which two VPN sites belong use private AS numbers, the AS numbers of the two VPN sites may be the same. If a CE in a VPN site sends a VPN route to the connected PE (EBGP peer) and this route is advertised to the remote PE and then to the remote CE, the remote CE will discard the route due to AS number repetition. As a result, different sites of the same VPN cannot communicate with each other. In this case, you need to run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the PE to enable AS number substitution. That is, the PE replaces the AS number of the VPN site where the CE resides in the received VPN route with the local AS number. This prevents the remote CE from discarding routes due to AS number repetition.
  
  In a BGP public network scenario, when two devices with the same AS number learn a BGP route from each other through the same EBGP peer, the route may be discarded because the AS\_Path attribute contains duplicate AS numbers. To prevent this problem, run the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command on the EBGP peer shared by the two devices to enable AS number substitution.
  
  ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
  
  Exercise caution when running the [**peer substitute-as**](cmdqueryname=peer+substitute-as) command because improper use of the command may cause routing loops.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+substitute-as) { *ipv4-address* | *group-name* } [**substitute-as**](cmdqueryname=peer+substitute-as)
     
     
     
     AS number substitution is enabled on the device.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the AS\_Path attribute to carry only public AS numbers.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+public-as-only) { *ipv4-address* | *group-name* } [**public-as-only**](cmdqueryname=peer+public-as-only) [ **force** [ **replace** ] [ **include-peer-as** ] | **limited** [ **replace** ] [ **include-peer-as** ] ]
     
     
     
     The AS\_Path attribute in the BGP Update messages to be sent is configured to carry only public AS numbers. You can also run the [**peer**](cmdqueryname=peer+public-as-only) { *ipv4-address* | *group-name* } [**public-as-only**](cmdqueryname=peer+public-as-only) **import** [ **force** ] command to configure the AS\_Path attribute not to carry private AS numbers in accepted BGP Update messages.
     
     
     
     Generally, AS numbers range from 1 to 4294967295, including public AS numbers, private AS numbers, and reserved AS numbers. Private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294 (or from 64086.59904 to 65535.65534). The AS numbers 65535 and 4294967295 are reserved for special applications. Other AS numbers are public AS numbers.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the 4-byte private AS number capability is disabled using the [**private-4-byte-as disable**](cmdqueryname=private-4-byte-as+disable) command, private AS numbers range from 64512 to 65534; the AS number 65535 is reserved, and others are public AS numbers.
     
     Public AS numbers can be used on the Internet, and are assigned and managed by the Internet Assigned Number Authority (IANA). Private AS numbers cannot be advertised to the Internet, and are used only within ASs.
     
     Generally, BGP routes to be advertised to peers carry either public or private AS numbers, or both. In certain cases, private AS numbers do not need to be advertised. In this case, you can run this command to configure the AS\_Path attribute to carry only public AS numbers.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the maximum number of AS numbers in the AS\_Path attribute.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**as-path-limit**](cmdqueryname=as-path-limit) *limit*
     
     
     
     The maximum number of AS numbers allowed in the AS\_Path attribute is set.
     
     After the [**as-path-limit**](cmdqueryname=as-path-limit) command is run, a device checks whether the number of AS numbers in the AS\_Path attribute of a received route exceeds the maximum value. If the number of AS numbers exceeds the maximum value, the device discards the route. Therefore, if the maximum number of AS numbers allowed in the AS\_Path attribute is set to an excessively small value, routes may be easily discarded.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable the BGP device from checking the first AS number contained in the AS\_Path attribute of each Update message received from an EBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**undo check-first-as**](cmdqueryname=undo+check-first-as)
     
     
     
     The BGP device is disabled from checking the first AS number in the AS\_Path attribute that is carried in each Update message received from an EBGP peer.
     
     
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     Exercise caution when running the [**undo check-first-as**](cmdqueryname=undo+check-first-as) command because use of this command may cause routing loops.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     After the check function is enabled, to enable the device to recheck received routes, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.
* Enable BGP to check, or disable BGP from checking, the first AS number in the AS\_Path attribute of each Update message received from a specified EBGP peer or peer group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+check-first-as) { *group-name* | *ipv4-address* } [**check-first-as**](cmdqueryname=peer+check-first-as) { **enable** | **disable** }
     
     
     
     The device is enabled to check or disabled from checking the first AS number in the AS\_Path attribute contained in each Update message received from a specified EBGP peer or peer group.
     
     
     
     If the [**peer check-first-as enable**](cmdqueryname=peer+check-first-as) command is run, BGP checks whether the first AS number in the AS\_Path attribute of each Update message received from the specified EBGP peer or peer group is the same as the number of the AS where the EBGP peer or peer group resides. The two AS numbers must be the same. If the AS numbers are different, the Update message is rejected. If the [**peer check-first-as disable**](cmdqueryname=peer+check-first-as) command is run, BGP accepts Update messages received from the specified EBGP peer or peer group, regardless of whether the first AS number in the AS\_Path attribute of the messages is the same as the number of the AS where the EBGP peer or peer group resides. If the undo command is run, the related configuration for the specified EBGP peer or peer group is deleted, and the default configuration is used.
     
     The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     After the check function is enabled, to enable the device to recheck received routes, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.