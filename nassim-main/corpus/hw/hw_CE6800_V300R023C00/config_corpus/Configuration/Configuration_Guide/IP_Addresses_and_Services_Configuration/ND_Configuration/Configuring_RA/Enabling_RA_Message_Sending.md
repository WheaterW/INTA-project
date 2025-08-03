Enabling RA Message Sending
===========================

Enabling RA Message Sending

#### Context

By default, a routing device does not send RA messages. However, a host that connects to a routing device uses these messages to obtain the prefix list and other configurations. You therefore need to enable the routing device to send multicast RA messages. If the host connects to the routing device through a Layer 2 forwarding device but the forwarding device cannot forward multicast RA messages, you can enable the routing device to send unicast RA messages instead. In this case, the routing device sends unicast RA messages in response to RS messages it receives on an interface.


#### Procedure

* Enable multicast RA message sending.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface on which multicast RA messages need to be sent.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  5. Enable the routing device to send multicast RA messages.
     
     
     ```
     [ipv6 nd ra halt disable](cmdqueryname=ipv6+nd+ra+halt+disable)
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable unicast RA message sending.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface on which unicast RA messages need to be sent.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  4. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  5. Enable the routing device to send unicast RA messages.
     
     
     ```
     [ipv6 nd ra-unicast send enable](cmdqueryname=ipv6+nd+ra-unicast+send+enable) 
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```