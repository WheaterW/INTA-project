Verifying the Configuration of BFD for IPv4 PIM
===============================================

After configuring BFD for IPv4 PIM, verify information about BFD for IPv4 PIM sessions.

#### Procedure

* Run the following commands to check information about a BFD for IPv4 PIM session:
  
  
  + [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **bfd** **session** **statistics**
  + [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **bfd** **session** [ **interface** *interface-type* *interface-number* | **neighbor** *neighbor-address* ] \*