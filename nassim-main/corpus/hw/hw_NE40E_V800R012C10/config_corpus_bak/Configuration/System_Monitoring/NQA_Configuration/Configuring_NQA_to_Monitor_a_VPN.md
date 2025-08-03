Configuring NQA to Monitor a VPN
================================

Before configuring NQA to monitor a virtual private network (VPN), familiarize yourself with the usage scenario of each test instance and complete the pre-configuration tasks.

#### Usage Scenario

**Table 1** NQA tests used to monitor VPNs
| Test Type | Usage Scenario |
| --- | --- |
| PWE3 ping test | A PWE3 ping test helps check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a virtual private wire service (VPWS) network. |
| VPLS PW ping test | A virtual private local area network service (VPLS) pseudo wire (PW) ping test can be used to check the PW connectivity and measure the packet loss rate, delay, and other indicators of a VPLS network. |
| VPLS MAC ping test | A VPLS MAC ping test can be used to check the connectivity of Layer 2 forwarding links on a VPLS network. |
| PWE3 trace test | A Pseudowire Emulation Edge-to-Edge (PWE3) trace test can be used to check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a virtual private wire service (VPWS) network. It can also be used to check the forwarding path of test packets. |
| VPLS PW trace test | A VPLS PW trace test can be used to check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a VPLS network. It can also be used to check the forwarding path of test packets. |



#### Pre-configuration Tasks

Before you configure NQA to check VPNs, configure basic VPN functions.


[Configuring a PWE3 Ping Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0040.html)

A PWE3 ping test helps check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a virtual private wire service (VPWS) network.

[Configuring a PWE3 Trace Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0044.html)

A Pseudowire Emulation Edge-to-Edge (PWE3) trace test can be used to check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a virtual private wire service (VPWS) network. It can also be used to check the forwarding path of test packets.

[Configuring a VPLS PW Ping Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0043.html)

A virtual private local area network service (VPLS) pseudo wire (PW) ping test can be used to check the PW connectivity and measure the packet loss rate, delay, and other indicators of a VPLS network.

[Configuring a VPLS PW Trace Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0045.html)

A VPLS PW trace test can be used to check the pseudo wire (PW) connectivity and measure the packet loss rate, delay, and other indicators of a VPLS network. It can also be used to check the forwarding path of test packets.

[Configuring a VPLS MAC Ping Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0056.html)

A VPLS MAC ping test can be used to check the connectivity of Layer 2 forwarding links on a VPLS network.

[Verifying the NQA Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0041.html)

After the test is complete, verify the test results.