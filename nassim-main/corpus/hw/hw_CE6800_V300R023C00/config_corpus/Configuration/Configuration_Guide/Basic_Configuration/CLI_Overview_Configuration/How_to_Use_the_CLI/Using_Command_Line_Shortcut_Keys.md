Using Command Line Shortcut Keys
================================

A device provides command shortcut keys to speed up and simplify command input.

Command shortcut keys are classified into user-defined shortcut keys and system default shortcut keys.

* There are four user-defined shortcut keys: **Ctrl+G**, **Ctrl+L**, **Ctrl+O**, and **Ctrl+U**. A user-defined shortcut key can be associated with any command. After you press a shortcut key, the system will automatically run the command associated with the shortcut key.
* System default shortcut keys: shortcut keys defined in the system that have fixed functions and cannot be defined by users. [Table 1](#EN-US_CONCEPT_0000001564130577__tab_dc_cfg_cli_001401) lists the common system shortcut keys.

![](public_sys-resources/note_3.0-en-us.png) 

The terminal being used may affect the functions of the shortcut keys. For example, if the shortcut keys defined by the terminal conflict with those defined in the device, the shortcut keys entered by the user are identified by the terminal program and the commands corresponding to the shortcut keys are not executed.


#### User-defined Shortcut Keys

If a user frequently uses a specific command or selection of commands, the user can use shortcut keys to define them. Only management-level users have the rights to define shortcut keys. The configurations are as follows:

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a shortcut key for a command.
   ```
   [hotkey](cmdqueryname=hotkey) { CTRL_G | CTRL_L | CTRL_O | CTRL_U } command-text
   ```
   The system supports four user-defined shortcut keys and the default values are as follows:
   * Ctrl+G: [**display current-configuration**](cmdqueryname=display+current-configuration)
   * Ctrl+L: [**display ip routing-table**](cmdqueryname=display+ip+routing-table)
   * Ctrl+O: **undo debugging all**
   * Ctrl+U: Null
3. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

![](public_sys-resources/note_3.0-en-us.png) 

* When defining shortcut keys, use double quotation marks to surround a command that contains several keywords separated by spaces, for example, **hotkey ctrl\_l "display tcp status"**. Do not use double quotation marks to surround a command that contains only one keyword.
* Run the [**display hotkey**](cmdqueryname=display+hotkey) command to view the status of the defined, undefined, and system-defined shortcut keys.
* Run the [**undo hotkey**](cmdqueryname=undo+hotkey) command to restore the default values of the configured shortcut keys.
* Entering shortcut keys is equivalent to command execution. The device records the commands corresponding to the entered shortcut keys in the command buffer and logs for fault detection and query.
* The user-defined shortcut keys are available to all users. However, if a user does not have the rights to use the command defined by a shortcut key, the system displays an error message when the user uses this shortcut key.


#### System-defined Shortcut Keys

**Table 1** System-defined shortcut keys
| Key | Function |
| --- | --- |
| <Ctrl+A> | Moves the cursor to the beginning of the current command line. |
| <Ctrl+B> | Moves the cursor back one character. |
| <Ctrl+C> | Stops performing the current functions. |
| <Ctrl+D> | Deletes the character where the cursor is located. |
| <Ctrl+E> | Moves the cursor to the end of the current command line. |
| <Ctrl+F> | Moves the cursor forward one character. |
| <Ctrl+H> | Deletes the character before the cursor. |
| <Ctrl\_I> | Provides the same function as that of the Tab key. |
| <Ctrl\_J> | Provides the same function as that of the Enter key. |
| <Ctrl+K> | Stops outgoing connections in the call establishment stage. |
| <Ctrl\_M> | Provides the same function as that of the Enter key. |
| <Ctrl+N> | Displays the next command in the history command buffer. |
| <Ctrl+P> | Displays the previous command in the history command buffer. |
| <Ctrl\_Q> | Specifies the escape operation. |
| <Ctrl+R> | Re-displays information about the current command line. |
| <Ctrl+T> | Stops outgoing connections. |
| <Ctrl+V> | Pastes the text of the clipboard. |
| <Ctrl+W> | Deletes the word before the cursor. |
| <Ctrl+X> | Deletes all characters before the cursor. |
| <Ctrl+Y> | Deletes all characters following the cursor and the character where the cursor is located. |
| <Ctrl+Z> | Returns to the user view. |
| <Ctrl+]> | Stops incoming connections or redirects them. |
| <Esc+B> | Moves the cursor back one word. |
| <Esc+D> | Deletes the word following the cursor. |
| <Esc+F> | Moves the cursor forward one word. |
| <Esc+N> | Moves the cursor downwards a line. |
| <Esc+P> | Moves the cursor upwards a line. |
| <Esc+<> | Positions the cursor at the beginning of the text to be copied. |
| <Esc+>> | Positions the cursor at the end of the text to be copied. |