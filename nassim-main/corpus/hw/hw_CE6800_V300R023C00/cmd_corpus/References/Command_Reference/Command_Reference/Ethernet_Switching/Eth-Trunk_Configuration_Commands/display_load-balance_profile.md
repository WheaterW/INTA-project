display load-balance profile
============================

display load-balance profile

Function
--------



The **display load-balance profile** command displays detailed information about a specified load balancing profile.




Format
------

**display load-balance profile** [ *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a load balancing profile. | The value is a string of 1 to 31 case-sensitive characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After a load balancing profile is configured, you can run the display load-balancing command to view information about the profile, including the load balancing settings for IP packets and Layer 2 packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the load balancing profile on the CE6866, CE6866K, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM and CE8851K.
```
<HUAWEI> display load-balance profile
Load-balance Profile: default
Packet    HashField
---------------------------------------------------
IP             session-id      dst-qp
               src-ip          dst-ip
               l4-src-port     l4-dst-port
L2             src-mac         dst-mac
               vlan
MPLS           top-label       2nd-label
Eth-Trunk      hash-mode(1)    seed(1)
Tunnel         outer-header
Mac-In-Mac     outer-header
Interface List:
---------------------------------------------------
Eth-Trunk 1

```

# Display detailed information about the load balancing profile on the CE8855, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, CE6885-SAN, and CE6885-LL in low latency mode.
```
<HUAWEI> display load-balance profile
Load-balance Profile: default
Packet    HashField
---------------------------------------------------
IP             dst-ip
L2             src-mac         dst-mac
               vlan
MPLS           top-label       2nd-label
Eth-Trunk      hash-mode(1)    seed(1)
               Universal_id(1)
Tunnel         outer-header
Mac-In-Mac     outer-header
Interface List:
---------------------------------------------------
Eth-Trunk 1

```

# Display information about the load balancing profile on the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H and CE6881H-K.
```
<HUAWEI> display load-balance profile
2023-01-16 11:49:49.92
Load-balance Profile: default
Packet    HashField
---------------------------------------------------
IP             src-ip          dst-ip 
IPv6           src-ip          dst-ip
L2             src-mac         dst-mac
MPLS           top-label       2nd-label
Interface List: 
---------------------------------------------------
Eth-Trunk 1

```

**Table 1** Description of the **display load-balance profile** command output
| Item | Description |
| --- | --- |
| Load-balance Profile | Load balancing profile. |
| Packet | Packet type. |
| HashField | Load balancing mode in the load balancing profile. |
| Interface List | Eth-Trunk that uses the load balancing profile. |