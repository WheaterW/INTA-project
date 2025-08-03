snmp-agent usm-user
===================

snmp-agent usm-user

Function
--------



The **snmp-agent usm-user** command adds a user to an SNMP user list.

The **undo snmp-agent usm-user** command deletes a user from an SNMP user list.



By default, an SNMP user list does not have any user.


Format
------

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* *group-name* [ **authentication-mode** *authen-protocol* *authKey* [ **privacy-mode** *privacy-protocol* *privKey* ] ] [ **acl** { *acl-number* | *aclName* } ]

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* **authentication-mode** *authen-protocol*

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* **privacy-mode** *privacy-protocol*

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* [ **group** *group-name* | **acl** { *acl-number* | *aclName* } ] \*

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* **authentication-mode** *authen-protocol* [ **localized-configuration** ] **cipher** *authKey*

**snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* **privacy-mode** *privacy-protocol* [ **localized-configuration** ] **cipher** *privKey*

**undo snmp-agent** [ **remote-engineid** *engine-Id* ] **usm-user** **v3** *user-name* [ **group** | **acl** | **authentication-mode** | **privacy-mode** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **remote-engineid** *engine-Id* | Specifies the ID of an engine associated with a user. | The value is a string of 10 to 64 case-insensitive characters, spaces not supported. The value cannot be all 0s or all Fs. |
| **v3** | Enables the SNMPv3 security mode. | - |
| *user-name* | Specifies a username. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **authentication-mode** *authen-protocol* | Sets the security level to authentication.  Authentication allows an agent (or management station) to verify that received information is sent by an authorized management station (or agent) and is not modified during transmission. Related standards define keyed hash-based message authentication code (HMAC), which is an effective tool that uses a security hash function and a key to generate a message authentication code, and is widely applied in the Internet. SNMP uses six types of HMACs: HMAC-MD5-96, HMAC-SHA-96, HMAC-SHA2-224, HMAC-SHA2-256, HMAC-SHA2-384, and HMAC-SHA2-512. | * md5: HMAC-MD5-96 (Hashed Message Authentication Code for Message Digest 5-96) is used as the authentication protocol. * sha: HMAC-SHA-96 is used as the authentication protocol. * sha2-224: HMAC-SHA2-224 is used as the authentication protocol. * sha2-256: HMAC-SHA2-256 is used as the authentication protocol. * sha2-384: HMAC-SHA2-384 is used as the authentication protocol. * sha2-512: HMAC-SHA2-512 is used as the authentication protocol. SHA2-256 and more complex algorithms are more secure than SHA2-224, SHA, and MD5, and are therefore recommended. |
| *authKey* | Specifies an authentication password. The password can be in plaintext or ciphertext.  In ciphertext mode, you need to enter cipher and then a character string that has been processed by the encryption algorithm.  If the password is in plaintext, you do not need to enter cipher. After the authentication protocol is selected, the password is delivered in interactive mode. | The password is a string of 8 to 255 characters in plaintext or a string of 32 to 432 characters in ciphertext. |
| **privacy-mode** *privacy-protocol* | Enables encryption. | * 3des168: Sets the encryption algorithm to Advanced Encryption Standard (3DES168 (Triple Data Encryption Standard 168)). * aes128: Sets the encryption algorithm to Advanced Encryption Standard (AES128 (Advanced Encryption Standard 128)). * aes192: Sets the encryption algorithm to Advanced Encryption Standard (AES192 (Advanced Encryption Standard 192)). * aes256: Sets the encryption algorithm to Advanced Encryption Standard (AES256 (Advanced Encryption Standard 256)). * des56: specifies DES56 (Data Encryption Standard 56) as the encryption algorithm. AES128 and higher-level encryption algorithms are more secure than DES56 and 3DES168. and are therefore recommended. |
| *privKey* | Indicates the encryption password. The password can be in plaintext or ciphertext.  In ciphertext mode, you need to enter cipher and then a character string that has been processed by the encryption algorithm.  If the password is in plaintext, you do not need to enter cipher. After the authentication protocol is selected, the password is delivered in interactive mode. | The password is a string of 8 to 255 characters in plaintext or a string of 32 to 432 characters in ciphertext. |
| **acl** *acl-number* | Specifies the ACL of the access view.  Currently, SNMP supports only basic ACL4 and ACL6. | The value is an integer that ranges from 2000 to 2999. |
| **acl** *aclName* | Specifies the name of a basic named ACL.  If no matching rule is configured for the referenced ACL, the matching rule is permit by default. | The value is a string of 1 to 32 case-sensitive characters without spaces. |
| **group** *group-name* | Name of the SNMP user list to which a user belongs. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **localized-configuration** | Indicates the localized password configuration mode. The ciphertext password in the configuration file relates to the engine ID of the device.  After the SNMPv3 authentication and encryption passwords are configured through MIB, the ciphertext password in the configuration file is a localized password.  You are advised not to set this parameter when configuring the SNMPv3 authentication and encryption passwords in CLI mode. If you want to set this parameter, the cipher password value must be a localized password. If you copy a ciphertext password with localized-configuration from the configuration file of another device, the password cannot be used. | - |
| **cipher** | Specifies that the password is entered in encrypted text. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Different from SNMPv1 or SNMPv2c, SNMPv3 implements access control, identity authentication, and data encryption using the local processing module and user-based security module. SNMPv3 helps achieve higher security and confidentiality and is applicable to a wider range than SNMPv1 and SNMPv2c.The **snmp-agent usm-user** command configures a user in an SNMP user group, configures an authentication password and privacy password, and grants this user view-specific access.

**Precautions**

* In this command, parameters md5, sha, sha2-224, DES56, and 3DES168 can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.
* After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. To check the passwords defined in the weak password dictionary, run the **display security weak-password-dictionary** command.


Example
-------

# In confirmation mode, set the authentication mode to sha2-512 and the authentication password to hello123 for the SNMP user named John.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent usm-user v3 John authentication-mode sha2-512
Please configure the authentication password (8-255)
Enter Password:
Confirm Password:

```

# Add user John to SNMP user list Johngroup and associate the user with ACL 2001.
```
<HUAWEI> system-view
[~HUAWEI] acl 2001
[*HUAWEI-acl4-basic-2001] quit
[*HUAWEI] snmp-agent usm-user v3 John group Johngroup acl 2001

```