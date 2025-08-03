Configuring Basic SNMPv3 Functions
==================================

After basic SNMP functions are configured, the NMS can perform basic operations such as Get and Set operations on a managed device, and the managed device can send alarms to the NMS.

#### Context

The NMS can communicate with managed devices after basic SNMPv3 functions have been configured.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**snmp-agent password min-length**](cmdqueryname=snmp-agent+password+min-length) *min-length* command to configure the minimum SNMP password length.
   
   
   
   After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.
3. (Optional) Run the [**snmp-agent**](cmdqueryname=snmp-agent) command to enable the SNMP agent service.
   
   
   
   This step is optional because the SNMP agent service can be enabled by running any [**snmp-agent**](cmdqueryname=snmp-agent) command, irrespective of whether any parameter is specified.
4. (Optional) Run the [**snmp-agent udp-port**](cmdqueryname=snmp-agent+udp-port) *port-number* command to change the port number monitored by the SNMP agent.
   
   
   
   If this command is not configured, the default port number is used.
5. (Optional) Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) **version** **v3** command to set the SNMP version.
6. Run the [**snmp-agent group**](cmdqueryname=snmp-agent+group) **v3** *group-name* { **authentication** | **privacy** | **noauthentication** } [ **read-view** *read-view* | **write-view** *write-view* | **notify-view** *notify-view* ] \* [ **acl** { *acl-number* | *acl-name* } ] command to configure an SNMPv3 user group.
   
   
   
   If the NMS and network devices are in an insecure environment (for example, the network is vulnerable to attacks), **authentication** or **privacy** can be configured in the command to enable data authentication or privacy.
   
   The available authentication and privacy modes are as follows:
   * No authentication and no privacy: Neither **authentication** nor **privacy** or **noauthentication** is configured in the command.
   * Authentication without privacy: Only **authentication** is configured in the command. In this mode, only the authenticated administrators can access the managed device.
   * Authentication and privacy: Both **authentication** and **privacy** are configured in the command. In this mode, only the authenticated administrators can access the managed device, and transmitted data is encrypted to guard against tampering and data leaking.
   
   **read-view** needs to be configured in the command if the NMS administrator needs the read permission in a specified view. For example, a low-level administrator needs to read certain data.
   
   **write-view** needs to be configured in the command if the NMS administrator needs the read and write permissions in a specified view. For example, a high-level administrator needs to read and write certain data.
   
   **notify-view** needs to be configured in the command if you want to filter out irrelevant alarms and configure the managed device to send only the alarms of specified MIB objects to the NMS. If the parameter is configured, only the alarms of the MIB objects specified by **notify-view** are sent to the NMS.
7. (Optional) Run the [**snmp-agent local-engineid**](cmdqueryname=snmp-agent+local-engineid) *engineid* command to set an engine ID for the local SNMP entity.
   
   
   
   The MAC address of the management interface on the main control board is used as device information.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To improve system security, run the [**snmp-agent packet contextengineid-check enable**](cmdqueryname=snmp-agent+packet+contextengineid-check+enable) command to check for consistency between the context engine ID and local engine ID.
