Configuring ARP Message Validity Check
======================================

Configuring ARP Message Validity Check

#### Context

You can configure ARP message validity check to reject ARP messages from authorized users who have been attacked, improving communication security and reliability.


#### Procedure

* Configure ARP message validity check globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure ARP message validity check.
     
     
     ```
     [arp validate source-mac](cmdqueryname=arp+validate+source-mac)
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure ARP message validity check for an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number } 
     ```
  3. Configure ARP message validity check.
     
     
     ```
     [arp validate](cmdqueryname=arp+validate) { destination-mac source-mac | source-mac destination-mac }
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp packet statistics**](cmdqueryname=display+arp+packet+statistics) [ **interface** [ *interface-name* | *interface-type interface-number* ] ] command to check statistics about ARP messages sent and received by the device.