SSH
===

SSH

#### Security Policy

* Authentication
  
  The SSH server supports AAA authentication, PKI certificate authentication, and public-key authentication. Only authenticated users can log in to the desired device and enter the CLI. AAA authentication supports both remote and local authentication, and remote authentication takes precedence over local authentication.
* Disabling services
  
  When the SSH server is started, socket listening is enabled for devices. In this case, the devices are prone to scanning by attackers. If the SSH server does not need to be used, you can disable the SSH server and the corresponding port.
* Disabling the SSHv1 service
  
  The SSHv1 service is prone to attacks and the algorithm used by it is insecure. To reduce attack risks, you can disable the SSHv1 service.
* Port number change
  
  SSH server port 22 is a well-known port number, which is prone to scanning and attacks. You can change the SSH server port number to a private port number to reduce the possibility of being scanned or attacked. A private port number can be 22 or range from 1025 to 65535.
* ACL
  
  On the SSH server, you can configure ACL rules to control the login to the device's client IP address through STelnet, SFTP, SCP, or SNETCONF.
  
  In the user interface view, you can configure an ACL rule for each VTY channel to control the IP addresses of clients that can log in to the device through STelnet. ACL rules do not control the IP addresses of clients that log in to the device in other modes.
  
  You are advised to configure the SSH client on the SSH server, not on the VTY channel.
* Source interface configuration
  
  Source interfaces supported by the SSH server can be configured. Users must access a device using the IP addresses of the configured source interfaces. In this way, the access range is controlled and the device security is enhanced.
* Configuring the source IPv6 address
  
  You can configure the source IPv6 address supported by the SSH server to allow users to log in to the device only through this IPv6 address. This restricts the access range and improves device security.
* CPCAR-based flood attack defense
  
  In the scenario where Internet public addresses are deployed, a device may be attacked by traffic flooding on the management and control plane. You can configure a CPU defense policy to protect the device against traffic attacks.

#### Attack Methods

* Brute-force attack
  
  After an attacker obtains the SSH port number, the attacker attempts to access a device. When the device asks authentication information, the attacker may crack the password, pass the authentication, and obtain the access right.
* DoS attack
  
  An SSH server supports only a limited number of users. When the number of login users reaches the upper limit, new users cannot access the server. This problem may be caused by normal use or attacks.

#### Configuration and Maintenance Methods

