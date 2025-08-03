Configuring Basic SNMPv2c Functions
===================================

After basic SNMP functions are configured, the NMS can perform basic operations such as Get and Set operations on a managed device, and the managed device can send alarms to the NMS.

#### Context

The NMS can communicate with managed devices after basic SNMPv2c functions have been configured.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. (Optional) Run the [**snmp-agent password min-length**](cmdqueryname=snmp-agent+password+min-length) *min-length* command to configure the minimum SNMP password length.
   
   
   
   After this command is run, the length of a configured SNMP password must be longer than or equal to the minimum SNMP password length.
3. (Optional) Run the [**snmp-agent**](cmdqueryname=snmp-agent) command to enable the SNMP agent service.
   
   
   
   This step is optional because the SNMP agent service can be enabled by running any [**snmp-agent**](cmdqueryname=snmp-agent) command, irrespective of whether any parameter is specified.
4. (Optional) Run the [**snmp-agent udp-port**](cmdqueryname=snmp-agent+udp-port) *port-number* command to change the port number monitored by the SNMP agent.
   
   
   
   If this command is not configured, the default port number is used.
5. Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) **version** **v2c** command to set the SNMP version.
   
   
   
   After SNMPv2c is enabled on the managed device, the device supports both SNMPv2c and SNMPv3. This means that the device can be monitored and managed by NMSs running SNMPv2c or SNMPv3.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SNMP version must be the same as that of the destination host that sends trap messages and error codes.
