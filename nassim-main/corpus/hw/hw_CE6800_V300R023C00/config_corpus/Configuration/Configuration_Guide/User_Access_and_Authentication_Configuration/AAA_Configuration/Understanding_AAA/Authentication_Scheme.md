Authentication Scheme
=====================

An authentication scheme defines the authentication methods to be used and the order in which authentication methods take effect.

#### Authentication Methods Supported by a Device

* RADIUS authentication: User information is configured on the RADIUS server through which user authentication is performed.
* HWTACACS authentication: User information is configured on the HWTACACS server through which user authentication is performed.
* LDAP authentication: User information is configured on the LDAP server through which user authentication is performed.
* Local authentication: The device functions as an authentication server and user information is configured on the device. This method features fast processing and low operation costs. However, the information storage capacity is subject to the device hardware.
* Non-authentication: Users are completely trusted without validity check. This method is rarely used.![](public_sys-resources/note_3.0-en-us.png) 
  + If the authentication method is set to non-authentication using the [**authentication-mode**](cmdqueryname=authentication-mode) [**none**](cmdqueryname=none) command, an access user will be authenticated successfully after entering any user name and password for login. Therefore, for security purposes, you are advised to set an authentication method other than non-authentication to ensure that only authenticated users can access the device or network.
  + If the authentication method is set to non-authentication using the [**authentication-mode**](cmdqueryname=authentication-mode) [**none**](cmdqueryname=none) command, administrators are not allowed to go online. If the authentication method of administrators is set to AAA authentication using the **authentication-mode** command in the user interface view, the device does not allow administrators to log in from the user interface view.
  + Third-party authentication may lack security mechanisms such as password complexity check and brute force attack defense. Check whether third-party authentication is used.

#### Order in Which Authentication Methods Take Effect

An authentication scheme enables you to designate one or more authentication methods to be used, thus ensuring a backup system for authentication in case the initial method does not respond.

An NAS uses the first method listed in the authentication scheme to authenticate users; if that method does not respond, the NAS selects the next method in the authentication scheme. This process continues until there is successful communication with a listed authentication method or the authentication method list is exhausted, in which case authentication fails.

![](public_sys-resources/note_3.0-en-us.png) 

The NAS attempts authentication with the next listed authentication method only when there is no response from the previous method. If authentication fails at any point in this cycle â meaning that the AAA server responds by denying the user access â the authentication process stops and no other authentication methods are attempted.