* Set the authentication mode to AAA.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  When the authentication mode is set to AAA, you must specify the access type of the local user.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**aaa**](cmdqueryname=aaa) command to enter the AAA view.
  3. Run the [**local-user**](cmdqueryname=local-user) *user-name* **password** [**cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ] command to configure a local username and password.
  4. Run the [**local-user**](cmdqueryname=local-user) *user-name* **user-group manage-ug** command to configure administrator rights for the local user.
  5. Run the [**local-user**](cmdqueryname=local-user) *user-name* **service-type ssh** command to configure the local user's access type as SSH.
  6. Run the [**quit**](cmdqueryname=quit) command to exit the AAA view.
  7. Run the [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ] command to enter VTY user interface view.
  8. Run the [**authentication-mode aaa**](cmdqueryname=authentication-mode+aaa) command to set the user authentication mode to AAA.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Disable the SSH service. (By default, the SSH service is enabled.)
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**undo stelnet server enable**](cmdqueryname=undo+stelnet+server+enable) command to disable the STelnet service.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Change the port number to 53555.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ssh server port**](cmdqueryname=ssh+server+port) **53555** command to change the port number to 53555.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure an ACL to restrict login rights of users.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**acl**](cmdqueryname=acl) { [ **number** ] *acl-number* | **name** *acl-name* [ **advance** ] [ **number** *acl-number* ] } [ **match-order** { **auto** | **config** } ] command to create an advanced ACL and enter the advanced ACL view.
  3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } *protocol* [ **destination** { *destination-ip-address destination-wildcard* | **any** } | **fragment** | **source** { *source-ip-address source-wildcard* | **any** } | **time-range** *time-name* | **dscp** *dscp* **vpn-instance** *vpn-instance-name* ] command to configure an ACL rule.
  4. Run the [**quit**](cmdqueryname=quit) command to exit the ACL view.
  5. Run the [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ] command to enter VTY user interface view.
  6. Run the [**acl**](cmdqueryname=acl) *acl-number* { **inbound** | **outbound** } command to configure inbound and outbound limits for the VTY user interface.
     
     To control the permission of users logging in to the Router from a specified IP address or IP address segment, specify **inbound** in the command.
     
     To prevent users who have logged in from logging in to other Routers, specify **outbound** in the command.
  7. Run the [**quit**](cmdqueryname=quit) command to exit the VTY user interface view.
  8. Run the [**ssh server acl**](cmdqueryname=ssh+server+acl) { *acl-number* | *acl-name* } command to configure the IP address of the client that is allowed to log in to the device through SSH.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Specify the source interface for a user to log in to the SSH server.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ssh server-source**](cmdqueryname=ssh+server-source) **-i** **loopback** *interface-number* command to specify the source interface of the SSH server.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before specifying the source interface for the SSH server, ensure that the loopback interface has been created. Otherwise, the configuration fails to be executed.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Specify the source IPv6 address for a user to log in to the SSH server.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ssh ipv6 server-source**](cmdqueryname=ssh+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ] command to specify a source IPv6 address for the SSH server.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A VPN instance has been created before you specify it for an SSH server. Otherwise, the command cannot be executed.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure CPCAR-based flood attack defense.
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the ACL view.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     SSH is a TCP-based protocol. You can use SSH to log in to a device. To ensure security, you are advised to configure an independent ACL to protect SSH. The device supports dynamic link protection for SSH. The protocol packets with session entries being set up can be forwarded through a dynamic whitelist. In this example, ACLs are used to limit the rate of SSH protocol packets for which no connection has been established. It is recommended that the management protocol directly filter and discard the access traffic from unknown sources.
  3. Run the following commands to configure ACL rules to allow SSH packets with the source IP addresses in the specified range to be sent to the CPU and deny other SSH packets:
     
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **permit** **tcp** **source** *source-ip-address* *source-wildcard* **source-port** **eq 22** command to configure the device to send protocol packets with a specified source address and the source interface type being SSH.
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **permit** **tcp** **source** *source-ip-address* *source-wildcard* **destination-port** **eq 22** command to configure the device to send protocol packets with a specified source address and the destination interface type being SSH.
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] **deny** **tcp** **destination-port** **eq 22** command to deny the SSH packets that are not in the whitelist.
  4. Run the [**quit**](cmdqueryname=quit) command to exit the ACL view.
  5. Run the [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number* command to create an attack defense policy.
  6. Run the [**tcpsyn-flood enable**](cmdqueryname=tcpsyn-flood+enable) command to enable defense against TCP SYN flood attacks.
  7. Run the [**fragment-flood enable**](cmdqueryname=fragment-flood+enable) command to enable defense against fragmented packet attacks.
  8. Run the [**udp-packet-defend enable**](cmdqueryname=udp-packet-defend+enable) command to enable defense against UDP packet attacks.
  9. Run the [**abnormal-packet-defend enable**](cmdqueryname=abnormal-packet-defend+enable) command to enable defense against malformed packet attacks.
  10. Run the [**user-defined-flow**](cmdqueryname=user-defined-flow) *flow-id* **acl** { *acl-number* | **name** *acl-name* } [ **prior** ] command to configure a user-defined flow and associate it with the ACL.
  11. Run the [**car**](cmdqueryname=car) **user-defined-flow** *flow-id* { **cir** *cir-value* | **cbs** *cbs-value* | **min-packet-length** *min-packet-length-value* } command to configure a CAR rule for packets in the user-defined flow.
  12. Run the [**priority**](cmdqueryname=priority) { *protocol-name* | **index** *index* | **whitelist** | **whitelist-v6** | **blacklist** | **tcpsyn** | **fragment** | **user-defined-flow** *flow-id* } { **high** | **middle** | **low** | **be** | **af1** | **af2** | **af3** | **af4** | **ef** | **cs6** } command to configure a priority for packets to be sent to the CPU.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      SSH is an access protocol, which requires less processing bandwidth and does not have high requirements on real-time performance. Therefore, you are advised to set the priority to medium.
  13. Run the [**quit**](cmdqueryname=quit) command to exit the attack defense policy view.
  14. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the view of the specified slot.
  15. Run the [**cpu-defend-policy**](cmdqueryname=cpu-defend-policy) *policy-number* command to apply the attack defense policy to the specified LPU.
  16. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Configuration and Maintenance Suggestions

* Plan IP addresses for managing devices separately to prevent the devices from being scanned and listened on.
* Change the port number of the SSH server.
* Configure an ACL policy to limit the IP addresses that can access the SSH server.
* Configure public-key authentication for SSH users.

#### Verifying the Security Hardening Result

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration aaa** command to check the AAA configuration.
* Run the **[**display ssh server status**](cmdqueryname=display+ssh+server+status)** command to check global configurations of the SSH server.
* Run the **[**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy)** **policy-number** command to check the attack defense policy.