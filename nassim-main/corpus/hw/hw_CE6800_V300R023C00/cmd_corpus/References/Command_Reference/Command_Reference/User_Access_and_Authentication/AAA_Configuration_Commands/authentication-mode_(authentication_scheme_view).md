authentication-mode (authentication scheme view)
================================================

authentication-mode (authentication scheme view)

Function
--------



The **authentication-mode** command configures an authentication mode for an authentication scheme.

The **undo authentication-mode** command restores the default authentication mode in an authentication scheme.



By default, local authentication is used.


Format
------

**authentication-mode none**

**authentication-mode** { **hwtacacs** | **ldap** | { **local** | **local-case** } | **radius** } \* [ **none** ]

**undo authentication-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hwtacacs** | Authenticates users using an HWTACACS server. To perform HWTACACS authentication, configure an HWTACACS authentication server in an HWTACACS server template. | - |
| **local** | Authenticates users locally and sets local user names to case-insensitive. | - |
| **local-case** | Authenticates users locally and sets local user names to case-sensitive. | - |
| **radius** | Authenticates users using a RADIUS server. To perform RADIUS authentication, configure a RADIUS authentication server in a RADIUS server template. | - |
| **ldap** | Authenticates users using an LDAP server. To perform LDAP authentication, configure an LDAP authentication server in an LDAP server template. | - |
| **none** | Indicates non-authentication. That is, users access the network without being authenticated. | - |



Views
-----

Authentication scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To authenticate users, configure an authentication mode in an authentication scheme.If multiple authentication modes are configured in an authentication scheme, the authentication modes are used according to the sequence in which they were configured.

* In the sequence of local authentication followed by remote authentication:If a login account is not created locally but exists on the remote server, the authentication mode is changed from local authentication to remote authentication.If a login account is created locally and on the remote server, and local authentication fails because the password is incorrect, remote authentication will not be performed.
* In the sequence of remote authentication followed by local authentication:If a login account is created locally but not on the remote server, remote authentication fails and local authentication will not be performed.A user is authenticated using the local authentication mode only when the remote server is Down or does not respond to the user's authentication request.You can configure multiple authentication modes in an authentication scheme to reduce authentication failure possibilities.
* After the **authentication-mode radius local** command is used, the device cannot complete RADIUS authentication if it fails to connect to the RADIUS authentication server. In this case, the device starts local authentication.
* After the **authentication-mode local radius** command is used, if the entered user name exists on the device but the entered password is incorrect, the user fails the authentication; if the entered user name does not exist on the device, the user is redirected to the RADIUS authentication mode and is authenticated based on user information on the RADIUS server.

**Precautions**

* If you run the **authentication-mode none** command to set the authentication mode to non-authentication, an access user can be authenticated successfully after entering any user name and password. Therefore, to ensure device or network security, you are advised to enable the authentication mode to ensure that users can access the device or network only after being authenticated.
* If the **authentication-mode none** command is used to set the authentication mode to non-authentication and the authentication-mode (user interface view) command is used to set the authentication mode for administrators to AAA in the user interface view, the device does not allow administrators in the user interface view to log in to the device.


Example
-------

# Configure the authentication scheme named scheme1 to use RADIUS authentication.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme scheme1
[*HUAWEI-aaa-authen-scheme1] authentication-mode radius

```