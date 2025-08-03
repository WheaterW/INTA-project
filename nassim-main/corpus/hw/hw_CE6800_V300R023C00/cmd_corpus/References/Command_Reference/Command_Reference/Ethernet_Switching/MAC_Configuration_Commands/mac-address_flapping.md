mac-address flapping
====================

mac-address flapping

Function
--------



The **mac-address flapping detection** command configures global MAC address flapping detection.

The **undo mac-address flapping detection** command disables global MAC address flapping detection.

The **mac-address flapping detection exclude** command configures a whitelist for MAC address flapping detection.

The **undo mac-address flapping detection exclude** command deletes a whitelist for MAC address flapping detection.

The **mac-address flapping aging-time** command sets the aging time of flapping MAC addresses.

The **undo mac-address flapping aging-time** command restores the default aging time of flapping MAC addresses.



By default, global MAC address flapping detection is configured, the security level is medium, the VLAN/BD whitelist for MAC address flapping detection is not configured, and the aging time of flapping MAC addresses is 300 seconds.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**mac-address flapping detection** [ **security-level** { **low** | **middle** | **high** } | **security-threshold** *flapCnt* ]

**mac-address flapping detection exclude vlan** { { *vlan-id1* } [ **to** *vlan-id2* ] } &<1-10>

**mac-address flapping aging-time** *aging-time*

**undo mac-address flapping detection** [ **security-level** { **low** | **middle** | **high** } | **security-threshold** *flapCnt* ]

**undo mac-address flapping detection exclude vlan** { { { *vlan-id1* } [ **to** *vlan-id2* ] } &<1-10> | **all** }

**undo mac-address flapping aging-time**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**mac-address flapping detection exclude bridge-domain** *bd-id1* [ **to** *bd-id2* ]

**undo mac-address flapping detection exclude bridge-domain** { *bd-id1* [ **to** *bd-id2* ] | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **security-level** | Globally enables or disables MAC address flapping detection with a specific security level. | - |
| **low** | Sets the security level of MAC address flapping detection to low. That is, the system considers that MAC address flapping occurs after MAC address flapping occurs 500 times. | - |
| **middle** | Specifies a middle security level for MAC address flapping detection. Specifically, after MAC addresses change for 10 times, the system considers that MAC address flapping occurs. | - |
| **high** | Specifies a high security level for MAC address flapping detection. Specifically, after MAC addresses change for 3 times, the system considers that MAC address flapping occurs. | - |
| **security-threshold** *flapCnt* | Specifies the security threshold for MAC address flapping detection. The system considers that MAC address flapping occurs when a MAC address flaps between interfaces for the specified number of times. | The value is an integer ranging from 3 to 10000. |
| *vlan-id1* | Specifies the start VLAN ID number in the VLAN whitelist. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** | Specifies the range. | - |
| *vlan-id2* | Specifies the end VLAN ID in the VLAN whitelist. If vlanEnd is not specified, only the VLAN specified by vlanBgn is displayed in the whitelist. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **aging-time** *aging-time* | Specified the aging period of MAC address flapping entries. | The value is an integer ranging from 60 to 900 seconds. |
| **all** | Deletes all VLANs where MAC address flapping detection is performed from the whitelist. | - |
| *bd-id1* | Specifies the start BD ID in a BD whitelist.  The parameter bridge-domain is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 16777215. |
| *bd-id2* | Specifies the end BD ID in a BD whitelist. If <bd-id2> is not specified, the whitelist contains only the BD specified by <bd-id1>.  The parameter bridge-domain is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 16777215. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

* MAC address flapping occurs when a MAC address learned by an interface is also learned by another interface in the same broadcast domain. The MAC address entry learned later overwrites the original one. To detect MAC address flapping, run the **mac-address flapping aging-time** command to change the aging time of flapping MAC address entries.
* MAC address flapping may be caused by the following reasons:
  + The network cable of the switching device is incorrectly connected or there is an incorrect configuration, forming a ring network.
  + Some unauthorized users launch MAC address attacks on the network.
* Global MAC address flapping detection can detect MAC address flapping on a device. If MAC address flapping occurs, the device reports a trap to the NMS. You can locate the fault according to the trap information. You can also run the **display mac-address flapping** command to view MAC address flapping records.
* By default, the system performs MAC address flapping detection in all broadcast domains on a switching device. In some scenarios, for example, when a switching device is connected to a load balancing server with two network adapters, the MAC address of the server may be learned by two interfaces. In this case, MAC address flapping does not need to be detected. To achieve this, you can run the **mac-address flapping detection exclude** command to add the broadcast domain where the server resides to the MAC address flapping detection whitelist so that MAC address flapping detection is not performed in this broadcast domain. After the configuration is complete, MAC address flapping in the broadcast domain is not reported to the NMS or displayed in the MAC address flapping history.

Example
-------

# Disable MAC address flapping detection in VLAN 5.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping detection exclude vlan 5

```

# Enable MAC address flapping detection with a middle security level.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping detection security-level middle

```

# Set the security threshold for MAC address flapping detection.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping detection security-threshold 200

```

# Disable MAC address flapping detection in BDs 5 to 10.
```
<HUAWEI> system-view
[~HUAWEI] mac-address flapping detection exclude bridge-domain 5 to 10

```