Example for Using Tab
=====================

You can press **Tab** to enable the system to display associated keywords or check whether the keywords are correct.

#### Networking Requirements

A Router is deployed.


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. If there is only one match for an incomplete keyword, enter the incomplete keyword and press **Tab**.
2. If there are several matches for an incomplete keyword, enter the incomplete keyword and press **Tab** repeatedly until the desired keyword is found.
3. Enter an incorrect keyword and press **Tab**. The incorrect keyword remains unchanged.

The use of **Tab** is described as follows:


#### Procedure

* If There Is Only One Match for an Incomplete keyword
  1. Enter an incomplete keyword.
     
     
     ```
     [~HUAWEI] ip rout
     ```
  2. Press **Tab**s.
     
     
     
     The system replaces the entered keyword with the complete keyword followed by a space.
     
     ```
     [~HUAWEI] ip route-static
     ```
* If There Are Several Matches for an Incomplete keyword
  
  
  
  # The keyword **ip route-static** can be followed by the following keywords:
  
  ```
  [~HUAWEI] ip route-static ?
  ```
  ```
    X.X.X.X             Destination IP address
    bfd                 BFD configuration information
    default-bfd         Default BFD parameter
    default-preference  Preference-value for IPv4 static-routes
  ...
  
  ```
  
  
  1. Enter an incomplete keyword.
     
     
     ```
     [~HUAWEI] ip route-static d
     ```
  2. Press **Tab**.
     
     
     
     The system first displays the prefixes of all the matched keywords. In this example, the prefix is **default**.
     
     ```
     [~HUAWEI] ip route-static default-
     ```
     
     Press **Tab** to switch from one matching keyword to another. The cursor closely follows the end of a word.
     
     ```
     [~HUAWEI] ip route-static default-bfd
     ```
     ```
     [*HUAWEI] ip route-static default-preference
     ```
     
     Stop pressing **Tab** when the desired keyword is found.
  3. Enter the value **10**.
     
     
     ```
     [~HUAWEI] ip route-static default-preference 10
     ```
* If an Incorrect Keyword Is Entered
  1. Enter an incorrect keyword.
     
     
     ```
     [~HUAWEI] ip route-static default-pe
     ```
  2. Press **Tab**.
     
     
     
     The system displays the output in a new line. The entered keyword remains unchanged.
     
     ```
     [~HUAWEI] ip route-static default-pe
     ```

#### Configuration Files

None.