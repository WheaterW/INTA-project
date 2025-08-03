Configuring Rate Limiting on ARP Miss Messages
==============================================

Configuring Rate Limiting on ARP Miss Messages

#### Context

After a rate limit is configured for ARP Miss messages, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the limit, the device does not process excess ARP Miss messages.

Rate limiting on ARP Miss messages protects a device against attacks that are initiated by sending a large number of different ARP Miss messages, whereas fake ARP entries protect a device against attacks that are initiated by sending the same ARP Miss messages repeatedly. You can run the [**arp fake timeout**](cmdqueryname=arp+fake+timeout) command to configure an aging time for fake ARP entries on an interface to control the frequency of sending the same ARP Miss messages repeatedly.


#### Procedure

* Configure rate limiting on ARP Miss messages based on source IP addresses.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure rate limiting on ARP Miss messages.
     
     
     ```
     [arp miss anti-attack rate-limit](cmdqueryname=arp+miss+anti-attack+rate-limit) source-ip [ source-ip-address [ mask { mask-length | mask } ] ] maximum limit-value
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure rate limiting on ARP Miss messages in a VLAN.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLAN view.
     
     
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     ```
  3. Configure rate limiting on ARP Miss messages.
     
     
     ```
     [arp miss anti-attack rate-limit](cmdqueryname=arp+miss+anti-attack+rate-limit) limit-value
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure rate limiting on ARP Miss messages on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure rate limiting on ARP Miss messages.
     
     
     ```
     [arp miss anti-attack rate-limit](cmdqueryname=arp+miss+anti-attack+rate-limit) limit-value
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display arp miss anti-attack**](cmdqueryname=display+arp+miss+anti-attack) **rate-limit** command to check the configuration of ARP Miss attack defense.
* Run the [**display arp miss anti-attack record**](cmdqueryname=display+arp+miss+anti-attack+record) command to check detailed information about ARP Miss messages discarded because the rate of ARP Miss messages exceeds the limit.