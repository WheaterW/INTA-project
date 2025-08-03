display ipv6 nd security nonce
==============================

display ipv6 nd security nonce

Function
--------



The **display ipv6 nd security nonce** command displays the Nonce value of the current secure ND transaction.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd security nonce** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. That is, the Nonce value in the SEND message on the specified interface is displayed. | - |
| *interface-type* *interface-num* | Specifies the type and number of an interface. That is, the Nonce value in the SEND message on the specified interface is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Nonce option contains a random number selected by the sender of a solicitation message. This option prevents replay attacks during packet exchange. For example, a sender sends an NS message carrying the Nonce option and receives an NA message as a response that also carries the Nonce option; the sender verifies the NA message based on the Nonce option.You can run the display ipv6 nd security nonce command to view the Nonce value in an SEND message and the IPv6 address of the peer interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the Nonce value in the SEND message on 100GE 1/0/1.
```
<HUAWEI> display ipv6 nd security nonce 100ge 1/0/1
Total Number of Nonce Entries : 1
--------------------------------------------------------------
Peer Address                                  Nonce Value
--------------------------------------------------------------
FE80::1CA1:5572:34D5:632F                  0x57 22 da 69 01 b3

```

**Table 1** Description of the **display ipv6 nd security nonce** command output
| Item | Description |
| --- | --- |
| Total Number of Nonce Entries | Total number of Nonce entries. |
| Nonce Value | Nonce value in an SEND message. |
| Peer Address | IPv6 address of the peer interface. |