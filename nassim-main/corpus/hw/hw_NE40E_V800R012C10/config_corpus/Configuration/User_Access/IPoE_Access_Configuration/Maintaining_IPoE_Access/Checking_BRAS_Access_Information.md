Checking BRAS Access Information
================================

This section describes how to check BRAS access information, including user login and logout records as well as related configurations.

#### Context

After configuring BRAS access, run the following **display** commands in any view to check BRAS access configurations.


#### Procedure

1. Run the [**display web-auth-server configuration**](cmdqueryname=display+web-auth-server+configuration) command to check the web authentication server configuration.
2. Run the [**display bas-interface**](cmdqueryname=display+bas-interface) command to check the configuration of all BAS interfaces or a specific one.
3. Run the [**display aaa online-fail-record**](cmdqueryname=display+aaa+online-fail-record) command to check the login failure records.
4. Run the [**display aaa offline-record**](cmdqueryname=display+aaa+offline-record) command to check the logout records.
5. Run the [**display aaa abnormal-offline-record**](cmdqueryname=display+aaa+abnormal-offline-record) command to check the abnormal logout records.
6. Run the [**display call rate**](cmdqueryname=display+call+rate) command to check call put-through rates for all types of users.
7. Run the [**display access-user**](cmdqueryname=display+access-user) command in any view to check information about online users.
   
   
   
   The [**protocol-statistics enable**](cmdqueryname=protocol-statistics+enable) command run in the AAA view enables statistics collection about protocol packets, including ND, PPPoE, PPP, DHCPv4, and DHCPv6 packets.
8. Run the [**display user-flow-statistics**](cmdqueryname=display+user-flow-statistics) [ **domain** *domain-name* ] command in any view to check users' uplink and downlink traffic statistics.
9. Run the [**display access trigger user-table**](cmdqueryname=display+access+trigger+user-table) command in any view to check information about users whose access packets are limited on a board.