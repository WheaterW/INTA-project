(Optional) Configuring the Resource Allocation Mode for Hardware Flow Entries
=============================================================================

(Optional) Configuring the Resource Allocation Mode for Hardware Flow Entries

#### Context

After the AnyFlow function is enabled, the device collects traffic and generates hardware flow entries. By default, IPv4 and IPv6 traffic each occupies half of the flow entry resources. If only IPv4 or IPv6 traffic is transmitted on the live network, you can adjust the allocation of hardware flow entry resources. The device must be restarted for the new resource allocation mode to take effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the allocation mode of the hardware flow entry resources.
   
   
   ```
   [assign forward any-flow resource](cmdqueryname=assign+forward+any-flow+resource) { large-ipv4 | large-ipv6 | standard }
   ```
   
   By default, the flow entry resource allocation mode is **standard**, meaning that IPv4 and IPv6 traffic each occupies half of the flow entries.
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```