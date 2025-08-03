Configuring Basic SNMPv3 Functions
==================================

Basic SNMPv3 functions can be configured to allow an NMS to monitor and operate a managed device.

#### Context

Before a local SNMPv3 user is configured on a device to communicate with an NMS, the user must be added to a user group at the AAA side, and the user group is associated with a specific task group. The task group consists of multiple tasks, and each task is mapped to a MIB object that is granted reading and writing permissions. Users assigned a specific task obtain the specified reading and writing permissions on MIB objects.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**aaa**](cmdqueryname=aaa) command to enable AAA and enter the AAA view.
3. Run the [**task-group**](cmdqueryname=task-group) *task-group-name* command to create a task group and enter its view.
4. Run the [**task**](cmdqueryname=task) **snmp** { **read | write | execute | debug** } \* command to add a task to the task group and granted permissions.
   
   
   
   Each MIB object is associated with a specific task. This step can be performed to grant permissions to SNMP MIB objects.
5. Run the [**quit**](cmdqueryname=quit) command to return to the AAA view.
6. Run the [**user-group**](cmdqueryname=user-group) *user-group-name* command to create a user group and enter its view.
7. Run the [**task-group**](cmdqueryname=task-group) *task-group-name* command to associate the user group with the task group.
8. Run the [**quit**](cmdqueryname=quit) command to return to the AAA view.
9. Run the [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ] command to create a local user and a password for the user to log in a device.
   
   
   
   If the AAA user is configured as a local SNMP user, the length of *user-name* ranges from 1 to 32 characters.
10. Run the [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *user-group-name* command to add the local user to the specified user group.
    
    
    
    One user group can be used by multiple local users. However, each local user can belong to only one user group.
11. Run the [**local-user**](cmdqueryname=local-user) *user-name* **level** *level* command to configure the level of the local user.
12. Run the [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **snmp** command to set the access type of the local user to SNMP.
13. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
14. (Optional) Run the [**snmp-agent**](cmdqueryname=snmp-agent) command to enable the SNMP agent service.
    
    
    
    This step is optional because the SNMP agent service can be enabled by running any [**snmp-agent**](cmdqueryname=snmp-agent) command, irrespective of whether any parameter is specified.
15. (Optional) Run the [**snmp-agent password min-length**](cmdqueryname=snmp-agent+password+min-length) *min-length* command to configure the minimum SNMP password length.
    
    
    
    After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.
16. (Optional) Run the [**snmp-agent udp-port**](cmdqueryname=snmp-agent+udp-port) *port-number* command to change the port number monitored by the SNMP agent.
    
    
    
    If this command is not configured, the default port number is used.
17. (Optional) Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) **version** **v3** command to set the SNMP version.
18. Run the [**snmp-agent local-user**](cmdqueryname=snmp-agent+local-user) **v3** *local-user-name* **authentication-mode** *authen-protocol* { **privacy-mode** *privacy-protocol* | **cipher** *authKey* **privacy-mode** *privacy-protocol* **cipher** privKey } command to configure local SNMP user information.
    
    
    
    The authentication password configured for an AAA user can be different from that for a local SNMP user. Deleting a local AAA user causes the local SNMP user to be also deleted. Deleting a local SNMP user, however, does not affect the local AAA user.
    
    The priority of an SNMP USM user is higher than that of a local SNMP user. Consequently, if an SNMP USM user and a local SNMP user have the same username but different authentication and encryption passwords, the SNMP USM user's authentication and encryption passwords are used for login.
    
    A device checks the complexity of the local users' authentication and encryption passwords. The configured passwords must meet the password complexity requirements. To disable the password complexity check, run the [**snmp-agent local-user password complexity-check disable**](cmdqueryname=snmp-agent+local-user+password+complexity-check+disable) command. However, enabling this function is recommended as this improves system security.
    
    To improve system security, it is recommended that you configure different authentication and encryption passwords for a local SNMP user.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In this command, the authentication algorithms MD5, SHA, and SHA2-224 and the encryption algorithms DES56 and 3DES168 are weak security algorithms and are not recommended. To configure a weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
19. (Optional) Configure the SNMP proxy for receiving and responding to requests from the CCU.
    
    
    * IPv4 network
      + Run the [**snmp-agent proxy protocol source-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-interface) { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* } command to specify a source interface for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+all-interface) command to allow all interfaces to be used by the SNMP proxy to receive and respond to IPv4 packets from the CCU.
    * IPv6 network
      + Run the [**snmp-agent proxy protocol ipv6 source-ip**](cmdqueryname=snmp-agent+proxy+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command to specify an IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+ipv6+all-interface) command to allow all IPv6 interfaces to be used by the SNMP proxy to receive and respond to requests from the CCU.
