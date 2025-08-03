Verifying the MP Configuration
==============================

After configuring the Multilink Point-to-Point Protocol (MP), verify the configuration.

#### Prerequisites

MP has been configured.


#### Procedure

* Run the [**display interface mp-group**](cmdqueryname=display+interface+mp-group) [ *number* ] command to check the status of and traffic statistics on an MP-Group interface.
* Run the [**display ppp mp**](cmdqueryname=display+ppp+mp) [ **interface** *interface-type* *interface-number* ] command to check information about member interfaces of an MP-Group interface and statistics about the packets sent and received by the MP-Group interface.
* Run the [**display ppp error-packet**](cmdqueryname=display+ppp+error-packet)  *interface-type* *interface-number* command to check statistics about error packets received by a Point-to-Point Protocol (PPP) interface.
* Run the [**display time-delay-detect status**](cmdqueryname=display+time-delay-detect+status) command to check the transmission delays of MP-Group member links.