(Optional) Configuring an HWTACACS Server Template
==================================================

When configuring an HWTACACS server template, you must specify the IP address, port number, and shared key of a specified HWTACACS server. Other configurations, such as whether the HWTACACS username carries the domain name and the time for the primary server to switch to the active state, have default settings and can be modified as required.

#### Context

You can configure an HWTACACS server template as follows:

* [Configure a shared key for the communication between the device and HWTACACS server.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100602)
* [Configure an IP address for the primary and for the secondary HWTACACS servers](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100611) using either of the following methods:
  
  + Configure IP addresses for the primary and secondary HWTACACS common servers.
  + Configure IP addresses for the primary and secondary HWTACACS authentication servers, primary and secondary HWTACACS authorization servers, and primary and secondary HWTACACS accounting servers.
* [Configure a source address for the device to communicate with the HWTACACS server.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100606)
* [Configure a response timeout period for the HWTACACS server.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100607)
* [Configure a timer value for the primary server to switch to the active state.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100608)
* [Configure the username to be sent to the HWTACACS server to carry the domain name or not.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100609)
* [Modify the password of an HWTACACS user.](#EN-US_TASK_0172371789__dc_vrp_aaa_cfg_100610)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To prevent data transmission risks between the device and HWTACACS server, you are advised to deploy them in a security domain.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**hwtacacs enable**](cmdqueryname=hwtacacs+enable)
   
   
   
   HWTACACS is enabled.
3. Run [**hwtacacs-server service-name**](cmdqueryname=hwtacacs-server+service-name) *service-name*
   
   
   
   The HWTACACS server name is set.
   
   
   
   On an HWTACACS server, a user name can be allocated different rights based on different service names. After the **hwtacacs-server service-name** command is run, a user logging in to the device is allocated a right based on the configured HWTACACS service name.
4. (Optional) Run [**hwtacacs-server default remote-address**](cmdqueryname=hwtacacs-server+default+remote-address)
   
   
   
   A default remote address is configured for the communication between the device (HWTACACS client) and an HWTACACS server.
   
   
   
   When interworking with a third-party TACACS server, the third-party TACACS server may require the rem\_addr field. In this case, you need to run the [**hwtacacs-server default remote-address**](cmdqueryname=hwtacacs-server+default+remote-address) command to configure the default remote address for the HWTACACS client to communicate with the HWTACACS server. When the HWTACACS client sends authentication, authorization, and accounting request packets to the HWTACACS server, if the rem\_addr field in the packets is empty, the configured address is inserted into the rem\_addr field of the packets sent to the HWTACACS server.
5. Run [**hwtacacs-server template**](cmdqueryname=hwtacacs-server+template) *template-name*
   
   
   
   An HWTACACS server template is created, and its view is displayed.
6. Run [**hwtacacs-server shared-key**](cmdqueryname=hwtacacs-server+shared-key) { **cipher** *cipher-string* | *key-string* }
   
   
   
   A shared key is configured for the communication between the device and the HWTACACS server.
   
   
   
   Setting the key improves the security of the communication between the NE40E and the HWTACACS server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure the validity of both parties, the Router and the HWTACACS server must be configured with the same key.
7. You can use either of the following methods to configure an IP address and shared key for the primary/secondary HWTACACS server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When the common server is configured as the primary server, the configurations of the primary authentication, accounting, and authorization servers are deleted. When another type of server (authentication, accounting, or authorization server) is configured as the primary server, the configurations of the common server are deleted.
   * When the common server is configured as the primary server and the server is available, the configurations of other types of servers (authentication, accounting, and authorization servers) do not take effect.
   * The IP addresses and host names of the primary and the secondary servers must be different; otherwise, the server configuration fails.
   * Configure an IP address and a shared key for the primary/secondary HWTACACS common server.
     
     For an IPv4 server, run the [**hwtacacs-server**](cmdqueryname=hwtacacs-server) *ip-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | { **vpn-instance** *vpn-instance-name* | **public-net** } ] \* [ **secondary** ] command.
     
     For an IPv6 server, run the [**hwtacacs-server**](cmdqueryname=hwtacacs-server) *ipv6-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | **vpn-instance** *vpn-instance-name* ]\* [ **secondary** ] command.
   * Configure IP addresses and shared keys for the primary/secondary HWTACACS authentication server, HWTACACS authorization server, and HWTACACS accounting server.
     
     1. Configure an IP address and a shared key for the primary/secondary HWTACACS authentication server.
        + For an IPv4 server, run the [**hwtacacs-server authentication**](cmdqueryname=hwtacacs-server+authentication) { *ip-address* } [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | { **vpn-instance** *vpn-instance-name* | **public-net** } ]\* [ **secondary** ] command.
        + For an IPv6 server, run the [**hwtacacs-server authentication**](cmdqueryname=hwtacacs-server+authentication) *ipv6-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | **vpn-instance** *vpn-instance-name* ]\* [ **secondary** ] command.
     2. Configure an IP address and a shared key for the primary/secondary HWTACACS authorization server.
        + For an IPv4 server, run the [**hwtacacs-server authorization**](cmdqueryname=hwtacacs-server+authorization) { *ip-address* } [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | { **vpn-instance** *vpn-instance-name* | **public-net** } ]\* [ **secondary** ] command.
        + For an IPv6 server, run the [**hwtacacs-server authorization**](cmdqueryname=hwtacacs-server+authorization) *ipv6-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | **vpn-instance** *vpn-instance-name* ]\* [ **secondary** ] command.
     3. Configure an IP address and a shared key for the primary/secondary HWTACACS accounting server.
        + For an IPv4 server, run the [**hwtacacs-server accounting**](cmdqueryname=hwtacacs-server+accounting) *ip-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** { **vpn-instance** *vpn-instance-name* | **public-net** } ]\* [ **secondary** ] command.
        + For an IPv6 server, run the [**hwtacacs-server accounting**](cmdqueryname=hwtacacs-server+accounting) *ipv6-address* [ *port* ] [ **shared-key** { *key-string* | **cipher** *cipher-string* } | **mux-mode** | **vpn-instance** *vpn-instance-name* ]\* [ **secondary** ] command.
8. (Optional) Run [**hwtacacs-server**](cmdqueryname=hwtacacs-server) { **source-ip** *ip-address* | **source-ipv6** *ipv6-address*}
   
   
   
   A source address is configured for the communication between the device and the HWTACACS server.
9. (Optional) Run [**hwtacacs-server timer response-timeout**](cmdqueryname=hwtacacs-server+timer+response-timeout) *value*
   
   
   
   A response timeout period is set for the HWTACACS server.
   
   
   
   If the device does not receive any response from the HWTACACS server within the specified response timeout period, the device considers the HWTACACS server unavailable. In this case, the device attempts to use other methods for authentication, authorization, and accounting.
10. (Optional) Run [**hwtacacs-server timer quiet**](cmdqueryname=hwtacacs-server+timer+quiet) *value*
    
    
    
    A timer value for the primary server to switch to the active state is set.
11. (Optional) Run [**hwtacacs-server user-name domain-included**](cmdqueryname=hwtacacs-server+user-name+domain-included)
    
    
    
    The device is configured to encapsulate the domain name into the username to be sent to the HWTACACS server.
    
    
    
    If the HWTACACS server does not accept the username containing the domain name, you can configure the device to delete the domain name and then send the username without the domain name to the HWTACACS server.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The format of a username is username@domain name.
12. (Optional) Run [**hwtacacs-user change-password hwtacacs-server**](cmdqueryname=hwtacacs-user+change-password+hwtacacs-server) *template-name*
    
    
    
    The password of the HWTACACS user is modified.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.