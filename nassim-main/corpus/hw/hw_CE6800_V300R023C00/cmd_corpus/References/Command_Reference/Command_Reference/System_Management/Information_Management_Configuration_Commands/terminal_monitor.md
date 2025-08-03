terminal monitor
================

terminal monitor

Function
--------



The **terminal monitor** command enables the display of logs, traps, alarm, and debugging information output by information management on the command line terminal.

The **undo terminal monitor** command disables the display of logs, traps, alarm, and debugging information output by information management on the command line terminal.



By default, the console display function is disabled, and the user terminal display function is disabled.


Format
------

**terminal monitor**

**undo terminal monitor**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After running the terminal monitor command, perform one of the following operations as needed:

* To enable the display of log information on the local terminal, run the terminal logging command.
* To disable the display of log information on the local terminal, run the undo terminal logging command.
* To enable the display of debugging information on the local terminal, run the terminal debugging command.
* To disable the display of debugging information on the local terminal, run the undo terminal debugging command.
* To enable the display of alarm information on the local terminal, run the terminal alarm command.
* To disable the display of alarm information on the local terminal, run the undo terminal alarm command.Running the undo terminal monitor command is equivalent to running commands undo terminal debugging, undo terminal logging, and undo terminal alarm. Then logs, alarms, or debugging information are not displayed on the local terminal.By default, terminal debugging is disabled. By default, terminal logging, terminal trapping, and terminal alarm are enabled.


Example
-------

# Enable the display of logs, traps, and debugging information on the command line terminal.
```
<HUAWEI> terminal monitor

```