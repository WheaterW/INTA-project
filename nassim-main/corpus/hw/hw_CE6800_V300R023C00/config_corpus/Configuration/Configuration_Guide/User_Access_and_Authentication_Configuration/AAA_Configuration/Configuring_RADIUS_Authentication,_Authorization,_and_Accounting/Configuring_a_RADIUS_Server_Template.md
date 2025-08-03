Configuring a RADIUS Server Template
====================================

Configuring a RADIUS Server Template

#### Context

A RADIUS server template contains the IP address, port number, source interface, and shared key of a specific RADIUS server. The configurations in the template must be the same as those on the RADIUS server.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RADIUS server template and enter the RADIUS server template view.
   
   
   ```
   [radius-server template](cmdqueryname=radius-server+template) template-name
   ```
3. Configure a RADIUS authentication server.
   
   
   ```
   [radius-server authentication](cmdqueryname=radius-server+authentication) ip-address port [ shared-key cipher share-key | vpn-instance vpn-instance-name | source { interface-type interface-number | ip-address source-ip-address } | weight weight-value ] *
   ```
   
   By default, no RADIUS authentication server is configured. In the preceding command:
   
   * The **source** parameter specifies the source IP address in the packets sent from the device to the RADIUS authentication server. If this parameter is not specified, the IP address of the outbound interface is used as the source IP address.
   * The **weight** parameter specifies the weight of a RADIUS authentication server. If this parameter is not specified, the default weight 80 is used.
   * You are advised to specify **shared-key cipher** *key-string* when running this command. In this case, you do not need to run the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command to configure a shared key for the server. If this parameter is not specified, you need to run the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command. If both this command and the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command are configured, the former takes precedence.
   * If the **source** parameter is specified in this command and the [**radius-server source**](cmdqueryname=radius-server+source) **ip-address** command is run, the former takes effect.
4. Configure a RADIUS accounting server.
   
   
   ```
   [radius-server accounting](cmdqueryname=radius-server+accounting) ip-address port [ shared-key cipher share-key | vpn-instance vpn-instance-name | source { interface-type interface-number | ip-address source-ip-address } | weight weight-value ] *
   ```
   
   By default, no RADIUS accounting server is configured. In the preceding command:
   
   * The **source** parameter specifies the source IP address in the packets sent from the device to the RADIUS accounting server. If this parameter is not specified, the IP address of the outbound interface is used as the source IP address.
   * The **weight** parameter specifies the weight of a RADIUS accounting server. If this parameter is not specified, the default weight 80 is used.
   * You are advised to specify **shared-key cipher** *key-string* when running this command. In this case, you do not need to run the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command to configure a shared key for the server. If this parameter is not specified, you need to run the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command. If both this command and the [**radius-server shared-key**](cmdqueryname=radius-server+shared-key) **cipher** *key-string* command are configured, the former takes precedence.
   * If the **source** parameter is specified in this command and the [**radius-server source**](cmdqueryname=radius-server+source) **ip-address** command is run, the former takes effect.
5. (Optional) Configure a shared key for a RADIUS server.
   
   
   ```
   [radius-server shared-key](cmdqueryname=radius-server+shared-key) cipher key-string
   ```
   
   For security purposes, it is recommended that the shared key contain at least 16 characters and at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   
   For security purposes, you are advised to periodically change the shared key.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When a RADIUS server is configured in multiple RADIUS server templates:
   
   * If different shared keys are required in different RADIUS server templates, you need to configure a different shared key in each RADIUS server template view.
6. (Optional) Configure the algorithm for selecting RADIUS servers.
   
   
   ```
   [radius-server algorithm](cmdqueryname=radius-server+algorithm) { loading-share | master-backup }
   ```
   
   
   
   By default, the algorithm for selecting RADIUS servers is **master-backup**, indicating the primary/secondary algorithm.
   
   ![](public_sys-resources/note_3.0-en-us.png) When multiple authentication or accounting servers are configured in a RADIUS server template, the device selects RADIUS servers based on the algorithm and weight configured for each RADIUS server.
   * If the primary/secondary algorithm is used, the server with a larger weight becomes the primary server. If the servers have the same weight, the server configured first becomes the primary server.
   * If the load balancing algorithm is used, packets are sent to the servers according to weights of the servers.
7. (Optional) Configure the format of the user name in the packets sent from the device to a RADIUS server.
   
   
   
   **Table 1** Configuring the format of the user name in the packets sent from the device to a RADIUS server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the device not to modify the user name entered by the user in the packets sent to a RADIUS server. | [**radius-server user-name original**](cmdqueryname=radius-server+user-name+original) | By default, a new RADIUS server template has the **radius-server user-name domain-included** command configuration, indicating that the device encapsulates the domain name in the user name in the packets sent to a RADIUS server. |
   | Configure the device to encapsulate the domain name in the user name in the packets sent to a RADIUS server. | [**radius-server user-name domain-included**](cmdqueryname=radius-server+user-name+domain-included) |
   | Configure the device not to encapsulate the domain name in the user name in the packets sent to a RADIUS server. | [**undo radius-server user-name domain-included**](cmdqueryname=undo+radius-server+user-name+domain-included) |
8. (Optional) Set the number of times that RADIUS Access-Request packets are retransmitted and the timeout period.
   
   
   ```
   [radius-server](cmdqueryname=radius-server) { retransmit retry-times | timeout time-value } 
   ```
   
   
   
   By default, RADIUS Access-Request packets can be retransmitted 3 times, and the timeout period is 5 seconds.
9. (Optional) Configure the unit in which the traffic of a RADIUS server is measured.
   
   
   ```
   [radius-server traffic-unit](cmdqueryname=radius-server+traffic-unit) { byte | kbyte | mbyte | gbyte }
   ```
   
   By default, the traffic of a RADIUS server is measured in bytes.
10. (Optional) Configure the source IP address for communication between the device and RADIUS server.
    
    
    ```
    [radius-server source](cmdqueryname=radius-server+source) ip-address source-ip-address
    ```
    
    By default, no source IP address is configured for communication between the device and RADIUS server.
    
    If this command is run and the **source** parameter is specified in the [**radius-server authentication**](cmdqueryname=radius-server+authentication) command, the latter configuration takes effect.
11. (Optional) Enable the device to encapsulate the RADIUS attribute Framed-IP-Address into a RADIUS Access-Request packet when the RADIUS Access-Request packet sent by a user does not carry the user IP address.
    
    
    ```
    radius-server framed-ip-address no-user-ip enable
    ```
    
    By default, the device does not encapsulate the RADIUS attribute Framed-IP-Address into a RADIUS Access-Request packet when the RADIUS Access-Request packet sent by a user does not carry the user IP address.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **template** *template-name* ] command to check the configuration of a specified RADIUS server template.
* Run the [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **radius-template** *template-name* [ **chap** | **pap** | **accounting** [ **start** | **realtime** | **stop** ] ] [ **called-station-id** ] command to test the connectivity between the device and server. For details about common fault information and troubleshooting methods, see [Testing the Server Connectivity](galaxy_aaa_cfg_0054.html).

####