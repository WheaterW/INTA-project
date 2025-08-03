display hotkey
==============

display hotkey

Function
--------



The **display hotkey** command displays the defined, undefined, and reserved shortcut keys.




Format
------

**display hotkey**


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

**Usage Scenario**

After acquiring knowledge of defined, undefined, and reserved shortcut keys, you can use a shortcut key to run a command assigned to this shortcut key, and you can also run the **hotkey** command to assign a command to a shortcut key.You can use a shortcut key as an alternative to a command. After you press a shortcut key, the system displays the complete command associated with the shortcut key. The shortcut key functions the same as the associated command.If no shortcut key is defined for common commands, the NULL operation is performed by default, that is, the entered characters are cleared.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the shortcut keys in use.
```
<HUAWEI> display hotkey
----------------- HOTKEY -----------------
            =Defined hotkeys=
Hotkeys Command
CTRL_G  display current-configuration
CTRL_L  display ip routing-table
CTRL_O  undo debugging all

           =Undefined hotkeys=
Hotkeys Command
CTRL_U  NULL
            =System hotkeys=
Hotkeys Function
CTRL_A  Move the cursor to the beginning of the current line.
CTRL_B  Move the cursor one character left.
CTRL_C  Stop current command function.
CTRL_D  Erase current character.
CTRL_E  Move the cursor to the end of the current line.
CTRL_F  Move the cursor one character right.
CTRL_H  Erase the character left of the cursor.
CTRL_I  Provide a function like the TAB key.
CTRL_J  Provide a function like the Enter key.
CTRL_K  Kill outgoing connection when connecting.
CTRL_M  Provide a function like the Enter key.
CTRL_N  Display the next command from the history buffer.
CTRL_P  Display the previous command from the history buffer.
CTRL_Q  Encoding.
CTRL_R  Redisplay the current line.
CTRL_T  Kill outgoing connection.
CTRL_V  Paste text from the clipboard.
CTRL_W  Delete the word left of the cursor.
CTRL_X  Delete all characters up to the cursor.
CTRL_Y  Delete all characters after the cursor.
CTRL_Z  Return to the user view.
CTRL_]  Kill incoming connection or redirect connection.
ESC_B   Move the cursor one word back.
ESC_D   Delete remainder of word.
ESC_F   Move the cursor forward one word.
ESC_N   Move the cursor down a line.
ESC_P   Move the cursor up a line.
ESC_<   Specify the beginning of clipboard.
ESC_>   Specify the end of clipboard.

```

**Table 1** Description of the **display hotkey** command output
| Item | Description |
| --- | --- |
| HOTKEY | Indicates shortcut keys. |
| CTRL\_G | Displays the current configuration. |
| CTRL\_L | Displays the IP routing table. |
| CTRL\_O | Disables all debugging. |
| CTRL\_U | Undefined. |
| CTRL\_A | Moves the cursor to the beginning of the current line. |
| CTRL\_B | Moves the cursor back one character. |
| CTRL\_C | Stops the running function. |
| CTRL\_D | Deletes the character at the cursor. |
| CTRL\_E | Moves the cursor to the end of the current line. |
| CTRL\_F | Moves the cursor forward one character. |
| CTRL\_H | Deletes the character on the left of the cursor. |
| CTRL\_I | Provides the same function as the Tab key. |
| CTRL\_J | Provides the same function as the Enter key. |
| CTRL\_K | Ends the connections for outgoing calls. |
| CTRL\_M | Provides the same function as the Enter key. |
| CTRL\_N | Displays the next command in the historical command buffer. |
| CTRL\_P | Displays the previous command in the historical command buffer. |
| CTRL\_R | Redisplays information in the current line. |
| CTRL\_T | Ends the connections for outgoing calls. |
| CTRL\_V | Pastes the text of the clipboard. |
| CTRL\_W | Deletes the word on the left of the cursor. |
| CTRL\_X | Deletes all characters on the left of the cursor. |
| CTRL\_Y | Deletes all characters on the right of the cursor. |
| CTRL\_Z | Returns to the user view. |
| ESC\_B | Moves the cursor back one word. |
| ESC\_D | Deletes the word on the right of the cursor. |
| ESC\_F | Moves the cursor forward one word. |
| ESC\_N | Moves the cursor to the next line. |
| ESC\_P | Moves the cursor to the previous line. |
| ESC\_< | Locates the cursor at the start of text in the clipboard. |
| ESC\_> | Locates the cursor at the end of text in the clipboard. |
| CTRL\_Q | Escape. |
| Defined hotkeys | Indicates defined shortcut keys. |
| Undefined hotkeys | Indicates undefined shortcut keys. |
| System hotkeys | Indicates reserved shortcut keys. |
| CTRL\_] | Ends the connections for incoming calls or redirects the connection. |