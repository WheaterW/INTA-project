Configuring an HWTACACS Server Template
=======================================

Configuring an HWTACACS Server Template

#### Context

The device uses an HWTACACS server template to specify the HWTACACS server to be connected to the device. This template contains the IP address, port number, source interface, and shared key of the HWTACACS server. The configurations in this template must be the same as those on the HWTACACS server.

![](public_sys-resources/note_3.0-en-us.png) 

When the HWTACACS server supports the multiplexing mode, if the **mux-mode** parameter is specified during the configuration of the HWTACACS authentication, authorization, or accounting server, the server multiplexing mode is enabled. After the server multiplexing mode is enabled, the TCP connection established for authentication, authorization, or accounting is not closed immediately. New authentication, authorization, or accounting requests will continue to use this TCP connection within a certain period of time to improve the authentication, authorization, or accounting rate. By default, the server multiplexing mode is disabled.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an HWTACACS server template and enter its view.
   
   
   ```
   [hwtacacs-server template](cmdqueryname=hwtacacs-server+template) template-name
   ```
3. Configure the HWTACACS authentication server.
   
   
   ```
   [hwtacacs-server authentication](cmdqueryname=hwtacacs-server+authentication) ipv4-address [ port ] [ public-net | vpn-instance vpn-instance-name ] [ secondary | third | fourth ] [ shared-key cipher cipher-string ] [ mux-mode ]
   ```
4. Configure the HWTACACS authorization server.
   
   
   ```
   [hwtacacs-server authorization](cmdqueryname=hwtacacs-server+authorization) ipv4-address [ port ] [ public-net | vpn-instance vpn-instance-name ] [ secondary | third | fourth ] [ shared-key cipher cipher-string ] [ mux-mode ]
   ```
5. Configure the HWTACACS accounting server.
   
   
   ```
   [hwtacacs-server accounting](cmdqueryname=hwtacacs-server+accounting) ipv4-address [ port ] [ public-net | vpn-instance vpn-instance-name ] [ secondary | third | fourth ] [ shared-key cipher cipher-string ] [ mux-mode ]
   ```
6. Configure the shared key of the HWTACACS server.
   
   
   ```
   [hwtacacs-server shared-key](cmdqueryname=hwtacacs-server+shared-key) cipher key-string
   ```
   
   For security purposes, it is recommended that the shared key contain at least 16 characters and at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   
   For security purposes, you are advised to periodically change the shared key.
7. (Optional) Configure the source IP address for communication between the device and HWTACACS server.
   
   
   ```
   [hwtacacs-server source-ip](cmdqueryname=hwtacacs-server+source-ip) { ip-address | source-loopback interface-number | source-vlanif interface-number1 }
   ```
   
   By default, the device uses the IP address of an outbound interface as the source IP address of HWTACACS packets.
8. (Optional) Configure the format of the user name in the packets sent by the device to the HWTACACS server.
   
   
   
   **Table 1** Configuring the format of the user name in the packets sent to the HWTACACS server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the user name entered by a user as the user name in the packets to be sent from the device to an HWTACACS server. | [**hwtacacs-server user-name original**](cmdqueryname=hwtacacs-server+user-name+original) | By default, the device encapsulates the domain name in the user name in the packets sent to the HWTACACS server. |
   | Configure the device to encapsulate a domain name in the user name when sending packets to the HWTACACS server. | [**hwtacacs-server user-name domain-included**](cmdqueryname=hwtacacs-server+user-name+domain-included) |
   | Configure the device not to encapsulate a domain name in the user name when sending packets to the HWTACACS server. | [**undo hwtacacs-server user-name domain-included**](cmdqueryname=undo+hwtacacs-server+user-name+domain-included) |
9. (Optional) Configure a user name to be carried in the authentication start packets of administrators.
   
   
   ```
   hwtacacs-server authentication user-name in-authentication-start
   ```
   
   By default, the authentication start packets of administrators do not carry the user name.
   
   This function takes effect only for administrators.
10. (Optional) Configure the unit in which the traffic of an HWTACACS server is measured.
    
    
    ```
    [hwtacacs-server traffic-unit](cmdqueryname=hwtacacs-server+traffic-unit) { byte | kbyte | mbyte | gbyte }
    ```
    
    By default, the traffic of an HWTACACS server is measured in bytes.
11. (Optional) Set the response timeout interval and activation interval for the HWTACACS server.
    
    
    
    | Operation | | Command | Description |
    | --- | --- | --- | --- |
    | Set the response timeout interval for the HWTACACS server. | | [**hwtacacs-server timer response-timeout**](cmdqueryname=hwtacacs-server+timer+response-timeout) *interval* | By default, the HWTACACS response timeout interval is 5 seconds.  If the device does not receive any response from the HWTACACS server within the specified response timeout interval, the device considers the HWTACACS server unavailable. In this case, the device attempts to use other authentication and authorization methods. |
    | Set the activation interval for the primary HWTACACS server. | | [**hwtacacs-server timer quiet**](cmdqueryname=hwtacacs-server+timer+quiet) *value* | By default, the primary HWTACACS server needs to wait for 5 minutes before it is restored to the active state. |
12. (Optional) In the user view, change the user password saved on the HWTACACS server.
    
    
    ```
    [hwtacacs-user change-password hwtacacs-server](cmdqueryname=hwtacacs-user+change-password+hwtacacs-server) template-name
    ```
    ![](public_sys-resources/note_3.0-en-us.png) 
    * For security purposes, change the password periodically.
    * After the weak password dictionary maintenance function is enabled, the passwords (which can be queried using the [**display security weak-password-dictionary**](cmdqueryname=display+security+weak-password-dictionary) command) defined in the weak password dictionary cannot be specified in this command.
    
    For example, run the following command to change the password of the user **user1** on the HWTACACS server. This user uses the HWTACACS server template named **huawei**.
    
    ```
    <HUAWEI> hwtacacs-user change-password hwtacacs-server huawei
    Username:user1
    Old Password: 
    New Password: 
    Re-enter New password: 
    Info: The password has been changed successfully. 
    ```
13. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display hwtacacs-server template**](cmdqueryname=display+hwtacacs-server+template) [ **name** *template-name* [ **verbose** ] ] command to check the HWTACACS server template configuration.
* Run the [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **hwtacacs-template** *template-name* [ **accounting** ] command to test the connectivity between the device and server. For details about common fault information and troubleshooting methods, see [Testing the Server Connectivity](galaxy_aaa_cfg_0054.html).