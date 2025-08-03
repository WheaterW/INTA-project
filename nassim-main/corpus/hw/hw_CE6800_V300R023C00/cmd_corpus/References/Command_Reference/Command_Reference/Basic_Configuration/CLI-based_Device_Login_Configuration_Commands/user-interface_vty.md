user-interface vty
==================

user-interface vty

Function
--------



The **user-interface vty** command displays the VTY user interface view. In this view, you can set Telnet and SSH parameters.



By default, there is no user interface view displayed.


Format
------

**user-interface vty** *first-ui-number* [ *last-ui-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *first-ui-number* | Specifies the first user interface to be configured. | The value is an integer that ranges from 0 to 20 . |
| *last-ui-number* | Specifies the last user interface to be configured. The last-ui-number number should be larger than the first-ui-number number.  The maximum values of the last-ui-number and first-ui-number parameters are determined by the maximum login users specified by the user-interface maximum-vty command. For example, if the maximum login users specified by the user-interface maximum-vty 5 command is 5, the maximum value of the last-ui-number and first-ui-number parameters is 4. | The value is an integer ranging from 1 to 20. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enter the VTY user interface view.


Example
-------

# Entering into vty view for updating configuration for vty 0 to vty 4
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0 4
[*HUAWEI-ui-vty0-4]

```

# Entering into vty view for updating vty 0 configuration
```
<HUAWEI> system-view
[~HUAWEI] user-interface vty 0
[*HUAWEI-ui-vty0]

```