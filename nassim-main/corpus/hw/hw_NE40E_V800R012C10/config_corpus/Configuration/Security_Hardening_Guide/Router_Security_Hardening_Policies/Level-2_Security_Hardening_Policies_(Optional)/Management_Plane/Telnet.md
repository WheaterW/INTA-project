Telnet
======

Telnet

#### Security Policy

* Authentication
  
  A Telnet server supports password authentication and AAA authentication. Only users who are authenticated can access a device and its command line interface. The Telnet server supports password authentication and AAA authentication. Only users who pass authentication can access devices and the command line window. AAA authentication supports remote and local authentication, and remote authentication takes precedence. Passwords used in authentication are encrypted using an irreversible algorithm.
* Service disabling
  
  After the Telnet server function is enabled, a device starts socket listening. In this case, attackers can easily scan devices. When the Telnet server is not in use, disable the Telnet server function and relative ports.
* Port number changes
  
  Telnet server port 23 is a well-known port number. Therefore, the port number is easily scanned and attacked. Telnet server port 23 can be changed to a private port number to reduce the possibility of being scanned or attacked. A private port number can be 23 or range from 1025 to 65535.
* Access control lists (ACLs)
  
  ACLs can be configured for virtual type terminal (VTL) channels in the user-interface view. ACLs are used to limit which client IP addresses can be used to access a device. Users are not advised to configure ACL rules in this view.
  
  ACL rules can be configured on the Telnet server to limit IP addresses of clients that access a device using Telnet. Users are advised to configure ACL rules on the Telnet server.
* Source interface configuration
  
  Source interfaces that are allowed to access the Telnet server can be specified. Users must access a Telnet server function-enabled device using the IP addresses of the specified source interfaces. In this way, the access range is controlled, and device security is enhanced.
* Source IPv6 address configuration
  
  Source IPv6 address that is allowed to access the Telnet server can be specified. Users must access a Telnet server function-enabled device using the IPv6 addresses of the specified source interfaces. In this way, the access range is controlled, and device security is enhanced.
* IP blacklist
  
  When network attackers send a large number of Telnet requests, authorized users cannot log in to the system through temporary sessions. To prevent this issue, network attackers' IP addresses are temporarily locked by the system for a period of time so that authorized users can log in to the system.
* CPCAR-based flood attack defense
  
  In the scenario where Internet public addresses are deployed, a device may be attacked by traffic flooding on the management and control plane. You can configure a CPU defense policy to protect the device against traffic attacks.

#### Attack Methods

* Port scanning
  
  Attackers attempt to obtain user packets by scanning and listening network-side ports on user devices. Device information can be easily obtained because user packets are transmitted in simple password.
* Password cracking
  
  After an attacker obtains a Telnet port number on a device, the attacker attempts to access the device. When the device requests authentication information, the attacker may crack the password. The device considers the attacker authenticated and allows the attacker to access.
* Denial of service (DoS)
  
  A Telnet server supports a limited number of users. When the number of allowed users reaches the upper limit, other users cannot access the device. This situation may occur as a result of normal Telnet server usage, or when a Telnet server is attacked.

#### Configuration and Maintenance Methods

