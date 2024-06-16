# `tracking_checker`

## Description
The tool is intended to check the presence of particular cookies on websites.
It collects affiliate links one by one from _campaign_list.py_ file and run _context_processor_ script in Chrome browser.
The results are stored in 2 files: _run_results_ (contains all data) and _error_results_ (contains failures only).
These files are JSON format. It is done in order to have a possibility to process them later on as well.

The tool returns:
* **Status** - response status
* **Login** - campaign login
* **Redirect_link** - final redirect link
* **Cookie** - _tagtag_aid_ cookie data
* **admitad_uid** - click id from _tagtag_aid_
* **Attribution** - _deduplication_cookie_ value

### Requirements for campaign_list.py

This is a dictionary.

* **Key** - campaign login
* **Value** - affiliate link. Deeplinks can be used as well

### Limitations

Some limits might occur on some websites (e.g. financial campaigns in Brazil). 
The tool might get stuck. If it happens, the tool needs to be stopped and the link should be deleted from the list.
