local-user
==========

local-user

Function
--------

The **local-user** command creates a local user and sets parameters of the local user.

The **undo local-user** command deletes a local user.

By default, no local user is created in the system.



Format
------

**local-user** *user-name* { **password** **irreversible-cipher** *ir-password* | **access-limit** *max-number* | **idle-timeout** *minutes* [ *seconds* ] | **privilege** **level** *level* | **state** { **block** | **active** } } \*

**local-user** *user-name* **privilege** **level** *level*

**local-user** *user-name* **user-group** *user-group-value*

**local-user** *user-name* **ftp-directory** *directory* [ **read** **execute** [ **write** ] ]

**undo local-user** *user-name* [ **access-limit** | **ftp-directory** | **idle-timeout** | **privilege** **level** ]

**undo local-user** *user-name* **privilege** **level**

**undo local-user** *user-name* **user-group**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies the user name of a local administrator.  If the user name contains a domain name delimiter such as @, the character before @ is the user name and the character after @ is the domain name. If the value does not contain @, the entire character string is the user name and the domain name is the default one. | The value is a string of 1 to 253 case-sensitive characters. It cannot contain spaces. |
| **password** | Specifies the login password of the local administrator. | - |
| **irreversible-cipher** | irreversible-cipher indicates that the user password is encrypted using the irreversible algorithm. Unauthorized users cannot obtain the plain text by using the decryption algorithm. | If irreversible-cipher is specified, the password can be a string of 8 to 128 characters in plaintext or a string of 62 characters in ciphertext. |
| *ir-password* | Specifies the password of a local user. | The value is a string of 8 to 128 case-sensitive characters in plaintext or 62 case-sensitive characters in ciphertext. By default, the password must contain at least four types of the following characters, including uppercase letters, lowercase letters, digits, and special characters. Special characters do not include question marks (?) and spaces. However, if the password is enclosed in double quotation marks (" "), spaces are allowed in the password.  ? If double quotation marks are used to set a password with spaces, the double quotation marks cannot contain other double quotation marks.  ? If double quotation marks are used to set a password without any space, the double quotation marks can contain other double quotation marks.  For example, "a 123"45"" is an invalid password, but "a123"45"" is a valid password. |
| **access-limit** *max-number* | Indicates the maximum number of connections that can be created with a specified user name.  If this parameter is not specified, a user can establish a maximum of 4294967295 connections by default. | The value is an integer ranging from 1 to 4294967295.  The actual number of connections is the smaller value between max-number and the maximum number of users of a type on different models. |
| **idle-timeout** | Specifies the timeout period of the user interface. | - |
| *minutes* | minutes specifies the period when the user interface is disconnected, in minutes. | The value is an integer that ranges from 0 to 35791, in minutes. |
| *seconds* | seconds specifies the period when the user interface is disconnected, in seconds. | The value is an integer that ranges from 0 to 59, in seconds. |
| **privilege** | Specifies the privilege level of the local administrator. | - |
| **level** *level* | Specifies the privilege level of a local administrator. After logging in to the device, a user can run only the commands of the same or lower privilege level.  By default, a local administrator does not have a privilege level. | The value is an integer that ranges from 0 to 3. A larger value indicates a higher user privilege level. |
| **state** | Indicates the status of the local administrator. | - |
| **block** | block indicates that a local user is in blocking state. The device rejects the authentication request from the user and does not allow the user to change the password. | - |
| **active** | active indicates that a local user is in active state. The device accepts and processes the authentication request from the user, and allows the user to change the password. | - |
| **user-group** *user-group-value* | Name of a user group. | The value is a string of 1 to 32 case-insensitive characters, spaces not supported. |
| **ftp-directory** *directory* | Sets the directory that FTP users can access.  Ensure that the configured FTP directory is an absolute path; otherwise, the configuration does not take effect. | The value is a string of 1 to 255 case-sensitive characters without a blank space. |
| **read** | Grants the read permission. | - |
| **execute** | Grants the execute permission. | - |
| **write** | Grants the write permission. | - |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

* To facilitate device maintenance , create a local administrator on the device and configure the password, privilege level, and FTP directory.
* By default, the permission on the FTP directory is read, write, and execute.
* After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. You can run the **display security weak-password-dictionary** command to view the passwords.
* By default, a password must contain at least four types of the following characters, including uppercase letters, lowercase letters, digits, and special characters. You can run the **password complexity** command in the administrator password policy view to change the password complexity.

**Precautions**

1. If the timeout period of a user is not set or is set to 0, the timeout period of the user is not limited. In this case, the timeout period of the user depends on the configuration on the user interface.
2. The configured user group takes effect only when the local administrator privilege level is invalid (including the privilege levels configured using the local-user privilege level command and the admin-user privilege level command in the service scheme).
3. After the FIPS mode is enabled, the ftp-directory parameter cannot be used.
4. When setting ftp-directory, ensure that the path exists on both the active and standby boards. Otherwise, FTP users may fail to log in after an active/standby switchover.
5. To ensure device security, change the password periodically. When logging in to the device for the first time, the administrator must change the password.
6. The HTTP local administrator is provided for the web system. If the web system is not supported, you do not need to configure the HTTP local administrator.
7. After complexity check is enabled for the local administrator user name using the **undo local-aaa-user user-name complexity-check disable** command, the user name must contain at least six characters. This function is enabled by default.


Example
-------

# Create a local administrator, and set the user name to user1, domain name to vipdomain, password to YsHsjx\_202206 in cipher text, maximum number of connections to 100, and idle timeout period to 10 minutes.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] local-user user1@vipdomain password irreversible-cipher YsHsjx_202206 access-limit 100 idle-timeout 10

```