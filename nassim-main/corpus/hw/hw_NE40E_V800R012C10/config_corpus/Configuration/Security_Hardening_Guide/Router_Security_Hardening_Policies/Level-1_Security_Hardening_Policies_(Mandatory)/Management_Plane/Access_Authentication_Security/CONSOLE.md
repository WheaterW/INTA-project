CONSOLE
=======

CONSOLE

#### Security Policy

Serial ports are physical interfaces. Isolating serial ports in device deployment and networking can prevent malicious users from accessing devices by means of serial ports.

Serial ports support password authentication and authentication, authorization and accounting (AAA) authentication. Users can log in to a device through serial ports only after being authenticated. Authentication must be configured because no default authentication is available. Passwords used in authentication are encrypted using an irreversible algorithm.

When a device is started for the first time, no authentication configuration is available. Therefore, a user must configure authentication information using a serial port:

1. Connect a PC to the serial port of the device, access the serial port, and presses **Enter**. The system prompts the user to configure and confirm a password. After the password is successfully configured, the user accesses the command line interface.
2. The configured password has been saved as a configuration. You need to record the configured password. The authentication mode of the console user interface is password authentication, and the user has management-level rights.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The user must record the configured password to log in to the serial port for further management. If the user forgets the password and does not configure Telnet or SSH, the user will be unable to access the device.



#### Attack Methods

Without a serial server used, an attacker may attempt to break down physical isolation. Once an attacker accesses a serial port of a device, the device becomes exposed to the attacker, and the device is insecure. The attacker can damage the device even without obtaining a username or password.

When a serial server used, attackers may attempt to crack user names and passwords over network connections and obtain the system administrator rights.


#### Configuration and Maintenance Methods

Configure AAA authentication the first time a device is accessed.

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   The AAA view is displayed.
3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
   
   The local username and password are configured.
4. Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type** **terminal**
   
   The user access type is set to terminal.
5. Run [**quit**](cmdqueryname=quit)
   
   Exit the AAA view.
6. Run [**user-interface**](cmdqueryname=user-interface) **console** *interface-number*
   
   The console user interface view is displayed.
7. Run [**authentication-mode aaa**](cmdqueryname=authentication-mode+aaa)
   
   AAA authentication is enabled.
8. Run the [**local-user**](cmdqueryname=local-user) *user-name*[**user-group**](cmdqueryname=user-group) **manage-ug**
   
   The rights of the user is set to the management level.

#### Configuration and Maintenance Suggestions

Configure an appropriate authentication mode for a serial port to improve security.

* Password authentication or AAA authentication can be used. It is recommended that AAA authentication be configured to authenticate users based on user names and passwords.
* When no authentication mode is configured on a serial port, a user can log in to a device, access the console user interface ([**user-interface console 0**](cmdqueryname=user-interface+console+0)), configure AAA authentication, and configure a username and password in the AAA view.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Device passwords are stored in ciphertext. Therefore, a user must record the configured password because the user cannot restore the password if the password is lost



#### Verifying the Security Hardening Result

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration aaa** command to check the AAA configuration.