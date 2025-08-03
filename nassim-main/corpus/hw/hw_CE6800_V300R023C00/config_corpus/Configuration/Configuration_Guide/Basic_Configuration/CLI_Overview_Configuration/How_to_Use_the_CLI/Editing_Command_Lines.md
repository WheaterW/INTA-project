Editing Command Lines
=====================

Editing Command Lines

#### Function Overview

You can edit command lines in a CLI. Each command can contain a maximum of 3100 characters. The keywords in the commands are case insensitive, and whether a command parameter is case sensitive depends on the parameter.

[Table 1](#EN-US_CONCEPT_0000001513170478__tab_dc_cfg_cli_000901) lists keys that are frequently used for editing command lines

**Table 1** Keys for editing command lines
| Key | Function |
| --- | --- |
| Common key | Inserts a character at the current location of the cursor and moves the cursor forward if the editing buffer is not full. Otherwise, an alarm is generated. |
| Backspace | Deletes the character before the cursor and moves the cursor back one character. When the cursor reaches the beginning of the command, an alarm is generated. |
| Left cursor key â or Ctrl+B | Moves the cursor back one character. When the cursor reaches the beginning of the command, an alarm is generated. |
| Right cursor key â or Ctrl+F | Moves the cursor forward one character. When the cursor reaches the end of the command, an alarm is generated. |



#### How to Edit Command Lines

**Incomplete Keyword**

You are not required to enter complete keywords on the device, as long as entered characters can match a unique keyword. This function improves operating efficiency.

If the current input keyword matches multiple commands, you need to type more of the keyword until it can match a unique command. Then the command can be successfully delivered.

For example, to execute the [**display current-configuration**](cmdqueryname=display+current-configuration) command, you can enter **d cu**, **di cu**, or **dis cu**, but you cannot enter **d c** or **dis c** because they do not match unique keywords.

![](public_sys-resources/notice_3.0-en-us.png) 

The maximum length of a command (including an incomplete command) is 3100 characters. If an incomplete command is configured, the system saves this command to the configuration file in its complete format, which may cause the command to have more than 3100 characters. In this case, the incomplete commands cannot be restored after the system restarts. As such, you must pay attention to the length of a command when configuring it in incomplete format.

**Tab**

Enter an incomplete keyword and press **Tab** to complete it.

* When the input matches a unique keyword, the system replaces it with the unique keyword and displays it in a new line with the cursor leaving a space behind. For example:
  1. Enter an incomplete keyword.
     
     ```
     [~HUAWEI] info-
     ```
  2. Press **Tab**.
     
     The system replaces the entered keyword with the complete keyword in a new line with the cursor leaving a space behind.
     ```
     [~HUAWEI] info-center 
     ```
* When the input has multiple matches, press **Tab** repeatedly to display the keywords beginning with the incomplete input one by one until the desired keyword is displayed. In this case, the cursor immediately follows the end of the keyword. For example:
  1. Enter an incomplete keyword.
     
     ```
     [~HUAWEI] info-center log
     ```
  2. Press **Tab**.
     
     The system displays the prefixes of all matched keywords. In this example, the prefix is **log**.
     ```
     [~HUAWEI] info-center log-severity
     ```
     Press **Tab** to switch from one matched keyword to another. In this case, the cursor immediately follows the end of the keyword.
     ```
     [~HUAWEI] info-center logbuffer
     [*HUAWEI] info-center logfile
     [*HUAWEI] info-center loghost
     ```
     
     Stop pressing **Tab** when the desired keyword is displayed.
* When a keyword that matches no command is entered, press **Tab** and the keyword is displayed in a new line without being changed. For example:
  1. Enter an incorrect keyword.
     
     ```
     [~HUAWEI] info-center loglog
     ```
  2. Press **Tab**.
     
     ```
     [~HUAWEI] info-center loglog
     ```
     
     The system displays information in a new line, but the keyword **loglog** remains unchanged and there is no space between the cursor and keyword, indicating that this keyword does not exist.