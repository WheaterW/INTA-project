(Optional) Configuring Global DHCPv4 Parameters
===============================================

Global DHCPv4 parameters include the maximum number of DHCPv4 access users allowed for a specified board and the limit on the packet transmission rate of a DHCPv4 server group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp**](cmdqueryname=dhcp) *slot-id* [**max-sessions**](cmdqueryname=max-sessions) *user-number*
   
   
   
   The maximum number of DHCPv4 users allowed to access a specified board of the device is configured.
3. Run [**dhcp check-client-packet strict**](cmdqueryname=dhcp+check-client-packet+strict)
   
   
   
   The Router is configured to perform strict checks on packets from DHCP clients.
4. Run [**dhcp-server**](cmdqueryname=dhcp-server) *ip-address* [ **vpn-instance** *vpn-instance* ] [**send-discover-speed**](cmdqueryname=send-discover-speed) *packet-number time-value*
   
   
   
   The packet transmission rate of a DHCPv4 server group is limited.
5. Run [**dhcp server identifier dest-ip**](cmdqueryname=dhcp+server+identifier+dest-ip)
   
   
   
   The destination IP address of a packet forwarded by a DHCP relay is configured as the identifier of the DHCP server.
   
   
   
   After the [**dhcp server identifier dest-ip**](cmdqueryname=dhcp+server+identifier+dest-ip) command is run, the DHCP response packet forwarded by the NE40E carries the destination IP address of the request packet as the DHCP server identifier.
   
   This command applies only to the scenario where the NE40E functions as a non-first PE and a DHCP server.
6. Run [**dhcp request-ip-address check**](cmdqueryname=dhcp+request-ip-address+check) { **enable** | **disable** }
   
   
   
   The device is enabled to check or disabled from checking DHCP Request messages carrying Option 50.
   
   
   
   After a large number of users send DHCP Request messages carrying Option 50 to apply for IP addresses and the users pass the authentication, if the Router finds that the requested IP addresses have been assigned to other users, it sends NAK messages to the users. If the [**dhcp request-ip-address check**](cmdqueryname=dhcp+request-ip-address+check) **enable** command is not run and users resend DHCP Discover messages for login, the Router authenticates the users again, causing high CPU usage. After the Router is enabled to check DHCP request packets carrying Option 50, if the request IP addresses have been assigned to other users, the Router replies with NAK messages without authenticating the users again. In this manner, high CPU usage is prevented.
7. (Optional) Run [**dhcp giaddr zero user-type layer2**](cmdqueryname=dhcp+giaddr+zero+user-type+layer2)
   
   
   
   The GiAddr field in the DHCPv4 header is set to 0 when the device sends DHCPv4 messages to Layer 2 access DHCPv4 clients.
8. Run [**access-line-id attach**](cmdqueryname=access-line-id+attach)
   
   
   
   The BRAS is enabled to send Option 82 information to the RADIUS server if user packets do not carry Option 82 or the BRAS does not trust Option 82 information in user packets.
9. (Optional) Run [**dhcp rebind no-user action keep-silence**](cmdqueryname=dhcp+rebind+no-user+action+keep-silence)
   
   
   
   The device is disabled from sending an NAK message in response to a DHCP Rebind message if no corresponding user entry exists on the device.
10. (Optional) Run [**dhcp rebind no-user action nak server-ip**](cmdqueryname=dhcp+rebind+no-user+action+nak+server-ip) *server-ip*
    
    
    
    The device is configured to send a DHCP NAK message in response to a DHCP Rebind message if no corresponding user entry exists on the device.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.