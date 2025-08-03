Configuring Packet Loss Ratio Testing for a Physical Link
=========================================================

You can configure remote loopback to check link connectivity, test the packet loss ratio of a physical link, and take effective measures to ensure link performance.

#### Usage Scenario

EFM OAM is introduced to implement Ethernet OAM in the last mile. Ethernet OAM provides the following functions:

* Link detection and analysis
* Fault detection
* Loop test

EFM OAM provides link-level loopback. During loopback, interfaces at both ends of a link can analyze loopback statistics to check whether the link is working properly. Periodically detecting loops helps to determine whether a link is working properly. On-demand loop detection helps to locate the specific scope where a fault occurs. In loopback mode, the local interface sends testing packets to the remote interface. Based on the numbers of sent packets and received packets, the local device computes communication quality parameters (such as the packet loss ratio of the current link) to determine link quality.

Remote loopback is initiated by the interface in active mode. In loopback mode, to check the connectivity, performance, or packet loss ratio of a link, you can perform this configuration task.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Configuring remote loopback affects service forwarding. Therefore, remote loopback must be configured on the link over which no service data is forwarded.

As shown in [Figure 1](#EN-US_TASK_0172362013__fig_dc_vrp_efm_cfg_201701), EFM OAM is configured on Device A and Device B, and remote loopback is configured on GE 0/1/1 of Device A. To test the packet loss ratio, send testing packets from Device A to Device B and observe the return results of the testing packets on Device A.

**Figure 1** Testing the packet loss ratio![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, interface2 in this example are GE0/1/1, GE0/2/1 respectively.


  
![](images/fig_dc_vrp_efm_cfg_201701.png)  


#### Pre-configuration Tasks

Before testing the packet loss ratio of a link, [configure basic EFM OAM functions](dc_vrp_efm_cfg_2003.html).


[Configuring Remote Loopback](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2018.html)

You can configure remote loopback to locate remote faults and test link quality. Perform the following steps on the device on which an interface in active mode resides:

[Configuring an Interface to Send Testing Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2019.html)

Testing packets are Ethernet packets that are used together with remote loopback to test the packet loss ratio of a link. Perform the following steps on the device on which an interface in active mode resides:

[(Optional) Disabling Remote Loopback](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2021.html)

Remote loopback can be disabled either automatically or manually. Perform the following steps on the device on which an interface in active mode resides:

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_efm_cfg_2022.html)

After configuring packet loss ratio testing for a physical link, verify the configurations.