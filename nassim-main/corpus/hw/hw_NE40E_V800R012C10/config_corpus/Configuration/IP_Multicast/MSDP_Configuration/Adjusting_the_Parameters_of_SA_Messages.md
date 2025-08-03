Adjusting the Parameters of SA Messages
=======================================

MSDP peers share (S, G) information by exchanging SA messages. You can configure the capacity of the SA cache, enable the sending of SA Request messages, enable the encapsulation of multicast data into SA messages, and create filtering policies for SA messages and SA Request messages.

#### Usage Scenario

SA messages carry the following information and are transmitted among multiple RPs.

* IP address of the source's RP
* Number of (S, G) entries contained in the message
* Active (S, G) lists in the domain

Enabling the sending of SA Request message on the local RP and enabling the SA cache function on the remote MSDP peer can shorten the time taken by a receiver to obtain multicast source information.

* The local RP sends an SA Request message, carrying the required group address, for obtaining the (S, G) list of this group.
* Upon receipt of the SA Request message, the remote MSDP peer responds with an SA Response message carrying the required (S, G) information.

#### Pre-configuration Tasks

Before adjusting the parameters of SA messages, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure PIM-SM inter-domain multicast](dc_vrp_multicast_cfg_0045.html) or [configure Anycast-RP](dc_vrp_multicast_cfg_0050.html).


[Configuring an SA Cache](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0062.html)

An SA cache is used to locally save (S, G) information carried in the Source Active (SA) messages. If a Router needs to receive multicast data, it directly obtains useful (S, G) information from the SA cache. Setting the maximum number of (S, G) entries in an SA cache can prevent Deny of Service (DoS) attacks. You are allowed to disable the SA cache function on the NE40E.

[Configuring Filtering Policies for SA Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0065.html)

By default, an MSDP peer permits all Source Active (SA) messages that pass the Reverse Path Forwarding (RPF) check, and forwards the SA messages to other MSDP peers. To control the transmission of SA messages among MSDP peers, configure filtering policies to filter SA messages to be created, received, or forwarded.

[Controlling the Sending of SA Request Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0063.html)

If the Source Active (SA) cache capacity is large on a remote MSDP peer, to shorten the time taken by a receiver to obtain multicast source information, you can enable the local Rendezvous Point (RP) to send SA Request messages, and configure a policy on the peer to filter SA Request messages to be received from the local RP.

[Encapsulating a Multicast Data Packet into an SA Message](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2165.html)

By default, a source active (SA) message contains only (S, G) information. To ensure successful multicast data packet transmission, enable the source Rendezvous Point (RP) configured with MSDP peer relationships to encapsulate multicast data packets into SA messages.

[(Optional) Setting the TTL Threshold for Forwarding an SA Message Containing a Multicast Data Packet](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2205.html)

After receiving a source active (SA) message encapsulated with a multicast data packet, an MSDP peer forwards the SA message to a specified remote MSDP peer only when the TTL value of the multicast packet is greater than the configured TTL threshold.

[(Optional) Setting a Hold Timer for Entries in the SA Cache](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_20026.html)

The NE40E supports hold timer adjustment for the (S, G) entries in the SA cache.

[Verifying the Configuration of SA Message Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0066.html)

After configuring source active (SA) message parameters, verify information about and the number of (S, G) entries in the SA cache and check details about MSDP peers.