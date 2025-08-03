(Optional) Configuring SNMPv3 Anti-Attack
=========================================

(Optional) Configuring SNMPv3 Anti-Attack

#### Context

Configure the SNMPv3 blacklist function to defense against a malicious user's attack on other users' passwords and improve security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the blacklist function for an IP address.
   
   
   ```
   [undo snmp-agent blacklist ip-block disable](cmdqueryname=undo+snmp-agent+blacklist+ip-block+disable)
   ```
3. Enable the user blacklist function.
   
   
   ```
   [undo snmp-agent blacklist user-block disable](cmdqueryname=undo+snmp-agent+blacklist+user-block+disable)
   ```
   
   By default, the blacklist function for an SNMPv3 user is enabled.
4. Configure the maximum number of consecutive authentication failures allowed for an SNMPv3 user.
   
   
   ```
   [snmp-agent blacklist user-block failed-times](cmdqueryname=snmp-agent+blacklist+user-block+failed-times) failed-times period period-time
   ```
   
   By default, an SNMPv3 user is locked if the user's five consecutive authentication attempts fail within 5 minutes
5. Configure the locking period for an SNMPv3 user after the user's authentication failures exceed a specified number of consecutive times.
   
   
   ```
   [snmp-agent blacklist user-block reactive](cmdqueryname=snmp-agent+blacklist+user-block+reactive) reactive-time
   ```
   
   
   
   By default, the locking period is 5 minutes. After the period elapses, the user is automatically unlocked and can continue to be authenticated.
   
   To unlock users during the locking period, run the [**snmp-agent activateusm-user**](cmdqueryname=snmp-agent+activateusm-user) *user-name* [ [**remote-engineid**](cmdqueryname=remote-engineid) *remote-engineid* ] command.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```