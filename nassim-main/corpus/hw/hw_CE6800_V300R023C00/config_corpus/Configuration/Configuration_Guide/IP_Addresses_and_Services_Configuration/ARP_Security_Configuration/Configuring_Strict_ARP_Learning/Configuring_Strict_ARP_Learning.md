Configuring Strict ARP Learning
===============================

Configuring Strict ARP Learning

#### Context

Strict ARP learning can be enabled for a device or interface, so that the device or interface learns only address information carried in the ARP reply messages in response to the ARP request messages sent by itself.


#### Procedure

* Enable strict ARP learning globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable strict ARP learning.
     
     
     ```
     [arp learning strict](cmdqueryname=arp+learning+strict)
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Enable strict ARP learning for an interface.
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
  4. Enable strict ARP learning.
     
     
     ```
     [arp learning strict force-enable](cmdqueryname=arp+learning+strict+force-enable)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp learning strict**](cmdqueryname=display+arp+learning+strict) command to check the configuration of strict ARP learning on all interfaces.