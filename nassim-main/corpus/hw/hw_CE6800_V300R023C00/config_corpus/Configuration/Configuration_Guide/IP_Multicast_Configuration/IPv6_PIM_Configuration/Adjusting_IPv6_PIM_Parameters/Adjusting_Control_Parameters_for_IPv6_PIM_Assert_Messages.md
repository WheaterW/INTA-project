Adjusting Control Parameters for IPv6 PIM Assert Messages
=========================================================

Adjusting Control Parameters for IPv6 PIM Assert Messages

#### Prerequisites

Before adjusting control parameters for IPv6 PIM Assert messages, enable IPv6 multicast routing in the public network instance.


#### Context

When multiple multicast data forwarders are available on a shared network segment, the Assert mechanism is used to elect only one forwarder from them. The devices that fail in the election do not forward multicast data through their downstream interfaces within the Assert holdtime. They restore such forwarding after the holdtime expires.

If the interface that receives a multicast packet is a local downstream interface corresponding to an (S, G) entry, another multicast forwarder exists on the network segment. The device sends an Assert message through the downstream interface, and this interface also receives an Assert message from another multicast forwarder on the network segment. The device compares its information with the information contained in the received message for Assert election.

* If the device wins, its downstream interface keeps forwarding data packets corresponding to the (S, G) entry on the network segment. This downstream interface is called an Assert winner.
* If the device fails, its downstream interface is prohibited from forwarding multicast packets and deleted from the downstream interface list of the (S, G) entry within the Assert holdtime. This downstream interface is called an Assert loser.
  
  All Assert losers can periodically restore multicast packet forwarding, leading to periodic Assert elections.

You can set the Assert holdtime in either of the following configuration modes:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If no interface-specific configuration is performed for an interface, the interface uses the global configuration.

#### Procedure

* Perform global configuration.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IPv6 PIM view.
     
     
     ```
     [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
     ```
  3. Set an Assert holdtime for all interfaces.
     
     
     ```
     [holdtime assert](cmdqueryname=holdtime+assert) interval
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Perform interface-specific configuration.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Set an Assert holdtime for the interface.
     
     
     ```
     [pim ipv6 holdtime assert](cmdqueryname=pim+ipv6+holdtime+assert) interval
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```