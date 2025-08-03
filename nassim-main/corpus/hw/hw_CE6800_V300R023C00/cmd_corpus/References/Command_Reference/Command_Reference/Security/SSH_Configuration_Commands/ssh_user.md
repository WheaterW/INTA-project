ssh user
========

ssh user

Function
--------



The **ssh user** command creates an SSH user.

The **ssh user assign** command assigns an existing public key to an SSH user.

The **ssh user authentication-type** command configures the authentication type of an SSH user.

The **ssh user service-type** command configures the service type for the SSH user.

The **ssh user sftp-directory** command configures the authorized directory of the SFTP service for SSH users.

The **undo ssh user** command deletes an SSH user.

The **undo ssh user assign** command deletes the binding between an SSH user and a public key.

The **undo ssh user authentication-type** command deletes the configured authentication mode.

The **undo ssh user service-type** command restores the default service type of an SSH user.

The **undo ssh user sftp-directory** command cancels the authorized SFTP service directory for an SSH user.



By default, no ssh user is created, public key is not assigned to the user, the authentication type of the SSH user is not configured, the service type of the SSH user is not configured, the authorized directory of the SFTP service for the SSH user is not configured.


Format
------

**ssh user** *user-name*

**ssh user** *user-name* **assign** { **rsa-key** | **dsa-key** | **ecc-key** | **sm2-key** } *key-name*

**ssh user** *user-name* **authentication-type** { **password** | **rsa** | **password-rsa** | **dsa** | **password-dsa** | **all** | **ecc** | **password-ecc** | **sm2** | **password-sm2** | **password-x509v3-rsa** | **x509v3-rsa** }

**ssh user** *user-name* **service-type** { **sftp** | **stelnet** | **snetconf** } \*

**ssh user** *user-name* **sftp-directory** *directoryname*

**ssh user** *user-name* **assign** **pki** *pki-name*

**undo ssh user** [ *user-name* ]

**undo ssh user** *user-name* **assign** { **rsa-key** | **dsa-key** | **ecc-key** | **sm2-key** }

**undo ssh user** *user-name* **authentication-type**

**undo ssh user** *user-name* **service-type**

**undo ssh user** *user-name* **sftp-directory**

**undo ssh user** *user-name* **assign** **pki**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Indicates the name of an SSH user. | The value is a string of 1 to 253 case-insensitive characters. |
| **rsa-key** | Specifies to assign an RSA public key to a user. | - |
| **dsa-key** | Specifies to assign a DSA public key to a user. | - |
| **ecc-key** | Assigns an ECC public key to a user. | - |
| **sm2-key** | Assigns an SM2 public key to a user. | - |
| *key-name* | Specifies the name of an ECC public key generated on the client. | The value is a string of 1 to 40 case-sensitive characters, spaces not supported. |
| **password** | Indicates password authentication. | - |
| **rsa** | Sets the SSH user authentication mode to RSA.  To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits as the authentication type for SSH users. You are advised to use a more secure ECC authentication algorithm to improve security. | - |
| **password-rsa** | Indicates that both password authentication and RSA authentication must be adopted. | - |
| **dsa** | Indicates DSA authentication. | - |
| **password-dsa** | Indicates that both password authentication and DSA authentication must be adopted. | - |
| **all** | Indicates all authentication modes. | - |
| **ecc** | Indicates ECC authentication. | - |
| **password-ecc** | Indicates that both password authentication and ECC authentication must be adopted. | - |
| **sm2** | Indicates SM2 authentication. | - |
| **password-sm2** | Indicates that both password authentication and SM2 authentication must be adopted. | - |
| **password-x509v3-rsa** | Indicates that both password authentication and X509V3-SSH-RSA authentication must be adopted. | - |
| **x509v3-rsa** | Indicates X509V3-SSH-RSA authentication. | - |
| **sftp** | Indicates the SFTP service type. | - |
| **stelnet** | Indicates the STelnet and SCP service type. | - |
| **snetconf** | Indicates the SNETCONF service type. | - |
| **sftp-directory** *directoryname* | Specifies the directory name of the SFTP server. | The value is a string of 1 to 255 characters. |
| **pki** *pki-name* | Indicates PKI domain. | The value is a string of 1 to 64 case-insensitive characters without spaces. If an initial certificate is loaded to the specified PKI realm, the certificate is delivered in interactive mode. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* You can create an SSH user in either of the following ways:
* Run the **ssh user** command to create an SSH user.
* When you run the ssh user authentication-type, ssh user service-type or **ssh user sftp-directory** command, if the system detects that user-name does not exist, the system creates an SSH user named user-name.
* The highest privilege level of an SSH user is set to aaa or root using the **ssh authorization-type default aaa** or **ssh authorization-type default root** command.
* When you run the **ssh user assign** command to assign a public key to an SSH user:
  + If a public key has been assigned to a user, the last assigned public key takes effect.
  + The newly configured public key takes effect upon the next login.
  + When ECC/DSA/RSA authentication is performed for an SSH user, the ECC/DSA/RSA public key generated on the client needs to be sent to the server, and then the server assigns the public key to the SSH user.
  + Before running this command, ensure that the public key on the SSH client is valid.
  + To ensure high security, do not use the RSA algorithm whose length is less than 3072 bits as the authentication mode for SSH users. You are advised to use a more secure ECC authentication algorithm.
