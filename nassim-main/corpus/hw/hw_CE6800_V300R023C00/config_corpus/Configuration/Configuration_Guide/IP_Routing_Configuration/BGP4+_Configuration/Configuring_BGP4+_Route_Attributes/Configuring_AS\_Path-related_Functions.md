Configuring AS\_Path-related Functions
======================================

Configuring AS\_Path-related Functions

#### Context

The AS\_Path attribute is used to prevent routing loops and control route selection.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Configure AS\_Path-related functions in the BGP view. For details, see [Table 1](#EN-US_TASK_0000001176741869__table243015269237).
   
   
   
   **Table 1** Configuring AS\_Path-related functions in the BGP view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Set the maximum quantity of AS numbers allowed in the AS\_Path attribute. | [**as-path-limit**](cmdqueryname=as-path-limit) *limit* | By default, a maximum of 255 AS numbers are allowed in the AS\_Path attribute.  After the [**as-path-limit**](cmdqueryname=as-path-limit) command is run, the device checks whether the quantity of AS numbers in the AS\_Path attribute of each received route exceeds the maximum value, and discards the route if this is the case. As such, if the maximum value is set too low, routes may be discarded. |
   | Disable the device from checking the first AS number in the AS\_Path attribute of each Update message received from an EBGP peer. | [**undo check-first-as**](cmdqueryname=undo+check-first-as) | By default, BGP4+ checks whether the first AS number in the AS\_Path attribute of an Update message received from an EBGP peer is the same as the number of the AS where the EBGP peer resides. If they are different, the Update message is rejected.  NOTICE:  Exercise caution when running the [**undo check-first-as**](cmdqueryname=undo+check-first-as) command, as use of this command may result in routing loops.  After the configuration is modified, you can run the [**refresh bgp ipv6**](cmdqueryname=refresh+bgp+ipv6) command for the new configuration to take effect immediately. |
   | Enable BGP4+ to check, or disable BGP4+ from checking, the first AS number in the AS\_Path attribute of each Update message received from a specified EBGP peer or peer group. | [**peer**](cmdqueryname=peer+check-first-as+enable+disable) { *group-name* | *ipv6-address* } **check-first-as** { **enable** | **disable** } | If the [**peer check-first-as enable**](cmdqueryname=peer+check-first-as) command is run, BGP4+ checks whether the first AS number in the AS\_Path attribute of each Update message received from the specified EBGP peer or peer group is the same as the number of the AS where the EBGP peer or peer group resides. The two AS numbers must be the same. If the AS numbers are different, the Update message is rejected. If the [**peer check-first-as disable**](cmdqueryname=peer+check-first-as+disable) command is run, BGP4+ accepts Update messages received from the specified EBGP peer or peer group, regardless of whether the two AS numbers are the same. If the undo command is run, the related configuration for the specified EBGP peer or peer group is deleted, and the default configuration is used.  The check on the first AS number in the AS\_Path attribute of each received Update message can be configured for a specified EBGP peer, the peer group that the EBGP peer belongs to, or the entire BGP process. The configuration takes effect in descending order of priority as follows: EBGP peer > peer group > entire BGP process.  After the configuration is modified, you can run the [**refresh bgp ipv6**](cmdqueryname=refresh+bgp+ipv6) command for the new configuration to take effect immediately. |
4. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
5. Configure AS\_Path-related functions. For details, see [Table 2](#EN-US_TASK_0000001176741869__table208316358116).
   
   
   
   **Table 2** Configuring AS\_Path-related functions in the BGP-IPv6 unicast address family view
   | Operation | Command | Description |
   | --- | --- | --- |
   | Allow repetition of the local AS number. | [**peer**](cmdqueryname=peer+allow-as-loop) { *ipv6-address* | *group-name* | *ipv4-address* } **allow-as-loop** [ *number* ] | Generally, BGP4+ checks the AS\_Path attribute of each route received from a peer. If the local AS number is carried in a route, BGP4+ discards this route to prevent routing loops.  However, you can use this command in some special applications to allow the AS\_Path attribute of a route received from a peer to contain the local AS number. You can also set a limit on the number of repetitions for the local AS number. |
   | Disable the device from comparing AS\_Path attributes during route selection. | [**bestroute as-path-ignore**](cmdqueryname=bestroute+as-path-ignore) | - |
   | Configure the AS\_Path attribute to carry only public AS numbers in the BGP Update messages to be sent. | [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* | *ipv4-address* } [**public-as-only**](cmdqueryname=public-as-only+force+replace+include-peer-as+limited+replace) [ **force** [ **replace** ] [ **include-peer-as** ] | **limited** [ **replace** ] [ **include-peer-as** ] ] | Generally, AS numbers range from 1 to 4294967295, including public AS numbers, private AS numbers, and reserved AS numbers. Private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294. The AS numbers 65535 and 4294967295 are reserved for special applications. Other AS numbers are public AS numbers.  NOTE:  If the 4-byte private AS number capability is disabled using the [**private-4-byte-as disable**](cmdqueryname=private-4-byte-as+disable) command, private AS numbers range from 64512 to 65534; the AS number 65535 is reserved, and others are public AS numbers.  Public AS numbers can be used on the Internet, and are assigned and managed by the Internet Assigned Number Authority (IANA). Private AS numbers cannot be advertised to the Internet, and are used only within ASs.  Generally, BGP4+ routes to be advertised to peers carry either public or private AS numbers, or both. In certain cases, private AS numbers do not need to be advertised. To ensure this, run this command. |
   | Configure the device to accept the BGP Update messages in which the AS\_Path attribute carries only public AS numbers. | [**peer**](cmdqueryname=peer+public-as-only+import+force) { *peerIpv6Addr* | *peerGroupName* | *peerIpv4Addr* } **public-as-only** **import** [ **force** ] | - |
   | Substitute the AS numbers in the AS\_Path attribute. | **peer** { *ipv4-address* | *ipv6-address* | *group-name* } **substitute-as** | - |
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```