* Set the authentication mode to AAA.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When the authentication mode is set to AAA, you must specify the access type of the local user.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     The AAA view is displayed.
  3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [**cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     The local username and password are configured.
  4. Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type telnet**
     
     The access type is set to Telnet for the local user.
  5. Run [**local-user**](cmdqueryname=local-user) *user-name* **user-group manage-ug**
     
     The local user is configured with administrative rights.
  6. Run [**quit**](cmdqueryname=quit)
     
     Exit the AAA view.
  7. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
     
     A VTY user interface view is displayed.
  8. Run [**authentication-mode aaa**](cmdqueryname=authentication-mode+aaa)
     
     AAA authentication is enabled.
  9. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

* Disable the Telnet service function.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**undo telnet**](cmdqueryname=undo+telnet) [ **ipv6** ] **server enable**
     
     The Telnet server function is disabled.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Change the public Telnet port number to a private number of 53555.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**telnet server port**](cmdqueryname=telnet+server+port) **53555**
     
     The port number is changed to 53555.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure an ACL to control permission to call in and out.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { [ **number** ] *acl-number* | **name** *acl-name* [ **advance** ] [ **number** *acl-number* ] } [ **match-order** { **auto** | **config** } ]
     
     An advanced ACL is created and the advanced ACL view is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Telnet is a TCP-based protocol. You can use Telnet to log in to a device. To ensure security, you are advised to configure an independent ACL to protect Telnet. The device supports dynamic link protection for Telnet. The protocol packets with session entries being set up can be forwarded through a dynamic whitelist. In this example, ACLs are used to limit the rate of Telnet protocol packets for which no connection has been established. It is recommended that the management protocol directly filter and discard the access traffic from unknown sources.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } *protocol* [ **destination** { *destination-ip-address destination-wildcard* | **any** } | **fragment** | **source** { *source-ip-address source-wildcard* | **any** } | **time-range** *time-name* | **dscp** *dscp* **vpn-instance** *vpn-instance-name* ]
     
     ACL rules are configured.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit the ACL view.
  5. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
     
     A VTY user interface view is displayed.
  6. Run [**acl**](cmdqueryname=acl) *acl-number* { **inbound** | **outbound** }
     
     The permission to call in and out using a VTY connection is configured. Either of the following parameters must be configured:
     
     **inbound**: prevents users using a specific IP address or a range of IP addresses on a network segment from accessing a device.
     
     **outbound**: prevents users who successfully access a device from accessing another device.
  7. Run [**quit**](cmdqueryname=quit)
     
     Exit the VTY user interface view.
  8. Run [**telnet server acl**](cmdqueryname=telnet+server+acl) { *acl-number* | *acl-name* }
     
     An ACL is specified to allow users with specified IP addresses to run Telnet to access the device.
  9. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Specify the source interface for a user to access a Telnet server.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**telnet server-source**](cmdqueryname=telnet+server-source) **-i** **loopback** *interface-number*
     
     The source interface for a Telnet server is specified.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before specifying a loopback interface as the source interface for the Telnet server, ensure that the loopback interface has been created. Otherwise, this command will fail to be executed.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Specify the source IPv6 address for a user to access a Telnet server.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]
     
     The source IPv6 address for a Telnet server is specified.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     VPN configuration must be successful, to configure the vpn instance using this command.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure CPCAR-based flood attack defense.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
     
     An advanced ACL is created, and the view of this advanced ACL is displayed.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Telnet is a TCP-based protocol. You can use Telnet to log in to a device. For security purposes, you are advised to configure a separate ACL. The device supports dynamic link protection for Telnet packets. The packets with session entries being set up can be forwarded preferentially. An ACL is used to limit the rate of Telnet packets without session entries. It is recommended that the device should filter and discard access traffic from unknown sources.
  3. Perform the following operations to configure an ACL rule to allow the device to send Telnet packets with the specified source interface address and deny other Telnet packets.
     
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **permit** **tcp** **source** *source-ip-address* *source-wildcard* **source-port** **eq 23** command to configure the device to send protocol packets with the specified source address and source interface type as Telnet.
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **permit** **tcp** **source** *source-ip-address* *source-wildcard* **destination-port** **eq 23** command to configure the device to send protocol packets with the specified source address and destination interface type as Telnet.
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **deny** **tcp** **destination-port** **eq 23** command to configure the device to deny Telnet packets that are not whitelisted.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit from the ACL view.
  5. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
     
     An attack defense policy is created.
  6. Run [**tcpsyn-flood enable**](cmdqueryname=tcpsyn-flood+enable)
  7. Run [**fragment-flood enable**](cmdqueryname=fragment-flood+enable)
  8. Run [**udp-packet-defend enable**](cmdqueryname=udp-packet-defend+enable)
  9. Run [**abnormal-packet-defend enable**](cmdqueryname=abnormal-packet-defend+enable)
  10. Run [**user-defined-flow**](cmdqueryname=user-defined-flow) *flow-id* **acl** { *acl-number* | **name** *acl-name* } [ **prior** ]
      
      A user-defined flow is configured and associated with the ACL.
  11. Run [**car**](cmdqueryname=car) **user-defined-flow** *flow-id* { **cir** *cir-value* | **cbs** *cbs-value* | **min-packet-length** *min-packet-length-value* }
      
      A CAR action rule is configured for packets in user-defined flows.
  12. Run [**priority**](cmdqueryname=priority) { *protocol-name* | **index** *index* | **whitelist** | **whitelist-v6** | **blacklist** | **tcpsyn** | **fragment** | **user-defined-flow** *flow-id* } { **high** | **middle** | **low** | **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** }
      
      The priorities of sending packets to the CPU are configured.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Telnet is an access protocol, requires less processing bandwidth, and has low real-time requirements. Therefore, it is recommended that you set its priority to medium.
  13. Run [**quit**](cmdqueryname=quit)
      
      Exit the attack defense policy view.
  14. Run [**slot**](cmdqueryname=slot) *slot-id*
      
      The specified slot view is displayed.
  15. Run [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number*
      
      The attack defense policy is applied to the specified interface board.
  16. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.

#### Configuration and Maintenance Suggestions

* Plan IP addresses to manage devices separately to prevent devices from being scanned or listened in.
* Change the public port number of a Telnet server.
* Configure ACLs to limit which IP addresses that can access the Telnet server.
* Replace Telnet with SSH to provide secure management channels.

#### Verifying the Security Hardening Result

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration aaa** command to check the AAA configuration.
* Run the **[**display telnet server**](cmdqueryname=display+telnet+server)** command to check the configuration of the Telnet server.
* Run the **[**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy)** **policy-number** command to check the attack defense policy.