20. (Optional) Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) { **contact** *contact* | **location** *location* } command to configure the device administrator contact information or location is configured.
    
    
    
    Configuring this information helps the NMS administrator contact the device administrators for fault locating and rectification, especially if the NMS manages many devices.
21. (Optional) Run the [**snmp-agent packet max-size**](cmdqueryname=snmp-agent+packet+max-size) *byte-count* command to set the maximum size of an SNMP packet that the device can receive or send.
    
    
    
    After the maximum size is set, the device discards any SNMP packet that is larger than the set size.
22. Configure SNMP to receive and respond to NMS request packets. To achieve this, run one or more of the following commands as needed:
    
    
    * To configure a source interface for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-interface) *protocol-interface-type* *protocol-interface-number* command.
    * To configure all interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status+all-interface) command.
    * To specify an isolated source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ipv4-address* [ **vpn-instance** *vpn-instance-name* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded.
    * To specify an IPv6 source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command.
    * To specify an isolated IPv6 source address for SNMP to receive and respond to request packets from the CCU, run the [**snmp-agent protocol ipv6 physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+ipv6+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ip-address* command.
    * To configure all IPv6 interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status+ipv6+all-interface) command.
    * Configure SNMP to receive and respond to NMS request packets through a VPN instance or public network.
      + For an IPv4 network, run the [**snmp-agent protocol**](cmdqueryname=snmp-agent+protocol) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
      + For an IPv6 network, run the [**snmp-agent protocol ipv6**](cmdqueryname=snmp-agent+protocol+ipv6) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In scenarios such as interface unnumbered, if an isolated source interface and a common source interface (non-isolated source interface) are configured to listen to the same IP address and VPN instance, the common source interface takes effect. When the TCP listening mode is set to all-interface and an isolated source interface is configured, the isolated source interface takes effect if it is matched based on the 5-tuple matching rule; the all-interface configuration takes effect if the isolated source interface is not matched based on the 5-tuple matching rule. The source IP address specified for the isolated source interface does not need to be the interface's IP address.
23. (Optional) Run the [**snmp-agent local-engineid**](cmdqueryname=snmp-agent+local-engineid) *engineid* command to set an engine ID for the local SNMP entity.
    
    
    
    The MAC address of the management interface on the main control board is used as device information.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To improve system security, run the [**snmp-agent packet contextengineid-check enable**](cmdqueryname=snmp-agent+packet+contextengineid-check+enable) command to check whether the contextEngineID is consistent with the local engine ID.
24. (Optional) Run the [**snmp-agent set-cache enable**](cmdqueryname=snmp-agent+set-cache+enable) command to enable the SET response message caching function.
25. (Optional) Run the [**snmp-agent protocol server**](cmdqueryname=snmp-agent+protocol+server) [ **ipv4** | **ipv6** ] [**disable**](cmdqueryname=disable) command to disable the SNMP IPv4 or IPv6 listening port.
    
    
    
    After you disable the SNMP IPv4 or IPv6 listening port using the [**snmp-agent protocol server disable**](cmdqueryname=snmp-agent+protocol+server+disable) command, SNMP no longer processes SNMP packets. Exercise caution when you disable the SNMP IPv4 or IPv6 listening port.
26. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.