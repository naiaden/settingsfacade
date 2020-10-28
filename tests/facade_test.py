import unittest


class DynaConfFacadeTestCase(unittest.TestCase):
    def test_get_secret_from_default(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertEqual(c.get_secret('asd'), 'blabla')

    def test_get_default_secret_from_default(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertIsNone(c.get_secret('asdasd'))

    def test_get_secret_from_env(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertEqual(c.get_secret('qwe'), 241241)
        self.assertEqual(c.get_secret('qwe', environment='production'), 395395)

    def test_get_setting_from_default(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertEqual(c.get_setting('asd'), 'bla')

    def test_get_default_setting_from_default(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertIsNone(c.get_setting('asdasd'))

    def test_get_setting_from_env(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertEqual(c.get_setting('qwe'), 241)
        self.assertEqual(c.get_setting('qwe', environment='production'), 395)

    def test_set_secret_on_default(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertIsNone(c.get_setting('sec'))
        c.set_secret(key='sec', value='hpoi')
        self.assertEqual(c.get_secret('sec'), 'hpoi')

    def test_set_secret_on_env(self):
        from analyticsconfig import ConfigFacade
        c = ConfigFacade()
        self.assertIsNone(c.get_secret('sec', environment='temp'))
        c.set_secret(key='sec', value='hpoi', environment='temp')
        self.assertEqual(c.get_secret('sec', environment='temp'), 'hpoi')
        self.assertIsNone(c.get_secret('sec'))

if __name__ == '__main__':
    unittest.main()
