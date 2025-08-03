Configuring Unidirectional CHAP Authentication
==============================================

CHAP performs three-way handshake authentication. Unidirectional
CHAP authentication involves two situations: the authenticator with
a user name and the authenticator without a user name.

#### Usage Scenario

CHAP authentication is performed
before a link is set up. After a link is set up, CHAP authentication
can be repeatedly performed anytime using CHAP negotiation packets.

In unidirectional CHAP authentication, one of two communicating
parties functions as the authenticator, whereas the other functions
as the supplicant. The authenticator sends a Challenge packet to the
supplicant. After performing one hash calculation, the supplicant
returns a calculated value to the authenticator. The authenticator
compares the value calculated by itself using the hash algorithm with
the value sent by the supplicant. If the two values match, authentication
is successful. If the two values are different, the authentication
fails, and the link is torn down.


#### Pre-configuration Tasks

Before configuring
unidirectional CHAP authentication, complete the following tasks:

* Connect interfaces and configure physical parameters of the
  interfaces to ensure that the physical status of the interfaces is
  Up.
* Configure PPP as the link layer protocol of the interfaces.
* Add the user name and password of the supplicant to the user
  list of the authenticator in the AAA view.

#### Configuration Procedures

In CHAP authentication,
the authenticator can be configured with or without a user name. In
practice, you can configure any type of unidirectional CHAP authentication
as required.


[Configuring the Authenticator with a User Name to Authenticate Its Peer in CHAP Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0016.html)



[Configuring the Authenticator Without a Username to Authenticate Its Peer in CHAP Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0017.html)

This section describes how to configure the authenticator without a username to authenticate its peer in CHAP mode.

[Verifying the Unidirectional CHAP Authentication Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ppp_cfg_0018.html)

After configuring unidirectional CHAP authentication, verify the configuration.