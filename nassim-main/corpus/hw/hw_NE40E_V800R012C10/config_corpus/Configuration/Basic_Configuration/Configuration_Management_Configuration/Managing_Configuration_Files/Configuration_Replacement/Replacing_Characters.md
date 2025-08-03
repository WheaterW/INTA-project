Replacing Characters
====================

This section describes how to replace a character string on a device. This function supports batch replacement.

#### Usage Scenario

If a character string or a type of character string on a device does not meet requirements, perform the following steps to replace the string in batches. This function replaces only the character strings in the current view.

This function is supported only in the two-phase configuration validation mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**replace configuration pattern**](cmdqueryname=replace+configuration+pattern) *src-string* **with** *target-string*
   
   
   
   The source character string is replaced with the target character string.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The source character string specified using *src-string* supports regular expressions. You can use a regular expression to specify a type of source character string.
   
   
   **Table 1** Syntax of regular expressions
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
   | \_ | Matches a regular expression with a sign, such as a comma (,), left brace ({), right brace (}), left parenthesis ((), right parenthesis ()), or space. In addition, it can be used at the beginning of a regular expression with the same function as the caret sign (^) or at the end of a regular expression with the same function as the dollar sign ($). | "\_65001\_" matches "20 65001 30", "20 65001", "65001 30", "65001", and so on. |
   | x|y | Matches "x" or "y". | "100|200" matches "100" or "200".  "1(2|3)4" matches "124" or "134", instead of "1234", "14", "1224", or "1334". |
   | [xyz] | Matches any character in a regular expression. It cannot simultaneously match multiple characters or match the same character multiple times. | "[123]" matches "2" in "255".  "[abc]" matches "a", "b", or "c". |
   | [^xyz] | Matches characters excluding "x", "y", and "z" in a character string. That is, if a character string contains characters other than "x", "y", and "z", the characters can be matched. | "[^123]" matches any character except "1", "2" and "3".  "[^abc]" matches any character except "a", "b", and "c". |
   | [a-z] | Matches any character within the specified range. It cannot simultaneously match multiple characters or match the same character multiple times. | "[0-9]" matches any digit in the specified range.  "[a-z]" matches any letter in the specified range.  "[z-a]" is an invalid pattern string. |
   | [^a-d] | Matches all characters except "a", "b", "c", and "d" in a character string. That is, if a character string contains characters beyond the range of "a" to "d", the characters can be matched. | "[^0-9]" matches all non-digit characters.  "[^a-z]" matches any character except letters.  "[^z-a]" is an invalid pattern string. |
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Unless otherwise specified, all the characters described in the preceding table must be printable characters.
3. (Optional) Run [**display configuration candidate**](cmdqueryname=display+configuration+candidate)
   
   
   
   Check whether the post-replacement configurations meet the expectation.
   
   
   
   * If the configurations meet the expectation, go to Step 4.
   * If the configurations do not meet the expectation, run the [**clear configuration candidate**](cmdqueryname=clear+configuration+candidate) command to clear the post-replacement string and perform Step 2 to perform string replacement again.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.