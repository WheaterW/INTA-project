monitor interface counters
==========================

monitor interface counters

Function
--------



The **monitor interface counters** command enables a device to monitor traffic statistics on an interface.




Format
------

**monitor interface counters** [ **rate** ] { *interface-name* | *interface-type* *interface-number* } [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate** | Displays the traffic rate on an interface. If rate is not specified, the number of packets on an interface is displayed.  This parameter is supported only on an interface whose physical status is Up. | - |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **interval** *interval-value* | Specifies the interval at which the running status and traffic statistics of an interface are monitored. | The value is an integer ranging from 2 to 600, in seconds. The default value is 10. |
| **times** *times-value* | Specifies the number of times that the running status and traffic statistics of an interface are monitored. | The value is an integer ranging from 1 to 999. The default value is 5. |
| **infinity** | Monitors the running status and traffic statistics of an interface for indefinite times. To stop the statistics display, press Ctrl+C. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view real-time traffic statistics on an interface, run the monitor counters interface command to enable a device to monitor traffic statistics on the interface at a specified interval and display the statistics in real time. The traffic statistics include the number of unicast, multicast, and broadcast packets sent or received by the interface and the packet transmission rate. The number of such packets is counted in the period from the last time when the interface statistics were cleared using the **reset interface counters** command to this time the monitor counters interface command is run.By default, once this command is run, the system displays real-time traffic statistics at an interval of 10s for five times. To stop the statistics display, press Ctrl+C.



**Prerequisites**



Traffic statistics collection has been enabled in the Layer 2 or Layer 3 sub-interface view. This function is disabled by default.



**Precautions**



If rate is not specified, the total number of packets on an interface is displayed. If you want to recalculate traffic statistics on the interface, run the **reset interface counters** command to delete existing statistics on the interface.




Example
-------

# Set the interval for displaying traffic statistics on 100GE 1/0/1 to 3 seconds and set the number of times for displaying traffic statistics on this interface to 2.
```
<HUAWEI> monitor interface counters 100GE 1/0/1 interval 3 times 2
Display counters of the interface at the interval of 3 seconds for up to 2 times. Press Ctrl + C to stop.
  0 seconds left
Times 1
Inbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                       0             0               0            3107
Outbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                       0             0               0            3084

  0 seconds left
Times 2
Inbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                       0             0               0            3108
Outbound
Interface           Octets(bytes) Unicast(pkts) Multicast(pkts) Broadcast(pkts)
100GE1/0/1                       0             0               0            3085

```

# Set the interval for displaying the traffic rate on 100GE 1/0/1 to 3 seconds and set the number of times for displaying the traffic rate on this interface to 2.
```
<HUAWEI> monitor interface counters rate 100GE 1/0/1 interval 3 times 2
Display counters of the interface at the interval of 3 seconds for up to 2 times. Press Ctrl + C to stop.
  0 seconds left
Times 1
Inbound
Interface           Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                         0               0                0                  0
Outbound
Interface           Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                         0               0                0                  0

  0 seconds left
Times 2
Inbound
Interface           Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                         0               0                0               3108
Outbound
Interface           Octets(bytes/s) Unicast(pkts/s) Multicast(pkts/s) Broadcast(pkts/s)
100GE1/0/1                         0               0                0               3085

```

**Table 1** Description of the **monitor interface counters** command output
| Item | Description |
| --- | --- |
| seconds left | Remaining time before the next interval for displaying traffic statistics on the interface expires, in seconds. |
| Times | Number of times for the statistics display. This field is displayed each time when the query starts. |
| Inbound | Statistics about traffic received by an interface. |
| Interface | Interface name. |
| Octets(bytes) | Total number of bytes sent or received by an interface. |
| Unicast(pkts) | Total number of unicast packets sent or received by an interface. |
| Multicast(pkts) | Total number of multicast packets sent or received by an interface. |
| Broadcast(pkts) | Total number of broadcast packets sent or received by an interface. |
| Outbound | Statistics about traffic sent by an interface. |
| Octets(bytes/s) | Traffic rate at which packets are sent or received by an interface, in byte/s. |
| Unicast(pkts/s) | Traffic rate at which unicast packets are sent or received by an interface, in packet/s. |
| Multicast(pkts/s) | Traffic rate at which multicast packets are sent or received by an interface, in packet/s. |
| Broadcast(pkts/s) | Traffic rate at which broadcast packets are sent or received by an interface, in packet/s. |