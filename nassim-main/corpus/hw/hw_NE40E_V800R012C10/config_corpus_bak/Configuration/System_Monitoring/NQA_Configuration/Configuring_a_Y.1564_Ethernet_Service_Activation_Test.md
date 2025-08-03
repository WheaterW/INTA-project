Configuring a Y.1564 Ethernet Service Activation Test
=====================================================

This section describes how to configure an Ethernet service activation test. This test is conducted before network services are activated and delivered to users. It checks whether configurations are correct and network performance meets SLA requirements.

#### Context

An Ethernet service activation test is a method defined in Y.1564. This test helps carriers rapidly and accurately verify whether network performance meets SLA requirements before service rollout.


#### Pre-configuration Tasks

Before configuring an Ethernet service activation test, complete the following tasks:

* Layer 2 scenarios:
  + In a native Ethernet scenario, configure reachable Layer 2 links between the initiator and reflector.
  + In an L2VPN/EVPN L2VPN scenario, configure reachable links between CEs on both ends of an L2VPN/EVPN L2VPN connection.
  + In an EVPN VXLAN scenario, configure reachable links between devices on both ends of an EVPN VXLAN connection.
  + In an HVPN scenario, configure reachable links between CEs on both ends of an HVPN connection.
* Layer 3 scenarios:
  + In a native IP scenario, configure reachable IP links between the initiator and reflector.
  + In an L3VPN/EVPN L3VPN scenario, configure reachable links between CEs on both ends of an L3VPN/EVPN L3VPN connection.
  + In an EVPN VXLAN scenario, configure reachable links between devices on both ends of an EVPN VXLAN connection.
* In an L2VPN+L3VPN scenario, configure reachable links between the L2VPN and L3VPN.


[Configuring a Reflector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0053.html)

This section describes how to configure a reflector, which loops traffic back to an initiator. Parameters configured on the reflector vary according to scenarios.

[Configuring an Initiator](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0054.html)

This section describes how to configure an initiator that sends simulated service traffic. You can set initiator parameters based on usage scenarios and test indicator types.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0055.html)

After configuring the Ethernet service activation test, you can check the test results.