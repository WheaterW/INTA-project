display ospf brief
==================

display ospf brief

Function
--------



The **display ospf brief** command displays brief OSPF information.




Format
------

**display ospf** [ *process-id* ] **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process.  If no OSPF process ID is specified, brief information about all OSPF processes is displayed. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When locating OSPF faults, you can run this command to obtain brief OSPF information. You can locate OSPF faults based on the command output.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPF brief information.
```
<HUAWEI> display ospf brief
OSPF Process 1 with Router ID 10.9.9.9
                  OSPF Protocol Information
RouterID: 10.9.9.9          Border Router: AREA 
Multi-VPN-Instance is not enabled 
Global DS-TE Mode is disabled 
Graceful-restart capability: disabled 
Helper support capability  : not configured 
OSPF Stub Router State Reason: Startup Synchronize
    Router LSA stub links with cost 65535
    Summary LSA with cost 16777214 
    External LSA with cost 16777214
Spf-schedule-interval: max 10000ms, start 500ms, hold 1000ms 
Default ASE parameters: Metric: 1 Tag: 0 Type: 2 
Route Preference: 10 
ASE Route Preference: 150 
Intra Route Preference: 50 
Inter Route Preference: 50 
SPF Computation Count: 56 
RFC 1583 Compatible
OSPF is in LSDB overflow status(remain time: 205s)
Retransmission limitation is disabled
Import routes limitation is enabled
  Self ASE LSA count: 8
  Current status: Normal
bfd enabled
BFD Timers: Tx-Interval 10 , Rx-Interval 10 , Multiplier 3 
Area Count: 2   Nssa Area Count: 1 
Exchange/Loading Neighbors: 0

 Area: 0.0.0.0             (MPLS TE not enabled)
 Authtype: None   Area flag: Normal
 SPF scheduled count: 2
 Exchange/Loading neighbors: 0
 Router ID conflict state: Normal

 Interface: 10.1.1.1 (100GE1/0/1)
 Cost: 1       State: DR      Type: Broadcast      MTU: 1500
 Priority: 1
 Designated Router: 10.1.1.1
 Backup Designated Router: 0.0.0.0
 Timers: Hello 10, Dead 40, Wait 40, Poll 120, Retransmit 5, Transmit Delay 1

 Area: 0.0.0.1             (MPLS TE not enabled)
 Authtype: None   Area flag: NSSA
 SPF scheduled count: 1
 Exchange/Loading neighbors: 0
 NSSA Translator State: Elected
 Router ID conflict state: Normal
 Import routes limitation is enabled
  Self NSSA LSA count: 2
  Current status: Normal

 Interface: 10.1.1.1 (100GE1/0/1)
 Cost: 1       State: P-2-P   Type: P2P      MTU: 1500
 Timers: Hello 10, Dead 40, Wait 40, Poll 120, Retransmit 5, Transmit Delay 1

```

