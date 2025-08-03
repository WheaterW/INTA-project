Configuring STP/RSTP Interoperability Between Huawei Devices and Non-Huawei Devices
===================================================================================

To support STP/Rapid Spanning Tree Protocol (RSTP) interoperability between Huawei devices and non-Huawei devices, proper parameters are required on Huawei devices running STP/RSTP to ensure nonstop communication.

#### Applicable Environment

On a network running STP/RSTP, inconsistent protocol packet formats and Bridge Protocol Data Unit (BPDU) keys may lead to a communication failure. Configuring proper STP/RSTP parameters on Huawei devices ensures interoperability between Huawei devices and non-Huawei devices.


#### Pre-configuration Tasks

Before configuring STP/RSTP interoperability between Huawei devices and non-Huawei devices, complete the following task:

* Configuring basic STP/RSTP functions


[Configuring the Proposal/Agreement Mechanism](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0027_1.html)

To enable Huawei Datacom devices to communicate with non-Huawei devices, a proper rapid transition mechanism needs to be configured on Huawei devices based on the Proposal/Agreement mechanism on non-Huawei devices.

[(Optional) Configuring an Interface to Transparently Transmit HVRP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mstp_cfg_0001.html)



[Verifying the STP/RSTP Interoperability Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0028.html)

After STP/RSTP parameters are configured for the interoperability between Huawei devices and non-Huawei devices, verify the configuration.