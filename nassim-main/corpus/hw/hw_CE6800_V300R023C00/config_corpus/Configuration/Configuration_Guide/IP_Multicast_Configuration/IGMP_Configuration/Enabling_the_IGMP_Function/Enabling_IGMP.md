Enabling IGMP
=============

Enabling IGMP

#### Context

IGMP can be configured only on PIM-SM-enabled devices. Therefore, before enabling IGMP on an interface, you need to run the **pim sm** command on the interface to ensure that the interface can forward multicast data normally.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the multicast function.
   
   
   ```
   [multicast routing-enable](cmdqueryname=multicast+routing-enable)
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
5. Enable PIM-SM.
   
   
   ```
   [pim sm](cmdqueryname=pim+sm) 
   ```
   
   By default, PIM-SM is disabled on an interface.
   
   Running the [**undo pim sm**](cmdqueryname=undo+pim+sm) command will clear the PIM neighbor information and protocol status on an interface. Therefore, exercise caution when running the [**undo pim sm**](cmdqueryname=undo+pim+sm) command after IGMP is enabled. Otherwise, multicast services cannot run normally.
6. Enable IGMP.
   
   
   ```
   [igmp enable](cmdqueryname=igmp+enable)
   ```
7. (Optional) Configure an IGMP version for the interface.
   
   
   ```
   [igmp version](cmdqueryname=igmp+version) VersionValue 
   ```
   
   If there are multiple multicast devices on a shared network segment of hosts, all of their host-side interfaces must run the same IGMP version. Note that IGMP cannot function normally on the network if such devices are running different IGMP versions.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```