Configuring RSVP Authentication
===============================

RSVP authentication is configured to protect a node from attacks and improve network security.

#### Usage Scenario

RSVP authentication prevents the following problems:

* An unauthorized node attempts to establish an RSVP neighbor relationship with a local node.
* A remote node constructs forged RSVP messages to establish an RSVP neighbor relationship with a local node and then initiates attacks to the local node.

RSVP key authentication cannot prevent replay attacks or RSVP message mis-sequence during network congestion. RSVP message mis-sequence causes authentication termination between RSVP neighbors. The handshake function, message window functions, and RSVP key authentication are used to prevent the preceding problems.

CR-LSP flapping may lead to frequent re-establishment of RSVP neighbor relationships. As a result, the handshake function is repeatedly performed and RSVP authentication is prolonged. An RSVP authentication lifetime is set to resolve the preceding problems. If no CR-LSP exists, RSVP neighbors still retain their neighbor relationship until the RSVP authentication lifetime expires.


#### Pre-configuration Tasks

Before configuring RSVP authentication, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


[Configuring an RSVP Authentication Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0019.html)

RSVP authentication modes are configured between RSVP neighboring nodes or between the interfaces of RSVP neighboring nodes. The keys on both ends to be authenticated must be the same; otherwise, RSVP authentication fails, and RSVP neighboring nodes discard received packets.

[(Optional) Setting RSVP Authentication Lifetime](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0021.html)

The RSVP authentication lifetime is set to prevent RSVP authentication from being prolonged when CR-LSP flapping causes frequent reestablishment of RSVP neighbor relationships and repeatedly performed handshake.

[(Optional) Configuring the Handshake Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0022.html)

The handshake function helps RSVP key authentication prevent replay attacks.

[(Optional) Configuring the Message Window Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0023.html)

The message window function prevents RSVP message mis-sequence. RSVP message mis-sequence terminates RSVP authentication between neighboring nodes.

[Verifying the RSVP Authentication Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0024.html)

After configuring RSVP authentication, you can view information about RSVP authentication.