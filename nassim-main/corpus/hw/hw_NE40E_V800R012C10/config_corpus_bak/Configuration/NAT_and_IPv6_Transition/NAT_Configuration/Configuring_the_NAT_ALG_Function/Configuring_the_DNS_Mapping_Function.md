Configuring the DNS Mapping Function
====================================

The DNS mapping function enables users on an enterprise network to send packets carrying DNS domain names to access a DNS server on a public network.

#### Usage Scenario

If a device on an enterprise network without a DNS server needs to use a DNS domain name to communicate with a server within the enterprise network, the communication can be implemented using a DNS server on a public network.

To meet this requirement, the DNS mapping function can be configured. When a DNS packet arrives at a NAT device, the NAT device searches for a static entry based on the configured UDP-based DNS mapping entry and translates the public IP address into the private IP address. Then the NAT device sends the private IP address that replaces the DNS resolution result to the user.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**nat dns-mapping**](cmdqueryname=nat+dns-mapping) **domain** *domain-name* **global-address** *global-address* **inside-address** *inside-address*
   
   
   
   DNS mapping is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.