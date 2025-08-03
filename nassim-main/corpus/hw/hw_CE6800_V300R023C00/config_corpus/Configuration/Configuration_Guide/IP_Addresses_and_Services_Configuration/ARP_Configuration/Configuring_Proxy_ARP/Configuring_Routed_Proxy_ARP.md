Configuring Routed Proxy ARP
============================

Configuring Routed Proxy ARP

#### Context

Hosts that belong to the same network segment but different physical networks are unable to communicate with each other if the gateways connected to the hosts have different IP addresses. In this case, you can enable routed proxy ARP on a device's interface connected to the hosts to enable the hosts to communicate.


#### Procedure

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
4. Configure an IP address for the interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
   
   The IP address of an interface must reside on the same network segment as the IP address of a host connected to the interface.
5. Enable routed proxy ARP on the interface.
   
   
   ```
   [arp proxy enable](cmdqueryname=arp+proxy+enable)
   ```
   
   After routed proxy ARP is enabled on a device, the aging time of ARP entries on hosts must be reduced. This ensures that invalid ARP entries are aged out as soon as possible, reducing the number of packets that are sent to but cannot be forwarded by the device.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type* *interface-number* } command to check ARP entries on an interface.