display telemetry destination
=============================

display telemetry destination

Function
--------



The **display telemetry destination** command displays information about a destination group to which the data sampled is sent.




Format
------

**display telemetry destination** [ *dest-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dest-name* | Displays the name of a destination group to which the data sampled is sent. | The value is a string of 1 to 64 case-sensitive characters containing letters and digits. Spaces are not supported between letters or digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view destination group information, such as the name, IP address, port number and its connection status, and transport protocol, run the display telemetry destination command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all destination groups.
```
<HUAWEI> display telemetry destination
----------------------------------------------------------------------------------------------------------------------------------------
Dest-name    Dest-addr        Dest-port  State     Vpn-name      Protocol  Src-address         Src-port      Src-interface       Compression
----------------------------------------------------------------------------------------------------------------------------------------
a            10.135.84.185    50000      RESOLVED  -             GRPC      10.1.1.2            -             LoopBack1           GZIP
----------------------------------------------------------------------------------------------------------------------------------------

```

# Display information about destination group a.
```
<HUAWEI> display telemetry destination a
----------------------------------------------------------------------------------------------------------------------------------------
Dest-name   Dest-addr        Dest-port   State     Vpn-name      Protocol Istls     Src-address      Src-port    Src-interface      FailedReason    Compression
----------------------------------------------------------------------------------------------------------------------------------------
a           10.135.84.185    50000       RESOLVED  -             GRPC      NO-TLS    10.1.1.2         -             LoopBack1          NA           NONE   
----------------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display telemetry destination** command output
| Item | Description |
| --- | --- |
| Dest-name | Name of the destination group to which the data sampled is sent. |
| Dest-addr | IP address of the destination group to which the data sampled is sent. |
| Dest-port | Port number of the destination group to which the data sampled is sent. |
| State | Port connection status of the destination group to which the data sampled is sent.   * RESOLVED: subscribed. * UNRESOLVED:subscription failed. * NA: not subscribed. |
| Vpn-name | VPN instance name. |
| Protocol | Data sending protocol. |
| Src-address | If both Src-interface and Src-address have values, it indicates the address of the source interface.  If Src-interface has no value but Src-address has a value, it indicates the source IP address. |
| Src-port | Source port number of UDP. |
| Src-interface | Source interface. |
| Compression | gRPC compression type. |
| Istls | Whether to adopt TLS encryption. |
| FailedReason | Failure reason:   * NA: The connection is normal. * NO-SUBSCRIPTION: No subscription. * NO-SENSOR: The subscription is successful, but no sampling sensor is available or no sampling path is configured for a sampling sensor. * NO-SOURCEIP: No IPv4 address is bound to the source interface. * UNKNOWN: Other unknown errors occur. |