6. Run the [**snmp-agent community**](cmdqueryname=snmp-agent+community) { **read** | **write** } **cipher** *host-string* [ **mib-view** *security-string-cipher* | **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \* command to set the community name.
   
   
   
   The community name will be saved in encrypted format in the configuration file.
   
   To disable the complexity check for community names, run the [**snmp-agent community complexity-check disable**](cmdqueryname=snmp-agent+community+complexity-check+disable) command. However, to ensure system security, enabling the complexity check for community names is recommended.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   HUAWEI has the following requirements on the complexity of community names:
   
   * A community name contains at least eight characters.
   * A community name contains at least two types of the following characters: uppercase characters, lowercase characters, digits, and special characters, excluding question marks (?) and spaces.
   
   After the community name is set, if no MIB view is configured, the NMS that uses the community name has permission to access objects in the ViewDefault view (1.3.6.1).
   
   * **read** needs to be configured in the command if the NMS administrator needs the read permission in a specified view in some cases. For example, a low-level administrator needs to read certain data.
   * **write** needs to be configured in the command if the NMS administrator needs the read and write permissions in a specified view in some cases. For example, a high-level administrator needs to read and write certain data.
7. Run either of the following commands:
   
   
   * On an IPv4 network, a managed device can send alarms in Inform or trap mode.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The difference between alarms in trap and Inform modes is as follows:
     
     + In trap mode, a managed device does not need to receive a response from the alarm host after sending an alarm.
     + In Inform mode, a managed device needs to receive a response from the alarm host after sending an alarm. If no response is received within the timeout period, the managed device retransmits the alarm until the number of sent alarms reaches the maximum number of allowed retransmissions.
       
       The managed device sends the alarm in Inform mode and records an alarm log at the same time. If the NMS or a link fails, the NMS can synchronize alarms generated during this period after the fault is rectified.
     
     Therefore, the alarm in Inform mode is more reliable than that in trap mode. However, a device needs to cache massive alarm messages and consume a great number of memory resources due to the retransmission mechanism.
     
     If the network environment is stable, sending alarms in trap mode is recommended. If device resources are sufficient and the network environment is unstable, sending alarms in Inform mode is recommended.
     
     + To configure a destination IP address for the traps and error codes sent from the device, run:
       
       [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **trap** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ **source** *interface-type* *interface-number* ] | [ **public-net** | **vpn-instance** *vpn-instance-name* ] ] \* **params** **securityname** { *security-name* [ **v2c** | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* | **cipher** *cipher-name* [ **v2c** | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* }
     + To configure a destination IP address for the informs and error codes sent from the device, run:
       
       [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **inform** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* ] | [ **source** *interface-type* *interface-number* ] | [ **public-net** | **vpn-instance** *vpn-instance-name* ] ] \* **params** **securityname** { *security-name* **v2c** | **cipher** *cipher-name* **v2c** } [ **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \*The following parameters can be configured as needed:
     + **udp-port** needs to be configured to change the default UDP port number of 162 to a non-well-known port number to meet special requirements.
     + **vpn-instance**: If the alarms sent from the managed device to the NMS need to be transmitted over a private network, the parameter **vpn-instance** *vpn-instance-name* needs to be used to specify a VPN that takes over the sending task.
     + **public-net**: If the alarms sent from the managed device to the NMS need to be transmitted over a public network, the parameter **public-net** needs to be used to specified.
     + **securityname** needs to be configured to identify a source device that sends traps.
   * To configure a destination IPv6 address for the traps and error codes sent from the device, run:
     
     [**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host) [ **host-name** *host-name* ] **trap** **ipv6** **address** **udp-domain** *ipv6-address* [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | **source** *interface-type* *interface-number* ] \* **params** **securityname** { *security-name* [ **v2c** | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* | **cipher** *cipher-name* [ **v2c** | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* }
   * To configure a destination IPv6 address for the informs and error codes sent from the device, run:
     
     **[**snmp-agent target-host**](cmdqueryname=snmp-agent+target-host)** [ **host-name***host-name* ] **inform** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port***server-port* ] | [ **vpn-instance***vpn-instance-name* | **public-net** ] | [ **source** { *interface-name* | *interface-type**interface-number* } ] ] \***params****securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher***cipher-name***v2c** } [ [ **private-netmanager** | **ext-vb** | **notify-filter-profile***profile-name* ] \* ] \*
8. (Optional) Run the [**snmp-agent sys-info**](cmdqueryname=snmp-agent+sys-info) { **contact** *contact* | **location** *location* } command to configure the device administrator contact information or location is configured.
   
   
   
   Configuring this information helps the NMS administrator contact the device administrators for fault locating and rectification, especially if the NMS manages many devices.
9. (Optional) Run the [**snmp-agent packet max-size**](cmdqueryname=snmp-agent+packet+max-size) *byte-count* command to set the maximum size of an SNMP packet that the device can receive or send.
   
   
   
   After the maximum size is set, the device discards any SNMP packet that is larger than the set size.
10. (Optional) Run the [**snmp-agent extend error-code enable**](cmdqueryname=snmp-agent+extend+error-code+enable) command to enable the extended error code function.
11. (Optional) Run the [**snmp-agent set-cache enable**](cmdqueryname=snmp-agent+set-cache+enable) command to enable the SET response message caching function.
12. Configure SNMP to receive and respond to NMS request packets. To achieve this, run one or more of the following commands as needed:
    
    
    * To configure a source interface for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-interface**](cmdqueryname=snmp-agent+protocol+source-interface) *protocol-interface-type* *protocol-interface-number* command.
    * To configure all interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status all-interface**](cmdqueryname=snmp-agent+protocol+source-status+all-interface) command.
    * To specify an isolated source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ipv4-address* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded.
    * To specify an IPv6 source address for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol ipv6 source-ip**](cmdqueryname=snmp-agent+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command.
    * To specify an isolated IPv6 source address for SNMP to receive and respond to request packets from the CCU, run the [**snmp-agent protocol ipv6 physic-isolate source-interface**](cmdqueryname=snmp-agent+protocol+ipv6+physic-isolate+source-interface) *protocol-interface-name* **source-ip** *ip-address* command.
    * To configure all IPv6 interfaces on the device for SNMP to receive and respond to NMS request packets, run the [**snmp-agent protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+protocol+source-status+ipv6+all-interface) command.
    * Configure SNMP to receive and respond to NMS request packets through a VPN instance or public network.
      + For an IPv4 network, run the [**snmp-agent protocol**](cmdqueryname=snmp-agent+protocol) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
      + For an IPv6 network, run the [**snmp-agent protocol ipv6**](cmdqueryname=snmp-agent+protocol+ipv6) { **vpn-instance** *vpn-instance-name* | **public-net** } command.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    In scenarios such as interface unnumbered, if an isolated source interface and a common source interface (non-isolated source interface) are configured to listen to the same IP address and VPN instance, the common source interface takes effect. When the TCP listening mode is set to all-interface and an isolated source interface is configured, the isolated source interface takes effect if it is matched based on the 5-tuple matching rule; the all-interface configuration takes effect if the isolated source interface is not matched based on the 5-tuple matching rule. The source IP address specified for the isolated source interface does not need to be the interface's IP address.
13. (Optional) Run the [**snmp-agent local-engineid**](cmdqueryname=snmp-agent+local-engineid) *engineid* command to set an engine ID for the local SNMP entity.
    
    
    
    The system uses the MAC address of the management interface on a main control board as the device information of the engine ID.
14. (Optional) Configure the SNMP proxy for receiving and responding to requests from the CCU.
    
    
    * IPv4 network
      + Run the [**snmp-agent proxy protocol source-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-interface) { *protocol-interface-type* *protocol-interface-number* | *protocol-interface-name* } command to specify a source interface for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+all-interface) command to allow all interfaces to be used by the SNMP proxy to receive and respond to IPv4 packets from the CCU.
    * IPv6 network
      + Run the [**snmp-agent proxy protocol ipv6 source-ip**](cmdqueryname=snmp-agent+proxy+protocol+ipv6+source-ip) *ip-address* [ **vpn-instance** *vpn-instance-name* ] command to specify an IPv6 source address for the SNMP proxy to receive and respond to requests from the CCU.
      + Run the [**snmp-agent proxy protocol source-status ipv6 all-interface**](cmdqueryname=snmp-agent+proxy+protocol+source-status+ipv6+all-interface) command to allow all IPv6 interfaces to be used by the SNMP proxy to receive and respond to requests from the CCU.
