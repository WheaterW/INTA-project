Configuring a Diameter Link
===========================

This section describes how to configure a Diameter link to connect a Diameter client and a Diameter server.

#### Context

A Diameter server group consists of the Diameter client, Diameter server, and Diameter link.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**diameter-local**](cmdqueryname=diameter-local) *localname* **interface** *interface-type* *interface-number* [ **host** *host-name* | **product** *product-name* | **realm** *realm-name* ] \*
   
   
   
   The Diameter client (Router) entity information is configured, including the name, host IP address, host name, domain name, and product name of the client.
3. Run [**diameter-peer**](cmdqueryname=diameter-peer) *peername* { **ip** *ip-address* | **ipv6** *ipv6-address* } [ **vpn-instance** *vpn-instance* ] **port** *port-number* [ **host** *host-name* | **realm** *realm-name* ] \*
   
   
   
   The Diameter server entity information is configured, including the host name, domain name, IP address, and port number of the server.
4. (Optional) Run [**diameter gx packet**](cmdqueryname=diameter+gx+packet+ignore+dest-host) { **cea** | **ccri** | **ccru** | **ccrt** } \* **ignore dest-host**
   
   
   
   The protocol stack is instructed not to verify the destination host name upon receipt of a CEA packet from the PCRF when a Diameter link is set up and the device is configured not to encapsulate the destination host name into packets (CCR-I, CCR-T, and CCR-U) to be sent to the PCRF.
   
   
   
   When multiple PCRFs work in load balancing mode, you are advised to configure CEA, CCR-I, CCR-T, and CCR-U packets to ensure successful setup of Diameter links.
5. Run [**diameter-server group**](cmdqueryname=diameter-server+group) *group-name*
   
   
   
   A Diameter server group is created, and its view is displayed.
6. Run [**diameter-link**](cmdqueryname=diameter-link) **local** *localname* **peer** *peername* **client-port** *port-number* [ **weight** *weight-value* ]
   
   
   
   A Diameter link is set up between the Diameter client and server.
7. (Optional) Run [**diameter no-send-ccri without subscription-id**](cmdqueryname=diameter+no-send-ccri+without+subscription-id)
   
   
   
   The device is disabled from sending CCR-I packets to a Diameter server for user login after receiving a RADIUS authentication response message that does not carry the Subscription-Id attribute.
8. (Optional) Run [**diameter case-sensitive predefined-rule edsg**](cmdqueryname=diameter+case-sensitive+predefined-rule+edsg)
   
   
   
   The device is enabled to distinguish between uppercase and lowercase names of predefined EDSG rules sent by a Diameter server.
9. (Optional) Run [**diameter gx ccri retransmit enhance**](cmdqueryname=diameter+gx+ccri+retransmit+enhance) *retrans-user-num* **timeout** *retrans-timer-len*
   
   
   
   The number of users (online before the Diameter link goes up) for whom the device retransmits CCR-I or CCR-U messages per second when the Diameter link goes from down to up as well as a retransmission interval are configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.