shutdown (BFD session view)
===========================

shutdown (BFD session view)

Function
--------



The **shutdown** command shuts down a BFD session. After a BFD session is shut down, the session enters the AdminDown state.

The **undo shutdown** command starts a BFD session.



By default, a BFD session is started.


Format
------

**shutdown**

**undo shutdown**


Parameters
----------

None

Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **shutdown** command to shut down the BFD session that detects a link in the following situations:

* You want to change the configurations of a BFD session. After the successful modification, you must run the **undo shutdown** command to enable the BFD session to detect the link.
* You need to set the BFD session status to AdminDown so that the BFD session is shut down without affecting an upper-layer application.

**Prerequisites**

A BFD session has been created.

**Configuration Impact**

After the **shutdown** command is run for a BFD session, the BFD session enters the AdminDown state.


Example
-------

# Shut down the BFD session named s1.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-s1] shutdown

```