Regular Expressions
===================

Regular Expressions

#### Context

A regular expression is a mode matching tool that consists of common characters (such as letters from a to z) and special characters (also called meta-characters). It functions as a template to match a character pattern with the searched character string.

A regular expression provides the following functions:

* Checks and obtains the sub-character string that matches a certain rule in the character string.
* Replaces the character string based on the matching rule.

A regular expression consists of the following characters:

* Common characters
  
  Common characters match themselves in a string. Common characters include all uppercase and lowercase letters, digits, punctuations, and special characters. For example, a matches the letter "a" in "abc", 10 matches the digits "10" in "10.113.25.155", and @ matches the symbol "@" in "xxx@xxx.com".
* Special characters
  
  Special characters, together with common characters, match complicated or special character strings. [Table 1](#EN-US_CONCEPT_0000001564130569__tab_dc_cfg_cli_001802) describes special characters and their functions.
  
  **Table 1** Special characters and their functions
  | Special Character | Function | Example |
  | --- | --- | --- |
  | \ | Defines an escape character. It converts a special or common character next to it into a common character. | \\* matches \*. |
  | ^ | Matches the start of the string. | ^10 matches 10.10.10.1 instead of 172.16.1.1. |
  | $ | Matches the end of the string. | 1$ matches 10.10.10.1 instead of 10.10.10.2. |
  | \* | Matches a sub-regular expression that it follows for zero or multiple times. | 10\* matches 1, 10, 100, 1000, and so on.  (10)\* matches null, 10, 1010, 101010, and so on. |
  | + | Matches a sub-regular expression that it follows once or for multiple times. | 10+ matches 10, 100, 1000, and so on.  (10)+ matches 10, 1010, 101010, and so on. |
  | ? | Matches a sub-regular expression that it follows for zero times or once.  NOTE:  When regular expressions with a question mark (?) are entered on Huawei datacom devices, the command help information is displayed. However, if the command output is displayed on more than one screen and filter criteria followed by a question mark (?) are entered, this question mark is considered a special character of a regular expression. | 10? matches 1 or 10.  (10)? matches null or 10. |
  | . | Matches any single character. | a.b matches any string of three characters that starts with a and ends with b.  0.0 matches 0x0, 020, and so on.  .oo matches book, look, tool, and so on. |
  | () | Matches and obtains a sub-regular expression within the parentheses.  If there is no value within the parentheses, the string is equivalent to a null string.  If a pattern string has only (), it can match any string.  If the right parenthesis in a pattern string has no matching left parenthesis, the right parenthesis is used as a common character.  If the left parenthesis in a pattern string has no matching right parenthesis, the pattern string is invalid. | 100(200)+ matches 100200, 100200200, and so on.  (ab) matches abcab.  () can match any string.  a()b matches 12ab12.  a)b matches za)bc.  a(b is an invalid pattern string. |
  | x|y | Matches x or y. | 100|200 matches 100 or 200.  1(2|3)4 matches 124 or 134, rather than 1234, 14, 1224, and 1334. |
  | [xyz] | Matches any character contained in a regular expression. It cannot simultaneously match multiple characters or match the same character multiple times. | [123] matches 2 in 255.  [abc] matches characters a, b, and c. |
  | [^xyz] | Matches characters excluding x, y, and z in a character string. That is, it matches any string with at least one character that is not x, y, or z. | [^123] matches any character except 1, 2, and 3.  [^abc] matches any character except a, b, and c. |
  | [a-z] | Matches any character within a specified range. It cannot simultaneously match multiple characters or match the same character multiple times. | [0-9] matches any digit within the range of 0 to 9.  [a-z] matches any letter from a to z.  [z-a] is an invalid pattern string. |
  | [^a-d] | Matches all characters except a, b, c, and d in a character string. That is, it matches any string with at least one character that is beyond the range of a to d. | [^0-9] matches all non-digit characters.  [^a-z] matches all non-letter characters.  [^z-a] is an invalid pattern string. |
  
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  Unless otherwise specified, all the characters in the preceding table must be printable characters.

#### Use of Characters

Certain special characters, when placed at certain positions in a regular expression, degenerate to common characters.

* The special characters following escape character \ match themselves.
* Special characters \* and + placed at the beginning of a regular expression. For example, +45 matches "+45" and abc(\*def) matches "abc\*def".
* Special character ^ placed in a non-start position of a regular expression. For example, abc^ matches "abc^".
* Special character $ placed in a non-end position of a regular expression. For example, 12$2 matches "12$2".
* A right parenthesis ) or right bracket ] alone. For example, abc) matches "abc)" and 0-9] matches "0-9]".

