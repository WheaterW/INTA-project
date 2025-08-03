Sending Information to a Syslog Server
======================================

Information can be sent to a Syslog server for user query. This allows users to learn the device operation in real time.

#### Context

When a device is working, the system records the operating status of the device in real time and generates certain information. If the UDP port number, information recording device, and information severity are specified for a Syslog server of a specified IP address, information is sent to the Syslog for query. This allows the network administrator to monitor the device operation and diagnose network faults.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, logs and traps are sent to a Syslog server.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**info-center enable**](cmdqueryname=info-center+enable)
   
   
   
   Information management is enabled to output information to a terminal or remote server.
3. (Optional) Run [**info-center channel**](cmdqueryname=info-center+channel) *channel-number* **name** *channel-name*
   
   
   
   The information channel specified by *channel-number* is named *channel-name*.
4. (Optional) Run [**info-center syslog packet-priority**](cmdqueryname=info-center+syslog+packet-priority) *priority-level*
   
   
   
   The output priority of Syslog packets is configured.
5. Run [**info-center loghost source**](cmdqueryname=info-center+loghost+source) *interface-type* *interface-number*
   
   
   
   The source interface through which the device sends information to the Syslog server is configured.
   
   
   
   After the configuration is complete, if the device sends information to the Syslog server, the Syslog server can check the source address to determine whether the information is sent from the device and can search the received information.
6. Run [**info-center loghost source-port**](cmdqueryname=info-center+loghost+source-port) *source-port*
   
   
   
   The source interface through which the device sends information to the syslog server is configured.
7. Send information to a specified Syslog server.
   
   
   * On an IPv4 network, run [**info-center loghost**](cmdqueryname=info-center+loghost) *ipv4-address* [ { **public-net** | **vpn-instance** *vpn-instance-name* } | **channel** { *channel-number* | *channel-name* } | **source-ip** *source-ip-address* | **facility** *local-number* | **port** *port-number* | **level** *log-level* | { **local-time** | **utc** } | **transport** { **udp** | **tcp** { [ **version** **rfc6587** ] [ **ssl-policy** *policy-name* [ **security** | **verify-dns-name** *dns-name* ] ] } } ] \*
     
     The device is configured to send information to a specified Syslog server.
   * On an IPv6 network, run [**info-center loghost**](cmdqueryname=info-center+loghost) **ipv6** *ipv6-address* [ { **public-net** | **vpn-instance** *vpn-instance-name* } | **facility** *local-number* | **source-ip** *source-ipv6-address* | **channel** { *channel-number* | *channel-name* } | **port** *port-number* | **level** *log-level* | { **local-time** | **utc** } | **transport** { **udp** | **tcp** { [ **version** **rfc6587** ] [ **ssl-policy** *policy-name* [ **security** | **verify-dns-name** *dns-name* ] ] } } ] \*
     
     The device is configured to send information to a specified Syslog server.
   * For a log host with a domain name specified, run [**info-center loghost**](cmdqueryname=info-center+loghost) **domain** *domain-name* [ { **local-time** | **utc** } | **channel** { *channel-number* | *channel-name* } | { **public-net** | **vpn-instance** *vpn-instance-name* } | **source-ip** *source-ip-address* | **facility** *local-number* | **level** *log-level* | **port** *port-number* | **transport** { **udp** | **tcp** { [ **version** **rfc6587** ] [ **ssl-policy** *policy-name* [ **security** ] ] } } ] \*
     
     The device is configured to send information to a specified Syslog server.
   
   The same information can be sent to multiple Syslog servers backing up each other. You can check the maximum number of Syslog servers supported by the system based on the **PafValue** field corresponding to **SPEC\_RES\_SYSLOG\_LOGHOST\_MAXNUM** in the [**display paf**](cmdqueryname=display+paf) command output.
   
   If the **security** parameter is set, the system sends only security logs to the log host.
   
   By default, a device sends logs to a Syslog server over UDP. To improve transmission security, you can configure TCP-based SSL encrypted transmission by specifying **transport** **tcp** **ssl-policy** *policy-name*.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring TCP-based SSL encrypted transmission, configure an SSL policy and load a digital certificate. For the detailed configuration procedure, see [Configuring and Binding an SSL Policy](dc_vrp_basic_cfg_0055.html).
   
   
   **Table 1** Source interface binding modes
   | Single Host's Source IP Address | Source Interface | Source IP Address Selection Rule |
   | --- | --- | --- |
   | The [**info-center loghost**](cmdqueryname=info-center+loghost) command is not run. | The [**info-center loghost source**](cmdqueryname=info-center+loghost+source) *interface-type* *interface-number* command is run to configure a source interface, and both a VPN and an IP address are configured for the source interface. | * If the effective VPN of a host is the same as the VPN configured for the source interface, the source IP address is the source interface's IP address. * If the effective VPN of a host is inconsistent with the VPN configured for the source interface, the source IP address is the outbound interface's IP address. |
   | The [**info-center loghost**](cmdqueryname=info-center+loghost) command is not run. | The [**info-center loghost source**](cmdqueryname=info-center+loghost+source) *interface-type* *interface-number* command is run to configure a source interface, and only an IP address is configured for the source interface. | * If the effective VPN of a host is a public network VPN, the source IP address is the source interface's IP address. * If the effective VPN of a host is not a public network VPN, the source IP address is the outbound interface's IP address. |
   | The [**info-center loghost**](cmdqueryname=info-center+loghost) command is not run. | The [**info-center loghost source**](cmdqueryname=info-center+loghost+source) *interface-type* *interface-number* command is not run. | If no source IP address or source interface is configured for a host, the source IP address is the outbound interface's IP address. |
   | The [**info-center loghost**](cmdqueryname=info-center+loghost) command is run with *ipv4-address* or *ipv6-address* specified. | The source interface is configured or not. | The source IP address is the host's source IP address if a source IP address is configured for a host. |
8. Run [**info-center source**](cmdqueryname=info-center+source) { *module-name* | **default** } **channel** { *channel-number* | *channel-name* } [ **log** { **state** { **off** | **on** } | **level** *log-level* } \* | **trap** { **state** { **off** | **on** } | **level** *trap-level* } \* | **debug** { **state** { **off** | **on** } | **level** *dbg-level* } \* ] \*
   
   
   
   Rules for outputting information through information channels are configured.
9. (Optional) Run [**info-center syslog packet-priority**](cmdqueryname=info-center+syslog+packet-priority) *priority-level*
   
   
   
   The output priority of Syslog packets is configured.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.