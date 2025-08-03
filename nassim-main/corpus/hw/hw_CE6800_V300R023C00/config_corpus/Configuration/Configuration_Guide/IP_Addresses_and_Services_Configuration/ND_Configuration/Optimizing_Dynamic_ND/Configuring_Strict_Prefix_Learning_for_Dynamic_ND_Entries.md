Configuring Strict Prefix Learning for Dynamic ND Entries
=========================================================

Configuring Strict Prefix Learning for Dynamic ND Entries

#### Context

When a device receives a valid NS message on an interface, the device checks whether IPv6 addresses with the same network prefix exist on the interface. If so, the device replies with an NA message and generates dynamic ND entries. Otherwise, the device performs the following operations:

* If strict prefix learning is enabled for dynamic ND entries on the interface, the device discards the NS message and does not generate dynamic ND entries.
* If strict prefix learning is disabled for dynamic ND entries on the interface, the device replies with an NA message and generates dynamic ND entries.

Strict prefix learning is effective for all interfaces if it is configured in the system view but effective only for a specific interface if it is configured in the interface view. If the function is configured in both the system and interface views, the configuration in the interface view has a higher priority.

By default, strict prefix learning is disabled for dynamic ND entries on an interface. The configuration in the system view applies to the interface.

Perform the following operations as required.


#### Procedure

* To disable strict prefix learning for dynamic ND entries on interfaces in batches, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Disable strict prefix learning for dynamic ND entries on all interfaces.
     
     
     ```
     [ipv6 nd learning prefix strict disable](cmdqueryname=ipv6+nd+learning+prefix+strict+disable)
     ```
     
     Strict prefix learning cannot be disabled for dynamic ND entries on interfaces that need to generate host routes, such as dot1q VLAN tag termination sub-interfaces and VLANIF interfaces. The configuration in the system view does not take effect on these interfaces.
  3. Enter the view of the interface on which strict prefix learning needs to be enabled for dynamic ND entries.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  5. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  6. Enable strict prefix learning for dynamic ND entries on the interface.
     
     
     ```
     [ipv6 nd learning prefix strict enable](cmdqueryname=ipv6+nd+learning+prefix+strict+enable)
     ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* To enable strict prefix learning for dynamic ND entries on interfaces in batches, perform the following operations:
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable strict prefix learning for dynamic ND entries on all interfaces.
     
     
     ```
     [undo ipv6 nd learning prefix strict disable](cmdqueryname=undo+ipv6+nd+learning+prefix+strict+disable)
     ```
  3. Enter the view of the interface on which strict prefix learning needs to be disabled for dynamic ND entries.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
  5. Enable IPv6.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  6. Disable strict prefix learning for dynamic ND entries on the interface.
     
     
     ```
     [ipv6 nd learning prefix strict disable](cmdqueryname=ipv6+nd+learning+prefix+strict+disable)
     ```
  7. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```