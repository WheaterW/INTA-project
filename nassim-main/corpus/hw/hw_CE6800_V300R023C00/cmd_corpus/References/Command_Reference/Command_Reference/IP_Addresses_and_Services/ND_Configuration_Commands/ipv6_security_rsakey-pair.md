ipv6 security rsakey-pair
=========================

ipv6 security rsakey-pair

Function
--------



The **ipv6 security rsakey-pair** command binds an RSA key pair to an interface.

The **undo ipv6 security rsakey-pair** command unbinds an RSA key pair from an interface.



By default no modifier is configured, an RSA key pair is not bound to any interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 security rsakey-pair** *key-label*

**undo ipv6 security rsakey-pair** *key-label*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-label* | Specifies the name of the RSA key pair. | The value is a string of 1 to 35 case-sensitive characters, spaces not supported. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An RSA key pair can be used to generate a modifier value and a CGA address on an interface only after the **ipv6 security rsakey-pair** command is run to bind the RSA key pair to the interface.After a CGA address is configured for an interface, the ND messages sent by the interface are protected against attacks.

**Prerequisites**

Before running the **ipv6 security rsakey-pair** command, you must complete the following configurations:1.An RSA key pair has been created using the **rsa key-pair label** command in the system view.2.IPv6 has been enabled on an interface using the **ipv6 enable** command in the interface view.

**Follow-up Procedure**

1.Run the **ipv6 security modifier** command in the interface view to configure a modifier value and a security level for the CGA address.2.Run the ipv6 address cga command or the ipv6 address link-local cga command to configure a CGA address.

**Precautions**

The binding between an RSA key pair and an interface cannot be deleted in the following cases:

* A modifier value and a security level are configured on the interface.
* A CGA address is configured on the interface.After the **undo rsa key-pair label** command is run in the system view, the ipv6 security rsakey-pair configuration of the RSA key corresponding to each interface will be deleted.

Example
-------

# Bind a key pair named huawei to Eth-Trunk 1.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair label huawei modulus 2048
[*HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 security rsakey-pair huawei
[*HUAWEI-Eth-Trunk1] ipv6 security modifier sec-level 1
[*HUAWEI-Eth-Trunk1] ipv6 address 2001:db8:1::1/64 cga

```