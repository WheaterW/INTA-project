Adjusting the Control Parameters for PIM Prune Messages
=======================================================

Adjusting the Control Parameters for PIM Prune Messages

#### Prerequisites

Before adjusting the control parameters for PIM Prune messages, enable IP multicast routing in the public network instance.


#### Context

PIM devices send join information through Join messages upstream to request the upstream device to forward multicast data to them, and send prune information through Prune messages upstream to request the upstream device to stop forwarding multicast data to them. You can adjust PIM prune control parameters in either of the following configuration modes:

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If no interface-specific configuration is performed for an interface, the interface uses the global configuration.

#### Procedure

* Perform global configuration.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  3. Configure PIM prune control parameters as required.
     
     
     
     **Table 1** Configuring PIM prune control parameters
     | Operation | Command | Description |
     | --- | --- | --- |
     | Set the interval for sending Join/Prune messages. | [**timer join-prune**](cmdqueryname=timer+join-prune) *interval* | Devices periodically send Join messages upstream, which prevents RPT branches from being deleted due to timeout. |
     | Set the holdtime of Join/Prune messages. | [**holdtime join-prune**](cmdqueryname=holdtime+join-prune) *interval* | When an upstream device receives a Join/Prune message, it sets a timer to the holdtime carried in the Join/Prune message and starts the timer. If the device does not receive subsequent Join/Prune messages from the corresponding downstream device within the holdtime:  + If the previously received Join/Prune message carries information about joining a multicast group, the downstream interface corresponding to the multicast group is suppressed from forwarding multicast data. + If the previously received Join/Prune message carries information about leaving a multicast group, forwarding through the downstream interface corresponding to the multicast group is restored. |
     | Configure the Join/Prune message sending mode. | [**join-prune triggered-message-cache disable**](cmdqueryname=join-prune+triggered-message-cache+disable) | Sending PIM Join/Prune messages in a package is more efficient than separately sending a large number of PIM Join/Prune messages. By default, a device sends PIM Join/Prune messages in a package. Because the size of a PIM Join/Prune message package is large, devices that have poor performance may fail to accept the package. To prevent such packages from being discarded, disable the Join/Prune message packaging function. |
     | Set a delay in transmitting messages on the shared network. | [**hello-option lan-delay**](cmdqueryname=hello-option+lan-delay) *interval* | During pruning, there is a delay from the time when the current device receives a Prune message from a downstream device to the time when the current device forwards the Prune message upstream. This delay is called a LAN-Delay. |
     | Set an interval for overriding a prune action. | [**hello-option override-interval**](cmdqueryname=hello-option+override-interval) *interval* | After forwarding a Prune message upstream, a PIM device does not immediately prune the corresponding downstream interface. Instead, the PIM device keeps forwarding multicast data downstream for a period. The period for overriding a prune action is called an Override-Interval. The delay from the time when the PIM device receives a Prune message to the time when the PIM device performs the prune action is the sum of LAN-Delay and Override-Interval. |
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Perform interface-specific configuration.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PIM interface view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure PIM prune control parameters as required.
     
     
     
     **Table 2** Configuring PIM prune control parameters
     | Operation | Command | Description |
     | --- | --- | --- |
     | Set the interval for sending Join/Prune messages. | [**timer join-prune**](cmdqueryname=timer+join-prune) *interval* | Devices periodically send Join messages upstream, which prevents RPT branches from being deleted due to timeout. |
     | Set the holdtime of Join/Prune messages. | [**holdtime join-prune**](cmdqueryname=holdtime+join-prune) *interval* | When an upstream device receives a Join/Prune message, it sets a timer to the holdtime carried in the Join/Prune message and starts the timer. If the device does not receive subsequent Join/Prune messages from the corresponding downstream device within the holdtime:  + If the previously received Join/Prune message carries information about joining a multicast group, the downstream interface corresponding to the multicast group is suppressed from forwarding multicast data. + If the previously received Join/Prune message carries information about leaving a multicast group, forwarding through the downstream interface corresponding to the multicast group is restored. |
     | Configure the Join/Prune message sending mode. | [**join-prune triggered-message-cache disable**](cmdqueryname=join-prune+triggered-message-cache+disable) | Sending PIM Join/Prune messages in a package is more efficient than separately sending a large number of PIM Join/Prune messages. By default, a device sends PIM Join/Prune messages in a package. Because the size of a PIM Join/Prune message package is large, devices that have poor performance may fail to accept the package. To prevent such packages from being discarded, disable the Join/Prune message packaging function. |
     | Set a delay in transmitting messages on the shared network. | [**hello-option lan-delay**](cmdqueryname=hello-option+lan-delay) *interval* | During pruning, there is a delay from the time when the current device receives a Prune message from a downstream device to the time when the current device forwards the Prune message upstream. This delay is called a LAN-Delay. |
     | Set an interval for overriding a prune action. | [**hello-option override-interval**](cmdqueryname=hello-option+override-interval) *interval* | After forwarding a Prune message upstream, a PIM device does not immediately prune the corresponding downstream interface. Instead, the PIM device keeps forwarding multicast data downstream for a period. The period for overriding a prune action is called an Override-Interval. The delay from the time when the PIM device receives a Prune message to the time when the PIM device performs the prune action is the sum of LAN-Delay and Override-Interval. |
     | Set the range of valid source addresses for Join information in Join/Prune messages. | [**pim join-policy**](cmdqueryname=pim+join-policy) { **asm** { *basic-acl-number* | **acl-name** *acl-name* }*basic-acl-number* | **ssm** { *advanced-acl-number* | **acl-name** *acl-name* }*advanced-acl-number* | *advanced-acl-number* | **acl-name** *acl-name* } | A range of valid source addresses can be set for Join information in Join/Prune messages to prevent unauthorized users from joining multicast groups. |
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```