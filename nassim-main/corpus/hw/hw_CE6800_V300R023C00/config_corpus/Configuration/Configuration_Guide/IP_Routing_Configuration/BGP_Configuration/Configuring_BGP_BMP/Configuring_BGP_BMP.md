Configuring BGP BMP
===================

Configuring BGP BMP

#### Prerequisites

Before configuring the BGP Monitoring Protocol (BMP), you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

BMP is mainly used in networking scenarios where monitoring servers exist and need to monitor the BGP running status and trace data of BGP routes on network devices in real time. Without BMP, only manual query can be used to obtain the BGP running status and trace data of BGP routes. The emergence of BMP eliminates this restriction and significantly improves network monitoring efficiency.


#### Procedure

* Configure BMP to report the BGP running status to a monitoring server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Start BMP and enter the BMP view.
     
     
     ```
     [bmp](cmdqueryname=bmp)
     ```
  3. (Optional) Configure an interval at which the BMP device sends BGP running statistics to a monitoring server.
     
     
     ```
     [statistics-timer](cmdqueryname=statistics-timer) time
     ```
     
     You can configure the interval at which the BMP device sends BGP running statistics to a monitoring server based on BGP stability requirements. In most cases, a short interval is required on a network with high quality requirements, but more bandwidth resources will be consumed because the device sends statistics frequently.
     
     By default, the interval at which the BMP device reports BGP running statistics to a monitoring server is 3600s. Using the default interval is recommended.
  4. Configure an IPv4 session address for the TCP connection to be established between the BMP device and the monitoring server.
     
     
     ```
     [bmp-session](cmdqueryname=bmp-session+vpn-instance+alias) [ vpn-instance vrf-name ] ipv4-address [ alias alias-name ]
     ```
     
     **alias** *alias-name* specifies a session alias. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  5. Configure the device to send statistics about routes of specific types to the monitoring server.
     
     
     + Configure the device to send statistics about RIB-in routes (all received routes or only accepted routes) from BGP peers in a specified address family.
       1. Run any of the following commands as required to enter the BMP-Monitor view and configure BMP to monitor the BGP running status of BGP peers.Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in the public network address family.
          ```
          [monitor](cmdqueryname=monitor+public) public 
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of a specified BGP peer in the public network address family.
          
          ```
          [monitor](cmdqueryname=monitor+peer) peer { ipv4-address | ipv6-address } 
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in VPN address families.
          
          ```
          [monitor all-vpn-instance](cmdqueryname=monitor+all-vpn-instance)
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of a specified BGP peer in a specified VPN instance.
          
          ```
          [monitor vpn-instance](cmdqueryname=monitor+vpn-instance+peer) vpn-instance-name peer { ipv4-address | ipv6-address }
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in a specified VPN instance.
          
          ```
          [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
          ```
       2. Configure the BMP device to send statistics about RIB-in routes (all received routes or only accepted routes) of BGP peers in a specified address family to the monitoring server.
          
          ```
          [route-mode](cmdqueryname=route-mode+ipv4-family+unicast+adj-rib-in+pre-policy+post-policy) ipv4-family unicast adj-rib-in { pre-policy | post-policy }
          ```
          
          To configure the device to send statistics about all received routes to the monitoring server, specify **pre-policy** in the command. To configure the device to send statistics about only the routes that match the import policy (those delivered to the routing table) to the monitoring server, specify **post-policy** in the command.
          
          ![](public_sys-resources/note_3.0-en-us.png) 
          
          If the **pre-policy** parameter is specified in the command, run the [**keep-all-routes**](cmdqueryname=keep-all-routes) command in the BGP view to save information about routes carried in BGP Update messages that are received from all BGP peers or peer groups after BGP connections are established. Alternatively, run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to save information about routes carried in the BGP Update messages that are received from a specified BGP peer or peer group after the BGP connection is established.
     + Configure the BMP device to send statistics about RIB-out routes of BGP peers in a specified address family to the monitoring server.
       1. Run any of the following commands as required to enter the BMP-Monitor view and configure BMP to monitor the BGP running status of BGP peers.Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in the public network address family.
          ```
          [monitor](cmdqueryname=monitor+public) public 
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of a specified BGP peer in the public network address family.
          
          ```
          [monitor](cmdqueryname=monitor+peer) peer { ipv4-address | ipv6-address } 
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in VPN address families.
          
          ```
          [monitor all-vpn-instance](cmdqueryname=monitor+all-vpn-instance)
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of a specified BGP peer in a specified VPN instance.
          
          ```
          [monitor vpn-instance](cmdqueryname=monitor+vpn-instance+peer) vpn-instance-name peer { ipv4-address | ipv6-address }
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in a specified VPN instance.
          
          ```
          [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
          ```
       2. Configure the BMP device to send statistics about RIB-out routes of BGP peers in a specified address family to the monitoring server.
          ```
          [route-mode](cmdqueryname=route-mode+ipv4-family+unicast+adj-rib-out+pre-policy) ipv4-family unicast adj-rib-out { pre-policy | post-policy }
          ```
          
          If you want the monitoring server to monitor all the routes to be advertised, regardless of whether they match the export policy, specify **pre-policy** in the command. If you want the monitoring server to monitor only the routes that match the export policy, specify **post-policy** in the command.
     + Configure the device to send statistics about Local-RIB routes of BGP peers in a specified address family.
       1. Enter the BMP-Monitor view and configure BMP to monitor the running status of BGP peers.Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in the public network address family.
          ```
          [monitor](cmdqueryname=monitor+public) public 
          ```
          
          Enter the BMP-Monitor view and configure BMP to monitor the running status of all BGP peers in a specified VPN instance.
          ```
          [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
          ```
       2. Configure the BMP device to send statistics about Local-RIB routes of BGP peers in a specified address family to the monitoring server.
          ```
          [route-mode](cmdqueryname=route-mode+ipv4-family+unicast+local-rib+add-path+all) ipv4-family unicast local-rib [ add-path | all ] [ path-marking ]
          ```
  6. Return to the BMP session view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Configure parameters for a TCP connection to be established between the device and monitoring server.
     
     
     ```
     [tcp](cmdqueryname=tcp+connect+port+password+md5+keychain) connect port port-number [ password md5 cipher-password | keychain keychain-name ]
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For security purposes, MD5 is not recommended. If MD5 is required, run the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command first to install the weak security algorithm/protocol feature package WEAKEA.
     
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
     + To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically.
  8. (Optional) Configure an SSL policy for BMP.
     
     
     ```
     [ssl-policy name](cmdqueryname=ssl-policy+name) policy-name
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Ensure that the specified SSL policy has been created using the [**ssl policy**](cmdqueryname=ssl+policy) *policy-name* command in the system view.
  9. (Optional) Configure a source interface for sending BMP messages.
     
     
     ```
     [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv4-source-address | interface-type interface-number | interface-name ipv4-source-address | interface-type interface-number ipv4-source-address }
     ```
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure BMP to report the trace data of IPv4 public network unicast routes to the monitoring server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Start BMP and enter the BMP view.
     
     
     ```
     [bmp](cmdqueryname=bmp)
     ```
  3. Configure an IPv4 session address for the TCP connection to be established between the BMP device and the monitoring server.
     
     
     ```
     [bmp-session](cmdqueryname=bmp-session+vpn-instance+alias) [ vpn-instance vrf-name ] ipv4-address [ alias alias-name ]
     ```
     
     
     
     **alias** *alias-name* specifies a session alias. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  4. Create and enter the BMP session IPv4 unicast view.
     
     
     ```
     [ipv4 unicast](cmdqueryname=ipv4+unicast)
     ```
  5. Configure BMP to monitor the trace data of all IPv4 public network unicast routes or the trace data of a specified IPv4 public network unicast route.
     
     
     ```
     [trace-prefix all](cmdqueryname=trace-prefix+all) or [trace-prefix](cmdqueryname=trace-prefix) ipv4-address mask-length
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure BMP to report the trace data of VPNv4 routes and the IPv4 VPN unicast routes to the monitoring server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Start BMP and enter the BMP view.
     
     
     ```
     [bmp](cmdqueryname=bmp)
     ```
  3. Configure an IPv4 session address for the TCP connection to be established between the BMP device and the monitoring server.
     
     
     ```
     [bmp-session](cmdqueryname=bmp-session+vpn-instance+alias) [ vpn-instance vrf-name ] ipv4-address [ alias alias-name ]
     ```
     
     
     
     **alias** *alias-name* specifies a session alias. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  4. Create and enter the BMP session IPv4 VPN view.
     
     
     ```
     [ipv4 vpn](cmdqueryname=ipv4+vpn)
     ```
  5. Configure BMP to monitor the trace data of all VPNv4 routes and IPv4 VPN unicast routes based on a specified RD. Alternatively, configure BMP to monitor the trace data of a VPNv4 route and the IPv4 VPN unicast route with a specified RD and route prefix.
     
     
     ```
     [trace-prefix route-distinguisher all](cmdqueryname=trace-prefix+route-distinguisher+all) or [trace-prefix route-distinguisher](cmdqueryname=trace-prefix+route-distinguisher) vrfRD ipv4-address mask-length
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bmp session**](cmdqueryname=display+bmp+session) [ **vpn-instance** *vrf-name* ] [ *ipv4-address* [ **alias** *alias-name* ] **verbose** ] command to check the configuration of the BMP session.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor) { **all** | **ipv4** *ipv4-address* } command to check information about BGP peers monitored through BMP in all address families or in a specified address family.
* Run the **display debugging bmp** command to check information about enabled BMP debugging functions.
* Run the [**display default-parameter bmp**](cmdqueryname=display+default-parameter+bmp) command to view default BMP configurations.