monitor interface-statistics
============================

monitor interface-statistics

Function
--------



The **monitor interface-statistics batch** command monitors traffic statistics on a batch of interfaces.

The **monitor interface-statistics** command monitors traffic statistics on a specified interface.




Format
------

**monitor interface-statistics interface** { *interface-name* | *interface-type* *interface-number* } &<1-5> [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ]

**monitor interface-statistics batch** [ **interface** *interface-type* [ *interface-number-begin* [ **to** *interface-number-end* ] ] ] [ [ **interval** *interval-value* ] [ **times** { *times-value* | **infinity** } ] | [ **times** { *times-value* | **infinity** } ] [ **interval** *interval-value* ] ] [ **main** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | The value is of the enumerated type. |
| *interface-number* | Specifies the start interface number in an interface range. | If the start number of an interface is not specified, the running status and statistics of all interfaces of this type are displayed. |
| **interval** *interval-value* | Specifies the interval at which traffic statistics are collected. | The value is an integer ranging from 2 to 600, in seconds. The default value is 10. |
| **times** *times-value* | Specifies the interval at which traffic statistics are collected. | The value is an integer ranging from 1 to 999, in seconds. The default value is 5. |
| **infinity** | Indicates that traffic statistics are collected for the infinity number of times. To stop the statistics display, press Ctrl+C. | - |
| **interface** | Specifies an interface. | - |
| *interface-number-begin* | Specifies a start interface number. | If the start number of an interface is not specified, the running status and statistics of all interfaces of this type are displayed. |
| **to** *interface-number-end* | Specifies an end interface number. | The interface-number-end value must be greater than the interface-number-begin value. interface-number-end and interface-number-begin specify an interface range. If to interface-number-end is not specified, only the interface specified by interface-number-begin can be configured. |
| **main** | Displays statistics about the main interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To monitor traffic statistics on a specified interface, run the monitor interface-statistics command. Traffic statistics can be displayed at a specified interval for a specified number of times.By default, once the monitor interface-statistics command is run on an interface, the system displays traffic statistics five times at an interval of 10s. To stop the statistics display, press Ctrl+C.



**Precautions**

You can enter the following characters to control command execution:

* c: deletes existing statistics and collects statistics again.
* q: stops statistics collection.
* u and d: pages up and down, respectively, to view more statistics.
* b: collects byte statistics.
* p: collects packet statistics.


Example
-------

# Monitor traffic statistics on a batch of interfaces.
```
<HUAWEI> system-view
[~HUAWEI] monitor interface-statistics batch
Seconds: 0
Interface     Link      Input packets    (pps)   BWUT    Output packets    (pps)   BWUT   Description                           
100GE1/0/1    DOWN          23315          0     0%             0            0     0%     Connect to DeviceA 100GE1/0/1 interface
100GE1/0/1    UP            23350          0     0%             0            0     0%
100GE1/0/2    DOWN          30000          1     0.01%          0            0     0%
100GE1/0/3    DOWN          29989          1     0.01%          0            0     0%
Temporary Clear=c, Quit=q, Up=u, Down=d, Bytes=b, Packets=p

```

# Display traffic statistics on 100GE 1/0/1, and 100GE 1/0/2 for twice at an interval of 10s.
```
<HUAWEI> system-view
[~HUAWEI] monitor interface-statistics interface 100GE1/0/1 100GE1/0/2 times 2
Display statistics of the interface at the interval of 10 seconds for up to 2 times. Press Ctrl + C to stop.
  0 seconds left
Times 1
Interface :100GE1/0/1
-------------------------------------------------------------------------
Input rate   :                    0 bits/sec,                      0 packets/sec
Output rate  :                    0 bits/sec,                      0 packets/sec
Input        :                    0 bytes,                         24911 packets
Output       :                    0 bytes,                         7382 packets
Input error  :                    0 packets
Output error :                    0 packets
Input bandwidth utilization  :    0%
Output bandwidth utilization :    0%


Interface : 100GE1/0/2
-------------------------------------------------------------------------
Input rate   :                    160 bits/sec,                    1 packets/sec
Output rate  :                    0 bits/sec,                      0 packets/sec
Input        :                    0 bytes,                         32081 packets
Output       :                    0 bytes,                         207 packets
Input error  :                    0 packets
Output error :                    0 packets
Input bandwidth utilization  :    0.01%
Output bandwidth utilization :    0%

  0 seconds left
Times 2
Interface : 100GE1/0/1
-------------------------------------------------------------------------
Input rate   :                    160 bits/sec,                    1 packets/sec
Output rate  :                    0 bits/sec,                      0 packets/sec
Input        :                    0 bytes,                         24923 packets
Output       :                    0 bytes,                         7386 packets
Input error  :                    0 packets
Output error :                    0 packets
Input bandwidth utilization  :    0.01%
Output bandwidth utilization :    0%


Interface : 100GE1/0/2
-------------------------------------------------------------------------
Input rate   :                    160 bits/sec,                    1 packets/sec
Output rate  :                    0 bits/sec,                      0 packets/sec
Input        :                    0 bytes,                         32097 packets
Output       :                    0 bytes,                         207 packets
Input error  :                    0 packets
Output error :                    0 packets
Input bandwidth utilization  :    0.01%
Output bandwidth utilization :    0%

```

# Enter b and c to switch to the byte statistics mode, delete existing statistics, and collect statistics again.
```
<HUAWEI> system-view
[~HUAWEI] monitor interface-statistics batch
Seconds: 0
Interface     Link     Input bytes    (bps) BWUT      Output bytes    (bps)  BWUT   Description
100GE1/0/1    DOWN             0       160  0.01%             0         0     0%    Connect to DeviceA 100GE1/0/1 interface
100GE1/0/1      UP             0       160  0.01%             0         0     0%
100GE1/0/2    DOWN             0       160  0.01%             0         0     0%
100GE1/0/3    DOWN             0       160  0.01%             0         0     0%
Temporary Clear=c, Quit=q, Up=u, Down=d, Bytes=b, Packets=p

```

**Table 1** Description of the **monitor interface-statistics** command output
| Item | Description |
| --- | --- |
| Interface | Interface type and number. Statistics about traffic on this interface are displayed. |
| Link | Link layer protocol status of the interface:   * UP: The link layer protocol status of the interface is Up. * DOWN: The link layer protocol status of the interface is Down or no IP address is assigned to the interface. |
| Input rate | Rate at which an interface receives packets. The results are displayed in two dimensions:   * bits/sec: bit rate. * packets/sec: packet rate. |
| Input error | Number of error packets received by the interface. |
| Input bandwidth utilization | Bandwidth usage of an interface that receives packets. |
| Input | Information about packets received by an interface:   * bytes: number of bytes. * BWUT: Utilization of the bandwidth. * packets: number of packets. * pps: packet rate. * bps: bit rate. |
| Output rate | Rate at which an interface sends packets: The results are displayed in two dimensions:   * bits/sec: bit rate. * packets/sec: packet rate. |
| Output error | Statistics about error packets sent by the interface. |
| Output bandwidth utilization | Bandwidth usage of an interface that sends packets. |
| Output | Information about packets sent by an interface:   * bytes: number of bytes. * BWUT: Utilization of the bandwidth. * packets: number of packets. * pps: packet rate. * bps: bit rate. |
| Description | Interface description. This field is displayed only for an interface whose description has been configured using the description command. |
| Packets=p | Control characters, which are case insensitive. After a character is entered, the system collects packet statistics. |
| seconds left | Time remaining before the interval for displaying statistics about traffic on the interface expires, in seconds. |
| Times | Number of times when traffic statistics are displayed. This field is available at the beginning of each query. |
| Seconds | Total monitoring time, in seconds. |
| Clear=c | Control characters, which are case insensitive. After a character is entered, existing packet statistics are deleted. |
| Quit=q | Control characters, which are case insensitive. After a character is entered, command execution is stopped. |
| Up=u | Control characters, which are case insensitive. After a character is entered, the screen pages up. |
| Down=d | Control characters, which are case insensitive. After a character is entered, the screen pages down. |
| Bytes=b | Control characters, which are case insensitive. After a character is entered, the system collects byte statistics. |