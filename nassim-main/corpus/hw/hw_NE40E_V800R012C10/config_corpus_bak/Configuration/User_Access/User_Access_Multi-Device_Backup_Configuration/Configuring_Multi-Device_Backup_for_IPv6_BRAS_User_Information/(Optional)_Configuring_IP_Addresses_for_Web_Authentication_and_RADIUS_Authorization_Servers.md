(Optional) Configuring IP Addresses for Web Authentication and RADIUS Authorization Servers
===========================================================================================

The source IP address of the master and backup devices is the same as the BAS-IP address of the web authentication server and the NAS-IP address of the RADIUS authorization server.

#### Context

In hot backup scenarios, the mapping between address pools and BAS-IP addresses must be specified on the web authentication server for each pair of master and backup devices. An IP address pool is shared only by the master and backup devices. Therefore, each pair of master and backup devices must have a source address to communicate with the web authentication server. The source IP address of portal packets sent by a device to the web authentication server can be configured as the BAS-IP address using the **[**web-auth-server**](cmdqueryname=web-auth-server)** { ****source-ipv6**** **source-ipv6**} [ ****vpn-instance**** **vpn-instance** ] command.

In Change-of-Authorization (CoA) and DM applications, the RADIUS authorization server sends requests to the Router, and the Router responds to the RADIUS authorization server. The RADIUS server then checks the source IP address of reply packets for security. In N:1 hot backup scenarios, the RADIUS authorization server determines the IP address of the Router to which authorization packets are sent based on user's bill information. This IP address can be a NAS-IP address or the address that the Router uses to exchange accounting-start packets with the RADIUS server.

To ensure that the RADIUS authorization server sends authorization packets to the exact Router in N:1 scenarios, run the [**radius-authorization source**](cmdqueryname=radius-authorization+source) command to specify a source IP address for each pair of master and backup devices. To ensure that the source IP address in the reply packets sent by the Router to the RADIUS server is the same as the NAS-IP address, run the [**radius-authorization source**](cmdqueryname=radius-authorization+source) **same-as** **nas-logic-ip** command. Alternatively, run the [**radius-authorization source**](cmdqueryname=radius-authorization+source) [ **vpn-instance** *vpn-instance-name* ] *source-ip-address* command to specify a source IP address.

Perform the following operations on both devices that back up each other:


#### Procedure

* Configure the source IP address of portal packets sent by the Router to the web authentication server as the BAS-IP address, which is used independently by the web authentication server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) **loopback** *loopback-number*
     
     
     
     A loopback interface is created, and the interface view is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured for the loopback interface.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the interface view.
  5. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
     
     
     
     The RBS view is displayed.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run **[**web-auth-server**](cmdqueryname=web-auth-server)** { ****source-ipv6**** **source-ipv6**} [ ****vpn-instance**** **vpn-instance** ]
     
     
     
     The loopback interface's IP address is configured as the BAS-IP address to be used independently by the web authentication server.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the source IP address of the master and backup devices to be the same as the NAS-IP address of the RADIUS authorization server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured for the interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the interface view.
  6. Run [**remote-backup-service**](cmdqueryname=remote-backup-service) *service-name*
     
     
     
     The RBS view is displayed.
  7. Run [**radius-authorization source**](cmdqueryname=radius-authorization+source) **same-as** **nas-logic-ip** or [**radius-authorization source**](cmdqueryname=radius-authorization+source) [ **vpn-instance** *vpn-instance-name* ] *source-ip-address*
     
     
     
     The NAS-IP address of the RADIUS authorization server is set to be the same as the source IP address of the master and backup devices.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If a NAS-IP address is specified in the RADIUS server template, run the [**radius-authorization source**](cmdqueryname=radius-authorization+source) **same-as** **nas-logic-ip** command; otherwise, run the [**radius-authorization source**](cmdqueryname=radius-authorization+source) [ **vpn-instance** *vpn-instance-name* ] *source-ip-address* command.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.