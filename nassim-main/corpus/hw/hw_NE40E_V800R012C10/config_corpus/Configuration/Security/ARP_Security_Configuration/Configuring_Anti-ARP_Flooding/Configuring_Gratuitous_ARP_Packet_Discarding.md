Configuring Gratuitous ARP Packet Discarding
============================================

After gratuitous Address Resolution Protocol (ARP) packet
discarding is configured, the device discards all received gratuitous
ARP packets to prevent excessive CPU consumption.

#### Context

When a device is connected to a network for the first time, the device broadcasts gratuitous ARP packets to announce its existence and checks whether its IP address conflicts with any other device IP address in the broadcast domain. Any device can send gratuitous ARP packets and receive gratuitous ARP packets without authentication. As a result, a large number of gratuitous ARP packets can be generated, causing devices to be busy processing these packets. This process overloads the CPU and affects the processing of other services. To resolve this problem, you can enable gratuitous ARP packet discarding. After gratuitous ARP packet discarding is enabled, the device discards all received gratuitous ARP packets to prevent excessive CPU consumption.

Gratuitous ARP packet discarding can be enabled in the system
view or in the interface view.

* If the [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop) command is enabled in the system view, the device discards gratuitous
  ARP packets received from all interfaces.
* If the [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop) command is enabled in the interface view, the device discards gratuitous
  ARP packets received from a specified interface.

Gratuitous ARP request discarding enabled in the system view
is independent upon that enabled in the interface view.

#### Procedure

* Configure gratuitous ARP packet discarding globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop)
     
     
     
     Gratuitous ARP packet discarding is enabled globally.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure gratuitous ARP packet discarding for an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**arp anti-attack gratuitous-arp drop**](cmdqueryname=arp+anti-attack+gratuitous-arp+drop)
     
     
     
     Gratuitous ARP packet discarding is enabled for an interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.