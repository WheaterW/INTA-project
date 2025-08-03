linkup-car
==========

linkup-car

Function
--------



The **linkup-car** command sets the CPCAR value for packets of a protocol connection.

The **undo linkup-car** command restores the default CPCAR rate limit.



By default, the CAR for M-LAG connections is 1024 pps, that for M-LAG-SYNC connections is 2048 pps, and that for connections of other protocols is 1536 pps.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**linkup-car packet-type** { **bgp** | **bgp4plus** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ospfv3** | **ssh** | **telnet** | **tftp** } **pps** *pps-value*

**undo linkup-car packet-type** { **bgp** | **bgp4plus** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ospfv3** | **ssh** | **telnet** | **tftp** }

For CE6885-LL (low latency mode):

**linkup-car packet-type** { **bgp** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ssh** | **telnet** | **tftp** } **pps** *pps-value*

**undo linkup-car packet-type** { **bgp** | **ftp** | **isis** | **m-lag** | **m-lag-sync** | **ospf** | **ssh** | **telnet** | **tftp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bgp** | Indicates that the protocol type is BGP. | - |
| **bgp4plus** | Indicates that the protocol type is BGP4+.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ftp** | Indicates that the protocol type is FTP. | - |
| **isis** | Indicates that the protocol type is ISIS. | - |
| **ssh** | Indicates the protocol type is SSH. | - |
| **telnet** | Indicates the protocol type is TELNET. | - |
| **tftp** | Indicates the protocol type is TFTP. | - |
| **pps** *pps-value* | Specifies the CAR value. The value is an integer that ranges from 64 to 10000, in pps. | The value is an integer ranging from 64 to 10000. The default value is 1024 for M-LAG packets, 2048 for M-LAG synchronization packets, and 1536 for other packets. |
| **packet-type** | Indicates the protocol type. | - |
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

The default CPCAR value of protocol is small. When a switch uses these protocols to transfer files or set up connections with other hosts or devices, the number of protocol packets sharply increases in a short period. When the packet rate exceeds the limit, the protocol packets are dropped. The switch may also undergo attacks of other protocols. This affects data transmission and causes service interruption.You can run the cpu-defend application-apperceive command to enable active link protection, ensuring normal operation of these protocols related services when attacks occur. When a connection is set up, the switch sends packets at the rate of the CPCAR value configured using the linkup-car command. The CPCAR value can be set as required.

**Precautions**

* After association between M-LAG and M-LAG-SYNC is enabled and a link is established, the system can send packets to the CPU based on the CPCAR value configured using the linkup-car command.
* After M-LAG and M-LAG-SYNC packets are transmitted and association between M-LAG and M-LAG-SYNC is enabled, the system can still send packets based on the CPCAR value configured using the linkup-car command.


Example
-------

# Configure the attack defense policy named test to limit the rate of FTP packets sent to the CPU to 5000 pps.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] linkup-car packet-type ftp pps 5000

```