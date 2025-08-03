Configuring TCP Authentication Parameters
=========================================

Describes how to configure of TCP Authentication Parameters.

#### Usage Scenario

Keychain is used to provide
authentication support to all the applications. Authenticated TCP
communication is required between two peers. TCP based applications
can communicate with other vendor nodes by using the authenticated
TCP connection. For authenticated communication, TCP uses TCP Enhanced
Authentication Option. Currently different vendors use different kind
value to represent the TCP Enhanced Authentication Option type. Hence,
kind value should be made configurable based on the type of vendor
to which it is connected. Similarly TCP Enhanced Authentication Option
has a field named algorithm-id which represents the authentication
algorithm type. As algorithm-ids are not defined by IANA, currently
different vendor uses different algorithm-id to represent the same
algorithm. In order to communicate with the other vendors, user has
to configure the TCP algorithm-id in the keychain.


#### Pre-configuration Tasks

Before configuring
the keychain feature on the peer routers supporting TCP, configure
the Network Time Protocol (NTP) so that the time is consistent on
the two routers.


[Configuring TCP Kind of a Keychain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0016.html)



[Configuring a TCP Authentication Algorithm ID for a Keychain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0017.html)



[Checking the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0018.html)