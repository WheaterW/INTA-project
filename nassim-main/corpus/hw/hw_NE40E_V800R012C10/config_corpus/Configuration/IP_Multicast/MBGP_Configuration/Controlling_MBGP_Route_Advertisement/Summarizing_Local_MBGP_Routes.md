Summarizing Local MBGP Routes
=============================

Configuring route summarization can reduce the size of a routing table on a peer.

#### Context

On a large-scale MBGP network, configuring route summarization can reduce the number of advertised route prefixes and improve MBGP stability.

MBGP supports automatic and manual route summarization.


#### Procedure

* Configure automatic route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**summary automatic**](cmdqueryname=summary+automatic)
     
     
     
     Subnet routes are summarized based on natural network segment masks.
     
     This command summarizes the routes imported into the MBGP routing table. The routes may be direct routes, static routes, RIP routes, OSPF routes, or IS-IS routes. Note that this command is invalid for the routes imported by using the [**network**](cmdqueryname=network) command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure manual route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run one of the following commands to configure route summarization as needed.
     
     
     + To advertise both the summary route and specific routes, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } command.
     + To advertise only the summary route, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } **detail-suppressed** command.
     + To advertise specific routes that meet specified conditions, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } **suppress-policy** *route-policy-name3* command.
       
       You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
     + To generate the summary route used for loop detection, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } **as-set** command.
     + To configure the attributes for the summary route, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } **attribute-policy** *route-policy-name1* command.
       
       You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
       
       If **as-set** is configured in the [**aggregate**](cmdqueryname=aggregate) command, the AS\_Path attribute configured in the [**apply as-path**](cmdqueryname=apply+as-path) command does not take effect.
     + To generate the summary route based on some specific routes, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } **origin-policy** *route-policy-name2* command.
     
     Only the routes that exist in the local MBGP routing table can be manually summarized. For example, if the route 10.1.1.0/24 is not in the MBGP routing table, MBGP will not advertise the summary route even though the [**aggregate**](cmdqueryname=aggregate) **10.1.0.0 16** command is run.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.