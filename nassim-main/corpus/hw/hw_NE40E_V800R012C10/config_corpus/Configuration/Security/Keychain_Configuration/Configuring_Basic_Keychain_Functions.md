Configuring Basic Keychain Functions
====================================

This section describes how to configure basic Keychain functions.

#### Usage Scenario

Keychain is used to provide authentication support to the applications. A keychain can have one or more key-ids. Key-id comprises of authentication algorithm and the key-string (secret shared key). Each key-id is associated with send and accept lifetime. Based on the send and accept lifetime, a key-id will be send-active or receive-active or both. When the key-id is send-active or receive-active, it will be used for authenticated communication. When the key-id is send-active, then it will be used to send out authenticated packet. On the receiver side that key-id should be receive-active to process the authenticated packet. The administrator has to configure the key-ids under the keychain in such a way that both sides can communicate without any packet loss.


#### Pre-configuration Tasks

Before configuring the keychain on the peer routers, configure the Network Time Protocol (NTP) so that the time is consistent on the two routers.


[Creating a Keychain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0006.html)



[(Optional) Configuring the Receive Tolerance Time for a Keychain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0007.html)



[Creating a Key-id in a Keychain](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0008.html)



[Configuring a Key String for a Key ID](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0009.html)



[Configuring an Authentication Algorithm for a Key ID](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0010.html)



[(Optional) Configuring a Key ID as the Default Send Key ID](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0011.html)



[Configuring Send-time of a Key-id](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0012.html)



[Configuring Receive-time of a Key-id](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0013.html)



[Verifying the Keychain Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_keychain_cfg_0014.html)