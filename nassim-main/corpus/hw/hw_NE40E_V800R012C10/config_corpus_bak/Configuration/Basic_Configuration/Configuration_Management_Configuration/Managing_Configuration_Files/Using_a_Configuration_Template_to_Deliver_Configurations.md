Using a Configuration Template to Deliver Configurations
========================================================

Configurations in different views may be identical. To simplify the configurations, create a configuration template, define configurations that are duplicate in different views in it, and apply the configuration template to specified views.

#### Context

Configurations in different views may be identical. To simplify the configurations, create a configuration template, define configurations that are duplicate in different views in it, and apply the configuration template to specified views.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**command group**](cmdqueryname=command+group) *group-name*
   
   
   
   A configuration template is created, and the configuration template view is displayed.
3. Run the corresponding service view instance command to access the service view instance to be configured. Use the interface view as an example. Run the [**interface**](cmdqueryname=interface) *interface-group-name* command to associate the loopback interface with the current configuration template.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Regular expressions can be used to run a service view instance command in the configuration template view. For example, run the [**interface**](cmdqueryname=interface) **<Loopback.>** command to associate all loopback interfaces on the device with the current configuration template.
   
   
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
4. Configure data to be delivered. For example, run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6.
5. (Optional) Run [**display this command group candidate merge**](cmdqueryname=display+this+command+group+candidate+merge)
   
   
   
   Configurations in the configuration template are displayed.
6. (Optional) Run [**display this command group candidate**](cmdqueryname=display+this+command+group+candidate)
   
   
   
   Changed configurations in the configuration template are displayed.
7. Run [**end-group**](cmdqueryname=end-group)
   
   
   
   The configuration is committed, and the system view is displayed.
   
   
   
   If the existing configuration template is not needed, run the [**abort**](cmdqueryname=abort) command to discard the existing configuration template and exit the configuration template view.
8. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   Loopback interfaces are created.
9. Run [**apply-command-group**](cmdqueryname=apply-command-group) *group-name* & < 1-8 > in the corresponding interface view
   
   
   
   The configuration template is applied.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After this command is run in a specified service view, the device delivers the command configurations to the corresponding service view instance.
   * Multiple configuration templates can be applied to the same service view instance.
   * This command can be run to apply multiple configuration templates.
   * The configurations in a configuration template cannot be applied to the null interface view.
   
   
   
   If a service view instance does not need configurations in a configuration template, run the [**undo**](cmdqueryname=undo) *command-string* command in the configuration template view to delete the specified service view instance.
   
   If redundant or incorrect configurations exist in a service view instance, access the corresponding instance in the configuration template view and run the [**undo**](cmdqueryname=undo) *command-string* command to delete these configurations.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *command-string* in the [**undo**](cmdqueryname=undo) *command-string* command can only be the service view instance associated with a configuration template and the command that has been run in that service view instance. If a service view instance is deleted, all configurations inherited from the configuration template are also deleted.

#### Follow-up Procedure

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) [ **inheritance** [ **no-comment** ] ] command to check configurations inherited from configuration templates.
* Run the [**display this**](cmdqueryname=display+this) [ **inheritance** [ **no-comment** ] ] command in a specified view to check configurations that the view inherits from configuration templates.
* Run the [**display configuration apply-command-group fail-result**](cmdqueryname=display+configuration+apply-command-group+fail-result) command to check the causes of the latest five configuration template application failures.
* Run the [**display command-group**](cmdqueryname=display+command-group) *groupName* **applied** command to check the number and names of views to which the specified configuration template is applied.