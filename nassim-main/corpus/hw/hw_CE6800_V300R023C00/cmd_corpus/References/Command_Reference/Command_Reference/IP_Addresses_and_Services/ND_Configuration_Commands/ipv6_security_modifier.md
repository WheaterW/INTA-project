ipv6 security modifier
======================

ipv6 security modifier

Function
--------



The **ipv6 security modifier** command sets a modifier value and a security level for a CGA address.

The **undo ipv6 security modifier** command deletes the modifier value and security level of a CGA address.



By default no modifier is configured, Security level is set to 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 security modifier sec-level** *sec-value* [ *modifier-value* ]

**undo ipv6 security modifier**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *modifier-value* | Specifies the modifier value of the CGA address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **sec-level** *sec-value* | Specifies the security level of the CGA address. | The value is an integer that can be 0 or 1.  1 indicates the highest security level. If the security level is 1, the modifier value will be automatically generated. The modifier value can be manually configured only when the security level of the CGA address is 0. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring a CGA address, you need to run the **ipv6 security modifier** command to set a modifier value and a security level for the CGA address. A CGA address is calculated by using a specific algorithm based on the public key, modifier value, and security level. The higher the security level, the more secure the generated CGA address.After a CGA address is configured for an interface, the ND messages sent by the interface are protected against attacks.

**Prerequisites**

Before running the **ipv6 security modifier** command, you must complete the following configurations:1.Run the **rsa key-pair label** command in the system view to create an RSA key pair.2.Run the **ipv6 enable** command in the interface view to enable IPv6 on the interface.3.Run the **ipv6 security rsakey-pair** command in the interface view to bind the created RSA key pair to the interface.

**Configuration Impact**

If a modifier value and a security level have already been configured on an interface, the binding between the RSA key pair and the interface cannot be deleted.

**Follow-up Procedure**

Run the ipv6 address cga command or the ipv6 address ipv6-address link-local [ cga ] command to configure a CGA address.

**Precautions**

If a CGA address has been configured on an interface, the modifier value and security level of the CGA address cannot be deleted.After the **undo rsa key-pair label label-name** command is run in the system view, the ipv6 security modifier configuration of the RSA key corresponding to each interface will be deleted.


Example
-------

# Configure a modifier value and a security level for the CGA address on Eth-Trunk1.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair label huawei modulus 2048
[*HUAWEI] interface Eth-Trunk1
[*HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 security rsakey-pair huawei
[*HUAWEI-Eth-Trunk1] ipv6 security modifier sec-level 1
[*HUAWEI-Eth-Trunk1] ipv6 address 2001:db8:1::1/64 cga

```