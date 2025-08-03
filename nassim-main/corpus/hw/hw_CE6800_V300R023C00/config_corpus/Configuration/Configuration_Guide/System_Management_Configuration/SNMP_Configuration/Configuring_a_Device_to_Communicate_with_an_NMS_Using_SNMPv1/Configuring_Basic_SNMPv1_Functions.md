Configuring Basic SNMPv1 Functions
==================================

Configuring Basic SNMPv1 Functions

#### Prerequisites

Before configuring a device to communicate with an NMS through SNMPv1, complete the following tasks:

* Configure a routing protocol to ensure that the device and NMS are reachable to each other.
* Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).

#### Context

SNMP needs to be deployed on a network to allow the NMS to manage network devices.

If the network is secure and has few devices (for example, a campus network or a small enterprise network), SNMPv1 can be deployed to ensure communication between the NMS and managed devices.

However, SNMPv1 has security risks; therefore, using SNMPv3 is recommended.

After basic SNMP functions are configured, an NMS can perform basic operations (such as Get and Set operations) on a managed device, and the managed device can send alarms to the NMS.

After basic SNMP functions are configured, the NMS can communicate with the managed device.


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
   [snmp-agent sys-info](cmdqueryname=snmp-agent+sys-info) version v1
   ```
   
   
   
   By default, SNMPv3 is used.
   
   After SNMPv1 is configured on the managed device, the device supports both SNMPv1 and SNMPv3. This means that the device can be monitored and managed by NMSs running SNMPv1 or SNMPv3.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) **version** **v1** command can be used only after the weak security algorithm/protocol feature package is installed.
6. Configure a read/write community name.
   
   
   ```
   [snmp-agent community](cmdqueryname=snmp-agent+community) { read | write } { community-name | cipher host-string } [ mib-view security-string-cipher | acl { acl-number | acl-name } | alias alias-name ]
   ```
   
   The community name is saved in encrypted format in the configuration file. To facilitate identification of community names, set the alias names for the communities. The alias names are stored in cleartext in the configuration file.
   
   By default, the device checks the complexity of community names. If the check fails, the community name cannot be configured. You can run the [**snmp-agent community complexity-check disable**](cmdqueryname=snmp-agent+community+complexity-check+disable) command to disable this complexity check. However, to ensure system security, you are advised to retain the default configuration.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The device has the following requirements for community name complexity:
   
   * A community name contains at least eight characters.
   * A community name contains at least two types of the following characters: uppercase characters, lowercase characters, digits, and special characters, excluding question marks (?) and spaces.
   * After the weak password dictionary maintenance function is enabled, the value of *community-name* cannot be any password defined in the weak password dictionary. (You can run the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command to view the passwords defined in the weak password dictionary.)
   
   After the community name is set, if no MIB view is configured, the NMS that uses the community name has permission to access objects in the ViewDefault view (1.3.6.1).
   
   * If the NMS administrator needs the read permission in a specified view, configure **read** in this command. For example, a low-level administrator needs to read certain data.
   * If the NMS administrator needs the read and write permissions in a specified view, configure **write** in this command. For example, a high-level administrator needs to read and write certain data.
7. Configure the destination IP address for the alarms and error codes sent from the device. Choose one of the following commands as required.
   
   
   * On an IPv4 network, run the following command:
     ```
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ [host-name](cmdqueryname=host-name) host-name ] [trap address udp-domain](cmdqueryname=trap+address+udp-domain) ip-address [ [ [udp-port](cmdqueryname=udp-port) port-number | [ alarm-udp-port alarm-port-number | event-udp-port event-port-number ] *] | [ { [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name | [public-net](cmdqueryname=public-net) } ] | [ [source](cmdqueryname=source) { interface-name | interface-type interface-number } ] ] * [params securityname](cmdqueryname=params+securityname) { security-name [ [v1](cmdqueryname=v1) | [private-netmanager](cmdqueryname=private-netmanager) | [ext-vb](cmdqueryname=ext-vb) | [notify-filter-profile](cmdqueryname=notify-filter-profile) profile-name | [heart-beat enable](cmdqueryname=heart-beat+enable) ] * | [cipher](cmdqueryname=cipher) cipher-name [ [v1](cmdqueryname=v1) | [private-netmanager](cmdqueryname=private-netmanager) | [ext-vb](cmdqueryname=ext-vb) | [notify-filter-profile](cmdqueryname=notify-filter-profile) profile-name | [heart-beat enable](cmdqueryname=heart-beat+enable) ] * }
     ```
   * On an IPv6 network, run the following command:
     ```
     [snmp-agent target-host](cmdqueryname=snmp-agent+target-host) [ [host-name](cmdqueryname=host-name) host-name ] [trap ipv6 address udp-domain](cmdqueryname=trap+ipv6+address+udp-domain) ipv6-address [ [ [udp-port](cmdqueryname=udp-port) port-number | [ alarm-udp-port alarm-port-number | event-udp-port event-port-number ] *] | [ [vpn-instance](cmdqueryname=vpn-instance) vpn-instance-name | [public-net](cmdqueryname=public-net) ] ] * [params securityname](cmdqueryname=params+securityname) { security-name [ [v1](cmdqueryname=v1) | [ext-vb](cmdqueryname=ext-vb) | [notify-filter-profile](cmdqueryname=notify-filter-profile) profile-name | [private-netmanager](cmdqueryname=private-netmanager) ] * | [cipher](cmdqueryname=cipher) cipher-name [ [v1](cmdqueryname=v1) | [ext-vb](cmdqueryname=ext-vb) | [notify-filter-profile](cmdqueryname=notify-filter-profile) profile-name | [private-netmanager](cmdqueryname=private-netmanager) ] * }
     ```
   
   The parameters can be set as follows:
   * **udp-port** needs to be set to a non-well-known port number if special requirements need to be met (default port number: 162). You can also configure **alarm-udp-port** and **event-udp-port** for different types of reported contents (alarms and events) to change the port number for receiving alarms and events to a specified port number.
   * **public-net** needs to be specified if the managed device sends alarms to the NMS through a public network. Alternatively, **vpn-instance** *vpn-instance-name* needs to be specified if the managed device sends alarms to the NMS through a private network.
   * **securityname** needs to be configured to identify a source device that sends alarms.
   * **private-netmanager** needs to be specified if the NMS and managed device are both provided by Huawei. In this way, alarm messages can carry more information (for example, the alarm type, sequence number, and sending time). Such information helps rectify faults.
   * **notify-filter-profile** needs to be specified if you want the device to send only desired alarms to the NMS, thereby reducing irrelevant alarms and speeding up fault identification. **notify-view** needs to be specified to allow the alarm filter policy to take effect when you configure a user group.
8. (Optional) Configure the contact and location information of the device administrator.
   
   
   ```
   [snmp-agent sys-info](cmdqueryname=snmp-agent+sys-info) { contact contact | location location }
   ```
   
   Configuring this information helps the NMS administrator contact the device administrators for fault locating and rectification, especially if the NMS manages many devices.
9. (Optional) Set the maximum size of an SNMP message that can be received or sent by the device.
   
   
   ```
   [snmp-agent packet max-size](cmdqueryname=snmp-agent+packet+max-size) byte-count
   ```
   
   
   
   By default, the maximum size of an SNMP message that the device can receive or send is 12000 bytes.
   
   After the maximum size is set, the device discards any SNMP message that is larger than the set size.
10. (Optional) Enable the SNMP extended error code function.
    
    
    ```
    [snmp-agent extend error-code enable](cmdqueryname=snmp-agent+extend+error-code+enable)
    ```
    
    
    
    By default, SNMP sends standard error codes to an NMS. The extended error code function allows an SNMP device to send extended error codes to the NMS.
11. (Optional) Enable the function to cache Set response packets.
    
    
    ```
    [snmp-agent set-cache enable](cmdqueryname=snmp-agent+set-cache+enable)
    ```
    
    
    
    By default, the function to cache Set response packets is disabled.
12. Configure a source interface for the SNMP agent to receive and respond to NMS request packets.
    
    
    
    **Table 1** Configuring a source interface for the SNMP agent to receive and respond to NMS request packets
    | Operation | Command |
    | --- | --- |
    | Specify the source interface for SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-status) { *protocol-interface-type protocol-interface-number* | *protocol-interface-name* } |
    | Enable all interfaces on the device to be used by SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
    | Specify an IPv6 source address for SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+source-status) *ip-address* [ **vpn-instance** *vpn-instance-name* ] |
    | Enable all IPv6 interfaces on the device to be used by SNMP to receive and respond to requests from an NMS. | [**snmp-agent protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
    
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    You are advised not to use all interfaces to receive and respond to NMS request messages. Specifying a source interface is recommended.
13. (Optional) Configure SNMP to receive and respond to NMS request packets through a VPN or public network.
    
    
    ```
    [snmp-agent protocol](cmdqueryname=snmp-agent+protocol) [ ipv6 ] { vpn-instance vpn-instance-name | public-net }
    ```
14. (Optional) Set the engine ID of the local SNMP entity.
    
    
    ```
    [snmp-agent local-engineid](cmdqueryname=snmp-agent+local-engineid) engineid
    ```
    
    
    
    By default, the system uses the internal algorithm to automatically generate a device engine ID, which includes the enterprise ID and device information. The system uses the MAC address of the management interface on a device as the device information of the engine ID.
    
    ![](public_sys-resources/note_3.0-en-us.png) 
    
    To improve system security, run the [**snmp-agent packet contextengineid-check enable**](cmdqueryname=snmp-agent+packet+contextengineid-check+enable) command to check for consistency between the context engine ID and local engine ID.
15. (Optional) Disable the SNMP IPv4 or IPv6 listening port.
    
    
    ```
    [snmp-agent protocol server](cmdqueryname=snmp-agent+protocol+server+disable) [ ipv4 | ipv6 ] [disable](cmdqueryname=disable)
    ```
    
    
    
    After you disable the SNMP IPv4 or IPv6 listening port using the [**snmp-agent protocol server disable**](cmdqueryname=snmp-agent+protocol+server+disable) command, SNMP no longer processes SNMP packets. Exercise caution when running this command.
16. (Optional) Configure the SNMP proxy to receive and respond to requests from the managed device.
    
    
    
    **Table 2** Configuring the SNMP proxy to receive and respond to requests from the managed device
    | Operation | Command |
    | --- | --- |
    | Specify the source interface for the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-status) { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* } |
    | Enable all IPv4 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
    | Specify the source IPv6 address for the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+source-status) *ip-address* [ **vpn-instance** *vpn-instance-name* ] |
    | Enable all IPv6 addresses on the device to be used by the SNMP proxy to receive and respond to requests from the managed device. | [**snmp-agent proxy protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status) |
17. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```