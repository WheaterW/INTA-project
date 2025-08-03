Maintaining eMDI
================

This section describes how to view or clear eMDI statistics.

#### Usage Scenario

After eMDI detection on video traffic is performed on a device, you can view the eMDI statistics of a specified channel or all channels. To avoid interference from irrelevant records, you can also clear the historical statistics of a specified channel or all channels.


#### Procedure

* Run the [**display emdi statistics history channel**](cmdqueryname=display+emdi+statistics+history+channel) [ *channel-name* ] [ **start** *start-index* **end** *end-index* | **latest-record** *record-number* ] command to view historical statistics about incoming traffic of a specified channel or all channels.
* Run the [**display emdi statistics history outbound channel**](cmdqueryname=display+emdi+statistics+history+outbound+channel) [ *channel-name* ] [ **start** *start-index* **end** *end-index* | **latest-record** *record-number* ] **slot** *slot-id* command to view historical statistics about outgoing traffic of a specified channel or all channels.
* Run the [**display emdi statistics history bier channel**](cmdqueryname=display+emdi+statistics+history+bier+channel) [ **source** *source-address* **group** *group-address* ] [ **start** *start-index* **end** *end-index* | **latest-record** *record-number* ] **slot** *slot-id* command to view historical statistics about incoming traffic of eMDI BIER channels on a specified board.
* Run the [**display emdi statistics history bier outbound channel**](cmdqueryname=display+emdi+statistics+history+bier+outbound+channel) [ **source** *source-address* **group** *group-address* ] [ **start** *start-index* **end** *end-index* | **latest-record** *record-number* ] **slot** *slot-id* command to view historical statistics about outgoing traffic of eMDI BIER channels on a specified board.
* Run the [**reset emdi statistics history channel**](cmdqueryname=reset+emdi+statistics+history+channel) [ *channel-name* ] command to clear historical statistics about incoming traffic of a specified channel or all channels.
* Run the [**reset emdi statistics history outbound channel**](cmdqueryname=reset+emdi+statistics+history+outbound+channel) [ *channel-name* ] **slot** *slot-id* command to clear historical statistics about outgoing traffic of a specified channel or all channels.
* Run the [**reset emdi statistics history bier channel**](cmdqueryname=reset+emdi+statistics+history+bier+channel) [ **source** *source-address* **group** *group-address* ] **slot** *slot-id* command to clear statistics about incoming traffic of eMDI BIER channels on a specified board.
* Run the [**reset emdi statistics history bier outbound channel**](cmdqueryname=reset+emdi+statistics+history+bier+outbound+channel) [ **source** *source-address* **group** *group-address* ] **slot** *slot-id* command to clear statistics about outgoing traffic of eMDI BIER channels on a specified board.