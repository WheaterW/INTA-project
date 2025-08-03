set-df
======

set-df

Function
--------



The **set-df** command disables packet fragmentation based on the Don't Fragment(DF) bit. After that, the packet will not be fragmented.

The **undo set-df** command enables packet fragmentation.



By default, fragmentation is allowed.


Format
------

**set-df**

**undo set-df**


Parameters
----------

None

Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In path MTU detection, to prevent packet fragmentation, run the **set-df** command. By increasing the packet size, the path MTU is obtained.You can check the path MTU by using a trace test instance as follows:Run the **set-df** command to disable packet fragmentation. Then, run the **datasize** command to set the size of the packet data area. After that, start the test instance. If the test is successful, the size of the sent packet's data area is smaller than the path MTU. Then, keep increasing the packet data area size using the **datasize** command until the test fails. If the test fails, the size of the sent packet's data area is greater than the path MTU.


Example
-------

# Prevent packets sent in the test instance named user test from being fragmented.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type trace
[*HUAWEI-nqa-user-test] set-df

```