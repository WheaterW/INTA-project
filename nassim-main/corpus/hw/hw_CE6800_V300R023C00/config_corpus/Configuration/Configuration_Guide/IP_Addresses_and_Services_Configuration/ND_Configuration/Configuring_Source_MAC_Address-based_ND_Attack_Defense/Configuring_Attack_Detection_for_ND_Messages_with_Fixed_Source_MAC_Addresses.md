Configuring Attack Detection for ND Messages with Fixed Source MAC Addresses
============================================================================

Configuring Attack Detection for ND Messages with Fixed Source MAC Addresses

#### Context

To prevent ND attack messages with fixed source MAC addresses from consuming CPU resources, configure attack detection for such messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the detection of ND attack messages with fixed source MAC addresses and set a detection mode.
   
   
   ```
   [ipv6 nd source-mac detect-mode](cmdqueryname=ipv6+nd+source-mac+detect-mode) { filter | monitor }
   ```
3. (Optional) Configure an aging time for ND attack entries with fixed source MAC addresses.
   
   
   ```
   [ipv6 nd source-mac aging-time](cmdqueryname=ipv6+nd+source-mac+aging-time) aging-value
   ```
4. (Optional) Configure an attack detection threshold for ND messages with fixed source MAC addresses.
   
   
   ```
   [ipv6 nd source-mac threshold](cmdqueryname=ipv6+nd+source-mac+threshold) threshold-value
   ```
   
   If the number of ND messages with the same source MAC address received within 5 seconds exceeds the configured threshold, the system considers that an attack has occurred and adds the MAC address to an attack entry.
5. (Optional) Configure a MAC address to be protected.
   
   
   ```
   [ipv6 nd source-mac exclude-mac](cmdqueryname=ipv6+nd+source-mac+exclude-mac) mac-address
   ```
6. (Optional) Configure the maximum number of ND messages with fixed source MAC addresses.
   
   
   ```
   [ipv6 nd source-mac max-detect-number](cmdqueryname=ipv6+nd+source-mac+max-detect-number) max-detect-value
   ```
7. (Optional) Configure the maximum number of ND attack entries with fixed source MAC addresses.
   
   
   ```
   [ipv6 nd source-mac max-entry-number](cmdqueryname=ipv6+nd+source-mac+max-entry-number) max-entry-value
   ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```