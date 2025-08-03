Setting the AS\_Path Attribute
==============================

Setting the AS\_Path Attribute

#### Prerequisites

Before setting the AS\_Path attribute, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

The AS\_Path attribute is used to prevent routing loops and control route selection.


#### Procedure

* Enable BGP to accept routes that contain the local AS number, as long as the number of repetitions in each route is within a configured limit.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Allow repetition of the local AS number.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [allow-as-loop](cmdqueryname=allow-as-loop) [ number ]
     ```
     
     Generally, BGP checks the AS\_Path attribute of each route received from a peer. If the local AS number is carried in a route, BGP ignores this route to prevent routing loops.
     
     However, you can use this command in some special applications to allow the AS\_Path attribute of a route received from a peer to contain the local AS number. You can also set a limit on the number of repetitions for the local AS number.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable BGP from comparing AS\_Path attributes during route selection.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Disable BGP from comparing AS\_Path attributes during route selection.
     
     
     ```
     [bestroute as-path-ignore](cmdqueryname=bestroute+as-path-ignore)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the AS\_Path attribute to carry only the public AS number.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Configure the AS\_Path attribute to carry only the public AS number.
     
     
     ```
     [peer](cmdqueryname=peer) { ipv4-address | group-name | peerIpv6Addr } [public-as-only](cmdqueryname=public-as-only+force+replace+include-peer-as+limited+replace) [ force [ replace ] [ include-peer-as ] | limited [ replace ] [ include-peer-as ] ]
     ```
     
     Generally, AS numbers range from 1 to 4294967295, including public AS numbers, private AS numbers, and reserved AS numbers. Private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294 (or from 64086.59904 to 65535.65534). The AS numbers 65535 and 4294967295 are reserved for special applications. Other AS numbers are public AS numbers.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If the 4-byte private AS number capability is disabled using the [**private-4-byte-as disable**](cmdqueryname=private-4-byte-as+disable) command, private AS numbers range from 64512 to 65534; the AS number 65535 is reserved, and others are public AS numbers.
     
     Public AS numbers can be used on the Internet, and are assigned and managed by the Internet Assigned Number Authority (IANA). Private AS numbers cannot be advertised to the Internet, and are used only within ASs.
     
     Generally, BGP routes to be advertised to peers carry either public or private AS numbers, or both. In certain cases, private AS numbers in BGP routes do not need to be advertised. To ensure this, run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**public-as-only**](cmdqueryname=public-as-only) [ **force** [ **replace** ] [ **include-peer-as** ] | **limited** [ **replace** ] [ **include-peer-as** ] ] command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Set the maximum quantity of AS numbers allowed in the AS\_Path attribute.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Set the maximum quantity of AS numbers allowed in the AS\_Path attribute.
     
     
     ```
     [as-path-limit](cmdqueryname=as-path-limit) limit
     ```
     
     By default, a maximum of 255 AS numbers are allowed in the AS\_Path attribute.
     
     After the [**as-path-limit**](cmdqueryname=as-path-limit) command is run, the device checks whether the quantity of AS numbers in the AS\_Path attribute of each received route exceeds the maximum value, and discards the route if this is the case. As such, if the maximum value is set too low, routes may be discarded.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Disable BGP from checking the first AS number in the AS\_Path attribute of each Update message received from an EBGP peer.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Disable BGP from checking the first AS number in the AS\_Path attribute of each Update message received from an EBGP peer.
     
     
     ```
     [undo check-first-as](cmdqueryname=undo+check-first-as)
     ```
     
     By default, BGP checks whether the first AS number in the AS\_Path attribute of an Update message received from an EBGP peer is the same as the number of the AS where the EBGP peer resides. If they are different, the Update message is rejected.
     
     ![](public_sys-resources/notice_3.0-en-us.png) 
     
     Exercise caution when running the [**undo check-first-as**](cmdqueryname=undo+check-first-as) command, as use of this command may result in routing loops.
     
     After a configuration change, to allow the new configuration to take effect on the routes that have been received on the local device, run the [**refresh bgp**](cmdqueryname=refresh+bgp) command.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable BGP to check, or disable BGP from checking, the first AS number in the AS\_Path attribute of each Update message received from a specified EBGP peer or peer group.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enable BGP to check, or disable BGP from checking, the first AS number in the AS\_Path attribute of each Update message received from a specified EBGP peer or peer group.
     
     
     ```
     [peer](cmdqueryname=peer+check-first-as+enable+disable) { group-name | ipv4-address } check-first-as { enable | disable }
     ```
     
     If the [**peer check-first-as enable**](cmdqueryname=peer+check-first-as) command is run, BGP checks whether the first AS number in the AS\_Path attribute of each Update message received from the specified EBGP peer or peer group is the same as the number of the AS where the EBGP peer or peer group resides. The two AS numbers must be the same. If the AS numbers are not the same, BGP rejects the Update message. After the [**peer check-first-as disable**](cmdqueryname=peer+check-first-as+disable) command is run, BGP no longer checks the first AS number in the AS\_Path attribute of each Update message received from the specified EBGP peer or peer group. Even if the first AS number differs from the number of the AS where the specified EBGP peer or peer group resides, BGP still accepts the Update message. If the [**undo peer**](cmdqueryname=undo+peer) { *group-name* | *ipv4-address* } **check-first-as** { **enable** | **disable** } command is run, the related configuration for the specified EBGP peer or peer group will be deleted, and the default configuration will be used.
     
     The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.
     
     After the configuration is modified, you can run the [**refresh bgp**](cmdqueryname=refresh+bgp) command to allow the new configuration to take effect immediately.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```