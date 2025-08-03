display ipv6 nd security timestamp
==================================

display ipv6 nd security timestamp

Function
--------



The **display ipv6 nd security timestamp** command displays the time stamp value of the last received and accepted SEND message (RDlast) and the local time at which the last SEND message for this peer is accepted (TSlast). The receiver records the two time values after receiving an SEND message.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd security timestamp** { *interface-name* | *interface-type* *interface-num* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. That is, the RDlast and the TSlast values of the SEND message on the specified interface is displayed. | - |
| *interface-type* *interface-num* | Specifies the type and the number of an interface. That is, the RDlast and the TSlast values of the SEND message on the specified interface is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display **ipv6 nd security timestamp** command to view the RDlast and the TSlast values of an SEND message on an interface. Then, you can determine whether the difference between the receive time and the send time of the SEND message is out of the allowed time range based on the following formula.

* When a message is received from a new peer:-delta-value TSlast + (RDnew - RDlast) x (1 - drift-value) - fuzz-value
* delta-value, drift-value, and fuzz-value: parameters in the **ipv6 nd security timestamp** command
* RDnew: the local time at which the new SEND message is received
* RDlast: the local time at which the last SEND message for this peer is accepted
* TSnew: the timestamp value present in the new received SEND message (the time is recorded by the sender in the Timestamp option in the newly sent ND message)
* TSlast: the timestamp value of the last received and accepted SEND message (the time is recorded by the sender in the Timestamp option in the last sent ND message)

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command in the interface view.

**Follow-up Procedure**

Run the **ipv6 nd security strict** command to enable the strict security mode on the interface.

**Precautions**



If no neighbor relationship is set up or no SEND message is transmitted between a local interface and a remote interface, running the display **ipv6 nd security timestamp** command does not display any command output.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the RDlast and the TSlast values of an SEND message.
```
<HUAWEI> display ipv6 nd security timestamp 100ge 1/0/1
Total Number of Timestamp Entries : 2
Peer Address : FE80::1812:16D1:319F:B44F
TSlast       : 4c209e350000
RDlast       : 4c209e350000
                             
Peer Address : FE80::3066:6FC:B4D7:5891
TSlast       : 4c209e360000
RDlast       : 4c209e360000

```

**Table 1** Description of the **display ipv6 nd security timestamp** command output
| Item | Description |
| --- | --- |
| Total Number of Timestamp Entries | Total number of timestamp entries. |
| Peer Address | IPv6 address of a peer interface. |
| TSlast | Timestamp value of the last received and accepted SEND message. |
| RDlast | Local time at which the last SEND message for this peer is accepted, converted into seconds elapsed since 0:00:00 January 1, 1970 Coordinated Universal Time (UTC). |