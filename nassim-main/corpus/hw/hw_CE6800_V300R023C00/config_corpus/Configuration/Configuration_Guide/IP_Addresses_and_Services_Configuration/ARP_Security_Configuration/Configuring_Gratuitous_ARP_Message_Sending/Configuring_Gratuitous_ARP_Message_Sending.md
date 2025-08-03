Configuring Gratuitous ARP Message Sending
==========================================

Configuring Gratuitous ARP Message Sending

#### Context

If an attacker forges a gateway address to send ARP messages to other user hosts, ARP entries on the hosts record an incorrect gateway address. As a result, the gateway cannot receive data from the hosts. You can enable gratuitous ARP message sending on the gateway. The gateway then sends gratuitous ARP messages at intervals to update the ARP entries of authorized users so that the entries contain the correct MAC address of the gateway.

You can configure gratuitous ARP message sending for a device or interface. If gratuitous ARP message sending is configured for a device, this function is enabled for all the interfaces of the device by default. If this function is configured for both a device and an interface, the interface's configuration takes precedence over the device's configuration.


#### Procedure

* Configure gratuitous ARP message sending globally.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enable gratuitous ARP message sending globally.
     
     
     ```
     [arp gratuitous-arp send enable](cmdqueryname=arp+gratuitous-arp+send+enable)
     ```
  3. (Optional) Set an interval for sending gratuitous ARP messages on the device.
     
     
     ```
     [arp gratuitous-arp send interval](cmdqueryname=arp+gratuitous-arp+send+interval) interval
     ```
     
     The default interval for sending gratuitous ARP messages on a device is 60 seconds.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure gratuitous ARP message sending for an interface.
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
  4. Enable or disable gratuitous ARP message sending for the interface.
     
     
     1. Enable gratuitous ARP message sending for the interface.
        ```
        [arp gratuitous-arp send enable](cmdqueryname=arp+gratuitous-arp+send+enable)
        ```
     2. Disable gratuitous ARP message sending for the interface.
        ```
        [arp gratuitous-arp send disable](cmdqueryname=arp+gratuitous-arp+send+disable)
        ```
     
     By default, gratuitous ARP message sending is not enabled or disabled on an interface. Instead, the global configuration policy is used as follows:
     + If gratuitous ARP message sending is enabled globally, it is also enabled on the interface.
     + If gratuitous ARP message sending is disabled globally, it is also disabled on the interface.
  5. (Optional) Set an interval for sending gratuitous ARP messages on the interface.
     
     
     ```
     [arp gratuitous-arp send interval](cmdqueryname=arp+gratuitous-arp+send+interval) interval
     ```
     
     The default interval for sending gratuitous ARP messages on an interface is 60 seconds.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

Run the [**display arp statistics**](cmdqueryname=display+arp+statistics) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check ARP entry statistics.