8. Run the following commands as needed:
   
   
   * On an IPv4 network, a managed device can send alarms in Inform or trap mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The difference between alarms in trap and Inform modes is as follows:
     
     + A managed device does not need to receive a response from the NMS when sending an alarm in trap mode. Therefore, no remote engine ID needs to be configured on the managed device.
     + A managed device needs to receive a response from the NMS when sending an alarm in Inform mode. Therefore, specify the NMS engine ID on the managed device. The remote engine ID must be the same as the engine ID of the destination host that receives the alarm. If the managed device receives no response from the NMS within a timeout period, it resends the alarm until a response is returned or the number of alarms reaches the configured upper limit.
       
       The managed device sends the alarm in Inform mode and records an alarm log at the same time. If the NMS or a link fails, the NMS can synchronize alarms generated during this period after the fault is rectified.
     
     Therefore, the alarm in Inform mode is more reliable than that in trap mode. However, a device needs to cache massive alarm messages and consume a great number of memory resources due to the retransmission mechanism.
     
     If the network environment is stable, sending alarms in trap mode is recommended. If device resources are sufficient and the network environment is unstable, sending alarms in Inform mode is recommended.
     
     The same destination host cannot be configured for Inform and trap messages. If the Inform and trap messages share the same destination host, the latest configuration overrides the previous configuration.
     
     
     Configure an alarm in trap mode.
     1. Run the [**snmp-agent**](cmdqueryname=snmp-agent) **usm-user v3** *user-name* *group-name* [ **authentication-mode** *authen-protocol* *authKey* [ **privacy-mode** *privacy-protocol* *privKey* ] ] [ **acl** { *acl-number* | *aclName* } ] command to configure an SNMP USM user and configure an authentication mode, an encryption mode, and passwords for the user.
     2. Run the [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **trap** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ **source** *interface-type* *interface-number* ] | [ **public-net** | **vpn-instance** *vpn-instance-name* ] ] \* **params** **securityname** { *security-name* [ **v3** [ **authentication** | **privacy** ] ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* } \* command to specify a destination host to which the device sends traps and error codes.
     
     Configure an alarm in Inform mode.
     
     1. Run the [**snmp-agent**](cmdqueryname=snmp-agent) [ **remote-engineid** *engine-Id* ] **usm-user v3** *user-name* *group-name* [ **authentication-mode** *authen-protocol* *authKey* [ **privacy-mode** *privacy-protocol* *privKey* ] ] [ **acl** { *acl-number* | *aclName* } ] command to configure an SNMP USM user and configure an authentication mode, an encryption mode, and passwords for the SNMP USM user.
     2. Run the [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **inform** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* ] | [ **source** *interface-type* *interface-number* ] | [ **public-net** | **vpn-instance** *vpn-instance-name* ] ] \* **params** **securityname** { *security-name* { **v3** [ **authentication** | **privacy** ] } } [ **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \* command to specify a destination host to which a device sends Inform alarms and error codes.
   * On an IPv6 network, alarms can be sent in trap mode.
     1. Run the [**snmp-agent usm-user**](cmdqueryname=snmp-agent+usm-user) **v3** *user-name* *group-name* [ **authentication-mode** *authen-protocol* *authKey* [ **privacy-mode** *privacy-protocol* *privKey* ] ] [ **acl** { *acl-number* | *acl-name* } ] command to configure an SNMP USM user and configure an authentication mode, an encryption mode, and passwords for the user.
     2. Run the [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **trap** **ipv6** **address** **udp-domain** *ipv6-address* [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | **source** *interface-type* *interface-number* ] \* **params** **securityname** { *security-name* [ **v3** [ **authentication** | **privacy** ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* } command to specify a destination host to which the device sends traps and error codes.
   * On an IPv6 network, alarms can be sent only in Inform mode.
     1. Run the [**snmp-agent**](cmdqueryname=snmp-agent) [ **remote-engineid** *engine-Id* ] **usm-user v3** *user-name* *group-name* [ **authentication-mode** *authen-protocol* *authKey* [ **privacy-mode** *privacy-protocol* *privKey* ] ] [ **acl** { *acl-number* | *aclName* } ] command to configure an SNMP USM user and configure an authentication mode, an encryption mode, and passwords for the SNMP USM user.
     2. Run the **[**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host)** [ **host-name** *host-name* ] **inform** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port** *server-port* ] | [ **vpn-instance** *vpn-instance-name* | **public-net** ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-name* **v2c** } [ [ **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* ] \* command to specify a destination host to which the device sends Informs and error codes.
   
   The following parameters can be configured as needed:
   
   * **udp-port** needs to be configured to change the default UDP port number of 162 to a non-well-known port number to meet special requirements.
   * **public-net** needs to be configured to allow a device that an NMS manages to send traps through a public network to the NMS. Alternatively, **vpn-instance** *vpn-instance-name* needs to be configured to allow the device that an NMS manages to send traps through a private network to the NMS.
   * **securityname** needs to be configured to identify a source device that sends traps.
   * **private-netmanager** needs to be configured to allow alarm messages to carry more information when the NMS and a device that the NMS manages are both Huawei devices. Alarm messages can carry alarm types, sequence number, and time when a message was sent. The information helps rectify faults.
   * **notify-filter-profile** needs to be configured to allow a device to send desired alarms to the NMS host, which reduces irrelevant alarms and speeds up fault identification. **notify-view** needs to be configured to allow the alarm filter policy to take effect when you configure a user group.
   
   To disable the password complexity check, run the [**snmp-agent usm-user password complexity-check disable**](cmdqueryname=snmp-agent+usm-user+password+complexity-check+disable) command. However, enabling this function is recommended as this improves system security.
   
   To improve system security, it is recommended that you configure different authentication and encryption passwords for an SNMP USM user.
9. (Optional) Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) { **contact** *contact* | **location** *location* } command to configure the device administrator contact information or location is configured.
   
   
   
   Configuring this information helps the NMS administrator contact the device administrators for fault locating and rectification, especially if the NMS manages many devices.
10. (Optional) Run the [**snmp-agent packet max-size**](cmdqueryname=snmp-agent+packet+max-size) *byte-count* command to set the maximum size of an SNMP packet that the device can receive or send.
    
    
    
    After the maximum size is set, the device discards any SNMP packet that is larger than the set size.
11. Configure SNMP to receive and respond to NMS request packets. To achieve this, run one or more of the following commands as needed:
    
    
    * To configure a source interface for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-interface) *protocol-interface-type* *protocol-interface-number* command.
    * To configure all interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status+all-interface) command.
    * To specify an isolated source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ipv4-address* command.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded.
    * To specify an IPv6 source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command.
    * To specify an isolated IPv6 source address for SNMP to receive and respond to request packets from the CCU, run the [**snmp-agent protocol ipv6 physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+ipv6+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ip-address* command.
    * To configure all IPv6 interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status+ipv6+all-interface) command.
    * Configure SNMP to receive and respond to NMS request packets through a VPN instance or public network.
      + For an IPv4 network, run the [**snmp-agent protocol**](cmdqueryname=snmp-agent+protocol) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
      + For an IPv6 network, run the [**snmp-agent protocol ipv6**](cmdqueryname=snmp-agent+protocol+ipv6) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In scenarios such as interface unnumbered, if an isolated source interface and a common source interface (non-isolated source interface) are configured to listen to the same IP address and VPN instance, the common source interface takes effect. When the TCP listening mode is set to all-interface and an isolated source interface is configured, the isolated source interface takes effect if it is matched based on the 5-tuple matching rule; the all-interface configuration takes effect if the isolated source interface is not matched based on the 5-tuple matching rule. The source IP address specified for the isolated source interface does not need to be the interface's IP address.
12. (Optional) Run the [**snmp-agent extend error-code enable**](cmdqueryname=snmp-agent+extend+error-code+enable) command to enable the extended error code function.
13. (Optional) Run the [**snmp-agent set-cache enable**](cmdqueryname=snmp-agent+set-cache+enable) command to enable the SET response message caching function.
14. (Optional) Run the [**snmp-agent protocol get-bulk timeout**](cmdqueryname=snmp-agent+protocol+get-bulk+timeout) *time* command to configure a get-bulk operation timeout period.
    
    
    
    You are advised not to change the get-bulk operation timeout period. The default get-bulk operation timeout period (2s) is recommended. To reconfigure a get-bulk operation timeout period, you must ensure that the configured period is less than an NMS's timeout period.
15. (Optional) Run the [**snmp-agent protocol server**](cmdqueryname=snmp-agent+protocol+server) [ **ipv4** | **ipv6** ] [**disable**](cmdqueryname=disable) command to disable the SNMP IPv4 or IPv6 listening port.
    
    
    
    After you disable the SNMP IPv4 or IPv6 listening port using the [**snmp-agent protocol server disable**](cmdqueryname=snmp-agent+protocol+server+disable) command, SNMP no longer processes SNMP packets. Exercise caution when you disable the SNMP IPv4 or IPv6 listening port.
16. (Optional) Configure the SNMP proxy for receiving and responding to requests from the CCU.
    
    
    * IPv4 network
      + Run the [**snmp-agent proxy protocol source-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-interface) { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* } command to specify a source interface for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+all-interface) command to allow all interfaces to be used by the SNMP proxy to receive and respond to IPv4 packets from the CCU.
    * IPv6 network
      + Run the [**snmp-agent proxy protocol ipv6 source-ip**](cmdqueryname=snmp-agent+proxy+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command to specify an IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+ipv6+all-interface) command to allow all IPv6 interfaces to be used by the SNMP proxy to receive and respond to IPv6 requests from the CCU.
17. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

After the configuration is complete, the NMS and managed device can communicate.

* Access control allows any NMS that uses the community name to monitor and manage all the objects on the managed device.
* The managed device sends alarms generated by the modules that are enabled by default to the NMS.

If finer device management is required, follow directions below to configure the managed device:

* To allow a specified NMS that uses the community name to manage specified objects on the device, follow the procedure described in [Controlling the NMS's Access to the Device](dc_vrp_snmp_cfg_0017.html).
* To allow a specified module on the managed device to report alarms to the NMS, follow the procedure described in [Configuring the Trap Function](dc_vrp_snmp_cfg_2007.html) or [Configuring the Inform Function](dc_vrp_snmp_cfg_1013.html).