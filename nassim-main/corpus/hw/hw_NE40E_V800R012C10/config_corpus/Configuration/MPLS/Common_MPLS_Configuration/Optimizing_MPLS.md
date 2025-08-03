Optimizing MPLS
===============

Optimizing MPLS includes the label value related to the penultimate hop popping (PHP) function and the MPLS maximum transmission unit (MTU) configured on interfaces.

#### Usage Scenario

The following MPLS parameters can be adjusted:

* Labels related to penultimate hop popping (PHP)
  
  The PHP function is configured on the egress. The egress assigns labels to the penultimate node based on the PHP status.
* MPLS maximum transmission unit (MTU) on MPLS interfaces
  
  The MPLS MTU defines the maximum number of bytes in an MPLS packet that an interface can forward without fragmenting the packet. The default MPLS MTU on an interface is equal to the interface MTU.

#### Pre-configuration Task

Before adjusting MPLS parameters, configure MPLS.


[Configuring PHP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0008.html)

When you configure penultimate hop popping (PHP), specify a label that the egress assigns to the penultimate hop.

[Configuring an MPLS MTU on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0009.html)

An MPLS MTU can be configured on an interface to determine the maximum number of bytes in an MPLS packet that an interface can forward without fragmenting the packet.

[Verifying the Configuration of Optimizing MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0010.html)

After you adjust MPLS parameters, verify MPLS-enabled interface information.