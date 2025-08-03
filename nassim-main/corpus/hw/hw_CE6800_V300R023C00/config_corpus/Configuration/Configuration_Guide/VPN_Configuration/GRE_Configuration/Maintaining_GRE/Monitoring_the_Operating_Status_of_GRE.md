Monitoring the Operating Status of GRE
======================================

Monitoring the Operating Status of GRE

#### Context

In routine maintenance, you can run GRE-related display commands to check the GRE operating status.


#### Procedure

* Check the operating status of tunnel interfaces.
  
  
  ```
  [display interface tunnel](cmdqueryname=display+interface+tunnel) [ interface-number ]
  ```
* Check whether the two ends of the tunnel can communicate with each other.
  
  
  ```
  [ping](cmdqueryname=ping) [ -a source-ip-address | -vpn-instance vpn-instance-name ] * host
  ```
* Check the numbers of keepalive messages and keepalive response messages sent and received by GRE tunnel interfaces.
  
  
  ```
  [display keepalive packets count](cmdqueryname=display+keepalive+packets+count)
  ```