display default-parameter
=========================

display default-parameter

Function
--------



The **display default-parameter ospf** command displays the default OSPF configuration.

The **display default-parameter ospfv3** command displays the default OSPFv3 configuration.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display default-parameter** { **ospfv3** | **ospf** }

For CE6885-LL (low latency mode):

**display default-parameter ospf**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ospfv3** | Display default OSPFv3 configurations.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **ospf** | Display default OSPF configurations. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view default OSPF configurations, run the **display default-parameter ospf** command.You can run the **display default-parameter ospfv3** command to view default OSPFv3 configurations.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display default OSPFv3 configurations.
```
<HUAWEI> display default-parameter ospfv3
OSPFv3 Default Values:
 Process View:
 -----------------------------------------------------
 Maximum ECMP Count                         : 32
 SPF Delay Time(sec)                        : 5
 SPF Hold Time(sec)                         : 10
 SPF Max Time(millisec)                     : 10000
 SPF Start Time(millisec)                   : 500
 SPF ExpHold Time(millisec)                 : 2000
 LSA Reorig Time(sec)                       : 5
 LSA Max Time(millisec)                     : 5000
 LSA Start Time(millisec)                   : 500
 LSA ExpHold Time(millisec)                 : 5000
 LSA Arrival Time(millisec)                 : 1000
 Wait Interval for stub-router on-startup   : 500 
 Grace Period(sec)                          : 120
 Retransmit-Interval for Grace LSAs(sec)    : 5 
 Ack wait-time for Grace LSAs(sec)          : 15 
 Helper Max Grace Period Support(sec)       : 1800 
 Bandwidth-Reference(Mbps)                  : 100
 Sham Link Cost                             : 1
 VPN Domain ID                              : 0
 VPN Router Tag                             : 0
 Default Metric                             : 1
 Default Tag                                : 1
 Default Type                               : 2
 Route Preference for Internal Routes       : 10
 Route Preference for External Routes       : 150
 -----------------------------------------------------
Area View:
 -----------------------------------------------------
 Default Stub Cost                          : 1
 NSSA Translator Stability Index(sec)       : 40
 -----------------------------------------------------
Interface View:
 -----------------------------------------------------
 Hello Interval(sec)                        : 10
 NBMA Hello Interval(sec)                   : 30
 Dead Interval(sec)                         : 40
 NBMA Dead Interval(sec)                    : 120
 Poll Interval(sec)                         : 120
 Retransmit Interval(sec)                   : 5
 Transmit Delay(sec)                        : 1
 Router DR Priority                         : 1

```

# Display default OSPF configurations.
```
<HUAWEI> display default-parameter ospf
Process View:
 -------------------------------------------------------
   Default Metric                               : 1
   Default Tag                                  : 1
   Default Type                                 : 2
   SPF Intelligent-timer Max-interval(msec)     : 10000
   SPF Intelligent-timer Start-interval(msec)   : 500
   SPF Intelligent-timer Hold-interval(msec)    : 1000
   Lsa Maxage (sec)                             : 3600
   Lsa Refresh Time(sec)                        : 1800
   Lsa Maxagediff Interval (sec)                : 900
   Minimum Lsa Arrival Interval(sec)            : 1
   Minimum Lsa Originate Interval(sec)          : 5
   Bandwidth-Reference (Mbps) : 100
   Sham Link Cost                               : 1
   VPN Domain ID                                : 0
   VPN Router Tag                               : 0
   Route Preference for Internal Routes         : 10
   Route Preference for External Routes         : 150
 -------------------------------------------------------

 Area View:
 -------------------------------------------------------
   Default Stub Cost                            : 1
 -------------------------------------------------------

 Interface View:
 -------------------------------------------------------
   P2P&Broadcast Hello Interval(sec)            : 10
   P2MP&NBMA Hello Interval(sec)                : 30
   P2P&Broadcast Dead Interval(sec)             : 40
   P2MP&NBMA Dead Interval(sec)                 : 120
   Poll Interval(sec)                           : 120
   Router DR Priority                           : 1
   Retransmit Interval(sec)                     : 5
   Transmit Delay(sec)                          : 1
 -------------------------------------------------------

```

