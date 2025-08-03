Configuration Precautions for MPLS-TP OAM
=========================================

Configuration Precautions for MPLS-TP OAM

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Loopback ping does not support bypass PWs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Unidirectional OAM does not support LT. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| LT does not support bypass PWs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The PW service type on the L2 side can only be VLL. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The PW control word must be enabled when MPLS-TP OAM is used to monitor PWs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Penultimate hop popping (PHP) cannot be performed in MPLS-TP OAM scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In MPLS-TP OAM auto-sensing mode, if the interval at which MPLS-TP OAM packets are sent is changed when a link fault is detected, MPLS-TP OAM status negotiation fails after the link recovers. In addition, MPLS-TP OAM reports an interval mismatch alarm after the link recovers.  Suggestions:  1. Do not modify the interval at which MPLS-TP OAM packets are sent when a link fault occurs.  2. Modify the interval at one end first. After the link recovers, run the undo cc send enable and cc send enable commands in sequence to trigger MEP renegotiation on the peer end. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If EOAM Y-1731 packet loss measurement is configured on PWs and MPLS-TP OAM packet loss measurement is configured on LSPs, MPLS-TP OAM packet loss measurement results do not contain PW traffic data. MPLS-TP OAM packet loss measurement results are inaccurate.  Do not configure both EOAM and TPOAM to implement PW packet loss measurement. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If EOAM and MPLS-TP OAM frame loss measurement functions are configured for the same PW, only the later configuration takes effect.  Do not configure both EOAM and MPLS-TP OAM to implement PW frame loss measurement. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MPLS-TP OAM single-ended and dual-ended frame loss measurement does not apply to the scenario where the service to be detected has multiple outbound interfaces and the outbound interfaces reside on different boards or chips. Typical scenarios: Public network load balancing or public network Eth-Trunk interfaces are used. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| TP-OAM/MPLS-OAM does not support RSVP-TE over GRE. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| LB and LT cannot be initiated at the same time on the NMS, and LB and LT of multiple OAM instances cannot be initiated at the same time.  You are advised to properly plan the execution sequence of LB and LT. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| MPLS OAM supports LOCV/Excess/MISMATCH/MISMERGE/UNKNOWN/BDI/OAMFAIL/SD/SF/FDI alarms. SD, SF, and FDI alarms apply only to static bidirectional co-routed TE LSPs. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |