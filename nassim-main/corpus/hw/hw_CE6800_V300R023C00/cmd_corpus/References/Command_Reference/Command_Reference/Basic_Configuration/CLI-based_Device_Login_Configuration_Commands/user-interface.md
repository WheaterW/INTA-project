user-interface
==============

user-interface

Function
--------



The **user-interface** command displays the console user interface view.



By default, there is no user interface view displayed.


Format
------

**user-interface** { *ui-type* | **console** *first-ui-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ui-type* | Specifies the type of user interface. | The value of ui-type can be console0. |
| **console** | Specifies to display the Console user interface view. | - |
| *first-ui-number* | Specifies the first user interface to be configured. | If the value of ui-type is console, the value of first-ui-number is 0. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a network administrator uses Telnet or SSH to log in to a device or logs in to a device through the console port, the system assigns a corresponding idle user interface with the smallest absolute or relative number for the network administrator to manage and monitor sessions between users and the device. One user interface corresponds to one user interface view. In a user interface view, the network administrator can set a range of parameters to specify whether login authentication is required, the level of a user after login, and other attributes. These parameter settings apply to all users logging in through this user interface, allowing user sessions to be managed in a centralized manner.

**Prerequisites**

* If you log in through the console port, ensure that a PC and an RS-232 cable have been prepared and a terminal emulation program has been installed on the PC.
* If you log in using Telnet or SSH, ensure that your PC can communicate with the device.

**Precautions**

After logging in to the device as a network administrator, run the **display user-interface** command to view user interfaces currently supported and the absolute and relative numbers of these user interfaces.


Example
-------

# Enter the user interface console 0 view.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0]

```