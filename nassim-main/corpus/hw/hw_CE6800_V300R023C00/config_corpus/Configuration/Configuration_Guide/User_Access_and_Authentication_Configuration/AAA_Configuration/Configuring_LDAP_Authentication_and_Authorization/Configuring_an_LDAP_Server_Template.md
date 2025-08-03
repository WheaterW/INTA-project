Configuring an LDAP Server Template
===================================

Configuring an LDAP Server Template

#### Context

In an LDAP server template, you must specify the server type, IP address, and port number. The other parameters have default settings, for example, the Base DN. These default settings can be modified as needed.

The LDAP server obtains the values of the user attribute filter field and group attribute filter field as the user name and group name, respectively. The user attribute filter field and group attribute filter field of the LDAP server do not need to be configured. Their default values are as follows:

* The user attribute filter fields vary according to the LDAP server type: sAMAccountName for AD-LDAP LDAP servers, cn for Open LDAP or IBM Tivoli LDAP servers, and uid for Sun ONE LDAP servers.
* The group attribute filter field of the LDAP server is ou.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an LDAP server template and enter the LDAP server template view.
   
   
   ```
   [ldap-server template](cmdqueryname=ldap-server+template) template-name
   ```
3. Set the LDAP server type.
   
   
   ```
   [ldap-server server-type](cmdqueryname=ldap-server+server-type) { ad-ldap | ibm-tivoli | open-ldap | sun-one }
   ```
   
   Set the LDAP server type based on the remote LDAP server type. By default, the LDAP server type in the LDAP server template created on the device is **ad-ldap**.
4. Configure an LDAP server.
   
   
   ```
   [ldap-server authentication](cmdqueryname=ldap-server+authentication) ip-address [ port ] [ secondary | third ] [ ssl | no-ssl ]
   ```
   
   By default, no LDAP server is configured. In the preceding command:
   
   * *port* specifies the port number of the LDAP server. If **ssl** is specified, the default port number is 636. If **no-ssl** is specified, the default port number is 389. The **ssl** parameter is specified by default.
   * **ssl** indicates that LDAP packets are encrypted for transmission based on the SSL protocol to improve security. After this parameter is configured, the device uses a CA certificate to verify the validity of the LDAP server.![](public_sys-resources/note_3.0-en-us.png) 
     
     After the FIPS mode is enabled, the **no-ssl** parameter cannot be used.
5. (Optional) Configure the source IP address for communication between the device and LDAP server.
   
   
   ```
   [ldap-server source](cmdqueryname=ldap-server+source) { loopback interface-number1 | ip-address ip-address | vlanif interface-number2 }
   ```
   
   By default, when the device sends packets to the LDAP server, the IP address of the outbound interface is used as the source IP address.
   
   If the specified loopback interface or VLANIF interface is not created or has no IP address configured, the IP address of the outbound interface is used as the source IP address.
6. Set a Base DN for the LDAP server.
   
   
   ```
   [ldap-server authentication base-dn](cmdqueryname=ldap-server+authentication+base-dn) base-dn
   ```
   
   By default, no the Base DN is configured for an LDAP server.
7. Set the administrator DN and password of the LDAP server.
   
   
   ```
   ldap-server authentication manager manager password
   ```
   
   By default, no administrator DN and password are configured for an LDAP server.
   
   For security purposes, it is recommended that the password contain at least eight characters and at least three types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   
   If you run the **ldap-server authentication manager-anonymous enable** command after the administrator DN and password of the LDAP server are set, the administrator DN and password settings will be automatically cleared, and the Base DN will also be deleted.
8. (Optional) Configure the server to allow administrators to log in anonymously.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   An anonymous login does not require the user name and password, posing security risks. Determine whether to enable anonymous login after risk assessment.
   
   ```
   ldap-server authentication manager-anonymous enable
   ```
   
   By default, administrators are not allowed to access the LDAP server anonymously.
   
   After the command is configured, if you run the **ldap-server authentication manager** *manager* *password* command to configure the administrator DN and password of the LDAP server, the anonymous login configuration will be cleared.
9. (Optional) Enable user binding during LDAP authorization.
   
   
   ```
   [ldap-server authorization bind-user enable](cmdqueryname=ldap-server+authorization+bind-user+enable)
   ```
   
   By default, user binding is required during LDAP authorization.
10. (Optional) Configure an administrator DN of the LDAP server to contain the Base DN.
    
    
    ```
    ldap-server authentication manager-with-base-dn enable
    ```
    
    By default, the Base DN is contained in the administrator DN during LDAP authentication.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display ldap-server template**](cmdqueryname=display+ldap-server+template) [ **name** *template-name* ] command to check the LDAP server template configuration.
* Run the [**test-aaa**](cmdqueryname=test-aaa) *user-name* *user-password* **ldap-template** *template-name* command to test the connectivity between the device and server. For details about common fault information and troubleshooting methods, see [Testing the Server Connectivity](galaxy_aaa_cfg_0054.html).