display ipv6 nd source-mac statistics
=====================================

display ipv6 nd source-mac statistics

Function
--------



The **display ipv6 nd source-mac statistics** command displays statistics about dropped ND attack messages with fixed source MAC addresses.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 nd source-mac statistics** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specify value of User interface. | - |
| **interface** *interface-type* *interface-num* | Specifies an interface type and number. | The value is a string of 1 to 63 case-insensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check statistics about dropped ND attack messages with fixed source MAC addresses, run the display ipv6 nd source-mac statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about dropped ND attack messages with fixed source MAC addresses.
```
<HUAWEI> display ipv6 nd source-mac statistics
-------------------------------------------------------------------------------------------
SourceMac            Interface         Dropped NS   Dropped NA   Dropped RS   Dropped RA
-------------------------------------------------------------------------------------------
00e0-fc22-1234        100GE1/0/1             36            0            0            0
00e0-fc22-1235        100GE1/0/2             10           20            0           30
-------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display ipv6 nd source-mac statistics** command output
| Item | Description |
| --- | --- |
| SourceMac | Source MAC address of an ND attack entry. |
| Interface | Interface name. |
| Dropped NS | Number of dropped NS messages. |
| Dropped NA | Number of dropped NA messages. |
| Dropped RS | Number of dropped RS messages. |
| Dropped RA | Number of dropped RA messages. |