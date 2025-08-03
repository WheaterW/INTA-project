Configuring NQA to Monitor an MPLS Network
==========================================

NQA can be configured to monitor an MPLS network. Before doing so, familiarize yourself with the usage scenario of each test instance and complete the pre-configuration tasks.

#### Usage Scenario

**Table 1** NQA test instances used to monitor an MPLS network
| Test Type | Usage Scenario |
| --- | --- |
| LSP ping test | A label switched path (LSP) ping test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network from end to end. |
| LSP trace test | An LSP trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network hop by hop. It can also monitor the forwarding path of MPLS packets. |
| LSP jitter test | An LSP jitter test can be used to measure the end-to-end jitter of services carried on an MPLS network. |



#### Pre-configuration Tasks

Before configuring NQA to monitor an MPLS network, configure basic MPLS functions.


[Configuring an LSP Ping Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0013.html)

A label switched path (LSP) ping test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network from end to end.

[Configuring an LSP Trace Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0014.html)

An LSP trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an MPLS network hop by hop. It can also monitor the forwarding path of MPLS packets.

[Configuring an LSP Jitter Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0015.html)

An LSP jitter test can be used to measure the end-to-end jitter of services carried on an MPLS network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0033.html)

After completing the test, you can check the test results.