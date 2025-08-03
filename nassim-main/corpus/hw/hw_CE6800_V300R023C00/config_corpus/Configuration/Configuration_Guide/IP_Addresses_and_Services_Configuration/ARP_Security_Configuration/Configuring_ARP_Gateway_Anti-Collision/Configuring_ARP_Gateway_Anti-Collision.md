Configuring ARP Gateway Anti-Collision
======================================

Configuring ARP Gateway Anti-Collision

#### Context

If an attacker forges the gateway IP address to send ARP messages to other user hosts on a LAN, the user hosts record incorrect gateway address mappings in their ARP tables. As a result, all traffic from the user hosts to the gateway is sent to the attacker and the attacker can intercept related data, causing network access failures of these user hosts.

To defend against attacks from a bogus gateway, enable ARP gateway anti-collision on the gateway if user hosts are directly connected to the gateway.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable ARP gateway anti-collision.
   
   
   ```
   [arp anti-attack gateway-duplicate enable](cmdqueryname=arp+anti-attack+gateway-duplicate+enable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp anti-attack gateway-duplicate item**](cmdqueryname=display+arp+anti-attack+gateway-duplicate+item) command to check ARP gateway anti-collision entries.