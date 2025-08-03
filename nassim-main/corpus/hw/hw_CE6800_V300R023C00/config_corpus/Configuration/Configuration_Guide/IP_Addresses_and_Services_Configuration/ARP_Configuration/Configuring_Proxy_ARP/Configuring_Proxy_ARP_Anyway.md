Configuring Proxy ARP Anyway
============================

Configuring Proxy ARP Anyway

#### Context

In scenarios where servers are partitioned into hosts, the flexible deployment and migration of hosts on multiple servers or devices can be achieved by configuring Layer 2 interconnection between multiple devices. However, this approach may lead to larger Layer 2 domains on the network and the risk of broadcast storms. To resolve this problem, enable proxy ARP anyway on a host gateway. In this way, the gateway sends its interface MAC address to a source host and communication between hosts is implemented through route forwarding.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the VLANIF interface where proxy ARP anyway needs to be enabled.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) interface-number
   ```
3. Configure an IP address for the interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
   
   The IP address of an interface must reside on the same network segment as the IP address of a host connected to the interface.
4. Enable proxy ARP anyway on the interface.
   
   
   ```
   [arp proxy anyway enable](cmdqueryname=arp+proxy+anyway+enable)
   ```
   
   After proxy ARP anyway is enabled on a device, the aging time of ARP entries on hosts must be reduced. This ensures that invalid ARP entries are aged out as soon as possible, reducing the number of packets that are sent to but cannot be forwarded by the device.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type* *interface-number* } command to check ARP entries on an interface.