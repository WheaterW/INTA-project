application-apperceive enable
=============================

application-apperceive enable

Function
--------



The **application-apperceive enable** command enables protocol association.

The **undo application-apperceive enable** command disables protocol association.



By default, IS-IS, OSPF, OSPFv3, M-LAG, and M-LAG-SYNC are disabled, and BGP, BGP4+, FTP, TFTP, Telnet, and SSH are enabled.

For the CE6885-LL low-latency model, IS-IS, OSPF, M-LAG, and M-LAG-SYNC are disabled by default, and BGP, FTP, TFTP, Telnet, and SSH are enabled by default.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**application-apperceive** { **bgp** | **bgp4plus** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ospfv3** | **ssh** | **telnet** | **tftp** } **enable**

**undo application-apperceive** { **bgp** | **bgp4plus** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ospfv3** | **ssh** | **telnet** | **tftp** } **enable**

For CE6885-LL (low latency mode):

**application-apperceive** { **bgp** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ssh** | **telnet** | **tftp** } **enable**

**undo application-apperceive** { **bgp** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ssh** | **telnet** | **tftp** } **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bgp** | Indicates that the protocol type is BGP. | - |
| **bgp4plus** | Indicates that the protocol type is BGP4+.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ftp** | Indicates that the protocol type is FTP. | - |
| **isis** | Indicates that the protocol type is ISIS. | - |
| **ssh** | Indicates the protocol type is SSH. | - |
| **telnet** | Indicates that the protocol type is Telnet. | - |
| **tftp** | Indicates the protocol type is TFTP. | - |
| **ospf** | Indicates the protocol type is OSPF. | - |
| **ospfv3** | Indicates the protocol type is OSPFv3.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **m-lag** | Indicates that the protocol type is M-LAG. | - |
| **m-lag-sync** | Indicates that the protocol type is M-LAG-SYNC. | - |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When packets are sent to the CPU, they are placed into a CPU queue. If the rate of packets sent to the CPU exceeds the configured CAR value, excess packets are discarded. After you run this command to configure protocol association for packets and then establish a link, protocol association takes effect, and the protocol packets for establishing connections are placed into a special protocol association queue, preventing excess protocol packets above the CAR from being discarded.

**Precautions**

* After you run this command to configure association between M-LAG and M-LAG-SYNC packets and then establish a link, the association takes effect.
* After M-LAG and M-LAG-SYNC packets are used to establish a link, you can run this command to configure protocol association. In this case, M-LAG and M-LAG-SYNC protocol association also takes effect.


Example
-------

# Enable protocol association for Telnet packets.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] application-apperceive telnet enable

```