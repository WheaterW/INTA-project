ATM Interface Configuration
===========================

The Asynchronous Transfer Mode (ATM) is a technology applicable to backbone networks. Due to its high flexibility and support for multimedia services, ATM can be used to transmit voice, video, and data streams, and therefore is considered as a key technology for broadband communication.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This chapter is supported only by the NE40E-M2E/-M2F.



[Introduction](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_014053.html)

A conventional wide area network (WAN) uses X.25, frame relay (FR), or ATM. Any of these link-layer protocols can transmit data from one local area network (LAN) over a WAN to another LAN. As terminals become intelligent and the quality of physical links improves, the functions of error control and flow control for data at the data link layer on X.25 networks are no longer required. In addition, limited bandwidth resources on X.25 networks cannot meet requirements of users for services. ATM ensures high-quality service transmission, and therefore is widely applied to links that require high bandwidth.

[Configuration Precautions for ATM Interface](../../../../software/nev8r10_vrpv8r16/user/spec/ATM_Interface_limitation.html)



[Configuring ATM to Carry Upper-Layer Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_014055.html)

If upper-layer services need to be transmitted over an ATM network, configure ATM to carry upper-layer services.

[Configuring Parameters for an ATM OC-3/STM-1 Interface or an ATM OC-12/STM-4 Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0004.html)

This section describes how to configure parameters for an ATM OC-3/STM-1 or an ATM OC-12/STM-4 interface. Detailed operations include configuring the frame format and the scramble function for an ATM OC-3/STM-1 or an ATM OC-12/STM-4 interface.

[Configuring the Service Type and Optional Parameters for a PVC](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0012.html)

If PVC/PVP traffic planning is required, you can configure the service type and overload bandwidth for PVCs/PVPs.

[Configuring ATM OAM](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0018.html)

To detect and locate faults on ATM links, you can configure ATM OAM.

[Maintaining ATM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_014060.html)

You can clear ATM interface statistics and use the loopback function to detect whether ATM interfaces run properly.

[Configuration Examples for ATM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_014063.html)

This section provides ATM configuration examples with the networking requirements, configuration roadmap, data preparation, and configuration procedure.