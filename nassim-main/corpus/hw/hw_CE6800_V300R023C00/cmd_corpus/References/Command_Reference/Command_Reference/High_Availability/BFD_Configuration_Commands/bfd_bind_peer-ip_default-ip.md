bfd bind peer-ip default-ip
===========================

bfd bind peer-ip default-ip

Function
--------



The **bfd bind peer-ip default-ip** command creates a multicast BFD session.



By default, no multicast BFD session is created.


Format
------

**bfd** *sessname-value* **bind** **peer-ip** **default-ip** **interface** { *interface-name* | *interface-type* *interface-number* } [ **source-ip** *source-ip* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *sessname-value* | Specifies·the·name·of·a·BFD·session. | The value is a string of 1 to 64 case-insensitive characters. It cannot contain spaces. |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the local interface to which a BFD session is bound. | - |
| **source-ip** *source-ip* | Specifies the source IPv4 address carried in BFD packets. | The value is in dotted decimal notation. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A BFD session is established to rapidly detect link faults. If the physical status of a link is to be monitored and the peer IP address is unavailable (for example, when no peer IP address exists on an Eth-Trunk member link), the **bfd bind peer-ip default-ip** command can be used to create a BFD session to monitor the physical status.If the source IP address is configured for the interface whose physical status is to be monitored by BFD, BFD packets are correctly forwarded after URPF has been enabled. The source-ip parameter must be configured correctly because the system checks only the validity of the source IP address. A multicast or broadcast address is an invalid source IP address.



**Prerequisites**

BFD has been enabled globally using the **bfd** command in the system view.

**Precautions**

* BFD sessions monitor bidirectional links. Therefore, the command must be configured on both ends of a link.
* After a BFD session is created:If you change the source IP address of outbound interface during session negotiation, the source IP address in BFD packets is also changed.If you change the source IP address of outbound interface during session detection, the source IP address in BFD packets is not changed.
* If multicast BFD for 1:1 Eth-Trunk members has been configured and the **process-pst** command has been run, you must run the **process-interface-status** command to ensure that the interface states detected on the forwarding and control planes are the same. Otherwise, run only the **process-interface-status** command.
* When BFD sessions are enabled with the **process-interface-status** command and associated with Eth-Trunk member interfaces, the configurations on both ends must be the same. Otherwise, the BFD session may go down, causing unidirectional communication on the Eth-Trunk and affecting traffic forwarding.


Example
-------

# Create a BFD session named atob and use it to detect faults in a single-hop link on.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd atob bind peer-ip default-ip interface 100GE 1/0/1

```