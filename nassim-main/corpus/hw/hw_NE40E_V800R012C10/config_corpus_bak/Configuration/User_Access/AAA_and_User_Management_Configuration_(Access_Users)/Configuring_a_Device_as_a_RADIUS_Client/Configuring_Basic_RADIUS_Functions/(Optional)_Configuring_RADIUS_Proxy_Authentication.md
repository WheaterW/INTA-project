(Optional) Configuring RADIUS Proxy Authentication
==================================================

(Optional)_Configuring_RADIUS_Proxy_Authentication

#### Context

In some cases, different devices may be used to perform authentication and accounting for users. For example, the AC is responsible for user authentication, while the BRAS is responsible for user accounting. To eliminate the redundancy of both devices sending authentication packets to the RADIUS server, you can configure the device that performs user accounting (the BRAS in this example) as a RADIUS proxy. The RADIUS proxy then records authentication information of users when forwarding RADIUS authentication packets. The BRAS with RADIUS proxy authentication configured transparently transmits RADIUS packets from a specified RADIUS client to the RADIUS server, records authorization information delivered by the RADIUS server, and transparently transmits authentication response packets. If the authentication mode configured in the user domain of the BRAS is radius-proxy, the BRAS can use the recorded authorization information to authorize users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, RADIUS proxy authentication takes effect only for IPoE users.

In RADIUS proxy scenarios, RADIUS authentication and accounting packets sent by the AC and response packets received from the RADIUS server are sent to the MPU of the BRAS for processing. Adjust bandwidth parameters if the defaults do not meet service requirements by referring to [(Optional) Configuring RADIUS CAR](dc_ne_aaa_cfg_0624.html).



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-client**](cmdqueryname=radius-client) *ip-address* [ **mask** { *mask-ip* | *mask-length* } ] [ **vpn-instance** *instance-name* ] { { **shared-key** *key* | **shared-key-cipher** *key-string-cipher* } | **server-group** *groupname* | **roam-domain** *domain-name* | **domain-authorization** | **trigger-web** { **authentication** | **accounting** | **none** } } \*
   
   
   
   A RADIUS client is configured, including the IP address, VPN instance, shared key, and RADIUS server group.
3. (Optional) Run [**radius-client check-attribute-length loose**](cmdqueryname=radius-client+check-attribute-length+loose) [ **correct-forwarding** ]
   
   
   
   Loose check and correction of the length of attributes carried in authentication or accounting request packets are configured.
4. (Optional) Run [**radius-client packet dscp**](cmdqueryname=radius-client+packet+dscp) *dscp-value*
   
   
   
   A DSCP value is configured for RADIUS packets sent from the BRAS to the AP/AC.
5. (Optional) Run [**radius-client proxy-user aging-time**](cmdqueryname=radius-client+proxy-user+aging-time) *time*
   
   
   
   The aging time of RADIUS proxy users is configured.
6. (Optional) Run [**radius-client nas-ip-address from packet**](cmdqueryname=radius-client+nas-ip-address+from+packet) { **source-ip** | **radius-attribute** }
   
   
   
   A value source is configured for the destination IP address and NAS-IP-Address attribute in a logout request packet to be sent from the BAS to the radio controller in RADIUS proxy scenarios.
7. (Optional) Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
8. (Optional) Run [**access-speed adjustment system-state radius-proxy active-session threshold restrain**](cmdqueryname=access-speed+adjustment+system-state+radius-proxy+active-session+threshold+restrain) *restrain-threshold-value* **resume** *resume-threshold-value*
   
   
   
   The suppression and restoration thresholds for the number of active RADIUS proxy sessions are configured.
9. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
10. (Optional) Run [**radius-client nas-ip-address from packet**](cmdqueryname=radius-client+nas-ip-address+from+packet) { **source-ip** | **radius-attribute** }
    
    
    
    A value source is configured for the NAS-IP-Address attribute in a logout request packet to be sent from the BAS to the radio controller in RADIUS proxy authentication scenarios.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.