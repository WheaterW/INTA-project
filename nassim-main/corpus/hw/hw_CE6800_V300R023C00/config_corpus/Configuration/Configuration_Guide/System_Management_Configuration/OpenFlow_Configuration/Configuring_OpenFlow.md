Configuring OpenFlow
====================

Configuring OpenFlow

#### Prerequisites

Before configuring the OpenFlow agent on a device, complete the following tasks:

* Configure OpenFlow connection parameters on the controller.
* Ensure reachable routes between the device and controller.
* (Optional) [Configure a keychain.](vrp_keychain_cfg_0001.html)
  
  To enhance network security, configure keychain authentication for the OpenFlow connection. If keychain authentication is configured on the device or controller, make sure to configure it on the other end; otherwise, the OpenFlow connection cannot be set up.
* (Optional) [Configure the SSL policy.](galaxy_ssl_cfg_0001.html)
  
  To improve network security, configure an SSL policy for the OpenFlow connection. The device functions as an SSL client. If an SSL policy is configured on the device or controller, make sure to configure it on the other end; otherwise, the OpenFlow connection cannot be set up.
  
  ![](public_sys-resources/notice_3.0-en-us.png) 
  
  If keychain authentication or an SSL policy is not configured, security risks exist. To ensure network security, you are advised to configure keychain authentication or an SSL policy.


#### Context

Devices can set up OpenFlow connections with Huawei's iMaster NCE-Fabric, but not third-party controllers.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an OpenFlow-compatible device, and enter the SDN agent view.
   
   
   ```
   [sdn agent](cmdqueryname=sdn+agent)
   ```
   
   
   
   By default, a device is not OpenFlow-compatible.
3. Configure the global IP address used to establish an OpenFlow connection with the controller.
   
   On an IPv4 network:
   ```
   [source-ip](cmdqueryname=source-ip) ip-address
   ```
   
   After the global IPv4 address is configured, the device uses it to establish an OpenFlow connection with a controller by default.
   
   The device supports only one global IP address used to establish an OpenFlow connection with the controller. To reconfigure this IPv4 address, run the [**undo source-ip**](cmdqueryname=undo+source-ip) [ *ip-address* ] command to delete the existing one first.
   
   By default, the global IPv4 address used to establish an OpenFlow connection with a controller is not configured. The IP address of a loopback interface is recommended.
   
   
   
   On an IPv6 network:
   
   ```
   [source-ipv6](cmdqueryname=source-ipv6) ipv6-address
   ```
   
   After the global IPv6 address is configured, the device uses it to establish an OpenFlow connection with a controller by default.
   
   The device supports only one global IPv6 address used to establish an OpenFlow connection with a controller. To reconfigure this IPv6 address, run the [**undo source-ipv6**](cmdqueryname=undo+source-ipv6) [ *ipv6-address* ] command to delete the existing one first.
   
   By default, the global IPv6 address used to establish an OpenFlow connection with a controller is not configured. The IP address of a loopback interface is recommended.
4. (Optional) Configure the description of an OpenFlow-compatible device.
   
   
   ```
   [description](cmdqueryname=description) text
   ```
   
   
   
   There may be many OpenFlow-compatible devices on an SDN network. To facilitate memorization and management, you can run the [**description**](cmdqueryname=description) command on different devices to identify device features, such as the device location and access service.
   
   By default, no description is configured for an OpenFlow-compatible device.
