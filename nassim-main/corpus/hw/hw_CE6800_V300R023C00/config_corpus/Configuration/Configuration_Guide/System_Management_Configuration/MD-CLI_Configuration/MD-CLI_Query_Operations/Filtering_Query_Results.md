Filtering Query Results
=======================

The MD-CLI allows you to use the pipe character (|) or the **grep** command to filter the query result, helping you quickly find the required information.

For example, when you run the **display** command to check information about an interface, you can use the regular expression (that is, specify the filtering rule) to filter the names of all interfaces.

```
[ADMIN@HUAWEI]
MDCLI> display ifm/interfaces | grep '"name":'
      "name": "NULL0",
      "name": "MEth0/0/0",
      "name": "Virtual-if0",
      "name": "LoopBack2147483647",
```

The format of the **grep** command word is as follows:

```
grep TEXT [-A number] [ -B number ] -c -i -q -v
```

[Table 1](#EN-US_TOPIC_0000001564114273__table32447048) describes the filtering options.

**Table 1** grep filtering options and description
| **Filtering Option** | **Filtering Description** |
| --- | --- |
| TEXT | Specifies the content to be matched. The value is a regular expression. |
| -A number | Specifies the number of lines and displays the data in the Number line after the matched content. |
| -B number | Specifies the number of lines and displays the data in the Number line before the matched content. |
| -c | Displays the number of rows in the output result after filtering conditions are used. |
| -i | Specifies that the case is ignored. If this parameter is not specified, the case is exactly matched. |
| -q | Specifies that the command output is not displayed in split-screen mode. |
| -v | Specifies the reverse match for filtering output. |


#### Regular Expression

A regular expression defines a string matching mode. It consists of common characters (such as letters from a to z) and special characters (also called metacharacters). The regular expression functions as a template to match a character pattern with the searched character string.

A regular expression provides the following functions:

* Checks and obtains the substring that matches a certain rule in a character string.
* Replaces the character string based on the matching rule.

A regular expression consists of the following characters:

* Common characters
  
  Common characters match themselves in a string. Common characters include all uppercase and lowercase letters, digits, punctuations, and special characters. For example, a matches the letter "a" in "abc", 10 matches the digits "10" in "10.113.25.155", and @ matches the symbol "@" in "xxx@xxx.com".
* Special characters
  
  Special characters, together with common characters, match complicated or special character strings. [Table 2](#EN-US_TOPIC_0000001564114273__table82631959105920) describes special characters and their functions.
  
  **Table 2** Special characters and their functions
  | Special Character | Function | Example |
  | --- | --- | --- |
  | . | Matches any single character. | a.b can match aab, abb, acb, and so on. |
  | \* | Matches a sub-regular expression that it follows for zero or multiple times. | ab\* can match a, ab, abc, and so on. |
  | \+ | Matches a sub-regular expression that it follows once or multiple times. | ab\+ can match ab, abb, abc, and so on. |
  | ^ | Matches the start position of a string. | ^ab can match abcd but not efab. |
  | $ | Matches the end position of a string. | bc$ can match abc but not abcd. |
  | \(expr\) | The expr expression enclosed by **\(** and **\)** is a subexpression.  If expr is empty, it is equivalent to an empty string and can match any character string.  If **\(** has no pairing **\)** or vice versa, the string is invalid. | \(ab\) matches abcab.  a\(\)b matches abcd.  a\(b or a\)b is an invalid string. |
  | x\|y | Matches x or y. | ab\|ef matches ab or ef. |
  | [xyz] | Matches any character contained in the regular expression. | [abc] matches characters a, b, and c. |
  | [^xyz] | Matches characters other than x, y, and z. | [^abc] matches any characters excluding a, b, and c. |
  | [a-z] | Matches any character within a specified range in the regular expression. | [a-z] matches any lowercase letter within the specified range. |
  | [^a-z] | Matches characters other than a to z in a string. | [^0-9] matches any non-digit character. |
  | ( | Matches a left parenthesis (. | (a can match (abc. |
  | ) | Matches a right parenthesis ). | )a can match )abc. |
  | + | Matches a plus sign +. | a+b can match a+bcd. |
  | | | Matches a pipe |. | a|b can match a|bcd. |
  | \\ | Matches a backslash \. | \\a can match \a. |
  
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  Unless otherwise specified, all the characters described in the preceding table must be printable characters.
  
  + Degeneration of special characters
    
    Certain special characters degenerate to common characters when they are placed at certain positions in a regular expression.
    
    - The special characters following escape character \ match themselves.
    - Special characters \* and + placed at the beginning of a regular expression. For example, +45 matches +45 and abc(\*def) matches abc\*def.
    - Special character ^ placed in a non-start position of a regular expression. For example, abc^ matches abc^.
    - Special character $ placed in a non-end position of a regular expression. For example, 12$2 matches 12$2.
    - A right parenthesis ) or right bracket ] alone. For example, abc) matches abc), and 0-9] matches 0-9].
      
      ![](../public_sys-resources/note_3.0-en-us.png) 
      
      Unless otherwise specified, the preceding degeneration rules also apply to sub-regular expressions within parentheses.
  + Combination of common and special characters
    
    In actual usage, regular expressions combine multiple common and special characters to match certain strings.

