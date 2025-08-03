Regular Expression
==================

Regular_Expression

#### Background

A regular expression defines a string matching mode. It consists of common characters (such as letters from a to z) and special characters (also called metacharacters). The regular expression functions as a template to match a character pattern with the searched character string.

The regular expression provides the following functions:

* Checks and obtains the sub-character string that matches a certain rule in the character string.
* Replaces the character string based on the matching rule.

The common and special characters contained in a regular expression are described as follows:

* Common characters
  
  Common characters are used to match themselves in a string, including all uppercase and lowercase letters, digits, punctuations, and special symbols. For example, "a" matches "a" in "abc", and "@" matches "@" in "xxx@xxx.com".
* Special characters
  
  Special characters, together with common characters, match complicated or special character strings. For example, "^10" matches "10.10.10.1" instead of "2.2.2.2".
  
  [Table 1](#EN-US_CONCEPT_0000001411303466__tab_dc_vrp_cli_cfg_001302) describes special characters and their functions.
  
  **Table 1** Special characters and their functions
  | Special Character | Function | Example |
  | --- | --- | --- |
  | \ | Functions as an escape character, which is used to mark the next character (common or special) as a common character. | "\\*" matches "\*". |
  | ^ | Matches the start position of a string. | "^10" matches "10.10.10.1" instead of "2.2.2.2". |
  | $ | Matches the end position of a string. | "1$" matches "10.10.10.1" instead of "10.10.10.2". |
  | \* | Matches the preceding sub-regular expression zero or multiple times. | "10\*" matches "1", "10", "100", "1000", and so on.  "(10)\*" matches null, "10", "1010", "101010", and so on. |
  | + | Matches the preceding sub-regular expression once or multiple times. | "10+" matches "10", "100", "1000", and so on.  "(10)+" matches "10", "1010", "101010", and so on. |
  | ? | Matches the preceding sub-regular expression once or zero times.  NOTE:  When regular expressions with a question mark (?) are entered on Huawei datacom devices, command help information is displayed. Huawei datacom devices do not support regular expressions with "?". | "10?" matches "1" or "10".  "(10)?" matches null or "10". |
  | . | Matches any single character. | "a.b" matches any three-character string that starts with "a" and ends with "b".  "0.0" matches "0x0", "020", and so on.  ".oo." matches "book", "look", "tool", and so on. |
  | () | Matches a sub-regular expression within the parentheses and obtains the matching result.  If there is no character within the parentheses, the corresponding string is null.  If a pattern string contains only "()", it can match any string.  If the right parenthesis in a pattern string has no matching left parenthesis, the right parenthesis is used as a common character.  If the left parenthesis in a pattern string has no matching right parenthesis, the pattern string is invalid. | "100(200)+" matches "100200", "100200200", and so on.  "(ab)" matches "abcab".  "()" matches any character string.  "a()b" matches "12ab12".  "a)b" matches "za)bc".  "a(b" is an invalid pattern string. |
  | x|y | Matches "x" or "y". | "100|200" matches "100" or "200".  "1(2|3)4" matches "124" or "134", instead of "1234", "14", "1224", or "1334". |
  | [xyz] | Matches any character in a regular expression. It cannot simultaneously match multiple characters or match the same character multiple times. | "[123]" matches "2" in "255".  "[abc]" matches "a", "b", or "c". |
  | [^xyz] | Matches characters excluding "x", "y", and "z" in a character string. That is, if a character string contains characters other than "x", "y", and "z", the characters can be matched. | "[^123]" matches any character except "1", "2", and "3".  "[^abc]" matches any character except "a", "b", and "c". |
  | [a-z] | Matches any character within the specified range. It cannot simultaneously match multiple characters or match the same character multiple times. | "[0-9]" matches any digit in the specified range.  "[a-z]" matches any letter in the specified range.  "[z-a]" is an invalid pattern string. |
  | [^a-d] | Matches all characters except "a", "b", "c", and "d" in a character string. That is, if a character string contains characters beyond the range of "a" to "d", the characters can be matched. | "[^0-9]" matches all non-digit characters.  "[^a-z]" matches any character except letters.  "[^z-a]" is an invalid pattern string. |
  | {x,y} | Matches the preceding sub-regular expression for *x* to *y* times. The values of *x* and *y* must be less than 1000. Otherwise, a compilation error occurs. The larger the values of *x* and *y*, the slower the pattern string compilation.  If there is only one brace (left or right), the brace is regarded as a common character.  If there is only a digit in the braces, the digit indicates the number of times the preceding sub-regular expression is exactly matched.  If there is a digit on the right rather than the left of the comma between the left and right braces, the braces and all the characters between them are regarded as common characters.  If there is a digit on the left rather than the right of the comma between the left and right braces, the digit indicates the minimum number of times the preceding sub-regular expression is matched. In this case, no upper limit exists. | "a{3,5}" matches "aaa", "aaaa", and " aaaaa".  "a{3}" matches "za{3bc".  "a3}" matches "za3}bc".  "ab{3}" matches "abbbc".  "(ab){3}" matches "abababc".  "a{,3}bc" matches "za{,3}bc".  "a{3,}bc" matches "aaabc", "aaaaabc", and so on. |
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Unless otherwise specified, all the characters described in the preceding table must be printable characters.

#### Use of Characters

* Degeneration of special characters
  
  Certain special characters degenerate to common characters when they are placed at certain positions in a regular expression.
  
  + Special characters following the escape character "\" match themselves.
  + The special character "\*", "+", or "?" is placed at the beginning of a regular expression. For example, "+45" matches "+45", and "abc(\*def)" matches "abc\*def".
  + The special character "^" is placed at any position except the beginning of a regular expression. For example, "abc^" matches "abc^".
  + The special character "$" is placed at any position except the end of a regular expression. For example, "12$2" matches "12$2".
  + The right parenthesis ")" or right bracket "]" is not paired with the corresponding left parenthesis "(" or left bracket "[". For example, "abc)" matches "abc)", and "0-9]" matches "0-9]".![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Unless otherwise specified, the preceding degeneration rules also apply to sub-regular expressions within parentheses.
* Combination of common and special characters
  
  In practice, multiple common and special characters are often combined to match a special character string.

#### Filter Criteria for Regular Expressions

For the NE40E, you can specify filter criteria in a command to apply a regular expression. Currently, all **display** commands support regular expressions. When you query information by filter criteria, the first line in the command output begins with information containing the specified character string, instead of with the specified character string.

**| count** can be specified to control the number of lines to be displayed in the command output, and **| no-more** can be specified to disable the command output from being displayed on different screens. **| count** and **| no-more** can be used independently or used with the following filter criteria.

**| ignore-case** can be specified so that the character string is case-insensitive, and **| section** can be specified to control the result section to be displayed in the command output. **| ignore-case** and **| section** must be used with any of the following filter criteria.

The following three filter criteria are provided for commands that support regular expressions.

* **| begin** *regular-expression*
  
  Displays all the lines following the line that matches the specified regular expression. In this case, the system filters out all the character strings until the specified case-sensitive character string is displayed. All the character strings following this specified character string will be displayed on the screen.
* **| exclude** *regular-expression*
  
  Displays all the lines that do not match the specified regular expression. If the character strings to be output do not contain the specified case-sensitive character string, they are displayed on the screen; otherwise, they are filtered out.
* **| include** *regular-expression*
  
  Displays only the lines that match the specified regular expression. If the character strings to be output contain the specified case-sensitive character string, they are displayed on the screen; otherwise, they are filtered out.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The command output can be filtered by multiple filter criteria. The filter criteria take effect in configuration sequence. A maximum of 32 filter criteria can be configured to filter the command output. For example, you can run the following command to display the configuration that contains "ip" but does not contain "address 10.1" or "description".

```
display current-configuration | section include ip | exclude address 10.1 | exclude description
```

Pay attention to the following points when querying information by filter criteria:

* The first line in the command output begins with information containing the specified character string, instead of with the specified character string.
* If a configured command does not take effect, no command output is displayed.

The NE40E can redirect the output of a **display** command to a specified file in either of the following ways:

* **>** *filename*
  
  Exports the output of the **display** command to a specified file. If the target file already exists, the original content of the file is overwritten.
* **>>** *filename*
  
  Appends the output of the **display** command to the end of a specified file, with the original content of the file remaining unchanged.

**| refresh** can be specified to update the query results at a specific interval. The default interval is 5 seconds.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If the interval is too short, CPU usage will increase. As such, set the interval to a proper value.
* If the number of remaining VTY channels is less than four, **| refresh** cannot be specified for a new command. The commands with **| refresh** specified are not affected.
* Only **display** commands support **| refresh**.