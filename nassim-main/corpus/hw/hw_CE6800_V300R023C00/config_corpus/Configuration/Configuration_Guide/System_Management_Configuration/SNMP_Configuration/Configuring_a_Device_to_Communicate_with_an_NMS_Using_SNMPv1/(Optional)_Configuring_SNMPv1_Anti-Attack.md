(Optional) Configuring SNMPv1 Anti-Attack
=========================================

(Optional) Configuring SNMPv1 Anti-Attack

#### Context

Configure the SNMP blacklist function to defense against a malicious user's attack on other users' passwords and improve security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the blacklist function for an IP address.
   
   
   ```
   [undo snmp-agent blacklist ip-block disable](cmdqueryname=undo+snmp-agent+blacklist+ip-block+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```