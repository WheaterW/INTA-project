host interface (iNOF host access interface whitelist view)
==========================================================

host interface (iNOF host access interface whitelist view)

Function
--------



The **host interface** command configures a whitelist of interfaces through which hosts access the iNOF.

The **undo host interface** command deletes interfaces from the iNOF host access interface whitelist.



By default, no interface whitelist is configured for hosts to connect to the iNOF.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**host** *ip-address* [ **to** *ip-address* ] **interface** { *interface-name* | *interface-type* *interface-number* }

**undo host** *ip-address* [ **to** *ip-address* ] **interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a host. | * For IPv4 address, the value is in the decimal format. * For IPv6 address, the value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **to** | Specifies the IP address range of the hosts. | - |
| **interface** | Specifies the interface through which hosts can access the iNOF. | - |
| *interface-name* | Specifies an interface name. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |



Views
-----

iNOF host access interface whitelist view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to configure a whitelist of interfaces through which hosts access the iNOF.

* If the iNOF host access interface whitelist function is disabled, the configured whitelist does not take effect.
* If the iNOF host access interface whitelist function is enabled using the **access-filter enable** command, hosts access to iNOF is restricted based on the configured whitelist information.
  + If a host and its access interface are configured in the whitelist, the host can access the iNOF only through the specified interface.
  + If a host is not configured in the whitelist, the host is denied access to the iNOF.

You can run the **exclude interface** command to configure an exception interface for the iNOF host access interface whitelist. Hosts can access the iNOF through the exception interface without being restricted by the whitelist.

**Precautions**

* Only physical interfaces and Eth-Trunk interfaces can be configured as host access interfaces in the whitelist. If the configured host access interface is an Eth-Trunk interface, the specified host can access the iNOF through a member interface of the Eth-Trunk interface.
* An interface cannot be added to the iNOF host access interface whitelist while being configured as an exception interface of the iNOF host access interface whitelist.
* When a host needs to connect to two devices in the M-LAG and the iNOF host access interface whitelist function is enabled on the two M-LAG devices, you need to run the **host interface** command on both M-LAG devices to specify the IP address of the host to access the iNOF through the M-LAG member interface of the local M-LAG device; alternatively, run the **exclude interface** command on both M-LAG devices to specify an M-LAG member interface as an exception interface of the iNOF host access interface whitelist.
* The IPv4 address of a host cannot be set to a non-class A/B/C or loopback address.
* The IPv6 address of a host cannot be a link-local address, multicast address, unspecified address, or loopback address.

Example
-------

# Configure a whitelist of interfaces through which hosts access the iNOF.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] access-filter
[*HUAWEI-ai-service-inof-access-filter] host 192.168.1.1 to 192.168.1.2 interface 100GE 1/0/1

```