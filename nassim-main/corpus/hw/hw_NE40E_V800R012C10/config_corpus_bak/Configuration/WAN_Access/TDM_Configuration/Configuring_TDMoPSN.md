Configuring TDMoPSN
===================

Local CCC, SVC, and PWE3 pseudo wires (PWs) can be established
to transmit TDMoPSN services.

#### Applicable Environment

Services of the 2G
RAN network, mainly a small number of voice services, are transmitted
over TDM links. Generally, one to three E1 interfaces on a BTS are
connected to a BSC. Some mobile carriers do not own fixed network
infrastructure, and therefore have to lease E1 lines of the fixed
network at a high price.

With the introduction of TDMoPSN services,
the services between the CEs in the same city can be transparently
transmitted over TDM links in a Metro Ethernet (ME) network. Data
of the Fractional E1 interface can be transmitted from the BTS to
BSC in the mode of structuralized TDM circuit emulation.

A PW is established between Router through VLL or PWE3 to transparently transmit TDM frames.


#### Pre-configuration Tasks

Before configuring
a TDMoPSN service, complete the following tasks on the routers at
both ends of the PW:

* Configure static routes or an IGP protocol on PEs and Ps on
  the MPLS backbone network to ensure IP connectivity.
* Configure basic MPLS functions on PEs and Ps of the MPLS backbone
  network.
* Set up LDP sessions among PEs (if the PEs are indirectly connected,
  set up remote LDP sessions between them).
* Establish tunnels between PEs based on the tunnel policy (if
  no tunnel policy is configured, the default tunnel policy LDP is used).
* Configure synchronous serial interfaces and TDM link protocols.


[Configuring a Local TDMoPSN Service](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0006.html)

To configure the local TDMoPSN Service, you need to create a local CCC connection and only configure the incoming and outgoing interfaces of the CCC connection on a local PE. The local CCC connection is bidirectional and only one such connection needs to be created.

[Configuring a Remote TDMoPSN Service](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0007.html)

TDMoPSN supports SVC and PWE3 PWs.

[Configuring Local CEP Services](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0011.html)

To configure local CEP services, you only need to create a CCC connection on a PE and configure inbound and outbound interfaces for the CCC connection.

[Configuring a Remote CEP Service](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0012.html)

TDMoPSN supports the establishment of SVC and PWE3 PWs to transmit CEP services.

[(Optional) Enabling a Serial Interface to Use RML Bits in PW Control Words to Transparently Transmit Alarms](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0024.html)

When configuring the remote TDMoPSN service or remote CEP service, you can enable the serial interface to use RML bits in PW control words to transparently transmit alarms as required.

[Verifying the TDM Service Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_tdm_cfg_0008.html)

After a TDM service is configured, you cannot only view configurations and statuses of E1/CE1 interfaces, but also view information about the static PW and dynamic PW.