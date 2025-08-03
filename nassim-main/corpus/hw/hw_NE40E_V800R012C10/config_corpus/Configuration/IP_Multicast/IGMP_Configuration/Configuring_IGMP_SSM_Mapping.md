Configuring IGMP SSM Mapping
============================

To allow an IGMPv1 or IGMPv2 host to use the Source-Specific Multicast (SSM) service, configure SSM mapping on a multicast device.

#### Usage Scenario

If a multicast Router runs IGMPv3 but its connected user hosts have to run IGMPv1 or IGMPv2, configure SSM mapping on the multicast Router, so the multicast Router also provides the SSM service for the hosts that run IGMPv1 or IGMPv2.

The SSM mapping function effectively protects multicast sources from being attacked.


#### Pre-configuration Tasks

Before configuring IGMP SSM mapping, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing.
* [Configure basic IGMP functions](dc_vrp_multicast_cfg_2044.html).


[Enabling SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2051.html)

On the network segment that provides SSM services, interfaces on multicast devices run IGMPv3. Due to various restrictions, some hosts must run IGMPv1 or IGMPv2. To provide SSM services for these hosts, IGMP SSM mapping needs to be configured on the multicast devices' interfaces connected to the user network segment. Enabling SSM mapping is a prerequisite for configuring static SSM mapping. If SSM mapping is not enabled on an interface, SSM source/group address mapping entries cannot take effect on the interface.

[Configuring Static SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2052.html)

To allow IGMPv1 or IGMPv2 hosts to use the Source-Specific Multicast (SSM) service, configure static SSM mapping by establishing mappings between multicast groups and sources.

[Configuring DNS-based SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2290.html)

This section describes how to configure DNS-based SSM mapping on the multicast device connecting to the user network segment, so that the multicast device can obtain the multicast source corresponding to the multicast group through the DNS server and provide the SSM service for users.

[Verifying the IGMP SSM Mapping Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2053.html)

After configuring IGMP SSM mapping, verify the configuration, including multicast groups configured with SSM mapping, SSM mapping rules of a specific multicast group, and SSM mapping status.