display nqa support-test-type
=============================

display nqa support-test-type

Function
--------



The **display nqa support-test-type** command displays test instance types supported by NQA.




Format
------

**display nqa support-test-type**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view all the test instance types supported by the current device, run the **display nqa support-test-type** command.

* If the command is run on the NQA server, the test instances supported by the server are displayed.
* If the command is run on the NQA client, the test instances supported by the client to be tested are displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the test instance types supported by NQA.
```
<HUAWEI> display nqa support-test-type
NQA support test type information:
----------------------------------------------------
  Type                Description
  tcp                 TCP type NQA test
  jitter              JITTER type NQA test
  icmp                ICMP type NQA test
  trace               TRACE type NQA test
  dns                 DNS type NQA test
  icmpjitter          ICMPJITTER type NQA test

```

**Table 1** Description of the **display nqa support-test-type** command output
| Item | Description |
| --- | --- |
| NQA support test type information | Information of test types that NQA supports. |
| Type | Test instance types supported by NQA. |
| Description | Description of each type of test instance supported by NQA. |