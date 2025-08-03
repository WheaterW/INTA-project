Configuring Gratuitous ARP Message Discarding
=============================================

Configuring Gratuitous ARP Message Discarding

#### Context

When a device is connected to a network for the first time, the device broadcasts gratuitous ARP messages to announce its existence and checks whether its IP address conflicts with any other device IP address in the broadcast domain. Any device can send gratuitous ARP messages, and they can receive gratuitous ARP messages without authentication. As a result, a large number of gratuitous ARP messages are generated, consuming device resources to process these messages. This process overloads the CPU and affects the processing of other services. To resolve this issue, enable gratuitous ARP message discarding. After this function is enabled, the device discards all received gratuitous ARP messages to reduce CPU resource consumption.

Gratuitous ARP message discarding can be enabled in the system or interface view.

* If the [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop) command is enabled in the system view, the device discards gratuitous ARP messages received from all interfaces.
* If the [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop) command is enabled in the interface view, the device discards gratuitous ARP messages received from this interface.

Gratuitous ARP message discarding enabled in the system view is independent of that enabled in the interface view.

#### Procedure

* Configure gratuitous ARP message discarding globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure gratuitous ARP message discarding.
     
     
     ```
     [arp anti-attack gratuitous-arp drop](cmdqueryname=arp+anti-attack+gratuitous-arp+drop)
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure gratuitous ARP message discarding for an interface.
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
  4. Configure gratuitous ARP message discarding for an interface.
     
     
     ```
     [arp anti-attack gratuitous-arp drop](cmdqueryname=arp+anti-attack+gratuitous-arp+drop)
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp statistics**](cmdqueryname=display+arp+statistics) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check ARP entry statistics.