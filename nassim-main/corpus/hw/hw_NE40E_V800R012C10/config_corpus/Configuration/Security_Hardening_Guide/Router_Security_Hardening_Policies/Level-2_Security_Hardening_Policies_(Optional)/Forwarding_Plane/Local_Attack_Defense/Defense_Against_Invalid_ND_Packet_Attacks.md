Defense Against Invalid ND Packet Attacks
=========================================

Defense Against Invalid ND Packet Attacks

#### Security Policy

Defense against invalid ND packet attacks controls the invalid ND packets (IPv6 NS/NA/RS/RA/Redirect/CPS) to be sent to the CPU. The forwarding engine supports the function of identifying NS/NA/RS/RA/Redirect/CPS packets, which has fragmented packets and the non-fragmented packets that do not match the local route discarded. However, the function of identifying NS/NA/RS/RA/Redirect/CPS packets is not enabled by default. You can run a specific command to enable this function.


#### Attack Methods

**Table 1** ICMP headers of RS/RA/NS/NA/Redirect/CPS packets
| Packet Type | ICMP type |
| --- | --- |
| RS | 0x85 |
| RA | 0x86 |
| NS | 0x87 |
| NA | 0x88 |
| Redirect | 0x89 |
| CPS | 0x94 |


* Non-fragment: RS/RA/NS/NA/Redirect/CPS, with the nextheader field value in the IPv6 header being 0x3A or the source IP address being a non-link-local address.
* Fragment: RS/RA/NS/NA/Redirect/CPS, with the nextheader field value in the IPv6 header being 0x2C or the NextHeader field value in the IPv6 extended header being 0x3A.

The preceding packets are invalid ND packets and waste resources and bring risks if being sent to the CPU.

After defense against invalid ND packets is enabled on a device, the device discards the preceding packets.


#### Configuration and Maintenance Methods

* Delete statistics about the function of defense against invalid ND packet attacks on all interface boards or a specified interface board.
  
  [**reset nd packet filter statistics**](cmdqueryname=reset+nd+packet+filter+statistics) [ **slot** *slot-id* ]

#### Verifying the Security Hardening Result

Check statistics about the function of defense against invalid ND packet attacks on all interface boards or a specified interface board.

[**display nd packet filter statistics**](cmdqueryname=display+nd+packet+filter+statistics) [ **slot** *slot-id* ]


#### Configuration and Maintenance Suggestions

None.