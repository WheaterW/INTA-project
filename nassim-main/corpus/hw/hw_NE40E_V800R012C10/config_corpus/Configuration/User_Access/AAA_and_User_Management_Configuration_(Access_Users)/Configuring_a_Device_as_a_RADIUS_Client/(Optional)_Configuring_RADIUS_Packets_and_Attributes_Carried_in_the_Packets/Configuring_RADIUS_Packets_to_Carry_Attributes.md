Configuring RADIUS Packets to Carry Attributes
==============================================

Configuring RADIUS Packets to Carry Attributes

#### Context

To prevent the RADIUS server from receiving too many attributes that are not required or recognized, many attributes are not sent to the RADIUS server by default. These attributes can be carried in RADIUS packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
3. Configure the device to add specified attributes to RADIUS packets as required.
   
   
   
   **Table 1** Configuring the device to add specified attributes to RADIUS packets
   | Operation | Command |
   | --- | --- |
   | Configure the device to add a new attribute to RADIUS packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) *radius-attribute-name* |
   | Configure the device to add the NAS-IP-Address attribute to accounting-on/accounting-off packets. | [**radius-attribute include nas-ip-address**](cmdqueryname=radius-attribute+include+nas-ip-address) { **accounting-on** | **accounting-off** } \* |
   | Configure the device to add the Event-Timestamp attribute to accounting-on/accounting-off packets. | [**radius-attribute include event-timestamp**](cmdqueryname=radius-attribute+include+event-timestamp) { **accounting-on** | **accounting-off** } |
   | Configure the device to add the HW-Avpair attribute to authentication or accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-avpair** { *hw-avpair-name* *packet-type* | *hw-avpair-name-without-packet-type* } |
   | Configure the device to add the CMCC-NAS-Type attribute to authentication request and accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **cmcc-nas-type** |
   | Configure the device to add the 32-bit Framed-IP-Netmask attribute to accounting request packets. | [**radius-attribute enable**](cmdqueryname=radius-attribute+enable) **framed-ip-netmask** *netmask-length* **account-request** |
   | Configure the device to add the HW-Tunnel-Group-Name, HW-Client-Primary-DNS, or HW-Client-Secondary-DNS attribute to accounting request packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) { **hw-tunnel-group-name** | **hw-client-primary-dns** | **hw-client-secondary-dns** } **accounting-request** |
   | Configure the device to add the HW-DHCP-Option attribute to authentication request packets. | [**radius-attribute include hw-dhcp-option**](cmdqueryname=radius-attribute+include+hw-dhcp-option) *option-num* &<1-16> |
   | Configure the device to add the HW-DHCPv6-Option attribute to authentication request packets. | [**radius-attribute include hw-dhcpv6-option**](cmdqueryname=radius-attribute+include+hw-dhcpv6-option) *v6-option-num* &<1-16> |
   | Configure the device to add the HW-DHCPv6-Option37 attribute to accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-dhcpv6-option37 accounting-request** |
   | Configure the device to add the HW-VPN-Instance attribute to accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-vpn-instance accounting-request** |
   | Configure the device to add the Framed-Route attribute to accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **framed-route accounting-request** |
   | Configure the device to add the HW-Web-URL attribute to accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-web-url accounting-request** |
   | Configure the device to add the HW-Acct-terminate-subcause attribute to accounting stop packets. | [**radius-attribute include hw-acct-terminate-subcause**](cmdqueryname=radius-attribute+include+hw-acct-terminate-subcause) [ **edsg** ] |
   | Configure the device to add users' MAC addresses to EDSG service accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-user-mac edsg accounting-request** |
   | Configure the device to add the Class attribute to EDSG service accounting packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **class** **edsg** |
   | Configure the device to add the Reply-Message attribute to CoA-NAK messages. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **reply-message coa-nak** |
   | Configure the device to add the Reply-Message attribute to ACK packets when a switchover from the CoA-based pre-authentication domain to the authentication domain is performed successfully. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **reply-message** **logon-ack** |
   | Configure the device to add the Reply-Message attribute to CoA Query ACK packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **reply-message** **query-ack** |
   | Configure the device to add the remaining online duration, online duration, and user group information to CoA ACK packets. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) { **session-timeout** | **online-time** | **user-group** } **coa-query-ack** |
   | Configure the device to add the gateway IP address to DHCPv4 authentication packets sent to the RADIUS server. | [**radius-attribute include**](cmdqueryname=radius-attribute+include) **hw-gateway-address** **access-request** |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.