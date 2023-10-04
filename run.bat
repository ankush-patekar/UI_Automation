 pytest -s -v --html=.\Reports\report_sanity_firefox.html -m "sanity" .\testCases --browser firefox
 pytest -s -v --html=.\Reports\report_sanity_edge.html -m "sanity" .\testCases --browser edge

 pytest -s -v --html=.\Reports\report_regression_chrome.html -m "regression" .\testCases --browser chrome
