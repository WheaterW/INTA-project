Configuring 802.1X Port-based Authentication on the NE40E Functioning as a Supplicant
=====================================================================================

Before configuring 802.1X port-based authentication on a supplicant, familiarize yourself with the usage scenario, pre-configuration tasks, and configuration flowchart, which helps you quickly and accurately complete the configuration.

#### Usage Scenario

On a shared LAN, to prevent the connected NE40E from being replaced and ensure network security, 802.1X port-based authentication can be configured on a supplicant for control.


#### Pre-configuration Tasks

To configure 802.1X port-based authentication on a supplicant, complete the following configuration tasks:

* Configure the name of the 802.1X supplicant template, authentication username, authentication user password, and authentication mode.
* Enable 802.1X port-based authentication.


[Configuring an 802.1X Supplicant Template](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0013.html)

When 802.1X supplicant authentication is used, the NE40E and the authenticator perform authentication negotiation based on parameters defined in an 802.1X supplicant template.

[Configuring the 802.1X Supplicant Function on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0014.html)

After the 802.1X supplicant function is enabled on an interface, the interface initiates 802.1X authentication. After the authenticator passes the authentication, the 802.1X supplicant can access the network.

[Verifying the 802.1X Port-based Authentication Configuration on the Supplicant](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0015.html)

After 802.1X supplicant authentication is configured, you can check configuration information about the 802.1X supplicant and the corresponding template.