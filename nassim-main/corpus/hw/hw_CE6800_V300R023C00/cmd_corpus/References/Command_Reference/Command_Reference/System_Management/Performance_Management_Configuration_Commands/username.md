username
========

username

Function
--------



The **username** command configures the user name and password for logging in to the PM server.

The **undo username** command deletes the user name and password for logging in to the PM server.



By default, no user name and password for logging in to the PM server are configured.


Format
------

**username** *user-name* **password** [ *password* ]

**undo username**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **password** *password* | Specifies the password for logging in to a PM server.   * No security requirements of the password are needed when configuring remote server password as Client. * We advise the new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters. * For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password. | The password is a string of 1 to 128 case-sensitive characters, spaces or question marks not supported. The ciphertext of a configured password is a string of 24 or 32 to 268 characters in the configuration file.  When quotation marks are used around the string, spaces are allowed in the string. |
| **username** *user-name* | Specifies the user name for logging in to a PM server. | The name is a string of 1 to 255 case-sensitive characters, spaces or question marks not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

PM server view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before you log in to a PM server for upload performance statistics files to the PM server, run the username password command to configure the user name and password.

**Precautions**



In FIPS mode, passwords can be entered only in interactive mode.The configured password cannot be all asterisks (\*).




Example
-------

# Configure the username and password for logging in to a PM server.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] pm-server a
[*HUAWEI-pm-server-a] username admin password YsHsjx_202206

```