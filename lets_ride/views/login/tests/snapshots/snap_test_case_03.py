# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03LoginAPITestCase::test_case status'] = 200

snapshots['TestCase03LoginAPITestCase::test_case body'] = {
    'access_token': 'JBSJBNKJFGHJKNLKJMLTYT',
    'expires_in': '2020-08-09, 06:20:13',
    'refresh_token': 'DKBKVJBKJVTRTYDTYDYTFH',
    'user_id': 2
}

snapshots['TestCase03LoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '137',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
