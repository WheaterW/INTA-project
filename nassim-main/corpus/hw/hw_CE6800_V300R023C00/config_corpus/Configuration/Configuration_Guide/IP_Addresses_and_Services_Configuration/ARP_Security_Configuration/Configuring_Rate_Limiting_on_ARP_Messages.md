Configuring Rate Limiting on ARP Messages
=========================================

Configuring Rate Limiting on ARP Messages

#### Context

When processing a large number of ARP messages, a device may have no sufficient CPU resources to process other services. To protect CPU resources of the device, limit the rate of ARP messages.

After a rate limit is configured for ARP messages, if the number of ARP messages received per second exceeds the limit, the device discards excess ARP messages.

A rate limit and rate limiting duration can be configured for ARP messages globally, in a VLAN, or on an interface. If both global rate limiting and VLAN-based rate limiting are configured, the rate limit and rate limiting duration configured in the VLAN take precedence over those configured globally. If both global rate limiting and interface-based rate limiting are configured, the rate limit and rate limiting duration configured on the interface take precedence over those configured globally.

* If rate limiting on ARP messages is globally configured, the number of ARP messages to be processed on the device is limited.
* If rate limiting on ARP messages is configured on an interface, the number of ARP messages to be processed on the interface is limited.
* If rate limiting on ARP messages is configured in a VLAN, the number of ARP messages to be processed on all interfaces in the VLAN is limited. The configuration in a VLAN does not affect ARP entry learning on interfaces in other VLANs.

#### Procedure

* Configure rate limiting on ARP messages globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure rate limiting on ARP messages.
     
     
     ```
     [arp anti-attack rate-limit](cmdqueryname=arp+anti-attack+rate-limit) limit-value
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure rate limiting on ARP messages in a VLAN.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLAN view.
     
     
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     ```
  3. Configure rate limiting on ARP messages.
     
     
     ```
     [arp anti-attack rate-limit](cmdqueryname=arp+anti-attack+rate-limit) limit-value
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure rate limiting on ARP messages on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Configure rate limiting on ARP messages.
     
     
     ```
     [arp anti-attack rate-limit](cmdqueryname=arp+anti-attack+rate-limit) limit-value
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

1. Check the VLAN-based or global configuration result.
   * Run the [**display arp anti-attack**](cmdqueryname=display+arp+anti-attack) { **rate-limit** | ****entry-check**** } command to check the configuration of ARP attack defense.
   * Run the [**display arp anti-attack record**](cmdqueryname=display+arp+anti-attack+record) command to check detailed information about ARP messages discarded because the rate of ARP messages exceeds the limit.
2. Check the interface-based configuration result.
   * Run the [**display arp anti-attack rate-limit statistics**](cmdqueryname=display+arp+anti-attack+rate-limit+statistics) command to check statistics about ARP messages discarded because the rate of ARP messages exceeds the limit on interfaces.