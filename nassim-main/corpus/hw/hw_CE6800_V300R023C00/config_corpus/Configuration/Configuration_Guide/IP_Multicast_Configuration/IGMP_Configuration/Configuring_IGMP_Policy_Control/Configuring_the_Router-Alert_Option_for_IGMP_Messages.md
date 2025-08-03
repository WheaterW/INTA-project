Configuring the Router-Alert Option for IGMP Messages
=====================================================

Configuring the Router-Alert Option for IGMP Messages

#### Context

You can configure a device to reject IGMP messages that do not contain the Router-Alert option and to send IGMP messages that contain the Router-Alert option.

Ensure that the Router-Alert option configurations on the IGMP message transmit and receive ends on the same network segment are consistent.

![](public_sys-resources/note_3.0-en-us.png) 

The Router-Alert option can be configured globally (IGMP view) or on an interface. The configuration takes effect according to the following rules:

* The configuration in the IGMP view takes effect globally, whereas that in the interface view takes effect only for the specified interface.
* If the same message type is configured in both the interface and IGMP views, the configuration in the interface view takes effect. If the configuration is not performed on an interface, the configuration in the IGMP view takes effect.
* If non-default values are configured in the IGMP view, the corresponding default values in the interface view do not take effect.


#### Procedure

* Configure the Router-Alert option globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IGMP view.
     
     
     ```
     [igmp](cmdqueryname=igmp) [ vpn-instance vpn-instance-name ]
     ```
  3. Configure the device to process IGMP messages with the Router-Alert option and discard those without it.
     
     
     ```
     [require-router-alert](cmdqueryname=require-router-alert)
     ```
     
     By default, a device does not check whether IGMP messages contain the Router-Alert option and processes all received IGMP messages.
  4. Configure the device to include the Router-Alert option in sent IGMP messages.
     
     
     ```
     [undo send-router-alert disable](cmdqueryname=undo+send-router-alert+disable)
     ```
     
     By default, sent IGMP messages carry the Router-Alert option.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the Router-Alert option on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface connected to a user host or switching device.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure the interface to process received IGMP messages with the Router-Alert option and discard those without the Router-Alert option.
     
     
     ```
     [igmp require-router-alert](cmdqueryname=igmp+require-router-alert)
     ```
     
     By default, a device does not check whether IGMP messages contain the Router-Alert option and processes all received IGMP messages.
  5. Configure the device to include the Router-Alert option in sent IGMP messages.
     
     
     ```
     [undo igmp send-router-alert disable](cmdqueryname=undo+igmp+send-router-alert+disable)
     ```
     
     By default, sent IGMP messages carry the Router-Alert option.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```