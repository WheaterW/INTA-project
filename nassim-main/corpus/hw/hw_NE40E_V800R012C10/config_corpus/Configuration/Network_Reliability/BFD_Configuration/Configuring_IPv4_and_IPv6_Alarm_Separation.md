Configuring IPv4 and IPv6 Alarm Separation
==========================================

After IPv4 and IPv6 alarms are separated, IPv4 and IPv6 alarms are reported using different trap messages.

#### Usage Scenario

By default, the BFD IPv4 and IPv6 sessions use the same trap messages to report alarms. If both BFD IPv4 and IPv6 sessions exist on a link and the traffic is heavy, trap suppression is triggered. When the session link status changes, only the IPv4 or IPv6 trap messages are reported. As a result, alarms are lost.

To solve this problem, configure IPv4 and IPv6 alarms separation. Trap messages of the BFD IPv6 session are added. When the link status of the BFD IPv6 session changes, the new trap messages are used to report alarms. The BFD IPv4 session uses the original trap messages for reporting alarms. In this manner, alarms for the BFD IPv4 and IPv6 sessions are separated, preventing alarms from being lost during traffic suppression.


#### Pre-configuration Tasks

Before configuring BFD authentication information, complete the following tasks:

* Enable BFD globally.
* Establish a BFD session.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally, and the BFD view is displayed.
   
   You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
3. Run [**ipv6-trap separated**](cmdqueryname=ipv6-trap+separated)
   
   
   
   Alarms of BFD IPv4 and IPv6 sessions are reported by different trap messages.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.