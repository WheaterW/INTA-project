Configuring an Authentication Mode for IPoE Access
==================================================

Authentication technologies allow a user terminal to be authenticated by submitting the username and password to the NE40E. The NE40E supports multiple authentication technologies.

#### Applicable Environment

Web authentication requires a user who wants to access the network to enter the username and password on the authentication page of a web authentication server for authentication.

Fast authentication is a simplified form of web authentication in which a user accesses the authentication page of a web authentication server for authentication, without entering the username and password. The NE40E then automatically generates the username and password for authentication based on information about the BAS interface that the user accesses.

Binding authentication allows the NE40E to automatically generate the username and password based on the physical location of a user.


[Configuring Web Authentication or Fast Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0037.html)

Web authentication requires a user who wants to access the network to enter the username and password on the authentication page of a web authentication server for authentication. Fast authentication is an authentication mode in which a user accesses the authentication page of a web authentication server for authentication, without entering the username and password.

[Configuring HTTPS Redirect for Web Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_https_redirect.html)

This section describes how to configure a BRAS to redirect HTTPS access requests.

[Configuring Binding Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0005.html)

In addition to web authentication, users can also be authenticated using binding authentication.

[Verifying the Authentication Mode Configuration for IPoE Access](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipox_cfg_0006.html)

After an authentication mode is configured, you can view the authentication mode by checking the domain configuration.