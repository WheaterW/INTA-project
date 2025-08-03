(Optional) Configuring SNMPv3 Anti-Attack
=========================================

To defense against a user's attack on other users' passwords, configuring the SNMPv3 blacklist function to improve security.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**undo snmp-agent blacklist ip-block disable**](cmdqueryname=undo+snmp-agent+blacklist+ip-block+disable) command to enable the IP address blacklist function.
3. Run the [**undo snmp-agent blacklist user-block disable**](cmdqueryname=undo+snmp-agent+blacklist+user-block+disable) command to enable the user blacklist function.
4. Run the [**snmp-agent
   blacklist user-block failed-times**](cmdqueryname=snmp-agent+blacklist+user-block+failed-times) *failed-times* **period** *period-time* command to configure the maximum number of consecutive authentication failures allowed for an SNMPv3 user.
5. Run the [**snmp-agent blacklist user-block reactive**](cmdqueryname=snmp-agent+blacklist+user-block+reactive) *reactive-time* command to configure the locking period for an SNMPv3 user after the user's authentication failures exceed a specified number of consecutive times.
   
   
   
   After the period of time elapses, the user is automatically unlocked and can continue to be authenticated.
   
   To unlock users during the locking period, run the [**snmp-agent activateusm-user**](cmdqueryname=snmp-agent+activateusm-user) *user-name* [ [**remote-engineid**](cmdqueryname=remote-engineid) *remote-engineid* ] command.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.