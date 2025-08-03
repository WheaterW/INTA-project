Configuring MAC Address Check for ND
====================================

Configuring MAC Address Check for ND

#### Context

To enable MAC address check for ND, run the [**ipv6 nd mac-check enable**](cmdqueryname=ipv6+nd+mac-check+enable) command. After the command is run, the system proactively checks source MAC address consistency to improve network reliability.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable MAC address check for ND.
   
   
   ```
   [ipv6 nd mac-check enable](cmdqueryname=ipv6+nd+mac-check+enable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```