#### Example of Matching and Filtering

When no filtering is performed, check the current configuration in the running database in the MEth0/0/0 view.
```
[ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
MDCLI> display this
{
  "name": "MEth0/0/0",
  "class": "main-interface",
  "type": "MEth",
  "number": "0/0/0",
  "admin-status": "up",
  "link-protocol": "ethernet",
  "router-type": "broadcast",
  "clear-ip-df": false,
  "link-up-down-trap-enable": true,
  "statistic-enable": true,
  "statistic-mode": "interface-based",
  "mtu": 1500,
  "spread-mtu-flag": false,
  "vrf-name": "_public_",
  "l2-mode-enable": false,
  "huawei-ip:ipv4": {
    "addresses": {
      "address": [
        {
          "ip": "10.89.68.255",
          "mask": "255.255.254.0",
          "type": "main"
        }
      ]
    }
  },
  "huawei-arp:arp-entry": {
    "expire-time": 1200,
    "probe-interval": 5,
    "probe-times": 3,
    "arp-learn-disable": false,
    "arp-learn-strict": "trust",
    "route-proxy-enable": false,
    "inner-proxy-enable": false,
    "inter-proxy-enable": false,
    "fake-expire-time": 5,
    "probe-unicast": false,
    "dest-mac-check": false,
    "src-mac-check": false,
    "gratuitous-send": "enable",
    "fake-penalty-time": 5,
    "gratuitous-arp-drop": false
  },
  "huawei-lldp:lldp": {
    "session": {
      "admin-status": "tx-rx",
      "tlv-enable": {
        "management-address": true,
        "port-description": true,
        "system-capability": true,
        "system-description": true,
        "system-name": true
      }
    }
  }
}
```

You can specify filter criteria to filter the query results. For example:

* **Matching and filtering example 1**: Check the configuration data in the lines that start with fewer than four spaces (two spaces at the beginning). For example, check the configuration data of the direct subnode in the MEth0/0/0 view.
  ```
  [ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
  MDCLI> display this | grep "    " -v
  {
    "name": "MEth0/0/0",
    "class": "main-interface",
    "type": "MEth",
    "number": "0/0/0",
    "admin-status": "up",
    "link-protocol": "ethernet",
    "router-type": "broadcast",
    "clear-ip-df": false,
    "link-up-down-trap-enable": true,
    "statistic-enable": true,
    "statistic-mode": "interface-based",
    "mtu": 1500,
    "spread-mtu-flag": false,
    "vrf-name": "_public_",
    "l2-mode-enable": false,
    "huawei-ip:ipv4": {
    },
    "huawei-arp:arp-entry": {
    },
    "huawei-lldp:lldp": {
    }
  }
  ```
* **Matching and filtering example 2**: Check the configuration data in the last five lines and the first line of the matching content MEth0/0/0.
  ```
  [ADMIN@HUAWEI]/ifm/interfaces/interface[name="MEth0/0/0"]
  MDCLI> display this | grep MEth0/0/0 -A 5 -B 1
  {
    "name": "MEth0/0/0",
    "class": "main-interface",
    "type": "MEth",
    "number": "0/0/0",
    "admin-status": "up",
    "link-protocol": "ethernet",
  ```