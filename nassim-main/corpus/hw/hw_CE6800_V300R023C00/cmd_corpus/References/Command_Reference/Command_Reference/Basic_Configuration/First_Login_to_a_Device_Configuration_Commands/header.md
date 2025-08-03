header
======

header

Function
--------



The **header** command configures the title contents to be displayed at a login.

The **undo header** command deletes the title contents to be displayed at a login.



By default, no title is displayed if a user logs in.


Format
------

**header login information** *text*

**header login file** *file-name*

**header shell information** *text*

**header shell file** *file-name*

**undo header login**

**undo header shell**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **login** | Displays the title when the terminal connection is activated during the login to the device. | - |
| **file** *file-name* | Specifies the file name used in the title. | The value is a string of 1 to 64 characters without spaces. The size of a title file should be equal to or smaller than 2 KB. For a title file larger than 2 KB, only the contents of the first 2 KB are displayed. |
| *file-name* | Specifies the file name used in the title. | The value is a string of 1 to 64 characters without spaces. The size of a title file should be equal to or smaller than 2 KB. For a title file larger than 2 KB, only the contents of the first 2 KB are displayed. |
| **shell** | Displays the title when a session is set up after the successful login to the device. | - |
| **information** *text* | Specifies the title information. | The value is a string of 1 to 480 characters with spaces supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* To display some prompts or alarms to users, you can configure such information as titles on the device. When a user logs in to the device, the configured titles will be displayed.
* You can use the information <text> parameter to define the title information or use the file <file-name> parameter to configure the content of a specified file as the title information.
* When a terminal connection is activated and a user attempts to log in, the terminal displays the title configured using the header login command. If the user successfully logs in, the terminal displays the title configured using the header shell command.

**Configuration Impact**

If you run the header command several times, the last configuration overrides the previous configuration.After the login title is configured, any user that logs in to the system can view the title.

**Precautions**

* The title text must start and end with the same letter.
* To enter the interactive mode, enter the start delimiter to enter the text editing mode. After the end delimiter is entered, the system automatically exits the interaction process.
* If you do not need to enter the interactive mode, you only need to press Enter after the same letter is displayed at the beginning and end of the text.

Example
-------

# Set the file of the title to header-file.txt, in which the contents are Hello Welcome.
```
<HUAWEI> system-view
[~HUAWEI] header login file flash:/header-file.txt

```

# Set the session creation title to Hello Welcome by using the character h as the start and end characters.
```
<HUAWEI> system-view
[~HUAWEI] header shell information hHello Welcomeh

```