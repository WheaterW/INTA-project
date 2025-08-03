display debugging bfd
=====================

display debugging bfd

Function
--------



The **display debugging bfd** command displays the status of BFD debugging functions.




Format
------

**display debugging bfd**


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

To view whether the BFD debugging functions are enabled, run the **display debugging bfd** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the status of BFD debugging functions.
```
<HUAWEI> display debugging bfd
 BFD process debug switch is on
 BFD timer debug switch is on
 BFD HA debug switch is on
 BFD FSM debug switch is on
 BFD session control management debug switch is on
 BFD error debug switch is on
 BFD message debug switch is on
 BFD sock debug switch is on
 BFD packet debug switch is on
 BFD event debug switch is on

```

**Table 1** Description of the **display debugging bfd** command output
| Item | Description |
| --- | --- |
| BFD event debug switch is on | BFD event debugging was enabled. |
| BFD packet debug switch is on | BFD packet debugging was enabled. |
| BFD sock debug switch is on | BFD socket debugging was enabled. |
| BFD message debug switch is on | BFD message queue debugging was enabled. |
| BFD error debug switch is on | BFD error debugging was enabled. |
| BFD session control management debug switch is on | The debugging of BFD session control management was enabled. |
| BFD FSM debug switch is on | BFD FSM debugging was enabled. |
| BFD HA debug switch is on | BFD HA debugging was enabled. |
| BFD timer debug switch is on | BFD timer debugging was enabled. |
| BFD process debug switch is on | The debugging of BFD processing was enabled. |