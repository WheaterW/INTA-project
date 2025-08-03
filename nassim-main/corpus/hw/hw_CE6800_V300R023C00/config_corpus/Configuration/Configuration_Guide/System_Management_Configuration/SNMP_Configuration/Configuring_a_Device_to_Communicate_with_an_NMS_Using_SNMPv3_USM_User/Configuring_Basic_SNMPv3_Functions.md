Configuring Basic SNMPv3 Functions
==================================

Configuring Basic SNMPv3 Functions

#### Prerequisites

Before configuring a device to communicate with an NMS using SNMPv3 USM user, configure a routing protocol to ensure that at least one route exists between the device and NMS.


#### Context

The NMS manages a device in the following ways:

* Sends requests to the managed device to perform the GetRequest, GetNextRequest, GetResponse, GetBulk, or SetRequest operation to obtain data or set values.
* Passively receives alarms (traps or informs) from the managed device to locate and handle device faults based on the alarm information.

After basic SNMP functions are configured, an NMS can perform basic operations (such as Get and Set operations) on a managed device, and the managed device can send alarms to the NMS.

After basic SNMP functions are configured, the NMS can communicate with the managed device.

The parameters **md5**, **sha**, **sha2-224**, **DES56**, and **3DES168** in the [**snmp-agent usm-user**](cmdqueryname=snmp-agent+usm-user) command can be used only after the weak security algorithm or protocol feature package (WEAKEA) is installed by running the **install feature-software WEAKEA** command.

After the weak password dictionary maintenance function is enabled, the password configured using the [**snmp-agent usm-user**](cmdqueryname=snmp-agent+usm-user) command cannot be any passwords defined in the weak password dictionary. (You can run the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command to view the passwords defined in the weak password dictionary.)


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Set the minimum SNMP password length.
   
   
   ```
   [snmp-agent password min-length](cmdqueryname=snmp-agent+password+min-length) min-length
   ```
   
   After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.
3. (Optional) Start the SNMP agent service.
   
   
   ```
   [snmp-agent](cmdqueryname=snmp-agent)
   ```
   
   By default, the SNMP agent service is disabled. Running any [**snmp-agent**](cmdqueryname=snmp-agent) configuration command (regardless of whether parameters are specified) starts the SNMP agent service. Therefore, this step is optional.
4. (Optional) Change the listening port number of the SNMP agent.
   
   
   ```
   [snmp-agent udp-port](cmdqueryname=snmp-agent+udp-port) port-number
   ```
   
   The default listening port number of the SNMP agent is 161. If this command is not configured, the default listening port number is used.
5. Configure an SNMP version.
   
   
   ```
   [snmp-agent sys-info](cmdqueryname=snmp-agent+sys-info) version v3
   ```
   
   By default, SNMPv3 is used.
6. Configure an SNMP user group.
   
   
   ```
   [snmp-agent group](cmdqueryname=snmp-agent+group) v3 group-name { authentication | privacy | noauthentication } [ read-view read-view | write-view write-view | notify-view notify-view ] * [ acl { acl-number | acl-name } ]
   ```
   
   If the NMS and network devices are in an insecure environment (for example, the network is vulnerable to attacks), **authentication** or **privacy** can be configured in the command to enable data authentication or privacy.
   
   The available authentication and privacy modes are as follows:
   * No authentication and no privacy: Neither **authentication** nor **privacy** or **noauthentication** is configured in the command. This mode is applicable to secure networks managed by a specified administrator.
   * Authentication without privacy: Only **authentication** is configured in the command. This mode is applicable to secure networks managed by many administrators who may frequently perform operations on the same device. In this mode, only the authenticated administrators can access the managed device.
   * Authentication and privacy: Both **authentication** and **privacy** are configured in the command. This mode is applicable to insecure networks managed by many administrators who may frequently perform operations on the same device. In this mode, only the authenticated administrators can access the managed device, and transmitted data is encrypted to guard against tampering and data leaking.
   
   If the NMS administrator needs the read permission in a specified view, configure **read-view** in this command. For example, a low-level administrator needs to read certain data.
   
   If the NMS administrator needs the read and write permissions in a specified view, configure **write-view** in this command. For example, a high-level administrator needs to read and write certain data.
   
   **notify-view** needs to be configured in the command if you want to filter out irrelevant alarms and configure the managed device to send only the alarms of specified MIB objects to the NMS. If the parameter is configured, only the alarms of the MIB objects specified by **notify-view** are sent to the NMS.
7. (Optional) Set the engine ID of the local SNMP entity.
   
   
   ```
   [snmp-agent local-engineid](cmdqueryname=snmp-agent+local-engineid) engineid
   ```
   
   
   
   By default, the system uses the internal algorithm to automatically generate a device engine ID, which includes the enterprise ID and device information. The system uses the MAC address of the management interface on a device as the device information of the engine ID.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To improve system security, run the [**snmp-agent packet contextengineid-check enable**](cmdqueryname=snmp-agent+packet+contextengineid-check+enable) command to check for consistency between the context engine ID and local engine ID.
