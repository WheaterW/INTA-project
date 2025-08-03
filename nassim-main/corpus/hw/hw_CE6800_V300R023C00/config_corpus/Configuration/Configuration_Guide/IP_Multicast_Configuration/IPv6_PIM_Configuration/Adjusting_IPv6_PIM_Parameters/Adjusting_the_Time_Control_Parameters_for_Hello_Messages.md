Adjusting the Time Control Parameters for Hello Messages
========================================================

Adjusting the Time Control Parameters for Hello Messages

#### Prerequisites

Before adjusting the time control parameters for Hello messages, enable IPv6 multicast routing in the public network instance.


#### Context

Devices establish neighbor relationships by exchanging Hello messages. You can set the interval for sending Hello messages and neighbor holdtime in either of the following configuration modes:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If no interface-specific configuration is performed for an interface, the interface uses the global configuration.

#### Procedure

* Configure the time control parameters for Hello messages globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IPv6 PIM view.
     
     
     ```
     [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
     ```
  3. Set an interval at which the device sends Hello messages.
     
     
     ```
     [timer hello](cmdqueryname=timer+hello) interval
     ```
     
     By default, a device sends Hello messages at an interval of 30 seconds. The interval at which the device sends Hello messages must be shorter than the neighbor holdtime.
  4. Set the neighbor holdtime carried in the PIM Hello message sent by the device.
     
     
     ```
     [hello-option holdtime](cmdqueryname=hello-option+holdtime) holdtimeValue
     ```
     
     By default, the neighbor holdtime is 105 seconds.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the time control parameters for Hello messages on an interface.
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
  4. Set an interval at which the interface sends Hello messages.
     
     
     ```
     [pim ipv6 timer hello](cmdqueryname=pim+ipv6+timer+hello) interval
     ```
     
     
     
     By default, an interface sends Hello messages at an interval of 30 seconds.
  5. Set the neighbor holdtime carried in the PIM Hello message sent by the interface.
     
     
     ```
     [pim ipv6 hello-option holdtime](cmdqueryname=pim+ipv6+hello-option+holdtime) helloHoldTime
     ```
     
     
     
     By default, the neighbor holdtime carried in the PIM Hello message sent by a PIM interface is 105s.
     
     The interval at which the interface sends Hello messages must be shorter than the neighbor holdtime.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```