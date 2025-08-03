Configuring a Link-local Address for an Interface
=================================================

Link-local addresses are used in neighbor discovery and in the communication between nodes on the local link during stateless address autoconfiguration. Link-local addresses are valid only on local links, meaning that packets with link-local addresses as source or destination addresses are not forwarded to other links.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled for the interface.
4. Perform either of the following operations according to on-site requirements:
   
   
   * To automatically configure the link-local address of the interface, run the [**ipv6 address auto link-local**](cmdqueryname=ipv6+address+auto+link-local) command.
   * To manually configure the link-local address of the interface, run the [**ipv6 address**](cmdqueryname=ipv6+address+link-local+tag) *ipv6-address* **link-local** [ **tag** *tag-value* ] or [**ipv6 address**](cmdqueryname=ipv6+address+tag)  { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } [ **tag** *tag-value* ] command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.