Configuring Control Parameters for PIM-SM DR Election
=====================================================

Configuring Control Parameters for PIM-SM DR Election

#### Prerequisites

Before configuring control parameters for PIM-SM DR election, complete one of the following tasks:

* [Configuring PIM-SM in the ASM Model](vrp_pim_cfg_0010.html)
* [Configuring PIM-SM in the SSM Model](vrp_pim_cfg_0017.html)

#### Context

The multicast source DR is responsible for sending Register messages to the RP, and the receiver DR is responsible for sending Join messages to the RP. Devices elect a DR by exchanging Hello messages. The device with the highest priority wins the election. If devices have the same priority, the one with the highest IP address wins the election.

* If all devices on the same network segment support Hello messages that carry DR priorities, the interface with the highest priority wins. If all interfaces have the same priority, the interface with the highest IP address wins.
* As long as one device does not support Hello messages that carry DR priorities, the interface with the highest IP address is elected as the DR.

You can configure a DR priority in either of the following configuration modes:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If no interface-specific configuration is performed for an interface, the interface uses the global configuration.

#### Procedure

* Configure global control parameters for PIM-SM DR election.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  3. Set a DR priority for all interfaces on the device.
     
     
     ```
     [hello-option dr-priority](cmdqueryname=hello-option+dr-priority) priority
     ```
     
     
     
     A larger priority value indicates a higher priority. By default, the DR priority for all interfaces on the device to participate in DR election is 1.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure interface-specific control parameters for PIM-SM DR election.
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
  4. Set a DR priority for the interface.
     
     
     ```
     [pim hello-option dr-priority](cmdqueryname=pim+hello-option+dr-priority) priority
     ```
     
     
     
     A larger priority value indicates a higher priority. By default, an interface's priority for DR election is 1.
  5. Enable DR switchover delay and set a delay time. When an interface changes from a DR to a non-DR, the original entries are valid until the delay timer expires. 
     
     
     ```
     [pim timer dr-switch-delay](cmdqueryname=pim+timer+dr-switch-delay) interval
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```