8. Run one of following commands as needed:
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The differences between alarms in trap and Inform modes are as follows:
   
   * A managed device does not need to receive a response from the alarm host when sending an alarm in trap mode. Therefore, **remote-engineid** does not need to be configured.
   * A managed device needs to receive a response from the alarm host when sending an alarm in Inform mode. Therefore, specify the engine ID of the alarm host on the managed device. This means that **remote-engineid** must be the same as the engine ID of the alarm host that receives the alarm. If the managed device receives no response from the NMS within a timeout period, it resends the alarm until a response is returned or the number of sent alarms reaches the maximum number of allowed retransmissions.
     
     At the same time as sending an alarm in Inform mode, a managed device also records an alarm log. If the NMS or a link fails, the NMS can synchronize alarms generated during the fault period after the fault is rectified.
   
   Although the Inform mode is more reliable than the trap mode for sending alarms, it may cause the device to cache many alarm messages due to the Inform mode's retransmission mechanism, consuming a lot of memory resources.
   
   If the network environment is stable, sending alarms in trap mode is recommended. If device resources are sufficient but the network environment is unstable, sending alarms in Inform mode is recommended.
   
   The same target host cannot be configured for Inform and trap messages. Otherwise, the latest configuration overrides the previous configuration.
   
   * On an IPv4 network, a device can be configured to send alarms in Inform or trap mode.
     
     Configure the device to send alarms in trap mode.
     ```
     [snmp-agent usm-user](cmdqueryname=snmp-agent+usm-user) v3 user-name group-name [ authentication-mode { md5 | sha | sha2-224 | sha2-256 | sha2-384 | sha2-512 } password [ privacy-mode { des56 | 3des168 | aes128 | aes192 | aes256 } password ] ] [ acl { acl-number | acl-name } ]
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ host-name host-name ] trap address udp-domain ip-address [ [ udp-port port-number | [ alarm-udp-port alarm-port-number | event-udp-port event-port-number ] *] | [ { [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name | [public-net](cmdqueryname=public-net) } ] | [ [source](cmdqueryname=source) { interface-name | interface-type interface-number } ] ] * params securityname { security-name [ v3 [ authentication | privacy ] | private-netmanager | ext-vb | notify-filter-profile profile-name | [heart-beat enable](cmdqueryname=heart-beat+enable) ] * }
     ```
     
     Configure the device to send alarms in Inform mode.
     
     ```
     [snmp-agent](cmdqueryname=snmp-agent) remote-engineid remote-engineid-name usm-user v3 user-name group-name [ authentication-mode { md5 | sha  | sha2-224 | sha2-256 | sha2-384 | sha2-512 } password [ privacy-mode { des56 | 3des168 | aes128 | aes192 | aes256 } password ] ] [ acl { acl-number | acl-name } ]
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ host-name host-name  ] inform address udp-domain ip-address [ [ udp-port server-port ] | [ vpn-instance vpn-instance-name | public-net ] | [ source interface-type interface-number ] ] * params securityname security-name v3 [ authentication | privacy ] [ [ private-netmanager| ext-vb | notify-filter-profile profile-name | heart-beat enable ] * ] *
     ```
   * On an IPv6 network, a device can be configured to send alarms in Inform or trap mode:
     
     Configure the device to send alarms in trap mode.
     
     ```
     [snmp-agent usm-user](cmdqueryname=snmp-agent+usm-user) v3 user-name group-name [ authentication-mode { md5 | sha | sha2-224 | sha2-256 | sha2-384 | sha2-512} password [ privacy-mode { des56 | 3des168 | aes128 | aes192 | aes256 } password ] ] [ acl { acl-number | acl-name } ]
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ host-name host-name ] trap ipv6 address udp-domain ipv6-address [ [ udp-port port-number | [ alarm-udp-port alarm-port-number | event-udp-port event-port-number ] *] | [ vpn-instance vpn-instance-name | public-net ]  ] * params securityname { security-name [ v3 [ authentication | privacy ] | ext-vb | notify-filter-profile profile-name | private-netmanager ] * }
     ```
     
     Configure the device to send alarms in Inform mode.
     
     ```
     [snmp-agent](cmdqueryname=snmp-agent) remote-engineid remote-engineid-name usm-user v3 user-name group-name [ authentication-mode { md5 | sha  | sha2-224 | sha2-256 | sha2-384 | sha2-512 } password [ privacy-mode { des56 | 3des168 | aes128 | aes192 | aes256 } password ] ] [ acl { acl-number | acl-name } ]
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ host-name host-name ] inform ipv6 address udp-domain ipv6-address [ [ udp-port server-port ] | [ vpn-instance vpn-instance-name | public-net ] | [ source { interface-name | interface-type interface-number } ] ] * params securityname security-name  v3 [ authentication | privacy ] [ [ private-netmanager | ext-vb | notify-filter-profile profile-name ] * ] *
     ```
     
     By default, a device checks the complexity of USM users' authentication and encryption passwords. The configured passwords must meet the password complexity requirements. To disable the password complexity check, run the [**snmp-agent usm-user password complexity-check disable**](cmdqueryname=snmp-agent+usm-user+password+complexity-check+disable) command. However, enabling this function is recommended as this improves system security.
     
     To improve system security, you are advised to configure different encryption and authentication passwords for an SNMP USM user.The parameters can be set as follows:
   * **udp-port** needs to be set to a non-well-known port number if special requirements need to be met (default port number: 162). You can also configure **alarm-udp-port** and **event-udp-port** for different types of reported contents (alarms and events) to change the port number for receiving alarms and events to a specified port number.
   * **public-net** needs to be specified if the managed device sends alarms to the NMS through a public network. Alternatively, **vpn-instance** *vpn-instance-name* needs to be specified if the managed device sends alarms to the NMS through a private network.
   * **securityname** needs to be configured to identify a source device that sends alarms.
   * **private-netmanager** needs to be specified if the NMS and managed device are both provided by Huawei. In this way, alarm messages can carry more information (for example, the alarm type, sequence number, and sending time). Such information helps rectify faults.
   * **notify-filter-profile** needs to be specified if you want the device to send only desired alarms to the NMS, thereby reducing irrelevant alarms and speeding up fault identification. **notify-view** needs to be specified to allow the alarm filter policy to take effect when you configure a user group.
