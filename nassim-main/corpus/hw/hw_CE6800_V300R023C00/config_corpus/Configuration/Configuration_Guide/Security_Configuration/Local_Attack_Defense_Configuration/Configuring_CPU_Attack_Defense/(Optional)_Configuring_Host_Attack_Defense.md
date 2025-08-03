(Optional) Configuring Host Attack Defense
==========================================

(Optional) Configuring Host Attack Defense

#### Context

After the **ssh server acl** and **telnet server acl** commands are configured, SSH and Telnet packets are sent to the CPU. If host attack defense is configured, these packets will match hardware-based ACLs. If packets match the deny rule in a hardware-based ACL, they are directly discarded before they are sent to the CPU, ensuring that normal packets can be successfully sent.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable host attack defense.
   
   
   ```
   [cpu-defend local-host anti-attack enable](cmdqueryname=cpu-defend+local-host+anti-attack+enable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```