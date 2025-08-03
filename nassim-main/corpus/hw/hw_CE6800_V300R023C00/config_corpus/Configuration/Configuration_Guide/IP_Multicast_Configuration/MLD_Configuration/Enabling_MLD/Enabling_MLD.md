Enabling MLD
============

Enabling MLD

#### Context

You can enable MLD on a multicast device's interface connected to a user network segment, so that the corresponding user hosts can dynamically join an IPv6 multicast group.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the multicast function.
   
   
   ```
   [multicast ipv6 routing-enable](cmdqueryname=multicast+ipv6+routing-enable)
   ```
3. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable IPv6 PIM-SM.
   
   
   ```
   [pim ipv6 sm](cmdqueryname=pim+ipv6+sm) 
   ```
   
   By default, IPv6 PIM-SM is disabled on an interface.
   
   Running the [**undo pim ipv6 sm**](cmdqueryname=undo+pim+ipv6+sm) command will clear the PIM neighbor information and protocol status on an interface. Therefore, exercise caution when running this command after MLD is enabled. Otherwise, multicast services cannot run normally.
6. Enable MLD.
   
   
   ```
   [mld enable](cmdqueryname=mld+enable)
   ```
7. (Optional) Configure an MLD version for the interface.
   
   
   ```
   [mld version](cmdqueryname=mld+version) version 
   ```
   
   If there is more than one multicast device on a shared network segment of hosts, all of these devices' host-side interfaces must run the same MLD version. Note that MLD cannot function normally on the network if such devices are running different MLD versions.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```