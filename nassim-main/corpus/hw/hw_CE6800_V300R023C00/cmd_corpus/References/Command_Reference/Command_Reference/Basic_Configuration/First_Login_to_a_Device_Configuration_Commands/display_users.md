display users
=============

display users

Function
--------



The **display users** command displays information about each user interface.




Format
------

**display users** [ **all** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about all user interfaces. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If all is not specified in the command, only information about the user interfaces that have established login connections is displayed. If all is specified in the command, information about all user interfaces is displayed, including information about the user interfaces that have not established login connections.After running this command, you can view the access users on the current device, login information such as the user name and address, and authentication and authorization information of the users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Run the display users command on the console interface.
```
<HUAWEI> display users
NOTE:
User-Intf: The absolute number and the relative number of user interface
Authen: Whether the authentication passes
Author: Command line authorization flag
--------------------------------------------------------------------------------
  User-Intf   Delay     Type   Network Address   Authen    Author   Username
--------------------------------------------------------------------------------
  34  VTY 0   16:07:36  TEL    10.135.34.246     pass      yes      huawei_123

  35  VTY 1   00:00:00  TEL    10.135.37.80      pass      yes      huawei_123

  36  VTY 2   24:03:21  TEL    10.135.32.164     pass      yes      huawei_123

* 37  VTY 3   23:33:44  TEL    10.135.23.55      pass      yes      huawei_123

```

**Table 1** Description of the **display users** command output
| Item | Description |
| --- | --- |
| User-Intf | Indicates the absolute number (in the first column) and the relative number (in the second column) of a user interface. |
| Delay | Indicates time elapsed since the last user input, in seconds. |
| Type | Indicates the connection type that can be Telnet, Console, or SSH. |
| Network Address | Indicates the IP address of the host that initiates a connection. |
| Authen | Indicates whether authentication passes. |
| Author | Indicates whether a user is authorized to use a command line:   * yes: indicates that the user is authorized to use the command. * no: indicates that the user is not authorized to use the command. |
| Username | Indicates the name of a user who uses this interface, that is, the login user name. If AAA authentication is not configured, the user name displays Unspecified. |
| \* | Indicates the terminal line in use. |