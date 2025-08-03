Binding Service PWs to an mPW
=============================

After service PWs are bound to an mPW, the service PW status is determined by the mPW status.

#### Context

To accelerate PW fault detection, BFD is generally used. If there are a large number of service PWs with the same source and same destination, you can configure an mPW with the same source and same destination as those of the service PWs and associate these service PWs with the mPW. By tracking the status of the mPW, BFD can quickly detect faults on service PWs associated with the mPW. This method does not require BFD to be configured for service PWs, thereby reducing the number of BFD sessions and conserving both system resources and public network link bandwidth.


#### Procedure

1. Configure an mPW.
   1. Run the [**interface loopback**](cmdqueryname=interface+loopback) *loopback-number* command to configure a loopback interface and enter its view.
   2. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* { [ **control-word** | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] \* **admin** | **admin** [ **control-word** | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] ] \* | **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] **admin** **control-word** | **control-word** | **admin** **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] } command to create an mPW.
2. Bind a service PW to the mPW.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view for the service PW.
   2. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) [ **secondary** | **bypass** ] **track** **admin-vc** **interface** *interface-type interface-number* command to bind the service PW to the mPW.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.