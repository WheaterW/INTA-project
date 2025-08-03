Configuring VPLS Interworking
=============================

VPLS interworking allows different types of VPLS networks
to communicate.

#### Usage Scenario

LDP VPLS uses LDP signaling
packets that carry the FEC 128 TLV to establish and maintain PWs after
VPLS members are manually specified. BGP VPLS uses BGP to automatically
discover VPLS members and BGP signaling packets to establish and maintain
PWs. BGP AD VPLS uses BGP to automatically discover VPLS members and
uses LDP signaling packets that carry the FEC 129 TLV to establish
and maintain PWs. LDP VPLS applies to VPLS networks with few sites,
whereas BGP VPLS and BGP AD VPLS apply to VPLS networks with large
numbers of sites. For carriers with both LDP VPLS and BGP VPLS or
both LDP VPLS and BGP AD VPLS networks, interworking between LDP VPLS
and BGP VPLS or between LDP VPLS and BGP AD VPLS enables them to improve
VPLS network expansibility and reduce network operation costs.


#### Pre-configuration tasks

Before configuring
VPLS interworking, complete the following tasks:

* Configure interface IP addresses and routes on PEs and SPEs
  to ensure IP connectivity.
* Configure LSR IDs and basic MPLS functions on PEs and SPEs.
* Establish tunnels between PEs and between PEs and SPEs to transmit
  service traffic.


[Configuring Interworking Between LDP VPLS and BGP AD VPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6012.html)

To enable an LDP VPLS network to communicate with a BGP AD VPLS network, configure interworking between LDP VPLS and BGP AD VPLS.

[Configuring Interworking Between LDP VPLS and BGP VPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6013.html)

To enable an LDP VPLS network to communicate with a BGP VPLS network, configure interworking between LDP VPLS and BGP VPLS.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6014.html)

After configuring VPLS interworking, check VPLS information.