display pki cmp statistics
==========================

display pki cmp statistics

Function
--------



The **display pki cmp statistics** command displays the statistics on CMP sessions.




Format
------

**display pki cmp statistics** [ **session** *session-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **session** *session-name* | Specifies the name of a CMP session. | The value must be an existing CMP session name. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays statistics on CMP sessions, including the number of sent IR packets, sent CR packets, sent KUR packets, and received IP packets.If a CMP session is specified, the statistics of the session is displayed. If no CMP session is specified, the statistics of all sessions is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on CMP session test.
```
<HUAWEI> display pki cmp statistics session test
 CMP Context Name: test
 Ir Send Counts        : 0
 Cr Send Counts        : 0
 Kur Send Counts       : 0
 Ir Faild Counts     : 0
 Cr Faild Counts     : 0
 Kur Faild Counts    : 0

```

**Table 1** Description of the **display pki cmp statistics** command output
| Item | Description |
| --- | --- |
| CMP Context Name | Name of the CMP session. |
| Ir Send Counts | Total number of IR packets sent during the session. |
| Ir Faild Counts | Total number of IR failures during the session. |
| Cr Send Counts | Total number of CR packets sent during the session. |
| Cr Faild Counts | Total number of CR failures during the session. |
| Kur Send Counts | Total number of KUR packets sent during the session. |
| Kur Faild Counts | Total number of KUR failures during the session. |