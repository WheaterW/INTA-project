NQA Test on an IP Network
=========================

IP networks carry various network services. To learn about the operating status of an IP network in real time, you can check the network status and performance indicators using different types of NQA tests. On an IP network, the following types of NQA tests can be performed:

* ICMP test: Based on a series of ping operations, an ICMP test checks the reachability, packet loss rate, delay, and time when the last ICMP Echo Reply message is received.
* Trace test: Based on the tracert operation, a trace test checks the network reachability and packet forwarding path on a per-hop basis.
* TCP test: A TCP test sends a request to set up a TCP connection with the destination to test the connection setup time.
* DNS test: By sending a domain name resolution request to the DNS server on the network, a DNS test checks the time required for resolving a domain name to an IP address.
* ICMP jitter test: An ICMP jitter test sends several ICMP messages to calculate the jitter of end-to-end delays and thereby determine whether data transmission is stable.
* UDP jitter test: A UDP jitter test sends several UDP packets to calculate the jitter of end-to-end delays and thereby determine whether data transmission is stable.

**Figure 1** NQA tests on an IP network  
![](figure/en-us_image_0000001130782112.png)
#### Application Scenario

**Table 1** Application scenarios of NQA tests on an IP network
| Test Type | Application Scenario |
| --- | --- |
| ICMP test | This test can be used to determine the network operating status. It improves on the ping operation, which must be performed manually and can test only one device at a time. |
| Trace test | This test can be used to determine whether the communication between two network nodes is smooth. In addition, a trace test can assist in diagnosing and locating a fault on the path. |
| TCP test | This test can be used when two communication parties on the network need to set up TCP connections and the TCP connection setup time needs to be checked. |
| UDP test | Many services on an IP network are transmitted over UDP. The UDP test can be used to check the performance of transmitting UDP packets. |
| DNS test | This test can be used when the time for a DNS server to resolve domain names needs to be checked. |
| ICMP jitter test | This test can be used when the network has stability-sensitive services. |
| UDP jitter test | This test can be used when an ICMP jitter test cannot be used due to the ICMP reply function being disabled on network devices for security purposes. In addition, the UDP jitter test can also be used to simulate voice traffic. |