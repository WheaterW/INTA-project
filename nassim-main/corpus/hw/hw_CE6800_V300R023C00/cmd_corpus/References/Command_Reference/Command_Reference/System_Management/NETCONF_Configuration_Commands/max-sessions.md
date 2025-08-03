max-sessions
============

max-sessions

Function
--------



The **max-sessions** command sets the maximum number of clients for the NETCONF service.

The **undo max-sessions** command restores the default maximum number of clients that are connected to the server for NETCONF service.



The default maximum number of clients is 15.


Format
------

**max-sessions** *count*

**undo max-sessions**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *count* | Sets the maximum number of NETCONF sessions. | The value is an integer ranging from 0 to 15. The default value is 5. |



Views
-----

NETCONF user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum number of NETCONF clients that can be connected to a server at any point, run the max-sessions command.


Example
-------

# Set the maximum number of NETCONF clients to 3.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] max-sessions 3

```