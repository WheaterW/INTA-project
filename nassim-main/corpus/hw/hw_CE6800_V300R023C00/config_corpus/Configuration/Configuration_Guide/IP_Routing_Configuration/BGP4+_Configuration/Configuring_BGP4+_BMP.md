Configuring BGP4+ BMP
=====================

Configuring BGP4+ BMP

#### Prerequisites

Before configuring BGP4+ BMP, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Without BGP4+ BMP, you have to run a query command on a BGP4+ device to learn the device's BGP4+ running status. BMP greatly improves the efficiency of network monitoring, because without it, BGP4+ running status of devices can be obtained only through manual query.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Start BMP and enter the BMP view.
   
   
   ```
   [bmp](cmdqueryname=bmp)
   ```
3. (Optional) Configure an interval at which the BMP device sends BGP4+ running statistics to a monitoring server.
   
   
   ```
   [statistics-timer](cmdqueryname=statistics-timer) time
   ```
   
   You can configure the interval at which the BMP device sends BGP4+ running statistics to a monitoring server based on BGP4+ stability requirements. Usually, a shorter interval is required for greater stability, but this consumes more bandwidth resources because the device sends BGP4+ running statistics more frequently.
   
   By default, the interval at which the BMP device reports BGP4+ running statistics to a monitoring server is 3600s. Using the default interval is recommended.
4. Configure an IPv6 session address for the TCP connection to be established between the BMP device and the monitoring server.
   
   
   ```
   [bmp-session](cmdqueryname=bmp-session+vpn-instance+alias) [ vpn-instance vrf-name ] ipv6-address [ alias alias-name ]
   ```
   
   **alias** *alias-name* specifies a session alias. If the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify one IPv6 address and different session aliases (through the **alias** *alias-name* parameter) to differentiate each connection.
5. Configure the device to send statistics about routes of specific types to the monitoring server.
   
   
   * Configure the BMP device to send statistics about RIB-in routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
     1. Run any of the following commands as required to enter the BMP-Monitor view and configure BMP to monitor the running status of BGP4+ peers.Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in the public network address family.
        ```
        [monitor](cmdqueryname=monitor+public) public 
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of a specified BGP4+ peer in the public network address family.
        
        ```
        [monitor](cmdqueryname=monitor+peer) peer { ipv4-address | ipv6-address } 
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in VPN address families.
        
        ```
        [monitor all-vpn-instance](cmdqueryname=monitor+all-vpn-instance)
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of a specified BGP4+ peer in a specified VPN instance.
        
        ```
        [monitor vpn-instance](cmdqueryname=monitor+vpn-instance+peer) vpn-instance-name peer { ipv4-address | ipv6-address }
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in a specified VPN instance.
        
        ```
        [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
        ```
     2. Configure the BMP device to send statistics about RIB-in routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
        
        ```
        [route-mode](cmdqueryname=route-mode+ipv6-family+unicast+adj-rib-in+pre-policy+post-policy) ipv6-family unicast adj-rib-in { pre-policy | post-policy }
        ```
        
        To configure the device to send statistics about all received routes to the monitoring server, specify **pre-policy** in the command. To configure the device to send statistics about only the routes that match the import policy (those delivered to the routing table) to the monitoring server, specify **post-policy** in the command.
        
        ![](public_sys-resources/note_3.0-en-us.png) 
        
        If **pre-policy** is specified in the command, run the [**keep-all-routes**](cmdqueryname=keep-all-routes) command in the BGP view to save the routes carried in the BGP4+ Update messages that are received from all BGP4+ peers or peer groups after BGP4+ connections are established. Alternatively, run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to save the routes carried in the BGP4+ Update messages that are received from a specified BGP4+ peer or peer group after the BGP4+ connection is established.
   * Configure the BMP device to send statistics about RIB-out routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
     1. Run any of the following commands as required to enter the BMP-Monitor view and configure BMP to monitor the running status of BGP4+ peers.Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in the public network address family.
        ```
        [monitor](cmdqueryname=monitor+public) public 
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of a specified BGP4+ peer in the public network address family.
        
        ```
        [monitor](cmdqueryname=monitor+peer) peer { ipv4-address | ipv6-address } 
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in VPN address families.
        
        ```
        [monitor all-vpn-instance](cmdqueryname=monitor+all-vpn-instance)
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of a specified BGP4+ peer in a specified VPN instance.
        
        ```
        [monitor vpn-instance](cmdqueryname=monitor+vpn-instance+peer) vpn-instance-name peer { ipv4-address | ipv6-address }
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in a specified VPN instance.
        
        ```
        [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
        ```
     2. Configure the BMP device to send statistics about RIB-out routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
        
        ```
        [route-mode](cmdqueryname=route-mode+ipv6-family+unicast+adj-rib-out+pre-policy) ipv6-family unicast adj-rib-out { pre-policy | post-policy }
        ```
        
        If you want the monitoring server to monitor all the routes to be advertised, regardless of whether they match the export policy, specify **pre-policy** in the command. If you want the monitoring server to monitor only the routes that match the export policy, specify **post-policy** in the command.
   * Configure the device to send statistics about Local-RIB routes of BGP4+ peers in a specified address family.
     1. Enter the BMP-Monitor view and configure BMP to monitor the running status of BGP4+ peers.Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in the public network address family.
        ```
        [monitor](cmdqueryname=monitor+public) public 
        ```
        
        Enter the BMP-Monitor view and configure the device to monitor the running status of all BGP4+ peers in a specified VPN instance.
        ```
        [monitor vpn-instance](cmdqueryname=monitor+vpn-instance) vpn-instance-name
        ```
     2. Configure the BMP device to send statistics about Local-RIB routes of BGP4+ peers in a specified address family to the monitoring server.
        ```
        [route-mode](cmdqueryname=route-mode+ipv6-family+unicast+local-rib+add-path+all) ipv6-family unicast local-rib [ add-path| all ] [ path-marking ]
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
   * It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   * To prevent high security risks, you are advised to select the ciphertext mode. To ensure device security, change the password periodically.
8. (Optional) Configure an SSL policy for BMP.
   
   
   ```
   [ssl-policy name](cmdqueryname=ssl-policy+name) policy-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Ensure that the specified SSL policy has been created using the [**ssl policy**](cmdqueryname=ssl+policy) *policy-name* command in the system view.
9. (Optional) Configure a source interface for sending BMP messages.
   
   
   ```
   [connect-interface](cmdqueryname=connect-interface) { interface-name | ipv6-soure-address | interface-type interface-number | interface-name ipv6-soure-address | interface-type interface-number ipv6-soure-address }
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After configuring BMP session parameters, you can run the [**reset bmp session**](cmdqueryname=reset+bmp+session) command to reset the BMP session for the new BMP session parameters to take effect immediately.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bmp session**](cmdqueryname=display+bmp+session) [ **vpn-instance** *vrf-name* ] [ *ipv6-address* [ **alias** *alias-name* ] **verbose** ] command to check the configuration of the BMP session.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor) { **all** | **ipv6** *ipv6-address* } command to check information about BGP4+ peers monitored through BMP in all address families or in a specified address family.