* You must specify an authentication mode for a new SSH user. Otherwise, the user cannot log in to the system. The newly configured authentication mode takes effect upon the next login.
* If an authentication type has been configured, running this command deletes the original authentication type and the new authentication type is used.
* Run the **ssh user service-type** command to configure the service type for the SSH user.
* When you run the **ssh user sftp-directory** command to configure an authorized SFTP service directory for an SSH user:
  + If user-name does not exist, create an SSH user named user-name and set the authorized SFTP service directory to the configured directory. Alternatively, use the user name configured in local-user <user-name> ftp-directory <directory> [ access-permission { read execute | read write execute } ] to log in.
  + If neither the configured directory nor the directory specified by local-user <user-name> ftp-directory <directory> [ access-permission { read execute | read write execute } ] exists, the SFTP client fails to connect to the SSH server.
  + When an SFTP user logs in to the device, the path configured using the **ssh user sftp-directory** command takes precedence over the path configured using the local-user <user-name> ftp-directory <directory> [ access-permission { read execute | read write execute } ] command. The path configured using the **sftp server default-directory** command has the lowest priority.
* These commands are valid for both IPv4 and IPv6.
* You can run the **display ssh user-information** command to view the configurations of all SSH users.
* If ssh user authentication-type all is executed, all can be any of the following types: password-rsa, password-dsa, password-ecc, password-sm2, and password-x509v3-rsa. The public key type in the end user authentication mode depends on the public key algorithm type negotiated during connection establishment. The priorities of public key algorithm negotiation are as follows: ECC, RSA\_SHA2\_512, RSA\_SHA2\_256, SM2, X509-RSA-SHA2-256, X509V3-SSH-RSA, RSA, DSA in descending order.


Example
-------

# Assign a PKI certificate to an SSH user.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser assign pki default
Warning: A preset certificate is loaded to the specified PKI domain. The current operation has security risks. Continue? [Y/N]:Y
[*HUAWEI]

```

# Configure the service type for SSH user testuser.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser service-type all

```

# Configure the SFTP service authorized directory of SSH users as flash:/ssh.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser sftp-directory flash:/ssh

```

# Delete the ssh user user123.
```
<HUAWEI> system-view
[~HUAWEI] undo ssh user user123

```

# Assign the key named sm2key001 to user testuser.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser assign sm2-key sm2key001

```

# Assign an ECC public key named key1 to the user named testuser.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser assign ecc-key key1

```

# Create an SSH user named testuser.
```
<HUAWEI> system-view
[~HUAWEI] ssh user testuser

```

# Set the authentication type to ECC to the SSH user named ssh\_user1@dom1.
```
<HUAWEI> system-view
[~HUAWEI] ssh user ssh_user1@dom1 authentication-type ecc

```