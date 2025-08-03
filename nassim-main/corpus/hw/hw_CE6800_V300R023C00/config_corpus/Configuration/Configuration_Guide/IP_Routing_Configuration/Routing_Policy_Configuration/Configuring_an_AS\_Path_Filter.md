Configuring an AS\_Path Filter
==============================

An AS\_Path filter is used to filter BGP routes by matching against AS\_Path attributes. The AS\_Path attribute records the numbers of all ASs through which a BGP route passes from the local end to the destination in the distance-vector (DV) order. In this case, AS\_Path attribute-based filtering rules can be defined to filter BGP routes.

![](public_sys-resources/note_3.0-en-us.png) 

The AS\_Path filter takes effect only on BGP routes because the AS\_Path attribute is a private attribute of BGP.

#### Introduction to the AS\_Path Filter

As shown in [Figure 1](#EN-US_TASK_0000001130783786__fig12776193754218), the AS\_Path attribute of a BGP route can be considered as a string that may contain spaces. A regular expression can be used to search for matching characters in the AS\_Path attribute.

**Figure 1** AS\_Path attribute of BGP routes  
![](figure/en-us_image_0000001130624000.png)

A regular expression uses a specific string to describe a trait and is used to check whether another string has the trait. The BGP AS\_Path filter defines an AS\_Path-based regular expression and matches it against the AS\_Path attributes of BGP routes to filter these routes.

For example, **ip as-path-filter 1 permit 495** defines AS\_Path filter 1 and the regular expression **495**. This regular expression matches any string that contains **495**.

#### AS\_Path Regular Expression Content

Regular expressions are the core of the AS\_Path filter and their content is complex. This section describes the regular expression content related only to the AS\_Path filter.

Regular expressions are used by the AS\_Path filter to define matching rules. A regular expression consists of the following parts:

* Metacharacter: defines a matching rule.
* Literal character: defines a matching object.

[Table 1](#EN-US_TASK_0000001130783786__table6628143231313) lists the metacharacters that can be used to match BGP AS\_Path attributes.

**Table 1** Metacharacters supported by BGP AS\_Path regular expressions
| Metacharacter | Meaning | Example |
| --- | --- | --- |
| . | Matches any single character (including a space) in an AS\_Path, except "\n". | .\* matches any string in an AS\_Path, which is used to match any route.  NOTE:  After multiple **ip as-path-filter** **deny** clauses are configured to reject matching routes, the **ip as-path-filter** *as-path-filter-name* **permit** .\* command is usually run to permit other routes. |
| \* | Matches a string with zero or multiple consecutive occurrences of a character before the asterisk (\*). | See the preceding example. |
| + | Matches a string with one or multiple consecutive occurrences of a character before the plus sign (+). | 65+ matches the string that begins with 65 and contains a single 5 or multiple occurrences of 5:  * Example of matching strings: 65, 655, 6559, 65259, and 65529 * Examples of unmatching strings: 56, 556, 5669, 55269, and 56259 |
| | | Matches any string with characters on either side of the vertical bar (|). | 100|65002|65003 matches 100, 65002, or 65003. |
| ^ | Matches the string that follows the caret sign (^). | ^65 matches strings beginning with 65:  * Example of matching strings: 65, 651, 6501, and 65001 * Example of unmatching strings: 165, 1650, 6650, and 60065 |
| $ | Matches the string that ends with characters displayed before the dollar sign ($). | 65$ matches strings ending with 65:  * Example of matching strings: 65, 165, 1065, 10065, and 60065 * Example of unmatching strings: 651, 1650, 6650, 60650, and 65001   NOTE:  ^$ matches an empty string (empty AS\_Path) and is usually used to match against locally generated routes. |
| ( ) | Functions as a sub-regular expression to match strings that contain the matching sub-string contained within the parenthesis. | 100(200)+ matches 100200, 100200200, and so on. |
| [ ] | Matches any character in a string or in a specified range defined in square brackets. | [896] matches 8, 9, or 6. [2-4] matches any of 2, 3, or 4, and [0-9] matches any digit in the range of 0 to 9. NOTE:  The value in the square brackets ([]) must be a digit from 0 to 9. For example, to match a number ranging from 735 to 907, use the regular expression of (73[5-9]|7[4-9][0-9]|8[0-9][0-9]|90[0-7]). |
| [^ ] | Matches any character other than the characters listed in the square brackets or any character that is not in the specified range. | [^2-4] matches strings without 2, 3, and 4, and [^0-9] matches strings without digits from 0 to 9.  [^896] matches any character, except 8, 9, and 6. |
| \_ | Matches a sign, such as a comma (,), left brace ({), right brace (}), left parenthesis ((), right parenthesis ()), and space. In addition, the underscore (\_) can be used at the beginning of a regular expression with the same function as the caret sign (^) or at the end of a regular expression with the same function as the dollar sign ($). | * ^65001\_ matches the AS\_Paths that begin with 65001 followed by a symbol. Specifically, ^65001\_ matches AS\_Paths with 65001 as the leftmost AS number (the number of the last AS through which a route passes) and the routes sent by peers in AS 65001. * \_65001\_ matches the strings (AS\_Paths) that contain 65001, which is used to match the routes that pass through AS 65001. * \_65001$ matches the AS\_Paths that end with a sign followed by 65001. Specifically, \_65001$ matches AS\_Paths with 65001 as the rightmost AS number (the number of the first AS through which a route passes), which is used to match the routes that originate in AS 65001. |
| \ | Defines an escape character. | An AS\_Confed\_Sequence contains parentheses (()). The parentheses (()) in regular expressions provide special functions. To match such special characters by removing their special meanings, you can use the backslash (\). For example:  * \(65002\_ matches the AS\_Confed\_Sequences that begin with (65002 followed by a special character. Specifically, \(65002\_ matches AS\_Confed\_Sequences with 65002 as the leftmost AS number (the number of the last AS through which a route passes) and the routes sent by peers in AS 65002. * \(.\*\_65003\_.\*\) matches the AS\_Confed\_Sequence that contains AS number 65003 and the routes that pass through AS 65003 in a BGP confederation. * \_65004\) matches a string that ends with 65004 and with a sign before 65004. That is, the leftmost AS number (start AS) of AS\_Confed\_Sequence is 65004. This string can also be used to match the routes originating from AS 65004 in a BGP confederation and the routes directly advertised by AS 65004 in the BGP confederation.  Similarly, backslashes (\) can be used to remove the special meanings of the left bracket ([) and right bracket (]) used in an AS\_Confed\_Set and the left brace ({) and right brace (}) used in an AS\_Set. |

Multiple rules (each in permit or deny mode) can be specified in an AS\_Path filter. The relationship between theses rules is "OR", which means that if a route meets one of the matching rules, the route matches the AS\_Path filter.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an AS\_Path filter.
   
   
   ```
   [ip as-path-filter](cmdqueryname=ip+as-path-filter) { as-path-filter-number | as-path-filter-name } [ index index-number ] matchMode regular-expression 
   ```
   
   In the preceding command, *regular-expression* defines a matching rule for the AS\_Path filter.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip as-path-filter**](cmdqueryname=display+ip+as-path-filter) [ *as-path-filter-number* | *as-path-filter-name* ] command to check information about the configured AS\_Path filter.