5. Configure an IP address for the controller that establishes an OpenFlow connection with the device, and enter the Controller-IP view.
   
   
   
   On an IPv4 network:
   
   
   
   ```
   [controller-ip](cmdqueryname=controller-ip) [ vpn-instance vpn-instance-name ] ipv4-address
   ```
   
   
   
   The device supports a maximum of 16 controller IPv4 addresses. If you need to reconfigure the IPv4 address of the controller connected to the device, run the [**undo controller-ip**](cmdqueryname=undo+controller-ip) [ **vpn-instance** *vpn-instance-name* ] *ip-address* command to delete the original IPv4 address of the controller first.
   
   
   
   On an IPv6 network:
   
   ```
   [controller-ipv6](cmdqueryname=controller-ipv6) [ vpn-instance vpn-instance-name ] ipv6-address
   ```
   
   A maximum of 16 controller IPv4 and IPv6 addresses can be configured on a device. To reconfigure a controller IPv6 address, run the [**undo controller-ipv6**](cmdqueryname=undo+controller-ipv6) [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* command to delete the existing one first.
   
   By default, the controller IPv6 address used to establish an OpenFlow connection with the device is not configured.
6. (Optional) Create an OpenFlow agent and enter the OpenFlow agent view.
   
   
   ```
   [openflow agent](cmdqueryname=openflow+agent)
   ```
   
   By default, no OpenFlow agent view is created.
7. (Optional) Configure the IP address used to establish an OpenFlow connection with the specified controller.
   
   
   
   On an IPv4 network:
   
   ```
   [transport-address](cmdqueryname=transport-address) ip-address
   ```
   
   By default, the IPv4 address used to establish an OpenFlow connection with the specified controller is not configured. The IP address of a loopback interface is recommended.
   
   
   
   On an IPv6 network:
   
   ```
   [transport-address](cmdqueryname=transport-address) ipv6-address
   ```
   
   By default, the IPv6 address used to establish an OpenFlow connection with the specified controller is not configured. The IP address of a loopback interface is recommended.
8. (Optional) Configure keychain authentication or an SSL policy for the OpenFlow connection to enhance network security. Keychain authentication and an SSL policy cannot be both configured for the same OpenFlow connection.
   1. Configure keychain authentication for the OpenFlow connection.
      
      
      ```
      [authentication keychain](cmdqueryname=authentication+keychain) keychain-name
      ```
      
      By default, keychain authentication is not configured for an OpenFlow connection.
   2. Configure an SSL policy for an OpenFlow connection.
      
      
      ```
      [authentication ssl](cmdqueryname=authentication+ssl) ssl-policy ssl-policy-name
      ```
      
      By default, no SSL policy is configured for an OpenFlow connection.
9. (Optional) Set a heartbeat interval for OpenFlow connections.
   
   
   ```
   [echo-interval](cmdqueryname=echo-interval) interval
   ```
   
   As specified by the OpenFlow protocol, the controller and device periodically exchange ECHO packets to detect whether the peer end is still available. If the initiator does not receive any OpenFlow packet after sending five consecutive ECHO\_REQUEST packets, it considers the peer device failed and closes the OpenFlow connection. If the initiator receives an OpenFlow before closing the OpenFlow connection, it restarts the counter.
   
   By default, the heartbeat interval of the OpenFlow connection is 5 seconds.
10. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    [quit](cmdqueryname=quit)
    [quit](cmdqueryname=quit)
    ```
11. (Optional) Set a DSCP priority for OpenFlow packets.
    
    
    ```
    [openflow dscp](cmdqueryname=openflow+dscp) dscp-value
    ```
    
    
    
    If you run the [**set priority dscp**](cmdqueryname=set+priority+dscp) and [**openflow dscp**](cmdqueryname=openflow+dscp) commands to set the DSCP priority of IP packets and OpenFlow packets, respectively, the DSCP priority configured using the [**openflow dscp**](cmdqueryname=openflow+dscp) command takes effect. If neither of these commands is run, the DSCP priority of OpenFlow packets is 0.
    
    By default, the DSCP priority of OpenFlow packets is the DSCP priority configured using the [**set priority dscp**](cmdqueryname=set+priority+dscp) command.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display sdn openflow session**](cmdqueryname=display+sdn+openflow+session) [ **slave** ] command to check whether the OpenFlow connection is successfully established.
* Run the [**display this**](cmdqueryname=display+this) command in the OpenFlow agent view to check the information about OpenFlow connection authentication and configured heartbeat interval.