Configuring 1588 ATR Time Synchronization
=========================================

In a 1588 ATR domain, a clock client establishes a client/server relationship only with a remote clock server. The client initiates unicast negotiation requests to the server and uses PTP packets to implement clock recovery.

#### Pre-configuration Tasks

Before configuring 1588 ATR time synchronization, complete the following tasks:

* Configure static routes or an IGP to ensure IP route reachability among nodes.
* Configure the clock server to properly process clock signals from the BITS source.
* Activate the license file for clock synchronization on the main control board using the [**license active**](cmdqueryname=license+active) *file-name* command. When the clock synchronization license is not loaded, the [**ptp-adaptive enable**](cmdqueryname=ptp-adaptive+enable) configuration is not allowed.


[Configuring Unicast Negotiation on a 1588 ATR Client](../../../../software/nev8r10_vrpv8r16/user/ne/dc_atn_cfg_010367_1.html)

The unicast negotiation function and parameters for a connection between a client and a clock server are configured on the HUAWEI NE40E-M2 series functioning as a 1588 ATR client.

[Configuring Unicast Negotiation on a 1588 ATR Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atr_cfg_9007.html)

A Router that functions as a 1588 ATR server needs to be enabled with unicast negotiation so that it can use Layer 3 unicast packets to establish clock links with a 1588 ATR client and use PTP packets to implement time synchronization over a third-party network.

[(Optional) Adjusting Unicast Negotiation Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atr_cfg_9008.html)

Time synchronization is the basis for normal network operations. 1588 ATR packets should have a higher priority than other service packets so that they can reach the destination in case of network congestion.

[(Optional) Configuring Lightweight Time Synchronization](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atr_cfg_9025.html)

Lightweight time synchronization implements automatic identification and switching within a device, loosening the requirements on time synchronization precision and simplifying the configuration process.

[Configuring Time Synchronization in Server-and-Client Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atr_cfg_9022.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atr_cfg_9009.html)

After configuring 1588 ATR on the Router that functions as a server or client in hop-by-hop mode, verify the configuration.