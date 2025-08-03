(Optional) Configuring RADIUS Dynamic Authorization
===================================================

(Optional) Configuring RADIUS Dynamic Authorization

#### Context

Authentication response packets sent by a RADIUS server that performs user authorization carry authorization information. For dynamic services, you need to configure a RADIUS authorization server so that it can dynamically authorize users who use such services.

When a user is online, the device can dynamically modify the authorization information about the user. Such modification is called Change of Authorization (CoA). While maintaining the online status of users, the network administrator can modify service attributes on the RADIUS server, which then sends CoA messages to dynamically change the services used by users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server authorization**](cmdqueryname=radius-server+authorization) *ip-address* [ **vpn-instance** *string* ] [ **destination-ip** *destination-ip-addr* ] [ **destination-port** *destination-port-id* ] { { **shared-key** *key* | **shared-key-cipher** { **key2** | *key3* } } | **server-group** *groupname* } \* [ **ack-reserved-interval** *interval* ]
   
   
   
   A global RADIUS authorization server is configured.
   
   
   
   * To retain RADIUS authorization response packets for retransmitted packets of the RADIUS authorization server, configure the **ack-reserved-interval** *interval* parameter.
   * If **destination-ip** *destination-ip-addr* or **destination-port** *destination-port-id* has been configured, the device checks the destination IP address or port number in the CoA messages and discards the messages if the destination IP address or port number does not match.
3. (Optional) Run [**radius-server authorization error-reply**](cmdqueryname=radius-server+authorization+error-reply) { **version1** | **version2** }
   
   
   
   The method for the device to respond to CoA messages is configured.
4. (Optional) Run [**radius-server authorization accounting-realtime-packet disable**](cmdqueryname=radius-server+authorization+accounting-realtime-packet+disable)
   
   
   
   The device is disabled from automatically responding with a real-time accounting packet upon receipt of a CoA message delivered by the RADIUS server.
5. (Optional) Run [**accounting interim interval**](cmdqueryname=accounting+interim+interval) *interval* [ **second** ] [ **traffic** ] [ **hash** ]
   
   
   
   The device is enabled to notify the RADIUS server of the latest user status within a specified period.
   
   
   
   After the [**radius-server authorization accounting-realtime-packet disable**](cmdqueryname=radius-server+authorization+accounting-realtime-packet+disable) command is run, the device does not automatically respond with a real-time accounting packet upon receipt of a CoA message from the RADIUS server. As a result, the RADIUS server cannot learn the latest user status in a timely manner. To solve this problem, run this command.
6. (Optional) Run [**radius-server coa update username**](cmdqueryname=radius-server+coa+update+username)
   
   
   
   The device is enabled to update usernames based on those delivered in CoA messages and switch users to the domains carried in the RADIUS-delivered usernames.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.