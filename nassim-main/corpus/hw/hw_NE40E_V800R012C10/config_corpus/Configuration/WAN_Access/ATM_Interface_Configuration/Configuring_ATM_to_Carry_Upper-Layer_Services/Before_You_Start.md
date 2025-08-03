Before You Start
================

Before configuring ATM to carry upper-layer services, familiarize
yourself with the usage scenario, complete the pre-configuration tasks,
and obtain the data required for the configuration.

#### Usage Scenario

Before the Gigabit Ethernet technology was developed, ATM backbone
switches were deployed on backbone networks to provide sufficient
bandwidth. As ATM is well-developed, its complex architecture causes
difficulties in ATM system development, configuration, management,
and fault location. Therefore, ATM is often used at the data link
layer currently to carry upper-layer protocol packets. ATM boasts
of high-quality comprehensive service transmission, and therefore
is considered as the best transport technology for Broadband Integrated
Services Digital Networks (B-ISDNs).

IPoA means that IP packets
are encapsulated in ATM cells and transmitted on ATM networks. As
shown in [Figure 1](#EN-US_CONCEPT_0172364313__fig_dc_vrp_cfg_01405601), ATM allows
devices on the same network to communicate with each other at the
data link layer by transmitting ATM cells in which IP packets have
been encapsulated. As bearer networks for IP services, ATM networks
provide good network performance and mature QoS assurance.**Figure 1** IPoA application networking
  
![](images/fig_dc_vrp_cfg_01405601.png)


#### Pre-configuration Tasks

ATM interfaces on the device have been physically
connected.


#### Data Preparation

To configure ATM to carry upper-layer services, you need the following
data.

| No. | Data |
| --- | --- |
| 1 | Number of each ATM interface or sub-interface, IP address and mask of each ATM interface or sub-interface, PVC name, VPI/VCI values, and AAL5 encapsulation type |
| 2 | (Optional)Minimum and maximum priorities of IP packets transmitted along PVCs |