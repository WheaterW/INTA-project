Configuring Multicast Shaping
=============================

Multicast shaping limits the jitter of a multicast source within an acceptable range when there is a large volume of multicast traffic and the multicast source is busy.

#### Usage Scenario

After the IPTV multicast service is deployed, the multicast source may jitter when the multicast traffic is huge. You can configure multicast shaping on the Router to limit the jitter of the multicast source within an acceptable range.


#### Pre-configuration Tasks

Before configuring multicast shaping, complete the following task:

* Configure the multicast service.


[Configuring a Multicast Program List](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013859.html)

A multicast program list contains one or more multicast addresses for identifying one or more IPTV channels or programs.

[Enabling Multicast Shaping](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013860.html)

When a multicast source is busy, excessive jitter may occur. In this case, you can configure multicast shaping to limit the jitter of the multicast source to an acceptable range.

[Configuring Bandwidth for a Multicast Program List](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013861.html)

You can perform multicast shaping on specific multicast programs by setting the CIR and PIR.

[Configuring an Upper Rate Limit for Multicast Traffic on a Board](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_002046.html)

To prevent multicast traffic bursts from resulting in multicast packet loss, set an upper rate limit for multicast traffic on a specified board.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013865.html)

After multicast shaping is configured, you can view information about the online users with specified IDs and the bandwidth consumed by them and applications of the QoS profile.