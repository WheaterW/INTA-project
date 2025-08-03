bfd bind link-bundle
====================

bfd bind link-bundle

Function
--------



The **bfd bind link-bundle** command creates a BFD for link-bundle session that detects Eth-Trunk faults and displays the BFD session view.



By default, no BFD for link-bundle session is created.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**bfd** *session-name* **bind** **link-bundle** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ip** *ip-address*

**bfd** *session-name* **bind** **link-bundle** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ip** *ip-address* **unshared-mode**

**bfd** *session-name* **bind** **link-bundle** **compatible-mode** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ip** *ip-address*

**bfd** *session-name* **bind** **link-bundle** **compatible-mode** **peer-ip** *ip-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ip** *ip-address* **unshared-mode**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**bfd** *session-name* **bind** **link-bundle** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ipv6** *ipv6-address*

**bfd** *session-name* **bind** **link-bundle** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ipv6** *ipv6-address* **unshared-mode**

**bfd** *session-name* **bind** **link-bundle** **compatible-mode** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ipv6** *ipv6-address*

**bfd** *session-name* **bind** **link-bundle** **compatible-mode** **peer-ipv6** *ipv6-address* [ **vpn-instance** *vpn-name* ] **interface** { *interface-name* | *interface-type* *interface-number* } **source-ipv6** *ipv6-address* **unshared-mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies·the·name·of·a·BFD·session. | The value is a string of 1 to 64 characters, spaces not supported. When quotation marks are used around the string, spaces are allowed in the string.   * When the name of a BFD session is configured, the uppercase and lowercase letters in the name must be the same as what you enter. * BFD session names are case-insensitive. For example, ABC and abc are regarded as the same BFD session. If you have configured ABC as the name of a BFD session, the ABC BFD session view is directly displayed when you configure abc. |
| **peer-ip** *ip-address* | Specifies the peer IP address bound to a BFD session. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-name* | Specifies the name of a VPN instance bound to a BFD session. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **interface** *interface-type* *interface-number* | Specifies the local interface to which a BFD session is bound. | Eth-Trunk interfaces are supported. |
| **source-ip** *ip-address* | Specifies the source IPv4 address carried in BFD packets. | The value is in dotted decimal notation.  Specifies the source IPv4 address carried in BFD packets. If the source IP address is not specified, the system searches for an outbound interface to the remote IP address in the local routing table. The IP address of this outbound interface is used as the source IP address of BFD packets sent by the local end.  You do not need to set this parameter. When BFD and Unicast Reverse Path Forwarding (URPF) are used together, URPF checks the source IP address of received packets. You need to manually configure the source IP address of BFD packets. |
| **unshared-mode** | Specifies unshared-mode. If this parameter is not configured, the shared mode takes effect. | - |
| **compatible-mode** | Enables a Huawei device to communicate with a non-Huawei device through a BFD session.  By default, UDP port 6784 defined by relevant standards is used. If this parameter is specified, UDP port 3784 is used. | - |
| **peer-ipv6** *ipv6-address* | Specifies the peer IPv6 address bound to a BFD session.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **source-ipv6** *ipv6-address* | Specifies the source IPv6 address carried in a BFD packet.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Two routing devices are connected through a Layer 3 Eth-Trunk interface that has multiple member interfaces. If a single-hop BFD session is bound to the Eth-Trunk interface to detect link faults, the session randomly selects a member interface. When the member interface fails (including link, interface, and board faults), the Eth-Trunk interface is considered faulty. However, the Eth-Trunk status may still be normal at that time. To resolve this issue, you can create a BFD for link-bundle session. A BFD sub-session is created for each Eth-Trunk member interface. The BFD for link-bundle session goes down only when all BFD sub-sessions go down.A BFD for link-bundle session can be created in shared or unshared mode.

* If unshared-mode is specified, a BFD for link-bundle session works in unshared mode. In this mode, a BFD for link-bundle session for detecting faults on a link is independent of a dynamic BFD session for detecting faults on the link. In this case, once a dynamic BFD session detects that an Eth-Trunk member interface fails, the dynamic BFD session may incorrectly go down.
* If unshared-mode is not specified, a BFD for link-bundle session works in shared mode. In this mode, a BFD for link-bundle session for detecting faults on a link is dependent of a dynamic BFD session for detecting faults on the link.

**Prerequisites**

BFD has been globally enabled using the **bfd** command in the system view before using the **bfd bind link-bundle** command.

**Follow-up Procedure**

After a BFD for link-bundle session is created, the system creates a sub-session for each member interface of an Eth-Trunk interface bound to the session to detect faults in each member link. Sub-session discriminators are determined through automatic negotiation, and main session discriminators are generated by the local system. That is, you do not need to configure local or remote discriminators for a BFD for link-bundle session.You can perform any of the following operations as required:

* Run the **min-tx-interval** command to set a desired minimum interval at which BFD packets are sent.
* Run the **min-rx-interval** command to set a desired minimum interval at which BFD packets are received.
* Run the **detect-multiplier** command to set a local detection multiplier for the BFD session.
* Run the **wtr** command to set a WTR time for the BFD session.

**Precautions**

* BFD for link-bundle sessions must be created on both ends of an Eth-Trunk and cannot interwork with other BFD sessions.
* You can run the **undo bfd session-name** command to delete a specified BFD session and cancel the BFD session binding.
* After a BFD for link-bundle session is configured using this command, dynamic sessions for detecting the same link share the BFD for link-bundle session. If the **bfd bind peer-ip auto** command is run to configure a BFD for peer IP auto session and the BFD for peer IP auto session is configured to detect the same link as the BFD for link-bundle session, the BFD for peer IP auto session shares the same session with the BFD for link-bundle session. As a result, the configuration is repeated, therefore, a BFD for link-bundle session and a BFD for peer IP auto session cannot be bound to the same Eth-Trunk interface and IP address at the same time.
* The process-interface-status command is run for BFD for link-bundle sessions by default. The protocol status of the associated interface goes down after the device restarts. After the BFD for link-bundle session goes up or AdminDown, the protocol status of the associated interface goes up. If the interface protocol status is up before the restart, the BFD for link-bundle session cannot go up after the restart. As a result, the interface protocol status before and after the restart is inconsistent.
* When BFD for link-bundle sessions are associated with Eth-Trunk member interfaces, the configurations on both ends must be the same. Otherwise, the BFD session may go down, causing unidirectional communication on the Eth-Trunk and affecting traffic forwarding.

Example
-------

# Create a BFD for link-bundle session named atob to detect Eth-Trunk faults, with the peer IPv4 address set to 10.10.20.2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] ip address 10.10.20.1 24
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] bfd atob bind link-bundle peer-ip 10.10.20.2 interface eth-trunk 1 source-ip 10.10.20.1
[*HUAWEI-bfd-session-atob]

```

# Create a BFD for link-bundle session named atob to detect Eth-Trunk faults, with the peer IPv6 address set to 2001:db8::2.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 address 2001:db8::1 64
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] bfd atob bind link-bundle peer-ipv6 2001:db8::2 interface eth-trunk 1 source-ipv6 2001:db8::1
[*HUAWEI-bfd-session-atob]

```