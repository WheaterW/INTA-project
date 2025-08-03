Configuring ICMPv6 Message Control
==================================

In ICMPv6 message control, the token bucket algorithm is adopted, and one token represents one ICMPv6 message. Tokens are placed in the virtual bucket at fixed intervals until the capacity of the token bucket reaches the upper threshold. If the number of ICMPv6 messages exceeds the upper threshold, extra messages are discarded.

#### Pre-configuration Tasks

Before configuring ICMPv6 message control, complete the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Configure IPv6 addresses for interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 icmp-error**](cmdqueryname=ipv6+icmp-error+bucket+ratelimit) { **bucket** *bucket-size* | **ratelimit** *interval* } \*
   
   
   
   The ICMPv6 error message transmission interval is set.
3. (Optional) Run [**undo ipv6 icmp**](cmdqueryname=undo+ipv6+icmp+all-famous+send) { *icmpv6-type* *icmpv6-code* | *icmpv6-name* | **all-famous** } **send**
   
   
   
   The system is disabled from sending ICMPv6 messages.
4. (Optional) Run [**undo ipv6 icmp**](cmdqueryname=undo+ipv6+icmp+all-famous+receive) { *icmpv6-type* *icmpv6-code* | *icmpv6-name* | **all-famous** } **receive**
   
   
   
   The system is disabled from accepting ICMPv6 messages.
5. (Optional) Run [**undo ipv6 icmp too-big-rate-limit**](cmdqueryname=undo+ipv6+icmp+too-big-rate-limit)
   
   
   
   The device is disabled from suppressing ICMPv6 Packet Too Big messages.
6. (Optional) Run [**ipv6 icmp multicast-address echo receive disable**](cmdqueryname=ipv6+icmp+multicast-address+echo+receive+disable)
   
   
   
   The device is disabled from responding to received ICMPv6 multicast Echo messages.
7. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
8. (Optional) Run [**undo ipv6 icmp hop-limit-exceeded send**](cmdqueryname=undo+ipv6+icmp+hop-limit-exceeded+send)
   
   
   
   An interface is disabled from sending ICMPv6 Hop Limit Exceeded messages.
9. (Optional) Run [**undo ipv6 icmp host-unreachable send**](cmdqueryname=undo+ipv6+icmp+host-unreachable+send)
   
   
   
   An interface is disabled from sending ICMPv6 Host Unreachable messages.
10. (Optional) Run [**undo ipv6 icmp port-unreachable send**](cmdqueryname=undo+ipv6+icmp+port-unreachable+send)
    
    
    
    An interface is disabled from sending ICMPv6 Port Unreachable messages.
11. (Optional) Run [**ipv6 icmp multicast-address echo receive disable**](cmdqueryname=ipv6+icmp+multicast-address+echo+receive+disable)
    
    
    
    The device is disabled from responding to received ICMPv6 multicast Echo messages.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration of ICMPv6 Message Control

After configuring ICMPv6 message control, verify the configuration.

* Run the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface+brief) [ *interface-type* *interface-number* | **brief** ] command to check IPv6 configurations on an interface.
* Run the [**display icmpv6 statistics**](cmdqueryname=display+icmpv6+statistics) [ **interface** *interface-type* *interface-number* ] command to check statistics about ICMPv6 traffic on an interface.