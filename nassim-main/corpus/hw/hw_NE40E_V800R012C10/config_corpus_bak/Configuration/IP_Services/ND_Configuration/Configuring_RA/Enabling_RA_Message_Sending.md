Enabling RA Message Sending
===========================

A routing device periodically sends RA messages carrying network prefixes and flags, or responds to RS messages with RA messages.

#### Context

By default, a routing device does not send RA messages. However, a host that connects to a routing device uses these messages to obtain the prefix list and other configurations. You therefore need to enable the routing device to send multicast RA messages. If the host connects to the routing device through a Layer 2 forwarding device but the forwarding device cannot forward multicast RA messages, you can enable the routing device to send unicast RA messages instead. In this case, the routing device sends unicast RA messages in response to RS messages it receives on an interface.


#### Procedure

* Enable multicast RA message sending.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which multicast RA messages need to be sent is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled.
  4. Run [**undo ipv6 nd ra halt**](cmdqueryname=undo+ipv6+nd+ra+halt)
     
     
     
     The routing device is enabled to send multicast RA messages.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable unicast RA message sending.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which unicast RA messages need to be sent is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled.
  4. Run [**ipv6 nd ra-unicast send enable**](cmdqueryname=ipv6+nd+ra-unicast+send+enable)
     
     
     
     The routing device is enabled to send unicast RA messages.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.