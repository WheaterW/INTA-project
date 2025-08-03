Configuring Unidirectional PAP Authentication
=============================================

The unidirectional PAP authentication configuration procedure involves configuring the authenticator to authenticate the supplicant in PAP mode and configuring the supplicant to be authenticated in PAP mode.

#### Usage Scenario

In PAP authentication, passwords are sent over a link in simple text. The user name and password of a supplicant can be added to the user list of the authenticator in authentication, authorization and accounting (AAA) mode or sent to a Remote Authentication Dial-In User Service (RADIUS) server for authentication.

In unidirectional PAP authentication, one of two communicating parties functions as the authenticator, whereas the other functions as the supplicant. In bidirectional PAP authentication, two communicating parties function as both the authenticator and supplicant of each other.

This section describes how to configure unidirectional PAP authentication by adding the user name and password of the supplicant to the user list of the authenticator in AAA mode.


#### Pre-configuration Tasks

Before configuring unidirectional PAP authentication, complete the following tasks:

* Connect interfaces correctly and configure physical parameters for the interfaces to ensure that the physical layer status of the interfaces is Up.
* Configure PPP as the link layer protocol of the interfaces.
* Add the user name and password of the supplicant to the user list of the authenticator in the AAA view.


[Configuring the Authenticator to Authenticate Its Peer in PAP Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0012.html)

This section describes how to configure PAP authentication on the authenticator. PAP performs two-way handshake authentication only in the initial link establishment phase.

[Configuring the Supplicant to Be Authenticated in PAP Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0013.html)

This section describes how to configure the supplicant to be authenticated in PAP mode.

[Verifying the Unidirectional PAP Authentication Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0014.html)

After configuring unidirectional PAP authentication, you can view the link status and LCP running status of the current interface.