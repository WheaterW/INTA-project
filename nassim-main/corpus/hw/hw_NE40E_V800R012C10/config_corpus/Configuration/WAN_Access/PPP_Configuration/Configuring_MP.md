Configuring MP
==============

The Multilink Point-to-Point Protocol (MP) is a technique
that bundles multiple Point-to-Point Protocol (PPP) links together
to increase link bandwidth and improve link reliability.

#### Usage Scenario

A single PPP link provides
only limited bandwidth. To increase link bandwidth and reliability,
bundle multiple PPP links into an MP link.

In [Figure 1](#EN-US_TASK_0172364177__fig_dc_vrp_mp_cfg_000101), there
are three PPP links between Device A and Device B. You can add these three PPP links to an MP-Group to create an
MP link. Compared with a single PPP link, an MP link provides higher
bandwidth. In an MP-Group, although one PPP link fails, other links
keep properly transmitting services.

**Figure 1** Communication over an MP link
  
![](images/fig_dc_vrp_mp_cfg_000101.png)  



#### Pre-configuration Tasks

Before you configure
an MP link, establish PPP links.


[Configuring MP Implementations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0002.html)

An MP-Group interface is a logical interface used by MP applications. MP is implemented by adding multiple interfaces to an MP-Group interface.

[(Optional) Disabling Endpoint Discriminator Negotiation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0003.html)

The Link Control Protocol (LCP) status is Up only if the endpoint discriminators for the MP-Group interfaces on both ends are the same. If they are different, disable endpoint discriminator negotiation on both ends.

[(Optional) Configuring the MRRU](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0004.html)

The maximum receive reconstructed unit (MRRU) defines the maximum size (in bytes) of each packet a device can receive without fragmenting the packet. The MRRU is negotiated by two ends on a Multilink Point-to-Point Protocol (MP) link. A local end sends packets or fragments with the maximum size equal to the negotiated MRRU to its peer. Upon receipt, the peer can accept the packets or reassemble fragments into packets.

[(Optional) Configuring the Short Sequence Number for Negotiation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0009.html)

A sequence number in the packet header indicates the sequence of a fragmented packet. Using short sequence number for negotiation shortens the packet length and improves communication reliability. 

[(Optional) Configuring MP Fragmentation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0008.html)

Setting a proper size for Multilink PPP (MP) fragments improves bandwidth use efficiency.

[(Optional) Improving MP Link Reliability](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0005.html)

This section describes how to configure flapping damping and the minimum number of Point-to-Point-Protocol (PPP) links allowed for a Multilink Point-to-Point Protocol (MP) link to improve MP link reliability.

[Verifying the MP Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mp_cfg_0006.html)

After configuring the Multilink Point-to-Point Protocol (MP), verify the configuration.