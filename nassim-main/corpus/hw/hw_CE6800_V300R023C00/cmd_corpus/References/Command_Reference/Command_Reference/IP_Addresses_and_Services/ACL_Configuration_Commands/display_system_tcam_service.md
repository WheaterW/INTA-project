display system tcam service
===========================

display system tcam service

Function
--------



The **display system tcam service brief** command displays the group index and rule count occupied by different services.




Format
------

**display system tcam service** { **cpcar** **slot** *slot-id* | *service-name* **slot** *slot-id* [ **chip** *chip-id* ] }

**display system tcam service brief** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cpcar** | Specifies the CPCAR service. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is an integer. You can enter the question mark (?) and select the value as prompted. |
| *service-name* | Indicates the service type. | For the CE6820H, CE6820H-K and CE6820S: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * bpdu-deny * brief * capture-packet * cpcar * dynamic-ctl-pkt * erps-global * erps-vlan * hard-zoning * hard-zoning-deny * icmpv6-ping-detect * in-port * ioam-encap-v4 * ioam-encap-v6 * nac-base-auth * networkcc * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * qos-group-sip * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * mlag-arp * mlag-nd * ifit-static * ifit-dyn * ifit-cfg * ifit-dyn-egress * ifit-cfg-egress  For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * brief * capture-packet * cpcar * dynamic-ctl-pkt * forward-drop * hard-zoning * hard-zoning-deny * hard-zoning-deny-v6 * hard-zoning-v6 * icmpv6-ping-detect * in-port * network-ack * network-ack-v6 * network-cc * network-cc-v6 * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * vxlan-local-preference * vxlan-local-preference-v6 * vxlan-tunnel-inbound * vxlan-tunnel-outbound * mlag-arp * mlag-nd * ifit-static * ifit-dyn * ifit-cfg * ifit-dyn-egress * ifit-cfg-egress * vmware  For the CE6860-SAN, CE6866K, CE6866 and CE6860-HAM: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * brief * capture-packet * cpcar * dynamic-ctl-pkt * forward-drop * hard-zoning * hard-zoning-deny * hard-zoning-deny-v6 * hard-zoning-v6 * icmpv6-ping-detect * in-port * ioam-encap-v4 * ioam-encap-v6 * network-ack * network-ack-v6 * network-cc * network-cc-v6 * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * qos-group-sip * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * vxlan-local-preference * vxlan-local-preference-v6 * vxlan-tunnel-inbound * vxlan-tunnel-outbound * traffic-segment * traffic-segment-IPv6 * segment-policy * segment-fragment-pass * segment-isolate * mlag-arp * mlag-nd * nslb * vmware  For the CE6863H and CE6863H-K: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * bpdu-deny * bpdu-forward * brief * capture-packet * cpcar * dynamic-ctl-pkt * icmpv6-ping-detect * in-port * ioam-encap-v4 * ioam-encap-v6 * l2pt * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * qos-group-sip * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * vxlan-tunnel-inbound * vxlan-tunnel-outbound * mlag-arp * mlag-nd * ifit-static * ifit-dyn * ifit-cfg * ifit-dyn-egress * ifit-cfg-egress  For the CE6881H and CE6881H-K: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * bpdu-deny * bpdu-forward * brief * capture-packet * cpcar * dynamic-ctl-pkt * forward-drop * icmpv6-ping-detect * in-port * ioam-encap-v4 * ioam-encap-v6 * l2pt * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * qos-group-sip * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * vxlan-tunnel-inbound * vxlan-tunnel-outbound * mlag-arp * mlag-nd * ifit-static * ifit-dyn * ifit-cfg * ifit-dyn-egress * ifit-cfg-egress  For the CE6885-LL (low latency mode): The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * bpdu-deny * bpdu-forward * brief * capture-packet * cpcar * dynamic-ctl-pkt * erps-global * erps-vlan * in-port * l2pt * mlag-arp * null-mac * pa-bfd-mc * pfc-hook-flow * port-arp-limit  For the CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM: The options are as follows:   * app-session * auto-defend * auto-defend-v6 * auto-port-defend * brief * capture-packet * cpcar * dynamic-ctl-pkt * forward-drop * hard-zoning * hard-zoning-deny * hard-zoning-deny-v6 * hard-zoning-v6 * icmpv6-ping-detect * in-port * ioam-encap-v4 * ioam-encap-v6 * network-ack * network-ack-v6 * network-cc * network-cc-v6 * null-mac * ou-port * out-port * pa-bfd-mc * pfc-hook-flow * ping-detect * port-arp-limit * qos-group-sip * trans-vlan-ip * trans-vlan-mac * trans-vlan-preip * trans-vlan-protocol * vxlan-local-preference * vxlan-local-preference-v6 * vxlan-tunnel-inbound * vxlan-tunnel-outbound * traffic-segment * traffic-segment-IPv6 * segment-policy * segment-fragment-pass * segment-isolate * mlag-arp * mlag-nd * vmware |
| **chip** *chip-id* | Specifies a chip ID. | The value is an integer. It must be the ID of an available chip. |
| **brief** | Displays the group index and rule count occupied by different services. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run this command to view detailed information about a specified service, including service priority, matched packet statistics, and delivered TCAM entries on chips.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the EntryId of the CPCAR service on the board in slot 1.
```
<HUAWEI> display system tcam service cpcar slot 1
Total: 12
--------------------------------------------------------
PacketType                         CPEntry    PAEntry
--------------------------------------------------------
ARP Proxy                              139        138
ARP REPLY                               22         11
ARP REQUEST BC                          21         10
ARP REQUEST UC                          20          9
FIB L3know                              43          -
FIB L3know LPM                          45          -
FIB MISS SYN                            46          -
FIB6 L3know                             64          -
FIB6 L3know LPM                         65          -
FTP L4Dstport20                         32          -
FTP L4Dstport21                         30          -
FTP L4Srcport21                         31          -
--------------------------------------------------------

```