9. (Optional) Configure the contact and location information of the device administrator.
   
   
   ```
   [snmp-agent sys-info](cmdqueryname=snmp-agent+sys-info) { contact contact | location location }
   ```
   
   Configuring this information helps the NMS administrator contact the device administrators for fault locating and rectification, especially if the NMS manages many devices.
10. (Optional) Set the maximum size of an SNMP message that can be received or sent by the device.
    
    
    ```
    [snmp-agent packet max-size](cmdqueryname=snmp-agent+packet+max-size) byte-count
    ```
    
    
    
    By default, the maximum size of an SNMP message that the device can receive or send is 12000 bytes.
    
    After the maximum size is set, the device discards any SNMP message that is larger than the set size.
11. Configure a source interface for the SNMP agent to receive and respond to NMS request packets.
    
    
    
    **Table 1** Configuring a source interface for the SNMP agent to receive and respond to NMS request packets
    | Operation | Command |
    | --- | --- |
    | Specify the source interface for SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-status) { *protocol-interface-type protocol-interface-number* | *protocol-interface-name* } |
    | Enable all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
    | Specify an IPv6 source address for SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+source-status) *ip-address* [ **vpn-instance** *vpn-instance-name* ] |
    | Enable all IPv6 interfaces on the device to be used by SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
    
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    You are advised not to use all interfaces to receive and respond to NMS request messages. Specifying a source interface is recommended.
12. (Optional) Enable the SNMP extended error code function.
    
    
    ```
    [snmp-agent extend error-code enable](cmdqueryname=snmp-agent+extend+error-code+enable)
    ```
    
    
    
    By default, SNMP sends standard error codes to an NMS. The extended error code function allows an SNMP device to send extended error codes to the NMS.
13. (Optional) Enable the function to cache Set response packets.
    
    
    ```
    [snmp-agent set-cache enable](cmdqueryname=snmp-agent+set-cache+enable)
    ```
    
    
    
    By default, the function to cache Set response packets is disabled.
14. (Optional) Set a Get-Bulk operation timeout period.
    
    
    ```
    [snmp-agent protocol get-bulk timeout](cmdqueryname=snmp-agent+protocol+get-bulk+timeout) time
    ```
    
    The default Get-Bulk operation timeout period is 2s. Using the default Get-Bulk operation timeout period is recommended. If you need to change the Get-Bulk operation timeout period, ensure that the configured period is less than an NMS's timeout period.
15. (Optional) Disable the SNMP IPv4 or IPv6 listening port.
    
    
    ```
    [snmp-agent protocol server](cmdqueryname=snmp-agent+protocol+server+disable) [ ipv4 | ipv6 ] [disable](cmdqueryname=disable)
    ```
    
    
    
    After you disable the SNMP IPv4 or IPv6 listening port using the [**snmp-agent protocol server disable**](cmdqueryname=snmp-agent+protocol+server+disable) command, SNMP no longer processes SNMP packets. Exercise caution when running this command.
16. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```