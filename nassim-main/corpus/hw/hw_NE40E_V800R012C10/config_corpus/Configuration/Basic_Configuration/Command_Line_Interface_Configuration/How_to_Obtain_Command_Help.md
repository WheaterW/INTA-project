How to Obtain Command Help
==========================

When you enter commands or configure services, command help offers real-time help in addition to the configuration guide.

The CLI on the NE40E provides the following online help.

#### Full Help

You can obtain full help using any of the following methods:

* Enter a question mark (?) in any command view to obtain all the commands and their simple descriptions.
  
  ```
  <HUAWEI> ?
  ```
* Enter a command followed by a space and a question mark (?). If the position of the question mark (?) is for a keyword, all the keywords and their brief description are listed. Use the following command output as an example:
  
  ```
  <HUAWEI> terminal ?
  ```
  ```
    debugging  Enable/disable debug information to terminal  
    logging    Enable/disable log information to terminal
  ```
  
  The words "debugging" and "logging" are keywords, following with their descriptions.
* Enter a command followed by a space and a question mark (?). If the position of the question mark (?) is for a parameter, the value range and function of the parameter are listed. Use the following command output as an example:
  
  ```
  [*HUAWEI] ftp timeout ?
  ```
  ```
    INTEGER<1-35791>  The value of FTP timeout, the default value is 10 minutes
  ```
  ```
  [*HUAWEI] ftp timeout 35 ?
  ```
  ```
  <cr>                    
  ```
  
  In the command output, "INTEGER<1-35791>" indicates the value range, and "The value of FTP timeout, the default value is 10 minutes" is the brief description of the parameter function. "<cr>" indicates that no parameter is in the position. In this case, press **Enter** to run the command.

#### Partial Help

You can obtain partial help using any of the following methods:

* Enter a string followed by a question mark (?). The system lists all the keywords that start with the string.
  
  ```
  <HUAWEI> d?
  ```
  ```
  
    debugging                               delete
    dir                                     display
  
  ```
* Enter a command followed by a question mark (?) if there are several matches for the keyword. The system lists all the keywords that start with the string.
  
  ```
  <HUAWEI> display c?
  ```
  ```
  
    car                                     clock
    configuration                           control-flap
    cpu-defend                              cpu-monitor
    cpu-usage                               current-configuration
  
  ```
* Enter the initial letters of a keyword in a command line and press **Tab**. The system lists the complete keyword. If there are several matches for the keyword, you can press **Tab** repeatedly. The system lists various keywords for you to choose the one you need.