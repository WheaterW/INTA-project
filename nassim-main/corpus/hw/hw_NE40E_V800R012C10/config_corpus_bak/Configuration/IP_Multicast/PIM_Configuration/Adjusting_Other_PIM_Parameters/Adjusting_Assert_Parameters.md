Adjusting Assert Parameters
===========================

When multiple multicast data forwarders exist on a shared network segment, the Routers elect a unique forwarder through the Assert mechanism. The Router that fails in the election prevents its downstream interface from forwarding multicast data within the holdtime of the Assert state. After the holdtime of the Assert state expires, the downstream interface is allowed to forward multicast data.

#### Context

If an interface that receives a multicast packet is a downstream interface in the (S, G) entry on the local Router, it indicates that other multicast forwarders exist on the network segment.

When a Router receives an Assert message from another multicast forwarder on the network segment through the downstream interface at the same time when the Router sends an Assert message through this interface, the Router compares its own information with the information carried in the message sent by other forwarders.

This process is called an Assert election.

* If the Router wins, the downstream interface retains the forwarding state and forwards (S, G) data packets on the network segment. This downstream interface is called an Assert winner.
* If the Router fails, the downstream interface is prohibited from forwarding multicast packets and deleted from the downstream interface list of the (S, G) entry. This downstream interface is called an Assert loser.
  
  All Assert losers can periodically restore multicast packet forwarding, leading to periodical Assert elections.

You can set the period during which an Assert loser retains the Assert state either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Set Assert parameters globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**holdtime assert**](cmdqueryname=holdtime+assert) *interval*
     
     
     
     A period is set for all interfaces on the Router to retain the Assert state.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set Assert parameters for an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The PIM interface view is displayed.
  3. Run [**pim holdtime assert**](cmdqueryname=pim+holdtime+assert) *interval*
     
     
     
     The period during which the interface retains the Assert state is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.