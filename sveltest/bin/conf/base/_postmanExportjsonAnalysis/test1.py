#!/usr/bin/env python
# -*- coding:utf-8 -*-


from sveltest import HttpTestCase
from sveltest import main


class TestExportCase(HttpTestCase):

    def setUp(self):
        pass


    

    def test_sveltest_0(self):
        """vip"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo?parameters',
            headers={'Cookie': ' csrftoken=vw8GAtgyjLUFC5TMN09IWsCfrtP6kWbbJzesLH1YmA0ANfwpm4mi26KEPke0UXR1; username=\\"2|1:0|10:1645769022|8:username|12:MTM0NTMwMDE=|81ccdeeea49276a7799f612efa465f7b4145ab668408cdbd35463469906a0556\\"; pwd=2|1:0|10:1645769022|3:pwd|8:MTIzNDU2|1a1270dfabb16745bfd11028cd947652ebfa8472b3318444950e9021a681c87f","description":"","type":"text","enabled":true}]', 'platform': 'qZgBxjSmodkk/NZ6+fUwBb8FFnMrkgNPOODxw7b3+gCBIf6lsudALtF+g7No1MwuaOvjFyLhQ18PHXRbOo2oeMeNmguN0He2HUyCeFG8FrnLoxymlw3hOAPKOEMHdbfrc9Dm83IXbgznAQmKPss+QZL1C/WWXXSVFYQFWiZV02s='},
            env_control=False,
            data={}
        )

    def test_sveltest_1(self):
        """vip Copy"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo?pwd=123456&parameters',
            headers={'Cookie': ' csrftoken=vw8GAtgyjLUFC5TMN09IWsCfrtP6kWbbJzesLH1YmA0ANfwpm4mi26KEPke0UXR1; username=\\"2|1:0|10:1645769022|8:username|12:MTM0NTMwMDE=|81ccdeeea49276a7799f612efa465f7b4145ab668408cdbd35463469906a0556\\"; pwd=2|1:0|10:1645769022|3:pwd|8:MTIzNDU2|1a1270dfabb16745bfd11028cd947652ebfa8472b3318444950e9021a681c87f","description":"","type":"text","enabled":true}]', 'platform': 'qZgBxjSmodkk/NZ6+fUwBb8FFnMrkgNPOODxw7b3+gCBIf6lsudALtF+g7No1MwuaOvjFyLhQ18PHXRbOo2oeMeNmguN0He2HUyCeFG8FrnLoxymlw3hOAPKOEMHdbfrc9Dm83IXbgznAQmKPss+QZL1C/WWXXSVFYQFWiZV02s='},
            env_control=False,
            data={}
        )

    def test_sveltest_2(self):
        """vip Copy 2"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo',
            headers={},
            env_control=False,
            data={}
        )

    def test_sveltest_3(self):
        """vip Copy 3"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo?pwd=123456',
            headers={},
            env_control=False,
            data={}
        )

    def test_sveltest_4(self):
        """vip Copy 4"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo?pwd=123456',
            headers={},
            env_control=False,
            data={}
        )

    def test_sveltest_5(self):
        """vip Copy 5"""

        self.get(
            router='https://restapi.amap.com/v3/weather/weatherInfo',
            headers={},
            env_control=False,
            data={}
        )


    def tearDown(self):
        pass


if __name__ == '__main__':
    main(debug=True)