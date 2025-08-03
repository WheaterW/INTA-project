Configuring MLD SSM Mapping
===========================

On an IPv6 multicast network that provides the SSM model, interfaces of multicast devices run MLDv2, but some hosts can run only MLDv1. To allow an MLDv1 host to use the Source-Specific Multicast (SSM) service, configure SSM mapping on a multicast Router.

#### Usage Scenario

If a multicast Router runs MLDv2 but its connected user hosts have to run MLDv1, configure SSM mapping on the Router, so the multicast Router also provides the SSM service for the hosts that run MLDv1.


#### Pre-configuration Tasks

Before configuring MLD SSM mapping, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic MLD functions](dc_vrp_multicast_cfg_2073.html).


[Enabling SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2080.html)

Enable the Source-Specific Multicast (SSM) mapping function on an interface before you configure MLD SSM mapping. If SSM mapping is not enabled, SSM source/group address mapping entries cannot take effect on the interface.

[Configuring Static SSM Mapping](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2081.html)

To allow MLDv1 hosts to use the Source-Specific Multicast (SSM) service, configure static SSM mapping by establishing mappings between multicast groups and sources.

[Verifying the MLD SSM Mapping Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2082.html)

After configuring MLD Source-Specific Multicast (SSM) mapping, verify the configurations, including multicast groups configured with SSM mapping, SSM mapping rules of a specific multicast group, and SSM mapping status.