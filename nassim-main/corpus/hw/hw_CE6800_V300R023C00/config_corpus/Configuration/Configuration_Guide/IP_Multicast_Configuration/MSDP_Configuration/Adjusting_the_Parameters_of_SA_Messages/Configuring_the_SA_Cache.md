Configuring the SA Cache
========================

Configuring the SA Cache

#### Context

An SA cache is used to locally save (S, G) information carried in SA messages. When a device needs to obtain (S, G) information, it directly obtains available (S, G) information from the SA cache. Setting the maximum number of (S, G) entries in an SA cache can prevent Deny of Service (DoS) attacks. You can also disable the SA cache function.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
3. Set the maximum number of (S, G) entries in an SA cache.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address sa-cache-maximum sa-limit
   ```
   
   By default, a maximum of 8192 (S, G) entries can be cached locally.
   
   *peer-address*: specifies the IP address of a remote MSDP peer. *sa-limit*: specifies the maximum number of (S, G) entries in an SA cache. If *sa-limit* is smaller than the SA cache specification, the *sa-limit* value takes effect; otherwise, the SA cache specification takes effect.
4. (Optional) Configure a holdtime for entries in the SA cache.
   
   
   ```
   [sa-cache-holdtime](cmdqueryname=sa-cache-holdtime) holdtime
   ```
   
   Each time the device receives a new SA message, the corresponding (S, G) cache holdtime is set to the value specified by this command.
5. (Optional) Disable the SA cache function.
   
   
   ```
   [cache-sa-disable](cmdqueryname=cache-sa-disable)
   ```
   
   
   
   By default, the SA cache function is enabled on the device that has an MSDP peer specified. To enable the SA cache function again, run the [**undo cache-sa-disable**](cmdqueryname=undo+cache-sa-disable) command.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```