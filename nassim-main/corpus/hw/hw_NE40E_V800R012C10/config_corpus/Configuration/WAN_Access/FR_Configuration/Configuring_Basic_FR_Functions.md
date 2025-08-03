Configuring Basic FR Functions
==============================

FR uses VCs and works at the physical and data link layers of the OSI model. FR is characterized by high throughput and short delay and is applicable in case of burst service traffic.

#### Context

The Internet and IP technology has gained an overwhelming competitive edge in the application field with their simplicity and flexibility. FR supports multiplexing. Therefore, when IP packets enter an FR-capable network, FR devices can forward the packets to the destination. Currently, IPoFR has become a primary alternative in deploying an IP broadband network.

[Figure 1](#EN-US_TASK_0172364110__fig_dc_vrp_fr_cfg_000501) shows locations where FR can be deployed. FR deployment includes the following parts:

* FR access (on the user side)
* FR switching (on the network side)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, only FR access is supported.


**Figure 1** Networking for IPoFR  
![](images/fig_dc_vrp_fr_cfg_000501.png)

FR access enables IP packets from DTEs to enter an FR-capable network and to be forwarded by DCEs.


#### Pre-configuration Tasks

Before configuring basic FR functions, configure physical attributes for FR interfaces.

Currently, interfaces that support FR configuration mainly include:

* POS interfaces.


[Configuring Basic FR Functions on a DCE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fr_cfg_0006.html)

Before deploying FR access links, configure basic FR functions on the DCE.

[Configuring Basic FR Functions on a DTE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fr_cfg_0007.html)

Before deploying FR access links, configure basic FR functions on the DTE.

[Verifying the Basic FR Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fr_cfg_0008.html)

After configuring basic FR functions, verify the configuration.