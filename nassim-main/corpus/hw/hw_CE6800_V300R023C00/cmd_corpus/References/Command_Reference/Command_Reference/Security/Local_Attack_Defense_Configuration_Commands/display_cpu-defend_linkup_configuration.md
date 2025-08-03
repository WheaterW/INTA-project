display cpu-defend linkup configuration
=======================================

display cpu-defend linkup configuration

Function
--------



The **display cpu-defend linkup configuration** command displays linkup configurations.




Format
------

**display cpu-defend linkup configuration** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Displays the configuration of rate limiting for packets of a specified type. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The options are as follows:   * bgp * bgp4plus * ftp * isis * m-lag * m-lag-sync * ospf * ospfv3 * ssh * telnet * tftp  For the CE6885-LL (low latency mode): The options are as follows:   * bgp * ftp * isis * m-lag * m-lag-sync * ospf * ssh * telnet * tftp |
| **all** | Specifies the device. | - |
| **slot** *slot-id* | Displays the configuration of protocol association sessions in a specified slot. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display cpu-defend linkup configuration command displays the rate limit information and session information of linkup messages. By default, information for all protocols is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the linkup configurations of all devices.
```
<HUAWEI> display cpu-defend linkup configuration packet-type telnet all
Linkup Information on slot 1:                                                                     
--------------------------------------------------------------------------------------------------
PacketType  Car(pps)  Source Address                                 Source Port            Status
                      Destination Address                       Destination Port                  
--------------------------------------------------------------------------------------------------
telnet          1536  192.168.1.1                                          53021            Normal
                      192.168.2.1                                             23
telnet          1536  192.168.3.1                                          63022          Punished
                      192.168.4.1                                             23
--------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend linkup configuration** command output
| Item | Description |
| --- | --- |
| Linkup Information on slot 1 | Linkup configurations on the device. |
| PacketType | Packet type. |
| Car(pps) | Rate limit for packets, in pps. To set the rate limit for packets, run the car command. |
| Source Address | Source address. |
| Source Port | Source port. |
| Status | Protocol association session status. Normal indicates the normal state. Punished indicates that the number of sessions exceeds the upper limit and is degraded to CPCAR. |
| Destination Address | Destination port. |
| Destination Port | Destination port. |