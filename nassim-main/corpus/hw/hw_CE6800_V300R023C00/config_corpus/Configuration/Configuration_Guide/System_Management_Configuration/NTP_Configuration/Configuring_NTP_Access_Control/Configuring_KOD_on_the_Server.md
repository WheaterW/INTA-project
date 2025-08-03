Configuring KOD on the Server
=============================

Configuring KOD on the Server

#### Context

KOD cannot be used in broadcast or multicast mode.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable KOD.
   
   
   ```
   [ntp kod-enable](cmdqueryname=ntp+kod-enable)
   ```
3. (Optional) Configure access control authority.
   
   
   ```
   [ntp access](cmdqueryname=ntp+access) { peer | query | server | synchronization | limited } { { acl-number | acl-name aclname } [ ipv6 { acl6-number | acl6-name acl6name } ] | ipv6 { acl6-number | acl6-name acl6name } [ { acl-number | acl-name aclname } ] }
   ```
4. (Optional) Configure the minimum and average intervals for receiving NTP packets.
   
   
   ```
   [ntp discard](cmdqueryname=ntp+discard) { min-interval min-interval-val | avg-interval avg-interval-val } *
   ```
   
   The value is expressed in the Nth power of 2 seconds. By default, the minimum interval for sending NTP packets is 1 (2 to the power of 1s = 2s), and the average interval is 5 (2 to the power of 5s = 32s).
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```