Configuring an Interface to Filter Multicast Data from Specified VLANs
======================================================================

Configuring an Interface to Filter Multicast Data from Specified VLANs

#### Context

If multicast data of some VLANs is not needed, you can configure an interface to filter the data from those VLANs. The interface then discards the filtered data, instead of forwarding it.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the interface to filter the data from specified VLANs.
   
   
   ```
   [multicast deny-vlan](cmdqueryname=multicast+deny-vlan) { start-vlan-id [ to end-vlan-id ] } &<1-10>
   ```
   
   By default, an interface forwards the data received from a VLAN if the interface has been added to the VLAN.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```