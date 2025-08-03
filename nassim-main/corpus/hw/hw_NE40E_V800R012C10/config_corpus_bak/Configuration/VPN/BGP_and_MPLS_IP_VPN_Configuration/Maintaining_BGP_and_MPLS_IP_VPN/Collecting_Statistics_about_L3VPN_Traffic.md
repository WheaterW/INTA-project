Collecting Statistics about L3VPN Traffic
=========================================

Before collecting L3VPN traffic statistics, you need to
enable the L3VPN traffic statistics function.

#### Prerequisites

L3VPN traffic statistics collection is applicable to the
interface traffic at the user side of a VPN.

Perform the following
steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance
   view is displayed.
3. Run [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable)
   
   
   
   The function of collecting statistics about L3VPN
   traffic is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.