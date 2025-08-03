Editing a Command
=================

The command editing function enables you to edit a command or obtain help using certain keys.

The CLI on an NE40E provides basic command editing functions and supports multi-line editing. Each command can contain a maximum of 3100 characters.

[Table 1](#EN-US_TASK_0172359715__tab_dc_vrp_cli_cfg_001001) describes common editing functions.

**Table 1** Common editing functions
| Key | Function |
| --- | --- |
| Common key | Inserts a character in the place of the cursor and moves the cursor to the right if the editing buffer is not fully occupied. |
| Backspace | Deletes a character before the cursor and moves the cursor to the left. If the cursor reaches the head of the command, the system does not respond. |
| Up cursor key (â) or **Ctrl+P** | Accesses the last historical command or displays the last historical command if there is an earlier historical command. |
| Down cursor key (â) or **Ctrl+N** | Accesses the next historical command or displays the next historical command if there is a later historical command or clears the command if there is no later historical command. |
| **Tab** | Runs partial help after you enter an incomplete keyword and press **Tab**.  * If the keyword matching the entered one is unique, the system replaces the entered one with the complete keyword and displays it in a new line with the cursor a space behind. * If there are several matches or no match at all, the system displays the prefix first. You can press **Tab** to switch from one matching keyword to another. In this case, the cursor closely follows the end of a word and you can press the spacebar and enter the next word. * If you enter an incorrect keyword and press **Tab**, the system directly displays it in a new line. |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

For Windows 9X HyperTerminal, the function provided by the Up cursor key (â) cannot be implemented, because Windows 9X HyperTerminal has defined a different function for the key. You can press **Ctrl+P** to implement the function provided by the key.



#### Follow-up Procedure

A terminal automatically saves typed historical commands, which can be any keyboard entry ending with **Enter**. To view historical commands, run the [**display history-command all-users**](cmdqueryname=display+history-command+all-users) or [**display history-command**](cmdqueryname=display+history-command) command. To delete the historical commands, run the [**reset history-command all-users**](cmdqueryname=reset+history-command+all-users) or [**reset history-command**](cmdqueryname=reset+history-command) command.