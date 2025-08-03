(Optional) Configuring Static IP Address Binding
================================================

The IP address pool configured for static address binding contains special IP addresses, which are assigned to servers in need of fixed IP addresses or users with particular requirements.

#### Context

Based on the clients' needs, you can adopt either static address binding or dynamic address assignment on a DHCPv4 server.

When dynamic address assignment is used, a range of IP addresses to be assigned needs to be specified; when static address binding is used, it can be considered to be a special DHCPv4 address pool with only one address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *pool-name* **bas** **local**
   
   
   
   The IP address pool view is displayed.
3. (Optional) Run [**static-bind**](cmdqueryname=static-bind) **ip-address** *ip-address* **mac-address** *mac-address*
   
   
   
   Certain IP and MAC addresses are statically bound.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Some clients may need fixed IP addresses that are bound to their MAC addresses. When the client with a specific MAC address uses DHCPv4 to apply for an IP address, the DHCPv4 server finds out the fixed IP address bound to the MAC address and assigns it to the client.