15. (Optional) Run the [**snmp-agent protocol get-bulk timeout**](cmdqueryname=snmp-agent+protocol+get-bulk+timeout) *time* command to configure a get-bulk operation timeout period.
    
    
    
    You are advised not to change the get-bulk operation timeout period. The default get-bulk operation timeout period (2s) is recommended. To reconfigure a get-bulk operation timeout period, you must ensure that the configured period is less than an NMS's timeout period.
16. (Optional) Run the [**snmp-agent protocol server**](cmdqueryname=snmp-agent+protocol+server) [ **ipv4** | **ipv6** ] [**disable**](cmdqueryname=disable) command to disable the SNMP IPv4 or IPv6 listening port.
    
    
    
    After you disable the SNMP IPv4 or IPv6 listening port using the [**snmp-agent protocol server disable**](cmdqueryname=snmp-agent+protocol+server+disable) command, SNMP no longer processes SNMP packets. Exercise caution when you disable the SNMP IPv4 or IPv6 listening port.
17. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Follow-up Procedure

After the configuration is complete, the NMS and managed device can communicate.

* Access control allows any NMS that uses the community name to monitor and manage all the objects on the managed device.
* The managed device sends alarms generated by the modules that are enabled by default to the NMS.

If finer device management is required, follow directions below to configure the managed device:

* To allow a specified NMS that uses the community name to manage specified objects on the device, follow the procedure described in [Controlling the NMS's Access to the Device](dc_vrp_snmp_cfg_0011.html).
* To allow a specified module on the managed device to report alarms to the NMS, follow the procedure described in [Configuring the Trap Function](dc_vrp_snmp_cfg_0007.html) or [Configuring the Inform Function](dc_vrp_snmp_cfg_0013.html).