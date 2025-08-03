Configuring a Rate Limit for ARP Packets to Be Sent to the CPU
==============================================================

Before configuring a rate limit for Address Resolution Protocol (ARP) packets to be sent to the CPU, familiarize yourself with the applicable environment, complete the pre-configuration tasks for the configuration.

#### Applicable Environment

You can configure a rate limit for ARP packets to be sent to the CPU in the following situations:

* The Router has many sub-interfaces configured, and therefore may encounter ARP request packet bursts.
* The Router has received a large number of ARP request packets, and valid ARP packets are affected.

#### Pre-configuration Tasks

Before configuring a rate limit for ARP packets to be sent to the CPU, complete the following task:

* Configuring link layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol on each interface is Up


[Enabling ARP Bidirectional Isolation](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_arpsec_cfg_5006_copy.html)

Address Resolution Protocol (ARP) bidirectional isolation enables the Router to process ARP request and reply packets separately, improving the fault locating efficiency when a large number of ARP packets are received in a short period.

[Configuring ARP VLAN CAR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_arpsec_cfg_5007.html)

ARP VLAN CAR allows you to limit the rate of ARP packets on the attacked interface without affecting other interfaces. This minimizes the impact of attacks on devices and services. After the alarm function is enabled for ARP VLAN CAR and the number of ARP packets to be sent to the CPU exceeds the threshold configured for ARP VLAN CAR, an alarm is reported.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_arpsec_cfg_5008.html)

After configuring the rate limit for Address Resolution Protocol (ARP) packets to be sent to the CPU, you can verify the configuration.