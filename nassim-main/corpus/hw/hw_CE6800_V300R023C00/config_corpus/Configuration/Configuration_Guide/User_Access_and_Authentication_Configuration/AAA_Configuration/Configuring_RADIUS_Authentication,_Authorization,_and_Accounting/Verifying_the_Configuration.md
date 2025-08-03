Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to check the AAA summary.
* Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **template** *template-name* ] command to check the RADIUS server template configuration.
* Run the [**display radius-server item**](cmdqueryname=display+radius-server+item) { **ip-address** *ip-address* { **accounting** | **authentication** } | **template** *template-name* } command to check the RADIUS server configuration.
* Run the **[**display radius-server**](cmdqueryname=display+radius-server)** { **dead-interval** | **dead-count** | [**detect-cycle**](cmdqueryname=detect-cycle) } command to check the specified RADIUS server detection interval, number of times the RADIUS server detection interval cycles, and maximum number of consecutive unacknowledged packets.
* Run the [**display radius-server authorization configuration**](cmdqueryname=display+radius-server+authorization+configuration) command to check the RADIUS authorization server configuration.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **name** *attribute-name* | **type** { *attribute-number1* | **huawei** *attribute-number2* | **microsoft** *attribute-number3* | **dslforum** *attribute-number4* } ] command to check the RADIUS attributes supported by the device.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **template** *template-name* ] **disable** command to check the disabled RADIUS attributes.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **template** *template-name* ] **translate** command to check the RADIUS attribute translation configuration.
* Run the [**display radius-server accounting-stop-packet**](cmdqueryname=display+radius-server+accounting-stop-packet) { **all** | **ip** *ip-address* } command to check information about the accounting-stop packets of the RADIUS server.
* Run the **[**display radius-attribute**](cmdqueryname=display+radius-attribute)** [ **template** *template-name* ] **check** command to check the attributes to be checked in RADIUS Access-Accept packets.
* Run the [**display remote-user authen-fail**](cmdqueryname=display+remote-user+authen-fail) [ **blocked** | **username** *username* ] command to check information about the accounts that fail remote AAA authentication.
* Run the **[**display radius-server max-unresponsive-interval**](cmdqueryname=display+radius-server+max-unresponsive-interval)** command to check the maximum period during which the RADIUS server does not respond.