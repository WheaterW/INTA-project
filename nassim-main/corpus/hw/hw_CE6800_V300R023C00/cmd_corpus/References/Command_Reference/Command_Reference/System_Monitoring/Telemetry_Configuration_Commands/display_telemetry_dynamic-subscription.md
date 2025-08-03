display telemetry dynamic-subscription
======================================

display telemetry dynamic-subscription

Function
--------



The **display telemetry dynamic-subscription** command displays dynamic subscription information.




Format
------

**display telemetry dynamic-subscription** [ *subName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *subName* | Specifies a dynamic subscription name. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The value is the name of an existing dynamic subscription name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view dynamic subscription information, run the display telemetry dynamic-subscription command. The command output includes the subscription name, sampling interval, encoding mode, sampling path, transport protocol, and subscription status.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dynamic subscription information.
```
<HUAWEI> display telemetry dynamic-subscription
------------------------------------------------------------------------------
Sub-name                    :_dyn_grpc_1_8001
Sub-id                      :32769
Request-id                  :0
Sample-interval(ms)         :60000
Heartbeat-interval(s)       :-
Suppress-redundant          :false
Delay-time(ms)              :1000
Originated-qos-marking      :0
Encoding                    :GPB 
Compression                 :GZIP
------------------------------------------------------------------------------
SampleInterval(ms)  Depth  Sensor-path
60000               1      huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
60000               3      huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info
------------------------------------------------------------------------------
Dest-ip           Dest-port Vpn-name                        Protocol 
192.168.0.1       54627     _public_                        GRPC     
------------------------------------------------------------------------------
Sub-state:SUCCESS 
------------------------------------------------------------------------------

```

**Table 1** Description of the **display telemetry dynamic-subscription** command output
| Item | Description |
| --- | --- |
| Sub-name | Subscription name. |
| Sub-id | Subscription ID. |
| Request-id | Subscription request ID. |
| Sample-interval(ms) | Sampling interval, in milliseconds. |
| Heartbeat-interval(s) | Heartbeat interval, in seconds. |
| Suppress-redundant | Redundancy suppression status.   * true: enabled. * false: disabled. |
| Delay-time(ms) | Delay time, in milliseconds. |
| Originated-qos-marking | DSCP value. |
| Encoding | Data encoding mode. |
| Compression | gRPC compression type. |
| SampleInterval(ms) | Actual sampling interval of a sampling path, in milliseconds. |
| Depth | Sampling path depth. |
| Sensor-path | Sampling path. |
| Dest-ip | Destination IP address. |
| Dest-port | Destination port number. |
| Vpn-name | Name of a VPN instance. |
| Protocol | Data sending protocol. |
| Sub-state | Subscription status.   * SUCCESS: Connection succeeds. * WAITING: Connection is waiting. |