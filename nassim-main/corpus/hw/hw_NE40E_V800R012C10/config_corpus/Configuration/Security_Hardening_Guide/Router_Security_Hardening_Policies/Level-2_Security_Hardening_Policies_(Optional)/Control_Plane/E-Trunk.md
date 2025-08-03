E-Trunk
=======

This section describes a security policy, attack methods, configuration and maintenance methods, as well as configuration and maintenance suggestions for an E-Trunk.

#### Security Policies

* To improve system security, E-Trunk provides the configurable authentication function. The E-Trunk transmit end uses the configured password to calculate a packet digest for a heartbeat message and the receive end also calculates the packet digest after receiving the heartbeat message. If the two digests are the same, the heartbeat message is valid. Otherwise, the heartbeat message is invalid and discarded.
* To protect service traffic against replay attacks launched by attackers who can obtain E-Trunk packet characteristics, E-Trunk provides configurable sequence number verification. To ensure system security and normal traffic forwarding, run the **sequence enable** command to enable E-Trunk sequence number verification for attack packet identification.
* If packets are received, the E-Trunk checks the length, digest, and key parameters of the packets. Invalid packets, such as error packets, are discarded.
* By default, the E-Trunk uses UDP port 1025 to transmit and receive protocol packets. To improve security, the E-Trunk allows users to set E-Trunk port numbers.

#### Attack Methods

* Protocol authentication can be configured to defend against attacks. To prevent attacks, you can set the authentication algorithm to HMAC-SHA1, HMAC-SHA256, or ENHANCED-HMAC-SHA256.
* Configure sequence number verification to defend against attacks. You can run the **sequence enable** command to enable E-Trunk sequence number verification.

#### Configuration and Maintenance Methods

1. Run the [**authentication-mode**](cmdqueryname=authentication-mode) command in the E-Trunk view to configure an E-Trunk authentication or encryption mode.
2. Run the [**security-key**](cmdqueryname=security-key) { **simple** *simple-key* | **cipher** { *cipher-key1* | *cipher-key2* | *cipher-key3* } } command in the E-Trunk view to set an authentication key.
   
   You can specify **simple** or **cipher** as needed:
   * If **simple** is specified, a password is displayed in clear text in the configuration file.
   * If **cipher** is specified, a ciphertext password is displayed as unidentifiable characters.
     
     + *cipher-key1*: specifies a ciphertext password. The value is a string of 32 to 432 characters. It cannot contain spaces.
     + *cipher-key2*: specifies a 24-character ciphertext password configured in an earlier version. Such a password is automatically converted into a supported format after an upgrade.
     + *cipher-key3*: specifies a clear text password. The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces.
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If **simple** is configured, the password is saved in the configuration file in clear text. The users with the least privilege may obtain the password by viewing the configuration file. This causes a network security risk. Therefore, **cipher** is recommended.
   
   Two devices whose interfaces join the same E-Trunk interface must have the same password for encrypting packets. After an E-Trunk interface is created, you must manually set an encryption password. Otherwise, E-Trunk negotiation fails to be performed.
3. Run the [**sequence enable**](cmdqueryname=sequence+enable) command in the E-Trunk view to enable sequence number verification.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   The [**sequence enable**](cmdqueryname=sequence+enable) command must be run on both the master and backup devices in an E-Trunk. If this command is run on only one device, sequence number verification fails and packets are discarded. As a result, both devices in the E-Trunk become master devices.
4. Run the [**e-trunk port**](cmdqueryname=e-trunk+port) *port-number* command in the system view to set an E-Trunk interface number. The value is an integer ranging from 1025 to 65535. The default value is 1025.

#### Configuration and Maintenance Suggestions

To enhance security, you are advised to set a ciphertext password.

Enhanced-HMAC-SHA256 is recommended for authentication and encryption.

Enabling sequence number verification on both ends of an E-Trunk is recommended.


#### Verifying the Security Hardening Result

Run the **display e-trunk** *etrunk-id* command to check E-Trunk details.