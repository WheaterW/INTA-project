switch md-cli (User view)
=========================

switch md-cli (User view)

Function
--------



The **switch md-cli** command switches the user operation environment from the traditional command line interface (CLI) mode to the MD-CLI mode.




Format
------

**switch md-cli** [ **read-only** ]


Parameters
----------

None

Views
-----

User view


Default Level
-------------

0: Visit level


Usage Guidelines
----------------

MD-CLI is a command line management interface for network devices. The objects accessed by MD-CLI are nodes in the YANG model. In MD-CLI mode, users can access YANG model nodes in the form of directories.After you log in to the device, the traditional command line mode is displayed by default. You can run the **switch md-cli** command to switch the user operation environment to the MD-CLI mode.To switch back to the traditional CLI mode, run the exit command in MD-CLI mode.


Example
-------

# Enter the MDCLI mode in the user view.
```
<HUAWEI> switch md-cli
Username:user1
Password:admin@12345
<ADMIN@HUAWEI>
MDCLI>

```