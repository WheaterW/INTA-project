Configuring Static PW FRR
=========================

Static pseudo wire (PW) fast reroute (FRR) enables service
traffic to be promptly switched to the secondary PW if the primary
PW fails. After the primary PW recovers, static PW FRR determines
whether to switch service traffic back to the primary PW based on
the configured revertive switching policy.

#### Usage Scenario

Pseudo wire emulation edge-to-edge
(PWE3) demands high network reliability. To prevent negative factors,
such as device power failures, from affecting services, configure
static PW FRR and dynamic BFD for PW.

On the network shown
in [Figure 1](#EN-US_TASK_0172369856__fig_dc_vrp_vpws_cfg_604801), a pair of primary
and secondary SVC PWs are established between PE1 and PE2. If BFD
detects a fault on the primary PW, traffic will be switched to the
secondary PW. After the primary PW recovers, traffic will be switched
back to the primary PW based on the configured revertive switching
policy.

**Figure 1** Static PW FRR networking
  
![](images/fig_dc_vrp_vpws_cfg_604801.png)  



#### Pre-configuration Tasks

Before configuring
static PW FRR, complete the following tasks:

* Configure interface IP addresses and an Interior Gateway Protocol
  (IGP) on PEs and SPEs.
* Configure basic MPLS functions on PEs and SPEs.
* Establish MPLS tunnels between PEs and SPEs.
* Configure CEs to access PEs.


[Configuring Primary and Secondary SVC PWs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6049.html)

To ensure that a primary PW fault does not interrupt services in a static PW FRR scenario, you need to configure a secondary PW for the primary PW, so that traffic can be switched to the secondary PW for transmission.

[Configuring Dynamic BFD for SVC PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6050.html)

Dynamic BFD for SVC PW accelerates PW fault detection, facilitating fast switching of SVC PWs.

[(Optional) Configuring a Revertive Switching Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6051.html)

In static PW FRR scenarios with both the primary and secondary PWs, if the primary PW fails, traffic will be switched to the secondary PW. If the primary PW recovers, traffic will be switched back to the primary PW after a period of time. To flexibly adjust the wait-to-restore (WTR) time, configure a revertive switching policy.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpws_cfg_6052.html)

After configuring static PW FRR, verify configured static PW information.