**Table 1** Description of the **display default-parameter** command output
| Item | Description |
| --- | --- |
| OSPFv3 Default Values | Default values of OSPFv3. |
| Default Metric | Default cost of the imported external route. |
| Default Tag | Default tag of the imported external route. |
| Default Type | Default type of the imported external route. |
| Default Stub Cost | Default cost of a stub area. |
| Process View | Process view. |
| Maximum ECMP Count | Maximum number of equal-cost routes. |
| SPF Delay Time(sec) | Default delay for Shortest Path First (SPF) calculation. |
| SPF Hold Time(sec) | Hold time interval between two consecutive SPF calculations. |
| SPF Max Time(millisec) | Maximum delay time between two consecutive SPF calculations. |
| SPF Start Time(millisec) | Initial SPF schedule delay. |
| SPF ExpHold Time(millisec) | Maximum hold time between two consecutive SPF calculations. |
| SPF Intelligent-timer Max-interval(msec) | Default maximum interval of Shortest Path First (SPF) calculation. |
| SPF Intelligent-timer Start-interval(msec) | Default start interval of SPF calculation. |
| SPF Intelligent-timer Hold-interval(msec) | Default hold interval of SPF calculation. |
| LSA Arrival Time(millisec) | Interval at which LSAs are received. |
| LSA ExpHold Time(millisec) | Hold interval for updating LSAs. |
| LSA Max Time(millisec) | Maximum interval for updating LSAs. |
| LSA Start Time(millisec) | Initial interval for updating LSAs. |
| LSA Reorig Time(sec) | Interval for generating the same LSA. |
| Wait Interval for stub-router on-startup | Default period during which a device remains a stub router during a master/slave switchover. |
| Grace Period(sec) | GR period. |
| Retransmit-Interval for Grace LSAs(sec) | Default interval at which Grace Link State Advertisements (LSAs) are retransmitted, in seconds. |
| Ack wait-time for Grace LSAs(sec) | Default time during which a router waits to reply to the received Grace LSA with an LSAck message.  If the Router does not receive any Grace LSA within the default waiting time, the device does not send the LSAck message. |
| Helper Max Grace Period Support(sec) | Default GR period of the helper router. |
| Bandwidth-Reference(Mbps) | Default bandwidth reference value used to calculate the link cost, in Mbit/s. |
| Sham Link Cost | Default cost of a sham link. |
| VPN Domain ID | Default domain ID of the VPN. |
| VPN Router Tag | Default router tag of the VPN. |
| Router DR Priority | Default priority of the designated router (DR). |
| Route Preference for Internal Routes | Default priority of the internal route. |
| Route Preference for External Routes | Default priority of the external route. |
| Area View | Area view. |
| NSSA Translator Stability Index(sec) | Stable conversion interval. |
| Interface View | Interface view. |
| Hello Interval(sec) | Default interval at which Hello packets are sent on a P2P or a broadcast network. |
| NBMA Hello Interval(sec) | Default interval at which Hello packets are sent on an NBMA network. |
| NBMA Dead Interval(sec) | Default interval for declaring a neighbor Down after no Hello packets are received on a non-broadcast multiple access (NBMA) network. |
| Dead Interval(sec) | Default interval for declaring a neighbor Down after no Hello packets are received on a P2P or broadcast network. |
| Poll Interval(sec) | Default interval for the local router to send Hello packets to a neighbor in the Down state on an NBMA network. The value of Poll Interval is greater than that of Hello Interval. |
| Retransmit Interval(sec) | Default interval at which packets are retransmitted. |
| Transmit Delay(sec) | Default estimated time it takes for an interface to transmit an LSU packet. The value is added to the age of the LSAs in the LSU packet before transmission. |
| Lsa Maxage (sec) | Default maximum age of the LSA. |
| Lsa Refresh Time(sec) | Default maximum interval for generating an LSA. If the LS age of the LSAs generated by the Router reaches the LSA Refresh Time, a new instance needs to be generated for the LSAs. |
| Lsa Maxagediff Interval (sec) | Default value difference in the MaxAge fields of LSAs. If the value difference in the MaxAge fields of two LSAs is greater than MaxAgeDiff Interval, the two LSAs belong to different instances of the same LSA. |
| Minimum Lsa Arrival Interval(sec) | Default minimum interval at which the same LSA is received. |
| Minimum Lsa Originate Interval(sec) | Default minimum interval at which the same LSA is sent. |
| Bandwidth-Reference (Mbps) | The bandwidth reference value. |
| P2P&Broadcast Hello Interval(sec) | Default interval at which Hello packets are sent on a P2P or a broadcast network. |
| P2P&Broadcast Dead Interval(sec) | Default interval for declaring a neighbor Down after no Hello packets are received on a P2P or broadcast network. |
| P2MP&NBMA Hello Interval(sec) | Default interval at which Hello packets are sent on a P2MP or an NBMA network. |
| P2MP&NBMA Dead Interval(sec) | Default interval for declaring a neighbor Down after no Hello packets are received on a P2MP or an NBMA network. |