# Display the group index and rule count occupied by different services in slot 1.
```
<HUAWEI> display system tcam service brief slot 1
Slot: 1
------------------------------------------------------------------------------
 Chip  GroupID    Width      Stage          ServiceName                 Count
------------------------------------------------------------------------------
 0           5    320Bit     Ingress        CPCAR CP                       90
             6    320Bit     Ingress        BPDU Deny                      63
             6    320Bit     Ingress        CPCAR PA                       19
------------------------------------------------------------------------------

```
```
<HUAWEI> display system tcam service brief
Slot: 1
------------------------------------------------------------------------------
 Chip  Pipe  GroupID    Width    Stage          ServiceName             Count
------------------------------------------------------------------------------
    0     0        2    320Bit   Pre-Ingress    Trans Vlan by IP            2
                   2    320Bit   Pre-Ingress    Trans Vlan by MAC           2
                   5    320Bit   Ingress        App-Session                 1
                   5    320Bit   Ingress        CPCAR CP                  107
                   6    320Bit   Ingress        BPDU Deny                  21
                   6    320Bit   Ingress        CPCAR PA                   27
                  28    320Bit   Ingress        Blacklist                   3
                  86     80Bit   Ingress        MQC QoS Group SIP           2
------------------------------------------------------------------------------
    0     2        5    320Bit   Ingress        App-Session                 1
                   5    320Bit   Ingress        CPCAR CP                  107
                   6    320Bit   Ingress        BPDU Deny                  21
                   6    320Bit   Ingress        CPCAR PA                   27
                  28    320Bit   Ingress        Blacklist                   3
                  86     80Bit   Ingress        MQC QoS Group SIP           2
------------------------------------------------------------------------------

```

**Table 1** Description of the **display system tcam service** command output
| Item | Description |
| --- | --- |
| PacketType | Displays the service type name. The service type name of CPCAR is displayed. For example, ARP BC indicates broadcast ARP. |
| CPEntry | The EntryId of the ACL rule for sending packets to the CPU. |
| PAEntry | EntryId of the protocol packet parsing rule. |
| Chip | Chip ID. |
| GroupID | ID of the group resource used by a service. |
| Width | Width of the group resource used by a service. |
| Stage | Stage of rules. |
| ServiceName | Names of all services on the chip. |
| Count | Number of rules for different services. |
| Pipe | Pipe where the service is located. |
| Slot | Slot ID. |
| Total | The total number of entries. |