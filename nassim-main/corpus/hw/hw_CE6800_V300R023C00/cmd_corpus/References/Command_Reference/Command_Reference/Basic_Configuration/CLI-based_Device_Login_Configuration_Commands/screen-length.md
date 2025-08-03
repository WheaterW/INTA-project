screen-length
=============

screen-length

Function
--------



The **screen-length** command sets the number of lines to be displayed on a terminal screen.

The **undo screen-length** command restores the default number of lines to be displayed on a terminal screen.



By default, the number of lines to be displayed on a terminal screen is 24.


Format
------

**screen-length** *screen-length*

**undo screen-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *screen-length* | Specifies the number of lines to be displayed on a terminal screen. | The value is an integer ranging from 0 to 512. Value 0 indicates that the split-screen function is disabled. |



Views
-----

VTY-type user interface view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Generally, you do not need to adjust the number of lines displayed on each screen of the terminal. In addition, you are not advised to set the number of lines displayed on each screen to 0. To change the number, run the **screen-length** command. The configuration takes effect after you re-log in to the device.

**Precautions**

* When a user logs in to the device, the system automatically allocates an idle user interface with the smallest number to the user based on the login mode of the user. To ensure that the **screen-length** command takes effect only for the current login user, run the **display users** command to view user login information on all user interfaces. Then, run the **screen-length** command in the specified user interface view to set the number of lines to be displayed on the next screen.
* The number of lines displayed on the terminal is determined by the terminal specifications. For example, the **screen-length** command is used to set the screen length to 30, but the terminal specification is 20. When you press the space bar to pause the screen display, the device sends the information in lines 1 to 30 to the terminal. However, the current screen displays the information in lines 11 to 30. You need to press â or â to view the information in the first 10 lines.
* Only the output of query commands and command help is restricted by the screen height. The output of other information, such as the output of configuration commands, is not restricted by the screen height.

Example
-------

# Set the number of lines in each vty screen of the terminal to 30.
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[~HUAWEI-ui-vty0-4] screen-length 30

```

# Set the number of lines displayed on each screen of the console user interface to 30.
```
<HUAWEI> system-view
[~HUAWEI] user-interface console 0
[~HUAWEI-ui-console0] screen-length 30

```