![](public_sys-resources/note_3.0-en-us.png) 

Unless otherwise specified, degeneration rules also apply when the preceding regular expressions are sub-regular expressions within parentheses.

* Combination of common and special characters
  
  In actual usage, regular expressions combine multiple common and special characters to match certain strings.

#### Filter Modes of Regular Expressions

![](public_sys-resources/note_3.0-en-us.png) 

When a character string is used to filter command output information, the first line of the output starts from the line where certain information matches the character string, not from the matched information.

The system allows you to use **| count** to display the number of lines, **| section** to display the command output by section, **| ignore-case** to match a string of case-insensitive characters, and **| no-more** to display filtered output information on only one screen. **| count**, **| section**, **| ignore-case**, and **| no-more** can work together with the following filter modes.

Three filter modes are provided for commands that support regular expressions.

* **| begin** *regular-expression*: displays all the lines beginning with the line that matches the regular expression.
  
  Filter the command output information until the information matches the specified case-sensitive character string is displayed. The output following the certain information that matches the character string will be displayed on the screen.
* **| exclude** *regular-expression*: displays all the lines that do not match the regular expression.
  
  If the character strings to be output do not contain the specified case-sensitive character string, they are displayed on the screen; otherwise, they are filtered.
* **| include** *regular-expression*: displays all the lines that match the regular expression.
  
  If the character strings to be output contain the specified case-sensitive character string, they are displayed on the screen; otherwise, they are filtered.

![](public_sys-resources/note_3.0-en-us.png) 

The value of *regular-expression* is a string of 1 to 255 characters.

The command output can be filtered by multiple regular expressions, which take effect in configuration sequence. A maximum of 32 regular expressions can be configured to filter the command output.

**| section** is used to display only the commands with section information in the output, such as the [**display current-configuration**](cmdqueryname=display+current-configuration) and [**display this**](cmdqueryname=display+this) commands.

The following examples describe how to specify a filter mode in a command.

Example 1: Use the Directory|Files regular expression to filter the [**display pm brief**](cmdqueryname=display+pm+brief) command output.

```
<HUAWEI> display pm brief | exclude Directory|Files 
Statistics Status                   : disable                                                                                       
Statistics Start Time               : -                                                                                             
Current Statistics Cycles           : -                                                                                             
Number of Statistics Tasks          : 0                                                                                             
Number of Statistics Objects        : 0                                                                                             
Number of Configured Pm Servers     : 0 
```

Example 2: Use the vlan regular expression to filter the [**display current-configuration**](cmdqueryname=display+current-configuration) command output.

```
<HUAWEI> display current-configuration | include vlan
vlan batch 7 10 18 to 19 30 60 66 70 77 100 105
vlan batch 200 1024
 port default vlan 77
 port default vlan 19
 port hybrid pvid vlan 10
 port hybrid untagged vlan 10
 port hybrid pvid vlan 60
 undo port hybrid vlan 1
 port hybrid tagged vlan 60
 port trunk allow-pass vlan 60
 port hybrid pvid vlan 10
 port hybrid tagged vlan 7
 port hybrid untagged vlan 10
```

Example 3: Use the vlan regular expression to filter the [**display current-configuration**](cmdqueryname=display+current-configuration) command output.

```
<HUAWEI> display current-configuration | include vlan | count
Total lines: 14.
```
![](public_sys-resources/note_3.0-en-us.png) 

The preceding information is used for reference only.


You can save the **display** command output to a specified file on devices in either of the following ways:

* **>** *filename*
  
  The output is saved to a specified file. If the target file already exists, the original content of the file is overwritten.
* **>>** *filename*
  
  The output is appended to a specified file, and the original content of the file remains unchanged.