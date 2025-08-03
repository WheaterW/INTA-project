(Optional) Configuring Users with the Same MAC Address to Go Online Again
=========================================================================

(Optional) Configuring Users with the Same MAC Address to Go Online Again

#### Context

When an STB is quickly powered off and then restarted, the NE40E cannot detect the user logout and retains the user entry. When the STB is restarted, the user goes online again. After a new account is obtained from the NMS, a Discover or Request message is sent. At this time, the user access domain of the new account may have changed. When receiving the message, the NE40E finds that a user entry with the same MAC address already exists. As such, the NE40E does not verify the Option 60 field but directly returns an ACK message. In this case, the user remains online in the initial domain but cannot access network resources. To resolve this problem, you can configure the NE40E to log out an online user upon receipt of a Discover or Request message from a user with the same MAC address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**dhcp**](cmdqueryname=dhcp) { **discover** | **reboot-request** }\* **user offline**
   
   
   
   The device is configured to log out an online user upon receipt of a Discover or Request message from a client with the same MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.