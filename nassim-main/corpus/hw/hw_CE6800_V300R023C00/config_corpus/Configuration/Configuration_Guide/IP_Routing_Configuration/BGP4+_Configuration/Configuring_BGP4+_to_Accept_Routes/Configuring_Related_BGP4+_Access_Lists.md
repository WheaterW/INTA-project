Configuring Related BGP4+ Access Lists
======================================

Configuring Related BGP4+ Access Lists

#### Context

BGP4+ has two specific access lists, the AS\_Path filter and the community filter. They can be used for checking the BGP4+ running status as well as being used in routing policies.

* AS\_Path filter
  
  An AS\_Path filter is used to filter BGP4+ routes based on the AS\_Path lists they carry. Routes that do not match the filtering conditions will be denied, and you can define multiple rules (permit or deny) for the same filter.
* Community filter
  
  A BGP4+ community attribute is used to identify a group of routes with the same properties. Routes can be classified manually using community attributes, which facilitates route management.

#### Procedure

* Configure an AS\_Path filter.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure an AS\_Path filter.
     
     
     ```
     [ip as-path-filter](cmdqueryname=ip+as-path-filter+index+permit+deny) { as-path-filter-number | as-path-filter-name } [ index index-number ] { permit | deny } regular-expression
     ```
     
     If the [**peer as-path-filter**](cmdqueryname=peer+as-path-filter) command is used to apply a routing policy based on the configured AS\_Path filter to BGP4+ routes, ineligible routes will be filtered out.
     
     AS\_Path filters use regular expressions to define matching rules. which is composed of the following parts:
     
     + Metacharacter: defines a matching rule.
     + Literal character: defines a matching object.
     
     **Table 1** Description of metacharacters
     | Special Character | Function |
     | --- | --- |
     | \ | Defines an escape character, which is used to mark the next character (common or special) as a common character. |
     | ^ | Matches the start position of a string. |
     | $ | Matches the end position of a string. |
     | \* | Matches a sub-regular expression that it follows zero or multiple times. |
     | + | Matches a sub-regular expression that it follows once or multiple times. |
     | ? | Matches a sub-regular expression that it follows once or zero times. |
     | . | Matches any single character. |
     | () | Matches a sub-regular expression within the parentheses, and obtains the matching result. The parentheses can also be empty. |
     | \_ | Matches regular expressions with a sign, such as a comma (,), left brace ({), right brace (}), left parenthesis ((), right parenthesis ()), or space. In addition, the underscore (\_) can be used at the beginning of a regular expression with the same function as the caret sign (^) or at the end of a regular expression with the same function as the dollar sign ($). |
     | x|y | Matches *x* or *y*. |
     | [xyz] | Matches any character contained in a regular expression. |
     | [^xyz] | Matches any character that is not contained in a regular expression. |
     | [a-z] | Matches any character within a specified range in a regular expression. |
     | [^a-z] | Matches any character beyond a specified range. |
     
     For example, ^10 matches only the AS\_Path attribute beginning with 10, with ^ indicating that the beginning of a character string is matched.
     
     Multiple rules (permit or deny) can be specified in a filter, and the relationship between them is OR, which means that a route matches the AS\_Path filter if it meets one of the matching rules.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For details about how to use regular expressions, see *Basic Configuration > CLI Overview.*
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a community filter.
  
  
  
  Community filters are classified as either standard or advanced community filters. The advanced community filter supports regular expressions and is more flexible than the standard community filter.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a community filter.
     
     
     + Configure a standard community filter.
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+basic+index+permit+deny+internet) basic comm-filter-name [ index index-number ] { permit | deny } [ community-number | aa:nn | internet [ strict-match ] | no-export-subconfed | no-advertise | no-export ] &<1-20>
       ```
       
       or
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+index+permit+deny+internet) basic-comm-filter-num [ index index-number ] { permit | deny } [ community-number | aa:nn | internet | no-export-subconfed | no-advertise | no-export ] &<1-20>
       ```
     + Configure an advanced community filter.
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+advanced+index+permit+deny) { advanced comm-filter-name | adv-comm-filter-num } [ index index-number ] { permit | deny } regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a Large-Community filter.
  
  
  
  There are two types of Large-Community filters: basic Large-Community filter and advanced Large-Community filter. Advanced Large-Community filters support regular expressions and are more flexible than basic Large-Community filters.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a Large-Community filter:
     
     
     + Configure a basic Large-Community filter.
       
       ```
       [ip large-community-filter](cmdqueryname=ip+large-community-filter+basic+index+permit+deny) basic large-comm-filter-name [ index index-number ] { permit | deny } { aa:bb:cc } &<1-16>
       ```
     + Configure an advanced Large-Community filter.
       
       ```
       [ip large-community-filter](cmdqueryname=ip+large-community-filter+advanced+index+permit+deny) advanced large-comm-filter-name [ index index-number ] { permit | deny } regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an extended community filter.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Perform either of the following operations as needed to configure an extended community filter.
     
     
     
     Configure a VPN-Target extended community filter:
     
     + Configure a basic VPN-Target extended community filter.
       
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter+basic+index+deny+permit+rt) { basic-extcomm-filter-num | basic basic-extcomm-filter-name }[ index index-number ]  { deny | permit } { rt { as-number:nn | 4as-number:nn | ipv4-address:nn } } &<1-16>
       ```
     + Configure an advanced VPN-Target extended community filter.
       
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter+advanced+index+deny+permit) { advanced-extcomm-filter-num | advanced advanced-extcomm-filter-name }[ index index-number ]  { deny | permit } regular-expression
       ```
     
     Configure an SoO extended community filter:
     
     + Configure a basic SoO extended community filter.
       
       ```
       [ip extcommunity-list soo basic](cmdqueryname=ip+extcommunity-list+soo+basic+index+permit+deny) basic-extcomm-filter-name [ index index-number ] { permit | deny } { site-of-origin } &<1-16>
       ```
     + Configure an advanced SoO extended community filter.
       
       ```
       [ip extcommunity-list soo advanced](cmdqueryname=ip+extcommunity-list+soo+advanced+index+permit+deny) advanced-extcomm-filter-name [ index index-number ] { permit | deny } regular-expression
       ```
     
     Multiple entries can be defined in one extended community filter identified either by a name or number. The relationship between the entries is "OR". This means that if a route matches one of the rules, the route matches the filter.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```