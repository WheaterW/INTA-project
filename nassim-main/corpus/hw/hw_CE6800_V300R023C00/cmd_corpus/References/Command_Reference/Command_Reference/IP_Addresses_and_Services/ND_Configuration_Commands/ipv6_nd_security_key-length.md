ipv6 nd security key-length
===========================

ipv6 nd security key-length

Function
--------



The **ipv6 nd security key-length** command sets a key length that is allowed on an interface.

The **undo ipv6 nd security key-length** command restores the default key length.



By default, the minimum key length is 512 bits and the maximum key length is 3072 bits.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd security key-length** { **minimum** *mini-keylen-value* | **maximum** *max-keylen-value* } \*

**undo ipv6 nd security key-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **minimum** *mini-keylen-value* | Specifies the minimum key length allowed on the interface. | The value is an integer ranging from 384 to 4096, in bits. |
| **maximum** *max-keylen-value* | Specifies the maximum key length allowed on the interface. | The value is an integer ranging from 384 to 4096, in bits. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an interface enabled with the strict security mode receives an ND message, it verifies the RSA key in the ND message to determine whether the ND message is secure. To set a key length that is allowed on an interface, you can run the ipv6 nd security key-length command. If the key length of the received ND message is out of the length range allowed on the interface, the interface regards the ND message insecure and discards it.

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Follow-up Procedure**



Run the **ipv6 nd security strict** command to enable the strict security mode on the interface.




Example
-------

# Set a minimum key length and a maximum key length to 1500 bits and 2000 bits respectively for 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd security key-length minimum 1500 maximum 2000
[*HUAWEI-100GE1/0/1] ipv6 nd security strict

```