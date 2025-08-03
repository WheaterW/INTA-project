Configuring TCP/IP Attack Defense
=================================

Defense against TCP/IP attacks protects the CPU of the Router against malformed packets, fragmented packets, TCP SYN packets,
and UDP packets, ensuring that normal services can be processed.

#### Usage Scenario

Defense against TCP/IP attacks
is applied to the Router on the edge of the network or other Routers that are easily to be attacked by illegal TCP/IP packets. Defense
against TCP/IP attacks can protect the CPU of the Router against malformed packets, fragmented packets, TCP SYN packets,
and UDP packets, ensuring that normal services can be processed.

In VS mode, this feature is supported only by the
admin VS.


#### Pre-configuration Tasks

Before configuring
TCP/IP attack defense, configure the parameters of the link layer
protocol and IP addresses for interfaces and ensure that the link
layer protocol on the interfaces is Up.


[Creating an Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0005a.html)

All local attack defense features must be added to an attack defense policy. These features take effect after the attack defense policy is applied to the interface board.

[Enabling Defense Against Malformed Packet Attacks](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0014.html)

With defense against malformed packet attacks, the Router checks the validity of received packets and filters out illegal packets, thus defending the CPU against attacks of IP packets with null load, null IGMP packets, LAND attack packets, Smurf attack packets, and packets with invalid TCP flag bits.

[Enabling Defense Against Fragmented Packet Attacks](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0015.html)

Defense against fragmented packet attacks protects the CPU by restricting the sending rate of fragmented packets and ensuring the correctness of packet reassembly.

[Enabling Defense Against TCP SYN Flooding Attacks](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0012.html)

The TCP SYN flooding attack is a denial-of-service attack. Defense against TCP SYN flooding attacks protects the CPU by restricting the rate at which packets are sent to the CPU.

[Enabling Defense Against UDP Packet Attacks](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0013.html)

With defense against UDP packet attacks, the Router can identify packets in Fraggle attacks and attack packets on UDP diagnosis ports according to the destination port of the received UDP packets.

[Applying the Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0009a.html)

The configured attack defense policy takes effect only after being applied to the interface board.

[Verifying the TCP/IP Attack Defense Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0016.html)

After defense against TCP/IP attacks is configured, you can view the statistics about it, including the total number of illegal TCP/IP packets, the number of legal TCP/IP packets, and the number of discarded packets.