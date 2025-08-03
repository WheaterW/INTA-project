local-user service-type
=======================

local-user service-type

Function
--------

The **local-user service-type** command sets the access type for a local user.

The **undo local-user service-type** command restores the default access type for a local user.

By default, a local user cannot use any access type.



Format
------

**local-user** *user-name* **service-type** { **none** | { **http** | **ftp** | **ssh** | **telnet** | **terminal** | **snmp** | **md-cli** } \* }

**undo local-user** *user-name* **service-type**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies a user name.  If the user name contains a domain name delimiter such as @, the character before @ is the user name and the character behind @ is the domain name. If the value does not contain @, the entire character string is the user name and the domain name is the default one. | The value is a string of 1 to 253 case-sensitive characters. It cannot contain spaces. |
| **none** | Indicates no access type. | - |
| **http** | Indicates an HTTP user. | - |
| **ftp** | Indicates an FTP user. | - |
| **ssh** | Indicates an SSH user. | - |
| **telnet** | Indicates a Telnet user, which is usually a network administrator. | - |
| **terminal** | Indicates a terminal user, which is usually a user connected using a console port. | - |
| **snmp** | Indicates an SNMP user. | - |
| **md-cli** | Indicates an MD-CLI user. | - |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The device can manage access types of local users. After you specify the access type of a user, the user can successfully log in only when the configured access type is the same as the actual access type of the user.

**Precautions**

* Telnet and FTP login modes pose security risks. STelnet and SFTP are recommended. In this case, set the user access type to SSH.
* Before the access type of a local administrator is configured, if the user already exists and the password is encrypted using an irreversible encryption algorithm, only the access type of the management type can be configured. If a reversible encryption algorithm is used, the access type can be set to common or management, but cannot be set to a combination of common and management. If the access type is set to management, the encryption algorithm is automatically changed to an irreversible encryption algorithm.
* After the FIPS mode is enabled, the telnet and ftp parameters cannot be used.
* The local administrator of the HTTP type is provided for the web NMS. If the web NMS is not supported, you do not need to configure the local administrator of the HTTP type.


Example
-------

# Set the access type of the local user user1@vipdomain to SSH.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-user user1@vipdomain service-type ssh

```