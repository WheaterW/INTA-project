Configuring Fixed ARP
=====================

Configuring Fixed ARP

#### Context

Fixed ARP can be configured globally or on VLANIF interfaces.

* By default, after fixed ARP is configured globally, it is enabled for all interfaces.
* If fixed ARP is configured in both the system view and VLANIF interface view, the configuration in the VLANIF interface view takes effect.


#### Procedure

* Configure fixed ARP globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure fixed ARP.
     
     
     ```
     [arp anti-attack entry-check](cmdqueryname=arp+anti-attack+entry-check) { fixed-mac | fixed-all | send-ack } enable
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure fixed ARP for an interface.
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
  4. Configure fixed ARP.
     
     
     ```
     [arp anti-attack entry-check](cmdqueryname=arp+anti-attack+entry-check) { fixed-mac | fixed-all | send-ack } enable
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp statistics**](cmdqueryname=display+arp+statistics) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check ARP entry statistics.