**Table 1** Description of the **display ospf brief** command output
| Item | Description |
| --- | --- |
| OSPF Stub Router State Reason | Reason why the Stub Router state is displayed. This state is displayed only when a stub router is restarting. |
| OSPF is in LSDB overflow status(remain time: 205s) | The maximum number of external routes in the OSPF LSDB is in the overload state (the remaining time of the overload timer is 205s).  When the number of external routes in the OSPF LSDB reaches or exceeds 90% of the maximum number, the following information is displayed:  OSPF LSDB is approaching overflow limit .  To configure the maximum number of external routes supported by the OSPF LSDB, run the lsdb-overflow-limit number command. |
| Router LSA stub links with cost 65535 | The maximum cost 65535 is set for stub links in router LSAs. The function is enabled using the stub-router command. |
| Router ID conflict state | Router ID conflict state. |
| Border Router | Border router. The values are as follows:   * AS: autonomous system boundary router (ASBR). * AREA: area border router (ABR). * NSSA: NSSA border router. |
| Multi-VPN-Instance | Whether VPN multi-instance is enabled. |
| Global DS-TE Mode | Diff-Serv-Traffic Engineering (DS-TE) mode in the current global configuration:   * Non-standard IETF Mode: The IETF mode is not supported. * Standard IETF Mode: The IETF mode is supported. |
| Graceful-restart capability | Whether graceful restart is enabled:   * disabled: Graceful restart is disabled. You can run the graceful-restart command to enable graceful restart. * planned only: The planned-GR mode is supported. * un-planned: The unplanned GR mode is supported. * totally: The totally GR mode is supported. * planned and un-planned: Planned-GR and unplanned-GR are supported. |
| Helper support capability | Whether the Helper mode is enabled:   * enabled: The GR Helper mode is enabled. * disabled: indicates that the GR Helper mode is disabled. You can run the graceful-restart command to enable the GR Helper mode. |
| State | Interface status, which can be Down, Waiting, Loopback, P-2-P, DR, BDR or DROTHER. DR, BDR, and DROTHER exist only on broadcast and NBMA networks, and P-2-P exists only on P2P and P2MP networks. |
| Summary LSA with cost 16777214 | Summary-LSAs with cost 16777214 are advertised. The function is enabled using the stub-router command. |
| External LSA with cost 16777214 | External LSAs with cost 16777214 are advertised. The function is enabled using the stub-router command. |
| Default ASE parameters | Default parameter values of the external link status advertisement (LSA), including:   * Metric: metric value. * Tag: route tag. * Type: route type. |
| ASE Route Preference | Priority of the external route. |
| Route Preference | Priority of the default route. |
| Intra Route Preference | Priority of the intra-area route. |
| Inter Route Preference | Priority of the inter-area route. |
| SPF Computation Count | Number of times that SPF calculation is performed. |
| SPF scheduled count | Number of times that SPF calculation is performed. |
| RFC 1583 Compatible | RFC 1583 compatibility is enabled. If not, you can run the rfc1583 compatible command to configure the rules defined in RFC 2328 to be compatible with those defined in RFC 1583. |
| Retransmission limitation | Whether a retransmission limit is configured. |
| Import routes limitation | Whether a limit is configured on the number of LSAs generated when an OSPF process imports routes. |
| Self ASE LSA count | Number of ASE LSAs.  This field is displayed only in an OSPFv3 process. |
| Self NSSA LSA count | Number of NSSA LSAs.  This field is displayed only in an NSSA. |
| Current status | A limit has been configured on the number of LSAs generated when an OSPF process imports external routes. The current status can be:   * Normal: The lower alarm threshold is not exceeded. * Approach limit: The alarm threshold is about to be reached, and the number of LSAs has reached 90% of the upper alarm threshold. * Exceed limit: The number has reached or exceeded the maximum. |
| bfd enabled | BFD is enabled. |
| BFD Timers | BFD session parameters. |
| Area Count | Number of areas in the process. |
| Area | Area ID. |
| Area flag | Area attribute. The options are as follows:   * Normal: common area. * Vlink: transmission area of the virtual link. * Stub: stub area. * Nssa: NSSA area. |
| Nssa Area Count | Number of Not-So-Stubby Areas (NSSAs) in the current process. |
| Exchange/Loading neighbors | Number of neighbors in ExChange or Loading state. |
| Designated Router | Interface of the designated router (DR). |
| Backup Designated Router | Interface of the BDR. |
| NSSA Translator State | NSSA translator role. |
| MPLS TE | Whether MPLS TE is enabled. |
| RouterID | Router ID of a device. |
| Authtype | Area authentication type. |
| Interface | Information about the interface in an area. |
| Cost | Cost of an OSPF interface. |
| Type | Type of an interface. The options are as follows:   * PTP: indicates that the interface type is P2P. * Broadcast: indicates that the interface is a broadcast interface. * NBMA: indicates that the interface type is NBMA. * PTMP: indicates that the interface is a P2MP interface. |
| MTU | Maximum transmission unit (MTU) of an interface. |
| Priority | Interface priority. |
| Timers | Timer intervals:   * Hello: interval at which an interface sends Hello packets, which can be set using the ospf timer hello command. * Dead: OSPF neighbor dead interval, which can be set using the ospf timer dead command. * Wait: OSPF wait interval, which can be set using the ospf timer wait command. * Poll: interval at which poll Hello packets are sent on NBMA networks, which can be set using the ospf timer poll command. * Retransmit: interval at which an interface retransmits LSAs, which can be set using the ospf timer retransmit command. * Transmit Delay: LSA transmission delay, which can be set using the ospf trans-delay command. |
| Spf-schedule-interval | Interval for performing the shortest path first (SPF) calculation. |