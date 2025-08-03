Configuring NQA to Monitor an IP Network
========================================

NQA test instances can be used to monitor IP networks. Before configuring NQA, familiarize yourself with the usage scenario of each test instance and complete the pre-configuration tasks.

#### Usage Scenario

**Table 1** NQA test instances used to monitor IP networks
| Test Type | Usage Scenario |
| --- | --- |
| DNS test | This section describes how to configure a DNS test to detect the speed at which a DNS name is resolved to an IP address. |
| ICMP test | An Internet Control Message Protocol (ICMP) test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network from end to end. |
| TCP test | A TCP test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network through a TCP connection. |
| UDP test | A UDP test can be used to measure the round-trip delay (RTD) of UDP packets exchanged between Huawei devices. |
| SNMP test | An NQA SNMP test can be used to measure the communication speed between a host and an SNMP agent using UDP packets. |
| Trace test | A trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network hop by hop. It can also monitor the packet forwarding path. |
| UDP jitter test | A UDP jitter test can be used to measure the end-to-end jitter of various services. It can also simulate a voice test. A UDP jitter test can be used when an ICMP jitter test cannot be used due to the ICMP reply function being disabled on network devices for security purposes. |
| ICMP Jitter test | An Internet Control Message Protocol (ICMP) Jitter test can be used to measure the end-to-end jitter of various services. |
| Path Jitter test | An NQA path jitter test instance, however, can identify the Router whose jitter value is great. |
| Path MTU test | A path MTU test can obtain the maximum MTU value that does not require packet fragmentation during the packet transmission on the link. |



#### Pre-configuration Tasks

Before configuring NQA to monitor an IP network, configure static routes or an Interior Gateway Protocol (IGP) to ensure IP route reachability among nodes.


[Configuring a DNS Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0066.html)

This section describes how to configure a DNS test to detect the speed at which a DNS name is resolved to an IP address.

[Configuring an ICMP Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0005.html)

An Internet Control Message Protocol (ICMP) test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network from end to end.

[Configuring a TCP Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0006.html)

A TCP test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network through a TCP connection.

[Configuring a UDP Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0036.html)

A UDP test can be used to measure the round-trip delay (RTD) of UDP packets exchanged between Huawei devices.

[Configuring an SNMP Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0037.html)

An NQA SNMP test can be used to measure the communication speed between a host and an SNMP agent using UDP packets.

[Configuring a Trace Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0007.html)

A trace test can be used to check the connectivity and measure the packet loss rate, delay, and other indicators of an IP network hop by hop. It can also monitor the packet forwarding path.

[Configuring an ICMP Jitter Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0008.html)

An Internet Control Message Protocol (ICMP) Jitter test can be used to measure the end-to-end jitter of various services.

[Configuring a UDP Jitter Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0009.html)

A UDP jitter test can be used to measure the end-to-end jitter of various services. It can also simulate a voice test. A UDP jitter test can be used when an ICMP jitter test cannot be used due to the ICMP reply function being disabled on network devices for security purposes.

[Configuring a Path Jitter Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0063.html)

An NQA path jitter test instance, however, can identify the Router whose jitter value is great.

[Configuring a Path MTU Test](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0064.html)

A path MTU test can obtain the maximum MTU value that does not require packet fragmentation during the packet transmission on the link.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0032.html)

After completing the test, you can check the test results.